import pytest
import tempfile
import os
from mcp_server_helm.commands import package


class TestHelmPackage:
    def test_helm_package_nonexistent_chart(self):
        """Test helm package with non-existent chart."""
        result = package.helm_package("/nonexistent/chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error",
            "Chart.yaml"
        ])

    def test_helm_package_with_hello_world_chart(self):
        """Test helm package with the hello-world chart."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Use the existing hello-world chart in the src directory
            chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
            result = package.helm_package(chart_path, destination=tmpdir)
            
            # Should succeed since the hello-world chart exists
            assert "Error executing command" not in result
            # Should mention successful packaging
            assert any(text in result for text in ["Successfully packaged", "hello-world"])

    def test_helm_package_with_version_parameter(self):
        """Test helm package with version parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
            result = package.helm_package(chart_path, destination=tmpdir, version="1.0.0")
            
            # Should succeed
            assert "Error executing command" not in result


class TestHelmPush:
    def test_helm_push_nonexistent_package(self):
        """Test helm push with non-existent package."""
        result = package.helm_push("/nonexistent/chart.tgz", "oci://registry.example.com/charts")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error"
        ])

    def test_helm_push_invalid_registry(self):
        """Test helm push with invalid registry URL."""
        # Create a dummy chart file
        with tempfile.NamedTemporaryFile(suffix=".tgz", delete=False) as tmp:
            tmp.write(b"fake chart content")
            tmp.flush()
            
            try:
                result = package.helm_push(tmp.name, "invalid-registry-url")
                
                # Should handle the error gracefully
                assert any(text in result for text in [
                    "Error executing command",
                    "invalid",
                    "error",
                    "registry"
                ])
            finally:
                os.unlink(tmp.name)

    def test_helm_push_with_flags(self):
        """Test helm push with various flags."""
        result = package.helm_push(
            "/nonexistent/chart.tgz",
            "oci://registry.example.com/charts",
            force=True,
            insecure=True,
            plain_http=True
        )
        
        # Should handle the error gracefully (file doesn't exist)
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error"
        ])


class TestHelmPull:
    def test_helm_pull_nonexistent_chart(self):
        """Test helm pull with non-existent chart."""
        result = package.helm_pull("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_pull_with_repo_and_chart(self):
        """Test helm pull with repo/chart format."""
        result = package.helm_pull("nginx", repo="nonexistent-repo")
        
        # Should handle the error gracefully (repo doesn't exist)
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "repository"
        ])

    def test_helm_pull_with_destination(self):
        """Test helm pull with destination parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = package.helm_pull("nonexistent-chart", destination=tmpdir)
            
            # Should handle the error gracefully
            assert any(text in result for text in [
                "Error executing command",
                "not found",
                "error"
            ])

    def test_helm_pull_with_options(self):
        """Test helm pull with various options."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = package.helm_pull(
                "nonexistent-chart",
                version="1.0.0",
                destination=tmpdir,
                untar=True
            )
            
            # Should handle the error gracefully
            assert any(text in result for text in [
                "Error executing command",
                "not found",
                "error"
            ])


class TestHelmLint:
    def test_helm_lint_nonexistent_chart(self):
        """Test helm lint with non-existent chart."""
        result = package.helm_lint("/nonexistent/chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "no such file",
            "not found",
            "error",
            "Chart.yaml"
        ])

    def test_helm_lint_with_hello_world_chart(self):
        """Test helm lint with the hello-world chart."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_lint(chart_path)
        
        # Should succeed since the hello-world chart exists and is valid
        assert "Error executing command" not in result
        # Helm lint typically outputs something about linting
        assert len(result.strip()) > 0

    def test_helm_lint_with_set_values(self):
        """Test helm lint with set values."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_lint(chart_path, set_values={"image.tag": "test"})
        
        # Should succeed
        assert "Error executing command" not in result


class TestHelmTemplate:
    def test_helm_template_nonexistent_chart(self):
        """Test helm template with non-existent chart."""
        result = package.helm_template("nonexistent-chart")
        
        # Should handle the error gracefully
        assert any(text in result for text in [
            "Error executing command",
            "not found",
            "error",
            "chart"
        ])

    def test_helm_template_with_hello_world_chart(self):
        """Test helm template with the hello-world chart path."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_template(chart_path)
        
        # Should succeed and output YAML manifests
        assert "Error executing command" not in result
        assert len(result.strip()) > 0
        # Should contain YAML content
        assert any(text in result for text in ["apiVersion", "kind", "metadata"])

    def test_helm_template_with_release_name(self):
        """Test helm template with release name."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_template(chart_path, release_name="test-release")
        
        # Should succeed
        assert "Error executing command" not in result
        assert "test-release" in result

    def test_helm_template_with_set_values(self):
        """Test helm template with set values."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_template(chart_path, set_values={"image.tag": "test"})
        
        # Should succeed
        assert "Error executing command" not in result

    def test_helm_template_with_options(self):
        """Test helm template with various options."""
        chart_path = "/mnt/b/root/helm-chart-cli-mcp/src/hello-world"
        result = package.helm_template(
            chart_path,
            release_name="test-release",
            namespace="test-namespace",
            kube_version="1.20.0"
        )
        
        # Should succeed
        assert "Error executing command" not in result