# PAT Debugger

PAT Debugger (`patdb`) is a fork of Panther Analysis Tool that adds an extra `debug` command. This command is useful for troubleshooting errors or unexpectd behaviour in rules. The other commands (`upload`, `test`, etc.) are intended to be unchanged from the main PAT, but caution is advised regardless if trying to fully replace PAT with `patdb`.

## Installation

Follow these steps to install and configure `patdb`. These instructios are for using `zsh` on OSX - you may need to adjust them for other shells and platforms.

### Prerequisities

Make sure you have the following dependencies installed before continuing:
- git
- python (version 3.9)
- pipx

### Instructions

1. Clone the repo using `git clone https://github.com/ben-githubs/patdb.git`. The location of the clone is not important.
1. Run `pipx install -e .`
1. Confirm the install worked by running `patdb --version`. If you see output, then install was successful!

### Upgrading

The upgrade process is handled through `git`, not `pipx`. To upgrade to a newer version of `patdb`, follow these steps:

1. In a terminal, `cd` to the directory hosting the `patdb` repo.
1. Run `git pull origin` to pull any changes.

Once the pull is complete, changes should be apparent. Use `patdb --version` to ensure the new version is working.

## Usage

Usage is simple: if you followed the instructions above, you should be able to invoke `patdb` from your terminal. For uploading, testing, etc, use the same commands and arguments as PAT. For debugging, see below.

The syntax for debugging is as follows:

```bash
patdb [RULE_ID] [TEST_NAME]
```

The `debug` command differs from the usual `test` command in the following ways:

- `debug` only runs a single test for a single rule - `test` runs all tests for all rules.
- You can print output to the terminal when using `debug` - for example, `print("hello world")` doesn't do anything when testing, but when debugging, will print `hello world` to the screen.
- You can use breakpoints within your rule code with `debug`. You can technically use them in `pat test` as well, but it'll lead to your rule seemingly hanging, since the interactive prompt isn't displayed when testing.
- `debug` will print the full traceback for any exceptions during rule execution, unlike `test`, which only prints the immediate error text.
- `debug` won't print summary statistics on whether a rule passes or fails.