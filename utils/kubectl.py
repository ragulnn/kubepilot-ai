import subprocess


def run_kubectl(command: str):
    result = subprocess.run(
        ["kubectl"] + command.split(),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout
