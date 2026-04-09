# Repository Guidelines

## Project Structure & Module Organization
This repository is a collection of standalone course and marketing pages. There is no shared application runtime or build pipeline.

- `lectures/`: main AI course materials, typically `lecture-X-slides.html`, `lecture-X-summary.html`, `lecture-X-study-guide.html`, and related homework pages.
- `ai4teens/`: teen course slide decks and course pages.
- `gipa/`, `tempo/`, `art/`, `oppa/`, `chatgpt.ge/`: independent program or client-specific HTML content.
- `dead_offers/`: archived material; treat as read-only unless explicitly asked.
- Root docs such as `CLAUDE.md` and `GEMINI.md` describe repository-specific workflow expectations.

## Build, Test, and Development Commands
There is no `npm`, bundler, or formal test suite in this repo. Work directly on the HTML files and verify changes in a browser.

- `start lectures/index.html`: open the main course index locally on Windows.
- `start tempo/index.html`: preview the Tempo deck locally.
- `git status --short`: review edited, new, and deleted files before committing.
- `push.bat`: stage all changes, create a timestamped commit, and push to `origin/master`.

## Coding Style & Naming Conventions
Keep files self-contained: HTML with embedded CSS/JS is the project norm. Preserve existing page structure and visual language within each directory.

- Use 2-space indentation in HTML, CSS, and inline JavaScript.
- Prefer descriptive file names already used by the repo, such as `lecture-4-summary.html` or `homework-7.html`.
- Keep Georgian text UTF-8 safe; do not replace technical terms like `API`, `prompt`, or `ROI`.
- Reuse existing patterns before inventing new components, especially in `lectures/` and `tempo/`.

## Testing Guidelines
Testing is manual. After edits, open the affected page and check layout, navigation, and any inline scripts.

- Verify links, buttons, slide navigation, and mobile responsiveness.
- If you touch `gipa/`, re-check the session-based password flow on `gipa/index.html`.
- When editing lecture series, confirm neighboring files still follow the same naming and navigation pattern.

## Commit & Pull Request Guidelines
Recent history uses short operational subjects such as `update Thu 04/09/2026 0:33:28.58`, plus occasional `CHECKPOINT:` commits for larger restructures. Follow one of those two styles consistently.

- Keep commits focused on one content area or program.
- In PRs, include the affected directories, a short summary of user-visible changes, and screenshots for layout-heavy edits.
- Call out renamed or archived files explicitly so reviewers can validate links and references.
