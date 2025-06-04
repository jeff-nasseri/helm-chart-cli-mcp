from mcp.types import Tool


def get_all_tools():
    """
    Returns all tool definitions for the Helm MCP server.
    """
    return [
        # Completion tools
        Tool(
            name="helm_completion",
            description="Generates the autocompletion script for the specified shell",
            inputSchema={
                "type": "object",
                "properties": {
                    "shell": {
                        "type": "string",
                        "enum": ["bash", "fish", "powershell", "zsh"]
                    }
                },
                "required": ["shell"]
            },
        ),

        # Create tool
        Tool(
            name="helm_create",
            description="Creates a new chart with the given name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "starter": {"type": "string"}
                },
                "required": ["name"]
            },
        ),

        # Dependency tools
        Tool(
            name="helm_dependency_build",
            description="Builds the chart's dependencies",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"}
                },
                "required": ["chart_path"]
            },
        ),
        Tool(
            name="helm_dependency_list",
            description="Lists the dependencies for the given chart",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"}
                },
                "required": ["chart_path"]
            },
        ),
        Tool(
            name="helm_dependency_update",
            description="Updates the chart's dependencies",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"}
                },
                "required": ["chart_path"]
            },
        ),

        # Environment tool
        Tool(
            name="helm_env",
            description="Shows Helm's environment information",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),

        # Get tools
        Tool(
            name="helm_get_all",
            description="Gets all information about a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),
        Tool(
            name="helm_get_hooks",
            description="Gets the hooks for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),
        Tool(
            name="helm_get_manifest",
            description="Gets the manifest for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),
        Tool(
            name="helm_get_metadata",
            description="Gets the metadata for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),
        Tool(
            name="helm_get_notes",
            description="Gets the notes for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),
        Tool(
            name="helm_get_values",
            description="Gets the values for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "all_values": {"type": "boolean"}
                },
                "required": ["release_name"]
            },
        ),

        # History tool
        Tool(
            name="helm_history",
            description="Gets the release history",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "max_": {"type": "integer"}
                },
                "required": ["release_name"]
            },
        ),

        # Install tool
        Tool(
            name="helm_install",
            description="Installs a chart",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "values_file": {"type": "string"},
                    "set_values": {"type": "object"},
                    "description": {"type": "string"},
                    "timeout": {"type": "string"},
                    "wait": {"type": "boolean"},
                    "atomic": {"type": "boolean"}
                },
                "required": ["chart"]
            },
        ),

        # Lint tool
        Tool(
            name="helm_lint",
            description="Runs a series of tests to verify that the chart is well-formed",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"},
                    "values_file": {"type": "string"},
                    "set_values": {"type": "object"}
                },
                "required": ["chart_path"]
            },
        ),

        # List tool
        Tool(
            name="helm_list",
            description="Lists releases",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string"},
                    "all_namespaces": {"type": "boolean"},
                    "filter_": {"type": "string"},
                    "uninstalled": {"type": "boolean"},
                    "deployed": {"type": "boolean"},
                    "failed": {"type": "boolean"}
                },
                "required": []
            },
        ),

        # Package tool
        Tool(
            name="helm_package",
            description="Packages a chart into a chart archive",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"},
                    "destination": {"type": "string"},
                    "app_version": {"type": "string"},
                    "version": {"type": "string"},
                    "dependency_update": {"type": "boolean"}
                },
                "required": ["chart_path"]
            },
        ),

        # Plugin tools
        Tool(
            name="helm_plugin_install",
            description="Installs a Helm plugin",
            inputSchema={
                "type": "object",
                "properties": {
                    "plugin_url": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["plugin_url"]
            },
        ),
        Tool(
            name="helm_plugin_list",
            description="Lists Helm plugins",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="helm_plugin_uninstall",
            description="Uninstalls a Helm plugin",
            inputSchema={
                "type": "object",
                "properties": {
                    "plugin_name": {"type": "string"}
                },
                "required": ["plugin_name"]
            },
        ),
        Tool(
            name="helm_plugin_update",
            description="Updates a Helm plugin",
            inputSchema={
                "type": "object",
                "properties": {
                    "plugin_name": {"type": "string"}
                },
                "required": ["plugin_name"]
            },
        ),

        # Pull tool
        Tool(
            name="helm_pull",
            description="Downloads a chart from a repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"},
                    "destination": {"type": "string"},
                    "untar": {"type": "boolean"},
                    "verify": {"type": "boolean"},
                    "keyring": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),

        # Push tool
        Tool(
            name="helm_push",
            description="Pushes a chart to a registry",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_path": {"type": "string"},
                    "registry_url": {"type": "string"},
                    "force": {"type": "boolean"},
                    "insecure": {"type": "boolean"},
                    "plain_http": {"type": "boolean"}
                },
                "required": ["chart_path", "registry_url"]
            },
        ),

        # Registry tools
        Tool(
            name="helm_registry_login",
            description="Logs in to a registry",
            inputSchema={
                "type": "object",
                "properties": {
                    "registry_url": {"type": "string"},
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "insecure": {"type": "boolean"}
                },
                "required": ["registry_url", "username", "password"]
            },
        ),
        Tool(
            name="helm_registry_logout",
            description="Logs out from a registry",
            inputSchema={
                "type": "object",
                "properties": {
                    "registry_url": {"type": "string"}
                },
                "required": ["registry_url"]
            },
        ),

        # Repo tools
        Tool(
            name="helm_repo_add",
            description="Adds a chart repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "pass_credentials": {"type": "boolean"}
                },
                "required": ["name", "url"]
            },
        ),
        Tool(
            name="helm_repo_index",
            description="Generates an index file for a chart repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {"type": "string"},
                    "url": {"type": "string"},
                    "merge": {"type": "string"}
                },
                "required": ["directory"]
            },
        ),
        Tool(
            name="helm_repo_list",
            description="Lists chart repositories",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="helm_repo_remove",
            description="Removes a chart repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="helm_repo_update",
            description="Updates chart repositories",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),

        # Rollback tool
        Tool(
            name="helm_rollback",
            description="Rolls back a release to a previous revision",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "revision": {"type": "integer"},
                    "namespace": {"type": "string"},
                    "timeout": {"type": "string"},
                    "wait": {"type": "boolean"},
                    "force": {"type": "boolean"}
                },
                "required": ["release_name"]
            },
        ),

        # Search tools
        Tool(
            name="helm_search_repo",
            description="Searches repositories for a keyword in charts",
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string"},
                    "version": {"type": "string"},
                    "regexp": {"type": "boolean"},
                    "versions": {"type": "boolean"}
                },
                "required": ["keyword"]
            },
        ),
        Tool(
            name="helm_search_hub",
            description="Searches the Helm Hub for a keyword in charts",
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string"},
                    "max_results": {"type": "integer"},
                    "repo_url": {"type": "string"}
                },
                "required": ["keyword"]
            },
        ),

        # Show tools
        Tool(
            name="helm_show_all",
            description="Shows all information of a chart",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),
        Tool(
            name="helm_show_chart",
            description="Shows the chart's definition",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),
        Tool(
            name="helm_show_crds",
            description="Shows the chart's CRDs",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),
        Tool(
            name="helm_show_readme",
            description="Shows the chart's README",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),
        Tool(
            name="helm_show_values",
            description="Shows the chart's values",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "repo": {"type": "string"},
                    "version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),

        # Status tool
        Tool(
            name="helm_status",
            description="Displays the status of the named release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "revision": {"type": "integer"}
                },
                "required": ["release_name"]
            },
        ),

        # Template tool
        Tool(
            name="helm_template",
            description="Renders chart templates locally and displays the output",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart": {"type": "string"},
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "values_file": {"type": "string"},
                    "set_values": {"type": "object"},
                    "api_versions": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "kube_version": {"type": "string"}
                },
                "required": ["chart"]
            },
        ),

        # Test tool
        Tool(
            name="helm_test",
            description="Runs tests for a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "timeout": {"type": "string"},
                    "filter_": {"type": "string"}
                },
                "required": ["release_name"]
            },
        ),

        # Uninstall tool
        Tool(
            name="helm_uninstall",
            description="Uninstalls a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "namespace": {"type": "string"},
                    "keep_history": {"type": "boolean"},
                    "no_hooks": {"type": "boolean"}
                },
                "required": ["release_name"]
            },
        ),

        # Upgrade tool
        Tool(
            name="helm_upgrade",
            description="Upgrades a release",
            inputSchema={
                "type": "object",
                "properties": {
                    "release_name": {"type": "string"},
                    "chart": {"type": "string"},
                    "namespace": {"type": "string"},
                    "values_file": {"type": "string"},
                    "set_values": {"type": "object"},
                    "install": {"type": "boolean"},
                    "force": {"type": "boolean"},
                    "atomic": {"type": "boolean"},
                    "timeout": {"type": "string"},
                    "wait": {"type": "boolean"}
                },
                "required": ["release_name", "chart"]
            },
        ),

        # Verify tool
        Tool(
            name="helm_verify",
            description="Verifies that a chart at the given path has been signed and is valid",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "keyring": {"type": "string"}
                },
                "required": ["path"]
            },
        ),

        # Version tool
        Tool(
            name="helm_version",
            description="Shows the Helm version information",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
    ]