import sys
import logging
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .core.server import HelmMCPServer


async def serve() -> None:
    """
    Main function to run the MCP server for Helm commands.
    """
    helm_server = HelmMCPServer()
    await helm_server.serve()


def main():
    """
    Entry point for the MCP Helm server when run as a command-line program.
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Starting MCP Helm server")

    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        logger.info("MCP Helm server stopped by user")
    except Exception as e:
        logger.error(f"Error running MCP Helm server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()