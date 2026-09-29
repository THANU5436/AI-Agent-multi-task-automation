import subprocess
import tempfile
import os


def execute_python_code(code, user_input=""):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as file:

        file.write(code)
        file_path = file.name

    try:

        result = subprocess.run(
            ["python", file_path],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=10
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "output": "",
            "error": "Code execution timed out."
        }

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)