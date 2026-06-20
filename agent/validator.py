SAFE_COMMANDS = {
    "get",
    "describe",
    "logs",
    "top"
}


def validate(command: str):
    command = command.strip()

    if not command.startswith("kubectl"):
        return False

    parts = command.split()

    if len(parts) < 2:
        return False

    verb = parts[1]

    return verb in SAFE_COMMANDS
