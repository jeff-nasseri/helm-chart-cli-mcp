import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_get_all(release_name: str, namespace: Optional[str] = None) -> str:
    """
    Gets all information about a release.
    """
    logger.info(f"Running helm get all for release={release_name}, namespace={namespace}")

    cmd = ["helm", "get", "all", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    return execute_helm_command(cmd)


def helm_get_hooks(release_name: str, namespace: Optional[str] = None) -> str:
    """
    Gets the hooks for a release.
    """
    logger.info(f"Running helm get hooks for release={release_name}, namespace={namespace}")

    cmd = ["helm", "get", "hooks", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    return execute_helm_command(cmd)


def helm_get_manifest(release_name: str, namespace: Optional[str] = None) -> str:
    """
    Gets the manifest for a release.
    """
    logger.info(f"Running helm get manifest for release={release_name}, namespace={namespace}")

    cmd = ["helm", "get", "manifest", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    return execute_helm_command(cmd)


def helm_get_metadata(release_name: str, namespace: Optional[str] = None) -> str:
    """
    Gets the metadata for a release.
    """
    logger.info(f"Running helm get metadata for release={release_name}, namespace={namespace}")

    cmd = ["helm", "get", "metadata", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    return execute_helm_command(cmd)


def helm_get_notes(release_name: str, namespace: Optional[str] = None) -> str:
    """
    Gets the notes for a release.
    """
    logger.info(f"Running helm get notes for release={release_name}, namespace={namespace}")

    cmd = ["helm", "get", "notes", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    return execute_helm_command(cmd)


def helm_get_values(release_name: str, namespace: Optional[str] = None, all_values: bool = False) -> str:
    """
    Gets the values for a release.
    """
    logger.info(f"Running helm get values for release={release_name}, namespace={namespace}, all={all_values}")

    cmd = ["helm", "get", "values", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    if all_values:
        cmd.append("--all")

    return execute_helm_command(cmd)