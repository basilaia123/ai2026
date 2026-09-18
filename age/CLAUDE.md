# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This repository is currently empty of source code. It contains only:
- `README.md` — describes the intended project (see below)
- `.kilo/.gitignore` — a gitignore stub for a future Node.js project (ignores `node_modules`, lockfiles, `package.json`, `agent-manager.json`); no code or tooling has been added yet

There are no build, lint, or test commands yet because no project has been scaffolded.

## Intended Purpose (from README.md)

This is meant to become a Telegram bot that automatically tracks a user's expenses. The bot determines the amount and category of each expense itself, and only saves a record after the user confirms it — nothing is saved without confirmation.

When scaffolding the actual implementation, the `.kilo/.gitignore` contents suggest a Node.js-based stack is expected (npm/pnpm/yarn/bun all ignored), so plan tooling and structure accordingly unless the user directs otherwise.
