import json
import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_repo_add(name: str, url: str, username: Optional[str] = None,
                  password: Optional[str] = None, pass_credentials: bool = False) -> str:
    """
    Adds a chart repository.
    """
    logger.info(f"Running helm repo add with name={name}, url={url}")

    cmd = ["helm", "repo", "add", name, url]

    if username:
        cmd.extend(["--username", username])

    if password:
        cmd.extend(["--password", password])

    if pass_credentials:
        cmd.append("--pass-credentials")

    return execute_helm_command(cmd)


def helm_repo_remove(name: str) -> str:
    """
    Removes a chart repository.
    """
    logger.info(f"Running helm repo remove with name={name}")

    return execute_helm_command(["helm", "repo", "remove", name])


def helm_repo_list() -> str:
    """
    Lists chart repositories.
    """
    logger.info("Running helm repo list")

    output = execute_helm_command(["helm", "repo", "list", "--output", "json"])

    try:
        repos = json.loads(output)

        if not repos:
            return "No repositories found."

        formatted_output = "REPOSITORY LIST:\n\n"
        formatted_output += "NAME\t\tURL\n"

        for repo in repos:
            formatted_output += f"{repo.get('name', 'N/A')}\t\t"
            formatted_output += f"{repo.get('url', 'N/A')}\n"

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Repository list:\n{output}"


def helm_repo_update() -> str:
    """
    Updates chart repositories.
    """
    logger.info("Running helm repo update")

    return execute_helm_command(["helm", "repo", "update"])


def helm_repo_index(directory: str, url: Optional[str] = None, merge: Optional[str] = None) -> str:
    """
    Generates an index file for a chart repository.
    """
    logger.info(f"Running helm repo index with directory={directory}, url={url}")

    cmd = ["helm", "repo", "index", directory]

    if url:
        cmd.extend(["--url", url])

    if merge:
        cmd.extend(["--merge", merge])

    return execute_helm_command(cmd)