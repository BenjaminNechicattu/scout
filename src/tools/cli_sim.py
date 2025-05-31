import subprocess

def execute_commands(commands):
    """
    Executes a list of command dicts and returns a list of outputs.
    Each command should be a dict with keys 'cmd' (str) and 'args' (list of str).
    Example: {"cmd": "ls", "args": ["-l", "/tmp"]}
    """
    outputs = []
    for command in commands:

        cmd = command.get("cmd")
        if not cmd:
            continue

        args = command.get("args", [])

        if args:
            result = subprocess.run([cmd] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            result = subprocess.run([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        outputs.append(result.stdout)
        
    return outputs