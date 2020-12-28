import subprocess


def get_date():
    return subprocess.check_output(["date"]).decode()