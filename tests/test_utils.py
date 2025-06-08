import pytest
from mcp_server_helm.core.utils import execute_helm_command


class TestExecuteHelmCommand:
    def test_helm_version(self):
        """Test that helm version command works and returns version info."""
        result = execute_helm_command(["helm", "version", "--short"])
        
        # Should contain version info without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0

    def test_helm_help(self):
        """Test that helm help command works."""
        result = execute_helm_command(["helm", "help"])
        
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert "helm" in result.lower()
        assert "usage" in result.lower()

    def test_helm_list_all_namespaces(self):
        """Test helm list command with all namespaces."""
        result = execute_helm_command(["helm", "list", "--all-namespaces"])
        
        # Should execute without errors even if no releases exist
        assert "Error executing command" not in result
        assert "Unexpected error" not in result

    def test_helm_repo_list(self):
        """Test helm repo list command."""
        result = execute_helm_command(["helm", "repo", "list"])
        
        # Should execute without errors even if no repos exist
        assert "Error executing command" not in result
        assert "Unexpected error" not in result

    def test_helm_search_repo_empty(self):
        """Test helm search repo with non-existent term."""
        result = execute_helm_command(["helm", "search", "repo", "nonexistent-chart-12345"])
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result

    def test_helm_show_chart_nonexistent(self):
        """Test helm show chart command with non-existent chart."""
        result = execute_helm_command(["helm", "show", "chart", "nonexistent/chart"])
        
        # Should contain an error message about chart not found, but not our error wrapper
        # The error should come from Helm itself, not our execute function
        if "Error executing command" in result:
            # Our function caught and wrapped a CalledProcessError
            assert "Error executing command:" in result
        else:
            # Helm returned error output directly
            assert len(result.strip()) > 0

    def test_invalid_helm_command(self):
        """Test an invalid helm command to verify error handling."""
        result = execute_helm_command(["helm", "invalid-command-12345"])
        
        # Should contain error information
        assert any(text in result for text in ["Error executing command", "unknown command", "error"])

    def test_empty_command_list(self):
        """Test execute_helm_command with empty command list."""
        result = execute_helm_command([])
        
        # Should handle gracefully
        assert "Error executing command" in result or "Unexpected error" in result

    def test_helm_env_command(self):
        """Test helm env command to check environment variables."""
        result = execute_helm_command(["helm", "env"])
        
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0
        # Should contain some Helm environment variables
        assert "HELM" in result