import argparse
import os
import subprocess
from shutil import which
from typing import Sequence


def run_sbt_task(task: str) -> int:
    sbt_path = which('sbt', mode=os.X_OK)
    if not sbt_path:
        print('sbt not found in path')
        return 1

    proc = subprocess.run([sbt_path, task])
    if proc.returncode != 0:
        print(f'sbt task {task} failed')

    return proc.returncode


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('task', metavar='task', type=str)
    args = parser.parse_args()
    return run_sbt_task(args.task)


if __name__ == '__main__':
    raise SystemExit(main())
