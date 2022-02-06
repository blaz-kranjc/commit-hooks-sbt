from typing import Sequence

from pre_commit_hooks.sbt_task import run_sbt_task


def main(argv: Sequence[str] | None = None) -> int:
    return run_sbt_task('compile')


if __name__ == '__main__':
    raise SystemExit(main())
