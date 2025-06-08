import pytest
from mcp_server_helm.commands import get


class TestHelmGetAll:
    def test_helm_get_all_nonexistent_release(self):
        """Test helm get all with non-existent release."""
        result = get.helm_get_all("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_all_with_namespace(self):
        """Test helm get all with namespace parameter."""
        result = get.helm_get_all("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_all_with_none_namespace(self):
        """Test helm get all with None namespace."""
        result = get.helm_get_all("nonexistent-release", namespace=None)
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmGetHooks:
    def test_helm_get_hooks_nonexistent_release(self):
        """Test helm get hooks with non-existent release."""
        result = get.helm_get_hooks("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_hooks_with_namespace(self):
        """Test helm get hooks with namespace parameter."""
        result = get.helm_get_hooks("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmGetManifest:
    def test_helm_get_manifest_nonexistent_release(self):
        """Test helm get manifest with non-existent release."""
        result = get.helm_get_manifest("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_manifest_with_namespace(self):
        """Test helm get manifest with namespace parameter."""
        result = get.helm_get_manifest("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmGetMetadata:
    def test_helm_get_metadata_nonexistent_release(self):
        """Test helm get metadata with non-existent release."""
        result = get.helm_get_metadata("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_metadata_with_namespace(self):
        """Test helm get metadata with namespace parameter."""
        result = get.helm_get_metadata("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmGetNotes:
    def test_helm_get_notes_nonexistent_release(self):
        """Test helm get notes with non-existent release."""
        result = get.helm_get_notes("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_notes_with_namespace(self):
        """Test helm get notes with namespace parameter."""
        result = get.helm_get_notes("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])


class TestHelmGetValues:
    def test_helm_get_values_nonexistent_release(self):
        """Test helm get values with non-existent release."""
        result = get.helm_get_values("nonexistent-release")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_values_with_namespace(self):
        """Test helm get values with namespace parameter."""
        result = get.helm_get_values("nonexistent-release", namespace="test-namespace")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_values_with_all_values(self):
        """Test helm get values with all_values flag."""
        result = get.helm_get_values("nonexistent-release", all_values=True)
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_values_with_all_params(self):
        """Test helm get values with all parameters."""
        result = get.helm_get_values("nonexistent-release", namespace="test-namespace", all_values=True)
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])

    def test_helm_get_values_with_all_values_false(self):
        """Test helm get values with all_values set to False."""
        result = get.helm_get_values("nonexistent-release", all_values=False)
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "release"
        ])