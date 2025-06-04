import sys
import logging
from typing import Dict, List, Any

# Try to import mcp with error handling
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
except ImportError as e:
    print(f"Error importing MCP: {e}")
    print(f"Current Python path: {sys.path}")
    sys.exit(1)

from ..schemas.tools import get_all_tools
from ..commands import (
    basic, dependencies, get, release, repository,
    registry, search, show, package, plugin
)

logger = logging.getLogger(__name__)


class HelmMCPServer:
    """
    MCP Server for Helm commands.
    """
    
    def __init__(self):
        self.server = Server("mcp-helm")
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup the MCP server handlers."""
        
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            logger.info("Listing available tools")
            return get_all_tools()

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            logger.info(f"Tool call: {name} with arguments {arguments}")

            result = ""

            # Use a dictionary mapping for "switch-case" approach
            command_handlers = {
                # Basic commands
                "helm_completion": lambda: basic.helm_completion(arguments["shell"]),
                "helm_create": lambda: basic.helm_create(arguments["name"], arguments.get("starter")),
                "helm_env": lambda: basic.helm_env(),
                "helm_version": lambda: basic.helm_version(),
                "helm_verify": lambda: basic.helm_verify(
                    arguments["path"],
                    arguments.get("keyring")
                ),

                # Dependency commands
                "helm_dependency_build": lambda: dependencies.helm_dependency_build(arguments["chart_path"]),
                "helm_dependency_list": lambda: dependencies.helm_dependency_list(arguments["chart_path"]),
                "helm_dependency_update": lambda: dependencies.helm_dependency_update(arguments["chart_path"]),

                # Get commands
                "helm_get_all": lambda: get.helm_get_all(arguments["release_name"], arguments.get("namespace")),
                "helm_get_hooks": lambda: get.helm_get_hooks(arguments["release_name"], arguments.get("namespace")),
                "helm_get_manifest": lambda: get.helm_get_manifest(arguments["release_name"], arguments.get("namespace")),
                "helm_get_metadata": lambda: get.helm_get_metadata(arguments["release_name"], arguments.get("namespace")),
                "helm_get_notes": lambda: get.helm_get_notes(arguments["release_name"], arguments.get("namespace")),
                "helm_get_values": lambda: get.helm_get_values(
                    arguments["release_name"],
                    arguments.get("namespace"),
                    arguments.get("all_values", False)
                ),

                # Release management commands
                "helm_install": lambda: release.helm_install(
                    arguments["chart"],
                    arguments.get("release_name"),
                    arguments.get("namespace"),
                    arguments.get("values_file"),
                    arguments.get("set_values"),
                    arguments.get("description"),
                    arguments.get("timeout"),
                    arguments.get("wait", False),
                    arguments.get("atomic", False)
                ),
                "helm_upgrade": lambda: release.helm_upgrade(
                    arguments["release_name"],
                    arguments["chart"],
                    arguments.get("namespace"),
                    arguments.get("values_file"),
                    arguments.get("set_values"),
                    arguments.get("install", False),
                    arguments.get("force", False),
                    arguments.get("atomic", False),
                    arguments.get("timeout"),
                    arguments.get("wait", False)
                ),
                "helm_uninstall": lambda: release.helm_uninstall(
                    arguments["release_name"],
                    arguments.get("namespace"),
                    arguments.get("keep_history", False),
                    arguments.get("no_hooks", False)
                ),
                "helm_rollback": lambda: release.helm_rollback(
                    arguments["release_name"],
                    arguments.get("revision"),
                    arguments.get("namespace"),
                    arguments.get("timeout"),
                    arguments.get("wait", False),
                    arguments.get("force", False)
                ),
                "helm_history": lambda: release.helm_history(
                    arguments["release_name"],
                    arguments.get("namespace"),
                    arguments.get("max_")
                ),
                "helm_status": lambda: release.helm_status(
                    arguments["release_name"],
                    arguments.get("namespace"),
                    arguments.get("revision")
                ),
                "helm_list": lambda: release.helm_list(
                    arguments.get("namespace"),
                    arguments.get("all_namespaces", False),
                    arguments.get("filter_"),
                    arguments.get("uninstalled", False),
                    arguments.get("deployed", False),
                    arguments.get("failed", False)
                ),
                "helm_test": lambda: release.helm_test(
                    arguments["release_name"],
                    arguments.get("namespace"),
                    arguments.get("timeout"),
                    arguments.get("filter_")
                ),

                # Repository commands
                "helm_repo_add": lambda: repository.helm_repo_add(
                    arguments["name"],
                    arguments["url"],
                    arguments.get("username"),
                    arguments.get("password"),
                    arguments.get("pass_credentials", False)
                ),
                "helm_repo_remove": lambda: repository.helm_repo_remove(arguments["name"]),
                "helm_repo_list": lambda: repository.helm_repo_list(),
                "helm_repo_update": lambda: repository.helm_repo_update(),
                "helm_repo_index": lambda: repository.helm_repo_index(
                    arguments["directory"],
                    arguments.get("url"),
                    arguments.get("merge")
                ),

                # Registry commands
                "helm_registry_login": lambda: registry.helm_registry_login(
                    arguments["registry_url"],
                    arguments["username"],
                    arguments["password"],
                    arguments.get("insecure", False)
                ),
                "helm_registry_logout": lambda: registry.helm_registry_logout(arguments["registry_url"]),

                # Search commands
                "helm_search_repo": lambda: search.helm_search_repo(
                    arguments["keyword"],
                    arguments.get("version"),
                    arguments.get("regexp", False),
                    arguments.get("versions", False)
                ),
                "helm_search_hub": lambda: search.helm_search_hub(
                    arguments["keyword"],
                    arguments.get("max_results"),
                    arguments.get("repo_url")
                ),

                # Show commands
                "helm_show_all": lambda: show.helm_show_all(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version")
                ),
                "helm_show_chart": lambda: show.helm_show_chart(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version")
                ),
                "helm_show_crds": lambda: show.helm_show_crds(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version")
                ),
                "helm_show_readme": lambda: show.helm_show_readme(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version")
                ),
                "helm_show_values": lambda: show.helm_show_values(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version")
                ),

                # Package commands
                "helm_package": lambda: package.helm_package(
                    arguments["chart_path"],
                    arguments.get("destination"),
                    arguments.get("app_version"),
                    arguments.get("version"),
                    arguments.get("dependency_update", False)
                ),
                "helm_push": lambda: package.helm_push(
                    arguments["chart_path"],
                    arguments["registry_url"],
                    arguments.get("force", False),
                    arguments.get("insecure", False),
                    arguments.get("plain_http", False)
                ),
                "helm_pull": lambda: package.helm_pull(
                    arguments["chart"],
                    arguments.get("repo"),
                    arguments.get("version"),
                    arguments.get("destination"),
                    arguments.get("untar", False),
                    arguments.get("verify", False),
                    arguments.get("keyring")
                ),
                "helm_lint": lambda: package.helm_lint(
                    arguments["chart_path"],
                    arguments.get("values_file"),
                    arguments.get("set_values")
                ),
                "helm_template": lambda: package.helm_template(
                    arguments["chart"],
                    arguments.get("release_name"),
                    arguments.get("namespace"),
                    arguments.get("values_file"),
                    arguments.get("set_values"),
                    arguments.get("api_versions"),
                    arguments.get("kube_version")
                ),

                # Plugin commands
                "helm_plugin_install": lambda: plugin.helm_plugin_install(
                    arguments["plugin_url"],
                    arguments.get("version")
                ),
                "helm_plugin_list": lambda: plugin.helm_plugin_list(),
                "helm_plugin_uninstall": lambda: plugin.helm_plugin_uninstall(arguments["plugin_name"]),
                "helm_plugin_update": lambda: plugin.helm_plugin_update(arguments["plugin_name"]),
            }

            # Execute the corresponding handler or return an error if the command is not found
            if name in command_handlers:
                try:
                    result = command_handlers[name]()
                except Exception as e:
                    error_msg = f"Error executing {name}: {str(e)}"
                    logger.error(error_msg)
                    return [TextContent(type="text", text=error_msg)]
            else:
                error_msg = f"Unknown tool: {name}"
                logger.error(error_msg)
                return [TextContent(type="text", text=error_msg)]

            return [TextContent(type="text", text=result)]

    async def serve(self) -> None:
        """
        Main function to run the MCP server for Helm commands.
        """
        logger.info("Starting Helm MCP server")

        logger.info("Creating initialization options")
        options = self.server.create_initialization_options()

        logger.info("Starting stdio server")
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Running MCP server")
            await self.server.run(read_stream, write_stream, options, raise_exceptions=True)