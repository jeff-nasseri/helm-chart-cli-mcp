import json
import logging
from typing import Optional
from ..core.utils import execute_helm_command

logger = logging.getLogger(__name__)


def helm_search_repo(keyword: str, version: Optional[str] = None, regexp: bool = False,
                     versions: bool = False) -> str:
    """
    Searches repositories for a keyword in charts.
    """
    logger.info(f"Running helm search repo with keyword={keyword}")

    cmd = ["helm", "search", "repo", keyword, "--output", "json"]

    if version:
        cmd.extend(["--version", version])

    if regexp:
        cmd.append("--regexp")

    if versions:
        cmd.append("--versions")

    output = execute_helm_command(cmd)

    try:
        charts = json.loads(output)

        if not charts:
            return f"No charts found for keyword: {keyword}"

        formatted_output = "SEARCH RESULTS:\n\n"
        formatted_output += "NAME\t\tCHART VERSION\t\tAPP VERSION\t\tDESCRIPTION\n"

        for chart in charts:
            formatted_output += f"{chart.get('name', 'N/A')}\t\t"
            formatted_output += f"{chart.get('version', 'N/A')}\t\t"
            formatted_output += f"{chart.get('app_version', 'N/A')}\t\t"
            formatted_output += f"{chart.get('description', 'N/A')}\n"

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Search results:\n{output}"


def helm_search_hub(keyword: str, max_results: Optional[int] = None,
                    repo_url: Optional[str] = None) -> str:
    """
    Searches the Helm Hub for a keyword in charts.
    """
    logger.info(f"Running helm search hub with keyword={keyword}")

    cmd = ["helm", "search", "hub", keyword, "--output", "json"]

    if max_results:
        cmd.extend(["--max-col-width", str(max_results)])

    if repo_url:
        cmd.extend(["--repository-url", repo_url])

    output = execute_helm_command(cmd)

    try:
        charts = json.loads(output)

        if not charts:
            return f"No charts found for keyword: {keyword}"

        formatted_output = "HUB SEARCH RESULTS:\n\n"
        formatted_output += "URL\t\tCHART VERSION\t\tAPP VERSION\t\tDESCRIPTION\n"

        for chart in charts:
            formatted_output += f"{chart.get('url', 'N/A')}\t\t"
            formatted_output += f"{chart.get('version', 'N/A')}\t\t"
            formatted_output += f"{chart.get('app_version', 'N/A')}\t\t"
            formatted_output += f"{chart.get('description', 'N/A')}\n"

        return formatted_output
    except json.JSONDecodeError:
        # If output is not JSON, return raw output
        return f"Hub search results:\n{output}"