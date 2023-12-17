import subprocess


def get_autorandr_profile():
    return subprocess.check_output("autorandr --current", shell=True, text=True).strip()
