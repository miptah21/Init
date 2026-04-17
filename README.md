# Project Init

[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-standard-blue)](https://agents.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Development template for AI-assisted TypeScript/JavaScript projects.
> Optimized for **Antigravity** (Google DeepMind), compatible with other AI coding assistants.

---

## What is this?

Project Init is a curated collection of instructions, skills, workflows, and conventions that make AI coding agents significantly more effective. It follows the [AGENTS.md](https://agents.md) open standard (Linux Foundation). Copy this template to get:

- ✅ **Agent instructions** (`AGENTS.md`) — Slim, focused behavioral rules (~200 lines)
- ✅ **33 skills** — PR review, security audit, web design, testing, Python, Node, data analysis, and more
- ✅ **10 workflows** — Step-by-step procedures including self-reflection
- ✅ **Convention docs** — TypeScript, testing, React/Next.js, comments, implementation protocol, communication style
- ✅ **Token optimization** — [RTK](https://github.com/rtk-ai/rtk) integration rules for 60-90% token savings on shell outputs

### Stack Focus

This template is optimized for **TypeScript/JavaScript** projects using **Bun** as the runtime. For other stacks (Python, Go, Rust):
- Remove JS-specific convention docs from `docs/`
- Remove React-specific skills if not applicable
- Add your own convention docs

## Quick Start

### 1. Copy to your new project

```bash
git clone <this-repo-url> my-new-project
cd my-new-project
rm -rf .git && git init
```

### 2. Customize AGENTS.md

Edit `AGENTS.md` to add project-specific context:
- Build & test commands
- Architecture overview
- Project-specific conventions

### 3. Install dependencies

```bash
bun install
```

### 4. Remove what you don't need

- Not using React? Remove `docs/react-best-practices.md` and `.agents/skills/react-useeffect/`
- Not using TypeScript? Remove `docs/typescript-conventions.md`
- See `/new-project` workflow for the full setup checklist

### 5. Start coding with AI

The agent reads `AGENTS.md` automatically and follows established patterns.

## Structure

```
.
├── AGENTS.md                          # 🧠 Agent behavioral rules (~170 lines)
├── README.md                          # This file
├── CHANGELOG.md                       # Version history
├── LICENSE                            # MIT license
├── package.json                       # Template package config
├── tsconfig.json                      # TypeScript configuration
├── .editorconfig                      # Editor formatting consistency
├── .gitattributes                     # Line ending normalization
├── .gitignore                         # Git ignore rules
│
├── .agents/
│   ├── skills/                        # 🛠️ Structured prompt templates
│   │   ├── pr-review-expert/          # PR review with blast radius analysis
│   │   ├── security-auditor/          # Security vulnerability scanning
│   │   ├── dependency-auditor/        # Dependency health & license check
│   │   ├── performance-profiler/      # Performance bottleneck detection
│   │   ├── ci-cd-pipeline-builder/    # CI/CD pipeline generation
│   │   ├── tech-debt-tracker/         # Tech debt scoring & tracking
│   │   ├── web-design-guidelines/     # UI/UX review (vendored guidelines)
│   │   ├── react-useeffect/           # React hooks best practices
│   │   └── git-workflow/              # Commit, branch, PR conventions
│   │
│   └── workflows/                     # 📋 Step-by-step procedures
│       ├── code-review.md             # Code review workflow
│       ├── dependency-audit.md        # Dependency audit workflow
│       ├── deploy-check.md            # Pre-deployment checklist
│       ├── interview.md               # Interactive user interviewing
│       ├── new-project.md             # New project setup
│       ├── oss-research.md            # Open-source library research
│       ├── planning.md                # Multi-step task planning
│       ├── prd.md                     # Product requirements drafting
│       ├── reflect.md                 # Self-reflection & improvement
│       └── tech-docs.md               # Technical documentation writing
│
└── docs/                              # 📖 On-demand convention docs
    ├── typescript-conventions.md       # TypeScript standards
    ├── testing-conventions.md          # Testing patterns
    ├── react-best-practices.md        # React/Next.js optimization
    ├── comment-policy.md              # Comment standards
    ├── implementation-protocol.md     # Delegation, verification, recovery
    └── communication-style.md         # Agent communication rules
```

## Skills

| Skill | What it does |
|-------|-------------|
| **pr-review-expert** | 30+ item checklist, blast radius analysis, security scan |
| **security-auditor** | Code execution risks, prompt injection, supply chain |
| **dependency-auditor** | CVE scanning, license compliance, upgrade planning |
| **performance-profiler** | CPU/memory profiling, bundle analysis, N+1 detection |
| **ci-cd-pipeline-builder** | Stack detection → GitHub Actions/GitLab CI generation |
| **tech-debt-tracker** | Debt scanning, scoring, prioritization, trend tracking |
| **web-design-guidelines** | Vendored Vercel guidelines + 10-point review checklist |
| **react-useeffect** | React hooks anti-patterns and state sync fixes |
| **git-workflow** | Conventional commits, branch naming, PR templates |
| **seo-optimizer** | Strategy, technical SEO, keywords |
| **ag-md-improver** | Audit, check, and improve AGENTS.md |
| **agentic-eval** | Self-critique, evaluator-optimizer pipelines |
| **algorithmic-art** | Seeded randomness, interactive parameters |
| **canvas-design** | Visual art in .png and .pdf |
| **chrome-devtools** | Chrome DevTools MCP, profiling, network |
| **clean-code** | Concise, direct, no over-engineering |
| **database-design** | Indexing, ORM, serverless databases |
| **docx** | Create, read, edit Word docs |
| **frontend-design** | Distinctive, production-grade interfaces |
| **image-manipulation-image-magick** | Resize, convert, batch process |
| **knowledge-synthesis** | Combine sources, deduplicate, attribute |
| **nextjs-best-practices** | Server Components, routing, data fetching |
| **payload** | Schema, hooks, access control |
| **pdf** | Read, merge, split, watermark, OCR |
| **playwright** | E2E automation via terminal |
| **python-expert** | Best practices, PEP 8, debugging |
| **react-patterns** | Hooks, composition, performance |
| **refactor** | Improve maintainability, eliminate smells |
| **skill-writer** | Author/design new SKILL.md files |
| **uv-package-manager** | Fast dependency management with uv |
| **webapp-testing** | Playwright-based local UI debugging |
| **worktree-manager** | Create/manage git worktrees |
| **xlsx** | Open, read, edit, clean tabular data |

## Workflows

| Workflow | Trigger |
|----------|---------|
| Code Review | `/code-review` or reviewing changes |
| Dependency Audit | `/dependency-audit` or checking packages |
| Deploy Check | `/deploy-check` or pushing to prod |
| Interview | `/interview` or vague requirements |
| New Project | `/new-project` or starting fresh |
| OSS Research | `/oss-research` or evaluating libraries |
| Planning | `/planning` or complex multi-step tasks |
| PRD | `/prd` or writing feature specs |
| Reflect | `/reflect` or end of major tasks |
| Tech Docs | `/tech-docs` or writing documentation |

## Design Principles

1. **Progressive Disclosure** — Root AGENTS.md is <200 lines. Details in on-demand `docs/` files
2. **Single Source of Truth** — Each convention lives in one file, referenced from AGENTS.md
3. **Situational Triggers** — Skills and workflows fire based on activity patterns, not just commands
4. **Self-Improving** — The `/reflect` workflow updates conventions based on real experience
5. **Cross-Tool Compatible** — Follows [AGENTS.md](https://agents.md) standard (Linux Foundation/AAIF)

## Credits

- [AGENTS.md Standard](https://agents.md) — Open format by AAIF/Linux Foundation
- [jarrodwatts/claude-code-config](https://github.com/jarrodwatts/claude-code-config) — Rules, skills, agents
- [Manus Context Engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents) — Planning principles
- [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) — UI guidelines

## License

MIT — see [LICENSE](LICENSE)
