# Repository Guidelines

## Project Structure & Module Organization
Root scripts (`pandoc-enhanced`, `pandoc-emoji`) wrap pandoc to enable themes, QR codes, and emoji handling; keep CLI entry points at the repository root. Python helpers (`config_manager.py`, `generate_*.py`) live alongside those scripts and should stay import-free so they remain executable via `python3 <file>`. Assets belong in `data/` (e.g., default business-card artwork), while worked examples sit in `examples/` to double as manual test inputs. The vendored `eisvogel/` template directory mirrors upstream; modify it sparingly and document syncs. Generated artifacts (`output - V1.pdf`) are for reference only—avoid committing new binaries.

## Build, Test, and Development Commands
Run `./install.sh` (or `npm run install`) to create the `pandoc-enhanced` symlink, populate default config, and verify dependencies. Quick smoke tests use `npm test`, which executes `./pandoc-enhanced test_qrcode.md --debug` and prints the underlying pandoc call. During feature work, invoke `./pandoc-enhanced input.md -o output.pdf --debug` to validate new flags, and `python3 config_manager.py show <project_dir>` to inspect merged configuration.

## Coding Style & Naming Conventions
Python modules follow PEP 8 with four-space indentation, descriptive `snake_case` functions, and UTF-8 source headers when emitting CJK defaults. Bash utilities target `/bin/bash`, declare `set -e` (extend to `set -euo pipefail` for new scripts), indent with four spaces inside functions, and name environment variables in `UPPER_SNAKE_CASE`. Keep CLI option names kebab-cased (`--qrcode-url`) and reserve camelCase for JSON keys only when required by external tools.

## Testing Guidelines
There is no automated test harness beyond the smoke script, so author high-signal manual checks. Add minimal Markdown fixtures under `examples/` describing the scenario, then run `npm test` plus any custom `./pandoc-enhanced <fixture> ...` commands relevant to the change. When adjusting templates or fonts, visually diff the produced PDF and note regressions. Cover new flags in the help output and confirm they appear in the debug command line.

## Commit & Pull Request Guidelines
History relies on Conventional Commit prefixes (`feat:`, `fix:`, `add:`); continue that format with concise, imperative summaries. Each pull request should explain the user-facing impact, list the commands used to verify the change, and attach before/after snippets or PDF screenshots when UI or layout shifts occur. Reference related GitHub issues, flag configuration migrations, and call out any manual post-install steps contributors must run.
