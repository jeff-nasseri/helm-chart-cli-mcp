import pytest
from mcp_server_helm.commands import search


class TestHelmSearchRepo:
    def test_helm_search_repo_nonexistent(self):
        """Test searching for non-existent charts in repositories."""
        result = search.helm_search_repo("nonexistent-chart-12345")
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Should either show no results or empty results
        assert any(text in result for text in [
            "No charts found",
            "[]",
            "no chart"
        ])

    def test_helm_search_repo_common_chart(self):
        """Test searching for a common chart name."""
        result = search.helm_search_repo("nginx")
        
        # Should execute without errors  
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Result should be parseable (either JSON array or formatted text)
        assert len(result.strip()) > 0


class TestHelmSearchHub:
    def test_helm_search_hub_nonexistent(self):
        """Test searching hub for non-existent charts."""
        result = search.helm_search_hub("nonexistent-chart-12345")
        
        # Should execute without errors
        assert "Error executing command" not in result  
        assert "Unexpected error" not in result
        
        # Should either show no results or empty results
        assert any(text in result for text in [
            "No charts found",
            "[]", 
            "no chart"
        ])

    def test_helm_search_hub_common_chart(self):
        """Test searching hub for a common chart."""
        result = search.helm_search_hub("nginx")
        
        # Should execute without errors
        assert "Error executing command" not in result
        assert "Unexpected error" not in result
        
        # Result should be parseable
        assert len(result.strip()) > 0