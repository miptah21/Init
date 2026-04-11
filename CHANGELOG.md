# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.0] - 2026-04-11

### Changed
- **AGENTS.md rewritten** — 532→168 lines via progressive disclosure. Behavioral details moved to `docs/implementation-protocol.md` and `docs/communication-style.md`
- **npm→bunx consistency** — All skills and workflows now use `bunx` exclusively
- **Workflow frontmatter** — All 10 workflows have YAML frontmatter with descriptions
- **Situational workflow triggers** — Workflows now fire based on activity patterns, not just slash commands
- **.gitignore cleanup** — Removed dead yarn/npm/pnp rules

### Added
- `.editorconfig` — Cross-editor formatting consistency
- `tsconfig.json` — Strict TypeScript template configuration
- `package.json` — Minimal template with placeholder scripts
- `.gitattributes` — Line ending normalization
- `LICENSE` — MIT license text
- `CHANGELOG.md` — This file
- `docs/implementation-protocol.md` — Delegation, verification, failure recovery
- `docs/communication-style.md` — Agent communication rules
- `.agent/skills/git-workflow/` — Commit conventions, branch naming, PR templates
- `.agent/workflows/reflect.md` — Self-reflection and AGENTS.md auto-improvement

### Removed
- `docs/react-best-practices-full.md` — 62KB vendored file (use condensed version instead)
- Duplicate Skill Invocation table from AGENTS.md
- Duplicate Workflow Invocation table from AGENTS.md
- Duplicate code standards content from AGENTS.md

## [1.0.0] - 2026-04-08

### Added
- Initial release
- 8 skills: pr-review-expert, security-auditor, dependency-auditor, performance-profiler, ci-cd-pipeline-builder, tech-debt-tracker, web-design-guidelines, react-useeffect
- 9 workflows: code-review, dependency-audit, deploy-check, interview, new-project, oss-research, planning, prd, tech-docs
- 4 convention docs: typescript-conventions, testing-conventions, react-best-practices, comment-policy
- AGENTS.md with behavioral rules and conventions
