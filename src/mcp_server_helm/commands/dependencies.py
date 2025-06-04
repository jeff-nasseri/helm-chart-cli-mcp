import logging
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_dependency_build(chart_path: str) -> str:
    """
    Builds the chart's dependencies.
    """
    logger.info(f"Running helm dependency build for chart={chart_path}")

    return execute_helm_command(["helm", "dependency", "build", chart_path])


def helm_dependency_list(chart_path: str) -> str:
    """
    Lists the dependencies for the given chart.
    """
    logger.info(f"Running helm dependency list for chart={chart_path}")

    return execute_helm_command(["helm", "dependency", "list", chart_path])


def helm_dependency_update(chart_path: str) -> str:
    """
    Updates the chart's dependencies.
    """
    logger.info(f"Running helm dependency update for chart={chart_path}")

    return execute_helm_command(["helm", "dependency", "update", chart_path])