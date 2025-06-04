import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_show_all(chart: str, repo: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Shows all information of a chart.
    """
    logger.info(f"Running helm show all with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "show", "all", chart_ref]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)


def helm_show_chart(chart: str, repo: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Shows the chart's definition.
    """
    logger.info(f"Running helm show chart with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "show", "chart", chart_ref]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)


def helm_show_crds(chart: str, repo: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Shows the chart's CRDs.
    """
    logger.info(f"Running helm show crds with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "show", "crds", chart_ref]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)


def helm_show_readme(chart: str, repo: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Shows the chart's README.
    """
    logger.info(f"Running helm show readme with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "show", "readme", chart_ref]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)


def helm_show_values(chart: str, repo: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Shows the chart's values.
    """
    logger.info(f"Running helm show values with chart={chart}, repo={repo}, version={version}")

    # Build chart reference
    chart_ref = chart
    if repo:
        chart_ref = f"{repo}/{chart}"

    cmd = ["helm", "show", "values", chart_ref]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)