import json
import logging
from typing import Dict, List, Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_install(chart: str, release_name: Optional[str] = None, namespace: Optional[str] = None,
                 values_file: Optional[str] = None, set_values: Optional[Dict[str, str]] = None,
                 description: Optional[str] = None, timeout: Optional[str] = None,
                 wait: bool = False, atomic: bool = False) -> str:
    """
    Installs a Helm chart.
    """
    logger.info(f"Running helm install with chart={chart}, release_name={release_name}, namespace={namespace}")

    # Build the command
    cmd = ["helm", "install"]

    # Add release name if provided, otherwise use --generate-name
    if release_name:
        cmd.append(release_name)
    else:
        cmd.append("--generate-name")

    # Add chart name
    cmd.append(chart)

    # Add namespace if provided
    if namespace:
        cmd.extend(["-n", namespace])

    # Add values file if provided
    if values_file:
        cmd.extend(["-f", values_file])

    # Add set values if provided
    if set_values:
        for key, value in set_values.items():
            cmd.extend(["--set", f"{key}={value}"])

    # Add description if provided
    if description:
        cmd.extend(["--description", description])

    # Add timeout if provided
    if timeout:
        cmd.extend(["--timeout", timeout])

    # Add wait flag if provided
    if wait:
        cmd.append("--wait")

    # Add atomic flag if provided
    if atomic:
        cmd.append("--atomic")

    # Add output format
    cmd.extend(["--output", "json"])

    output = execute_helm_command(cmd)

    try:
        # Try to parse JSON output
        release_info = json.loads(output)
        formatted_output = "INSTALLATION SUCCESSFUL:\n\n"
        formatted_output += f"NAME: {release_info.get('name', 'N/A')}\n"
        formatted_output += f"NAMESPACE: {release_info.get('namespace', 'N/A')}\n"
        formatted_output += f"STATUS: {release_info.get('info', {}).get('status', 'N/A')}\n"
        formatted_output += f"REVISION: {release_info.get('version', 'N/A')}\n"

        # Add notes if available
        notes = release_info.get('info', {}).get('notes')
        if notes:
            formatted_output += "\nNOTES:\n"
            formatted_output += notes

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Installation output:\n{output}"


def helm_upgrade(release_name: str, chart: str, namespace: Optional[str] = None,
                 values_file: Optional[str] = None, set_values: Optional[Dict[str, str]] = None,
                 install: bool = False, force: bool = False, atomic: bool = False,
                 timeout: Optional[str] = None, wait: bool = False) -> str:
    """
    Upgrades a release.
    """
    logger.info(f"Running helm upgrade with release={release_name}, chart={chart}")

    cmd = ["helm", "upgrade", release_name, chart]

    if namespace:
        cmd.extend(["-n", namespace])

    if values_file:
        cmd.extend(["-f", values_file])

    if set_values:
        for key, value in set_values.items():
            cmd.extend(["--set", f"{key}={value}"])

    if install:
        cmd.append("--install")

    if force:
        cmd.append("--force")

    if atomic:
        cmd.append("--atomic")

    if timeout:
        cmd.extend(["--timeout", timeout])

    if wait:
        cmd.append("--wait")

    cmd.extend(["--output", "json"])

    output = execute_helm_command(cmd)

    try:
        # Try to parse JSON output
        upgrade_info = json.loads(output)
        formatted_output = "UPGRADE SUCCESSFUL:\n\n"
        formatted_output += f"NAME: {upgrade_info.get('name', 'N/A')}\n"
        formatted_output += f"NAMESPACE: {upgrade_info.get('namespace', 'N/A')}\n"
        formatted_output += f"STATUS: {upgrade_info.get('info', {}).get('status', 'N/A')}\n"
        formatted_output += f"REVISION: {upgrade_info.get('version', 'N/A')}\n"

        # Add notes if available
        notes = upgrade_info.get('info', {}).get('notes')
        if notes:
            formatted_output += "\nNOTES:\n"
            formatted_output += notes

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Upgrade output:\n{output}"


def helm_uninstall(release_name: str, namespace: Optional[str] = None,
                   keep_history: bool = False, no_hooks: bool = False) -> str:
    """
    Uninstalls a release.
    """
    logger.info(f"Running helm uninstall with release={release_name}, namespace={namespace}")

    cmd = ["helm", "uninstall", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    if keep_history:
        cmd.append("--keep-history")

    if no_hooks:
        cmd.append("--no-hooks")

    return execute_helm_command(cmd)


def helm_rollback(release_name: str, revision: Optional[int] = None, namespace: Optional[str] = None,
                  timeout: Optional[str] = None, wait: bool = False, force: bool = False) -> str:
    """
    Rolls back a release to a previous revision.
    """
    logger.info(f"Running helm rollback with release={release_name}, revision={revision}")

    cmd = ["helm", "rollback", release_name]

    if revision is not None:
        cmd.append(str(revision))

    if namespace:
        cmd.extend(["-n", namespace])

    if timeout:
        cmd.extend(["--timeout", timeout])

    if wait:
        cmd.append("--wait")

    if force:
        cmd.append("--force")

    return execute_helm_command(cmd)


def helm_history(release_name: str, namespace: Optional[str] = None, max_: Optional[int] = None) -> str:
    """
    Gets the release history.
    """
    logger.info(f"Running helm history for release={release_name}, namespace={namespace}, max={max_}")

    cmd = ["helm", "history", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    if max_:
        cmd.extend(["--max", str(max_)])

    return execute_helm_command(cmd)


def helm_status(release_name: str, namespace: Optional[str] = None, revision: Optional[int] = None) -> str:
    """
    Displays the status of the named release.
    """
    logger.info(f"Running helm status with release={release_name}, namespace={namespace}")

    cmd = ["helm", "status", release_name, "--output", "json"]

    if namespace:
        cmd.extend(["-n", namespace])

    if revision:
        cmd.extend(["--revision", str(revision)])

    output = execute_helm_command(cmd)

    try:
        status = json.loads(output)

        formatted_output = f"STATUS: {status.get('info', {}).get('status', 'N/A')}\n"
        formatted_output += f"NAME: {status.get('name', 'N/A')}\n"
        formatted_output += f"NAMESPACE: {status.get('namespace', 'N/A')}\n"
        formatted_output += f"REVISION: {status.get('version', 'N/A')}\n"
        formatted_output += f"LAST DEPLOYED: {status.get('info', {}).get('last_deployed', 'N/A')}\n"

        # Add notes if available
        notes = status.get('info', {}).get('notes')
        if notes:
            formatted_output += "\nNOTES:\n"
            formatted_output += notes

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Status output:\n{output}"


def helm_list(namespace: Optional[str] = None, all_namespaces: bool = False,
              filter_: Optional[str] = None, uninstalled: bool = False,
              deployed: bool = False, failed: bool = False) -> str:
    """
    Lists all Helm releases.
    """
    logger.info(f"Running helm list with namespace={namespace}, all_namespaces={all_namespaces}")

    cmd = ["helm", "list", "--output", "json"]

    if namespace and not all_namespaces:
        cmd.extend(["-n", namespace])

    if all_namespaces:
        cmd.append("--all-namespaces")

    if filter_:
        cmd.extend(["-f", filter_])

    if uninstalled:
        cmd.append("--uninstalled")

    if deployed:
        cmd.append("--deployed")

    if failed:
        cmd.append("--failed")

    output = execute_helm_command(cmd)

    try:
        releases = json.loads(output)

        # Format the output for readability
        if not releases:
            return "No releases found."

        formatted_output = "RELEASE LIST:\n\n"
        formatted_output += "NAME\t\tNAMESPACE\t\tREVISION\t\tSTATUS\t\tCHART\t\tAPP VERSION\n"

        for release in releases:
            formatted_output += f"{release.get('name', 'N/A')}\t\t"
            formatted_output += f"{release.get('namespace', 'N/A')}\t\t"
            formatted_output += f"{release.get('revision', 'N/A')}\t\t"
            formatted_output += f"{release.get('status', 'N/A')}\t\t"
            formatted_output += f"{release.get('chart', 'N/A')}\t\t"
            formatted_output += f"{release.get('app_version', 'N/A')}\n"

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Release list:\n{output}"


def helm_test(release_name: str, namespace: Optional[str] = None,
              timeout: Optional[str] = None, filter_: Optional[str] = None) -> str:
    """
    Runs tests for a release.
    """
    logger.info(f"Running helm test with release={release_name}, namespace={namespace}")

    cmd = ["helm", "test", release_name]

    if namespace:
        cmd.extend(["-n", namespace])

    if timeout:
        cmd.extend(["--timeout", timeout])

    if filter_:
        cmd.extend(["--filter", filter_])

    return execute_helm_command(cmd)