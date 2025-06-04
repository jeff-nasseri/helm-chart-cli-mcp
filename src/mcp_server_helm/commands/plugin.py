import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_plugin_install(plugin_url: str, version: Optional[str] = None) -> str:
    """
    Installs a Helm plugin.
    """
    logger.info(f"Running helm plugin install with plugin={plugin_url}, version={version}")

    cmd = ["helm", "plugin", "install", plugin_url]

    if version:
        cmd.extend(["--version", version])

    return execute_helm_command(cmd)


def helm_plugin_list() -> str:
    """
    Lists Helm plugins.
    """
    logger.info("Running helm plugin list")

    return execute_helm_command(["helm", "plugin", "list"])


def helm_plugin_uninstall(plugin_name: str) -> str:
    """
    Uninstalls a Helm plugin.
    """
    logger.info(f"Running helm plugin uninstall with plugin={plugin_name}")

    return execute_helm_command(["helm", "plugin", "uninstall", plugin_name])


def helm_plugin_update(plugin_name: str) -> str:
    """
    Updates a Helm plugin.
    """
    logger.info(f"Running helm plugin update with plugin={plugin_name}")

    return execute_helm_command(["helm", "plugin", "update", plugin_name])