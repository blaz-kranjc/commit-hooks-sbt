# pre-commit-sbt

Pre-commit hooks for sbt based projects for use with [pre-commit](https://github.com/pre-commit/pre-commit).

## Using pre-commit-sbt with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/blaz-kranjc/pre-commit-sbt
    rev: v1.0.0 # Use the ref you want to point at
    hooks:
    -   id: sbt-test
    # -   id: ...
```

## Available hooks

* `sbt-compile`
Checks that `sbt compile` completes successfully.

* `sbt-test`
Checks that `sbt test` completes successfully.

* `sbt-task`
Checks that provided sbt task completes successfully.
Use `args: [<task>]` with the desired task.
