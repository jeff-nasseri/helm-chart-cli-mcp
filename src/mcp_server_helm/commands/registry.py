import logging
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_registry_login(registry_url: str, username: str, password: str,
                        insecure: bool = False) -> str:
    """
    Logs in to a registry.
    """
    logger.info(f"Running helm registry login with registry_url={registry_url}, username={username}")

    cmd = ["helm", "registry", "login", registry_url,
           "--username", username, "--password-stdin"]

    if insecure:
        cmd.append("--insecure")

    return execute_helm_command(cmd, stdin_input=password)


def helm_registry_logout(registry_url: str) -> str:
    """
    Logs out from a registry.
    """
    logger.info(f"Running helm registry logout with registry_url={registry_url}")

    return execute_helm_command(["helm", "registry", "logout", registry_url])