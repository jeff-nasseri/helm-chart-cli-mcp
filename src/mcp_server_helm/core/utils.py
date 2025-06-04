import subprocess
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


def execute_helm_command(cmd: List[str], stdin_input: Optional[str] = None) -> str:
    """
    Execute a Helm command and return the formatted output.
    """
    logger.info(f"Executing command: {' '.join(cmd)}")

    try:
        if stdin_input:
            # Use Popen to provide input via stdin
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=stdin_input)

            if process.returncode != 0:
                error_msg = f"Error executing command: {stderr}"
                logger.error(error_msg)
                return error_msg

            return stdout
        else:
            # Use subprocess.run for commands without stdin input
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
    except subprocess.CalledProcessError as e:
        error_msg = f"Error executing command: {e.stderr}"
        logger.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logger.error(error_msg)
        return error_msg