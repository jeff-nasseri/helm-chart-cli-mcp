import pytest
import tempfile
import os
from mcp_server_helm.commands import dependencies


class TestHelmDependencyBuild:
    def test_helm_dependency_build_nonexistent_chart(self):
        """Test helm dependency build with non-existent chart."""
        result = dependencies.helm_dependency_build("/nonexistent/chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error",
            "Chart.yaml"
        ])

    def test_helm_dependency_build_with_hello_world_chart(self):
        """Test helm dependency build with the hello-world chart."""
        # Use the existing hello-world chart in the src directory
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = dependencies.helm_dependency_build(chart_path)
        
        # Should succeed since the hello-world chart exists
        # Even if no dependencies, it should run without error
        assert "Error executing command" not in result


class TestHelmDependencyList:
    def test_helm_dependency_list_nonexistent_chart(self):
        """Test helm dependency list with non-existent chart."""
        result = dependencies.helm_dependency_list("/nonexistent/chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error",
            "Chart.yaml"
        ])

    def test_helm_dependency_list_with_hello_world_chart(self):
        """Test helm dependency list with the hello-world chart."""
        # Use the existing hello-world chart in the src directory
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = dependencies.helm_dependency_list(chart_path)
        
        # Should succeed even if no dependencies are found
        assert "Error executing command" not in result


class TestHelmDependencyUpdate:
    def test_helm_dependency_update_nonexistent_chart(self):
        """Test helm dependency update with non-existent chart."""
        result = dependencies.helm_dependency_update("/nonexistent/chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error",
            "Chart.yaml"
        ])

    def test_helm_dependency_update_with_hello_world_chart(self):
        """Test helm dependency update with the hello-world chart."""
        # Use the existing hello-world chart in the src directory
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = dependencies.helm_dependency_update(chart_path)
        
        # Should succeed even if no dependencies to update
        assert "Error executing command" not in result