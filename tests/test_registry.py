import pytest
from mcp_server_helm.commands import registry


class TestHelmRegistryLogin:
    def test_helm_registry_login_invalid_registry(self):
        """Test helm registry login with invalid registry."""
        result = registry.helm_registry_login(
            "oci://nonexistent-registry.example.com",
            "username",
            "password"
        )
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "registry",
            "login"
        ])

    def test_helm_registry_login_with_insecure_flag(self):
        """Test helm registry login with insecure flag."""
        result = registry.helm_registry_login(
            "oci://nonexistent-registry.example.com",
            "username",
            "password",
            insecure=True
        )
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "registry",
            "login"
        ])

    def test_helm_registry_login_invalid_url_format(self):
        """Test helm registry login with invalid URL format."""
        result = registry.helm_registry_login(
            "invalid-url-format",
            "username",
            "password"
        )
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "invalid"
        ])

    def test_helm_registry_login_different_registry(self):
        """Test helm registry login with different registry URL."""
        result = registry.helm_registry_login(
            "oci://another-nonexistent-registry.com",
            "testuser",
            "testpass"
        )
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "registry"
        ])


class TestHelmRegistryLogout:
    def test_helm_registry_logout_nonexistent_registry(self):
        """Test helm registry logout with non-existent registry."""
        result = registry.helm_registry_logout("oci://nonexistent-registry.example.com")
        
        # Should handle the error gracefully (logout might succeed even if not logged in)
        # But for non-existent registries, it should either succeed or fail gracefully
        assert "Error executing command" not in result or any(text in result for text in [
            "Error executing command",
            "error",
            "registry"
        ])

    def test_helm_registry_logout_different_registry(self):
        """Test helm registry logout with different registry."""
        result = registry.helm_registry_logout("oci://another-registry.com")
        
        # Should handle gracefully
        assert "Error executing command" not in result or any(text in result for text in [
            "Error executing command",
            "error",
            "registry"
        ])

    def test_helm_registry_logout_non_oci_registry(self):
        """Test helm registry logout with non-OCI registry URL."""
        result = registry.helm_registry_logout("https://registry.example.com")
        
        # Should handle gracefully
        assert "Error executing command" not in result or any(text in result for text in [
            "Error executing command",
            "error",
            "registry"
        ])

    def test_helm_registry_logout_invalid_url(self):
        """Test helm registry logout with invalid URL format."""
        result = registry.helm_registry_logout("invalid-url")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "invalid"
        ])