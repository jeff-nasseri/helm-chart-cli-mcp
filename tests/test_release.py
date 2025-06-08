import pytest
from mcp_server_helm.commands import release


class TestHelmInstall:
    def test_helm_install_nonexistent_chart(self):
        """Test installing non-existent chart."""
        result = release.helm_install("nonexistent-chart-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "failed"
        ])

    def test_helm_install_invalid_chart_format(self):
        """Test installing with invalid chart format."""
        result = release.helm_install("invalid/chart/format/too/many/slashes")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "invalid",
            "failed"
        ])


class TestHelmUninstall:
    def test_helm_uninstall_nonexistent_release(self):
        """Test uninstalling non-existent release."""
        result = release.helm_uninstall("nonexistent-release-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command", 
            "not found",
            "error",
            "release"
        ])


class TestHelmRollback:
    def test_helm_rollback_nonexistent_release(self):
        """Test rolling back non-existent release."""
        result = release.helm_rollback("nonexistent-release-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmHistory:
    def test_helm_history_nonexistent_release(self):
        """Test getting history of non-existent release."""
        result = release.helm_history("nonexistent-release-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found", 
            "error",
            "release"
        ])


class TestHelmStatus:
    def test_helm_status_nonexistent_release(self):
        """Test getting status of non-existent release."""
        result = release.helm_status("nonexistent-release-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error", 
            "release"
        ])


class TestHelmList:
    def test_helm_list_all_namespaces(self):
        """Test listing all releases across all namespaces."""
        result = release.helm_list()
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Should either show releases or indicate no releases found
        assert len(result.strip()) > 0


class TestHelmTest:
    def test_helm_test_nonexistent_release(self):
        """Test testing non-existent release."""
        result = release.helm_test("nonexistent-release-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])