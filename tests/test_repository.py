import pytest
import tempfile
import os
from mcp_server_helm.commands import repository


class TestHelmRepoAdd:
    def test_helm_repo_add_bitnami(self):
        """Test adding bitnami repository."""
        result = repository.helm_repo_add("test-bitnami", "https://charts.bitnami.com/bitnami")
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Clean up by removing the repo
        repository.helm_repo_remove("test-bitnami")

    def test_helm_repo_add_invalid_url(self):
        """Test adding repository with invalid URL."""
        result = repository.helm_repo_add("invalid-repo", "https://nonexistent.invalid.url")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "error",
            "failed",
            "unable"
        ])


class TestHelmRepoRemove:
    def test_helm_repo_remove_nonexistent(self):
        """Test removing non-existent repository."""
        result = repository.helm_repo_remove("nonexistent-repo-12345")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no repository",
            "not found",
            "error"
        ])


class TestHelmRepoList:
    def test_helm_repo_list(self):
        """Test listing repositories."""
        result = repository.helm_repo_list()
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Should either show repos or indicate no repos found
        assert len(result.strip()) > 0


class TestHelmRepoUpdate:
    def test_helm_repo_update(self):
        """Test updating repositories."""
        result = repository.helm_repo_update()
        
        # Should execute without errors (even if no repos exist)
        assert "Error executing command" not in result
        assert "Unexpected error" not in result


class TestHelmRepoIndex:
    def test_helm_repo_index_nonexistent_path(self):
        """Test indexing non-existent directory."""
        result = repository.helm_repo_index("/nonexistent/path")
        
        # Should handle error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error"
        ])

    def test_helm_repo_index_with_temp_dir(self):
        """Test indexing empty temporary directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = repository.helm_repo_index(tmpdir)
            
            # Should execute without errors (though may warn about no charts)
            assert "Error executing command" not in result
            assert "Unexpected error" not in result
            
            # Should create index.yaml file
            index_file = os.path.join(tmpdir, "index.yaml")
            assert os.path.exists(index_file)

    def test_helm_repo_index_with_url(self):
        """Test indexing with URL parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = repository.helm_repo_index(tmpdir, url="https://example.com/charts")
            
            # Should execute without errors
            assert "Error executing command" not in result
            assert "Unexpected error" not in result