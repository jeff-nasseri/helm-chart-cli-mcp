import pytest
from mcp_server_helm.commands import show


class TestHelmShowAll:
    def test_helm_show_all_nonexistent_chart(self):
        """Test helm show all with non-existent chart."""
        result = show.helm_show_all("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_show_all_with_repo(self):
        """Test helm show all with repo/chart format."""
        result = show.helm_show_all("nginx", repo="nonexistent-repo")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])

    def test_helm_show_all_with_version(self):
        """Test helm show all with version parameter."""
        result = show.helm_show_all("nonexistent-chart", version="1.0.0")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error"
        ])

    def test_helm_show_all_with_local_chart(self):
        """Test helm show all with local chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = show.helm_show_all(chart_path)
        
        # Should succeed with local chart
        assert "Error executing command" not in result
        assert len(result.strip()) > 0
        # Should contain chart information
        assert "hello-world" in result.lower()


class TestHelmShowChart:
    def test_helm_show_chart_nonexistent_chart(self):
        """Test helm show chart with non-existent chart."""
        result = show.helm_show_chart("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_show_chart_with_local_chart(self):
        """Test helm show chart with local chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = show.helm_show_chart(chart_path)
        
        # Should succeed with local chart
        assert "Error executing command" not in result
        assert len(result.strip()) > 0
        # Should contain chart metadata
        assert "name:" in result
        assert "version:" in result

    def test_helm_show_chart_with_repo(self):
        """Test helm show chart with repo/chart format."""
        result = show.helm_show_chart("nginx", repo="nonexistent-repo")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])


class TestHelmShowCrds:
    def test_helm_show_crds_nonexistent_chart(self):
        """Test helm show crds with non-existent chart."""
        result = show.helm_show_crds("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_show_crds_with_local_chart(self):
        """Test helm show crds with local chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = show.helm_show_crds(chart_path)
        
        # Should succeed (might be empty if no CRDs)
        assert "Error executing command" not in result

    def test_helm_show_crds_with_repo(self):
        """Test helm show crds with repo/chart format."""
        result = show.helm_show_crds("prometheus-operator", repo="nonexistent-repo")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])


class TestHelmShowReadme:
    def test_helm_show_readme_nonexistent_chart(self):
        """Test helm show readme with non-existent chart."""
        result = show.helm_show_readme("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_show_readme_with_local_chart(self):
        """Test helm show readme with local chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = show.helm_show_readme(chart_path)
        
        # Should succeed (might be empty if no README)
        assert "Error executing command" not in result

    def test_helm_show_readme_with_repo(self):
        """Test helm show readme with repo/chart format."""
        result = show.helm_show_readme("nginx", repo="nonexistent-repo")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])


class TestHelmShowValues:
    def test_helm_show_values_nonexistent_chart(self):
        """Test helm show values with non-existent chart."""
        result = show.helm_show_values("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_show_values_with_local_chart(self):
        """Test helm show values with local chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = show.helm_show_values(chart_path)
        
        # Should succeed and show values
        assert "Error executing command" not in result
        assert len(result.strip()) > 0
        # Should contain YAML values
        assert any(text in result for text in [":", "image", "name", "tag"])

    def test_helm_show_values_with_repo(self):
        """Test helm show values with repo/chart format."""
        result = show.helm_show_values("nginx", repo="nonexistent-repo")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])

    def test_helm_show_values_with_version(self):
        """Test helm show values with version parameter."""
        result = show.helm_show_values("nonexistent-chart", version="1.0.0")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error"
        ])


class TestChartReferenceBuilding:
    """Test that chart references are built correctly across all show commands."""

    @pytest.mark.parametrize("command_func", [
        show.helm_show_all,
        show.helm_show_chart,
        show.helm_show_crds,
        show.helm_show_readme,
        show.helm_show_values,
    ])
    def test_chart_reference_without_repo(self, command_func):
        """Test chart reference without repo for all show commands."""
        result = command_func("nonexistent-chart")
        
        # Should handle the error gracefully for all commands
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    @pytest.mark.parametrize("command_func", [
        show.helm_show_all,
        show.helm_show_chart,
        show.helm_show_crds,
        show.helm_show_readme,
        show.helm_show_values,
    ])
    def test_chart_reference_with_repo(self, command_func):
        """Test chart reference with repo for all show commands."""
        result = command_func("my-chart", repo="nonexistent-repo")
        
        # Should handle the error gracefully for all commands
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])

    @pytest.mark.parametrize("command_func", [
        show.helm_show_all,
        show.helm_show_chart,
        show.helm_show_crds,
        show.helm_show_readme,
        show.helm_show_values,
    ])
    def test_chart_reference_with_local_chart(self, command_func):
        """Test chart reference with local chart for all show commands."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = command_func(chart_path)
        
        # Should succeed for all commands with local chart
        assert "Error executing command" not in result