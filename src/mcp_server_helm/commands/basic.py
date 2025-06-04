import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_completion(shell: str) -> str:
    """
    Generates the autocompletion script for the specified shell.
    """
    logger.info(f"Running helm completion with shell={shell}")

    valid_shells = ["bash", "fish", "powershell", "zsh"]
    if shell not in valid_shells:
        return f"Invalid shell: {shell}. Valid options are: {', '.join(valid_shells)}"

    return execute_helm_command(["helm", "completion", shell])


def helm_create(name: str, starter: Optional[str] = None) -> str:
    """
    Creates a new chart with the given name.
    """
    logger.info(f"Running helm create with name={name}, starter={starter}")

    cmd = ["helm", "create", name]

    if starter:
        cmd.extend(["--starter", starter])

    return execute_helm_command(cmd)


def helm_env() -> str:
    """
    Shows Helm's environment information.
    """
    logger.info("Running helm env")

    return execute_helm_command(["helm", "env"])


def helm_version() -> str:
    """
    Shows the Helm version information.
    """
    logger.info("Running helm version")

    return execute_helm_command(["helm", "version", "--short"])


def helm_verify(path: str, keyring: Optional[str] = None) -> str:
    """
    Verifies that a chart at the given path has been signed and is valid.
    """
    logger.info(f"Running helm verify with path={path}")

    cmd = ["helm", "verify", path]

    if keyring:
        cmd.extend(["--keyring", keyring])

    return execute_helm_command(cmd)