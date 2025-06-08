import pytest
from mcp_server_helm.commands import plugin


class TestHelmPluginInstall:
    def test_helm_plugin_install_invalid_url(self):
        """Test helm plugin install with invalid URL."""
        result = plugin.helm_plugin_install("https://github.com/nonexistent/helm-plugin")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])

    def test_helm_plugin_install_with_version(self):
        """Test helm plugin install with version parameter."""
        result = plugin.helm_plugin_install("https://github.com/nonexistent/helm-plugin", version="v1.0.0")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])

    def test_helm_plugin_install_invalid_path(self):
        """Test helm plugin install with invalid local path."""
        result = plugin.helm_plugin_install("/nonexistent/plugin/path")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error"
        ])


class TestHelmPluginList:
    def test_helm_plugin_list(self):
        """Test helm plugin list command."""
        result = plugin.helm_plugin_list()
        
        # Should succeed (even if no plugins are installed)
        assert "Error executing command" not in result
        # Output might be empty if no plugins are installed, which is fine


class TestHelmPluginUninstall:
    def test_helm_plugin_uninstall_nonexistent(self):
        """Test helm plugin uninstall with non-existent plugin."""
        result = plugin.helm_plugin_uninstall("nonexistent-plugin")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])

    def test_helm_plugin_uninstall_different_name(self):
        """Test helm plugin uninstall with another non-existent plugin."""
        result = plugin.helm_plugin_uninstall("another-nonexistent-plugin")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])


class TestHelmPluginUpdate:
    def test_helm_plugin_update_nonexistent(self):
        """Test helm plugin update with non-existent plugin."""
        result = plugin.helm_plugin_update("nonexistent-plugin")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])

    def test_helm_plugin_update_different_name(self):
        """Test helm plugin update with another non-existent plugin."""
        result = plugin.helm_plugin_update("another-nonexistent-plugin")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "plugin"
        ])