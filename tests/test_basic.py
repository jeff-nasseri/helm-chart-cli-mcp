import pytest
import tempfile
import os
from mcp_server_helm.commands import basic


class TestHelmCompletion:
    def test_helm_completion_bash(self):
        """Test helm completion for bash shell."""
        result = basic.helm_completion("bash")
        
        # Should contain bash completion code without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0
        # Bash completion typically contains function definitions
        assert "_helm" in result or "complete" in result

    def test_helm_completion_invalid_shell(self):
        """Test helm completion with invalid shell returns error."""
        result = basic.helm_completion("invalid")
        
        assert "Invalid shell: invalid" in result
        assert "bash, fish, powershell, zsh" in result

    @pytest.mark.parametrize("shell", ["bash", "zsh", "fish", "powershell"])
    def test_helm_completion_all_valid_shells(self, shell):
        """Test helm completion for all valid shells."""
        result = basic.helm_completion(shell)
        
        # Should generate completion code for each valid shell
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0


class TestHelmCreate:
    def test_helm_create_basic(self):
        """Test basic helm create functionality."""
        with tempfile.TemporaryDirectory() as tmpdir:
            chart_name = "test-chart"
            chart_path = os.path.join(tmpdir, chart_name)
            
            # Change to temp directory to create chart there
            original_cwd = os.getcwd()
            os.chdir(tmpdir)
            
            try:
                result = basic.helm_create(chart_name)
                
                # Should create chart successfully
                assert "Error executing command" not in result
                assert "Unexpected error" not in result
                assert os.path.exists(chart_path)
                assert os.path.exists(os.path.join(chart_path, "Chart.yaml"))
                assert os.path.exists(os.path.join(chart_path, "values.yaml"))
                assert os.path.exists(os.path.join(chart_path, "templates"))
            finally:
                os.chdir(original_cwd)

    def test_helm_create_with_starter(self):
        """Test helm create with invalid starter (should fail gracefully)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            original_cwd = os.getcwd()
            os.chdir(tmpdir)
            
            try:
                result = basic.helm_create("test-chart", starter="nonexistent-starter")
                
                # Should handle the error gracefully
                # Either our error wrapper or Helm's own error message
                assert any(text in result for text in [
                    "Error executing command", 
                    "starter", 
                    "not found",
                    "error"
                ])
            finally:
                os.chdir(original_cwd)


class TestHelmEnv:
    def test_helm_env(self):
        """Test helm env command returns environment variables."""
        result = basic.helm_env()
        
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0
        # Should contain Helm environment variables
        assert "HELM" in result


class TestHelmVersion:
    def test_helm_version(self):
        """Test helm version command returns version information."""
        result = basic.helm_version()
        
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        assert len(result.strip()) > 0
        # Should contain version information
        assert any(text in result.lower() for text in ["version", "v3", "v2"])


class TestHelmVerify:
    def test_helm_verify_nonexistent_chart(self):
        """Test helm verify with non-existent chart."""
        result = basic.helm_verify("/nonexistent/chart.tgz")
        
        # Should handle the error gracefully
        # Either our error wrapper or Helm's own error message
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error"
        ])

    def test_helm_verify_with_keyring(self):
        """Test helm verify with keyring parameter."""
        result = basic.helm_verify("/nonexistent/chart.tgz", keyring="/nonexistent/keyring")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file", 
            "not found",
            "error"
        ])