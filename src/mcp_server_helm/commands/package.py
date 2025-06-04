import logging
from typing import Dict, List, Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_package(chart_path: str, destination: Optional[str] = None,
                 app_version: Optional[str] = None, version: Optional[str] = None,
                 dependency_update: bool = False) -> str:
    """
    Packages a chart into a chart archive.
    """
    logger.info(f"Running helm package for chart={chart_path}")

    cmd = ["helm", "package", chart_path]

    if destination:
        cmd.extend(["--destination", destination])

    if app_version:
        cmd.extend(["--app-version", app_version])

    if version:
        cmd.extend(["--version", version])

    if dependency_update:
        cmd.append("--dependency-update")

    return execute_helm_command(cmd)


def helm_push(chart_path: str, registry_url: str, force: bool = False,
              insecure: bool = False, plain_http: bool = False) -> str:
    """
    Pushes a chart to a registry.
    """
    logger.info(f"Running helm push with chart_path={chart_path}, registry_url={registry_url}")

    cmd = ["helm", "push", chart_path, registry_url]

    if force:
        cmd.append("--force")

    if insecure:
        cmd.append("--insecure")

    if plain_http:
        cmd.append("--plain-http")

    return execute_helm_command(cmd)


def helm_pull(chart: str, repo: Optional[str] = None, version: Optional[str] = None,
              destination: Optional[str] = None, untar: bool = False,
              verify: bool = False, keyring: Optional[str] = None) -> str:
    """
    Downloads a chart from a repository.
    """
    logger.info(f"Running helm pull with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "pull", chart_ref]

    if version:
        cmd.extend(["--version", version])

    if destination:
        cmd.extend(["--destination", destination])

    if untar:
        cmd.append("--untar")

    if verify:
        cmd.append("--verify")

    if keyring:
        cmd.extend(["--keyring", keyring])

    return execute_helm_command(cmd)


def helm_lint(chart_path: str, values_file: Optional[str] = None, set_values: Optional[Dict[str, str]] = None) -> str:
    """
    Runs a series of tests to verify that the chart is well-formed.
    """
    logger.info(f"Running helm lint for chart={chart_path}")

    cmd = ["helm", "lint", chart_path]

    # Add values file if provided
    if values_file:
        cmd.extend(["-f", values_file])

    # Add set values if provided
    if set_values:
        for key, value in set_values.items():
            cmd.extend(["--set", f"{key}={value}"])

    return execute_helm_command(cmd)


def helm_template(chart: str, release_name: Optional[str] = None, namespace: Optional[str] = None,
                  values_file: Optional[str] = None, set_values: Optional[Dict[str, str]] = None,
                  api_versions: Optional[List[str]] = None, kube_version: Optional[str] = None) -> str:
    """
    Renders chart templates locally and displays the output.
    """
    logger.info(f"Running helm template with chart={chart}, release_name={release_name}")

    cmd = ["helm", "template"]

    # Add release name if provided
    if release_name:
        cmd.append(release_name)

    # Add chart name
    cmd.append(chart)

    # Add namespace if provided
    if namespace:
        cmd.extend(["--namespace", namespace])

    # Add values file if provided
    if values_file:
        cmd.extend(["-f", values_file])

    # Add set values if provided
    if set_values:
        for key, value in set_values.items():
            cmd.extend(["--set", f"{key}={value}"])

    # Add API versions if provided
    if api_versions:
        for version in api_versions:
            cmd.extend(["--api-versions", version])

    # Add Kubernetes version if provided
    if kube_version:
        cmd.extend(["--kube-version", kube_version])

    return execute_helm_command(cmd)