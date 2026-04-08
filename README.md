# Project Init

> Standardized development template for AI-assisted product development.
> Optimized for **Antigravity** (Google DeepMind), compatible with other AI coding assistants.

---

## What is this?

Project Init is a curated collection of instructions, skills, workflows, and conventions that make AI coding agents significantly more effective. Instead of starting every project from scratch, copy this template to get:

- ✅ **Agent instructions** (`AGENTS.md`) — How the AI should behave, code, and communicate
- ✅ **8 production skills** — PR review, security audit, dependency check, performance profiling, CI/CD, tech debt, web design, react
- ✅ **9 workflows** — Step-by-step procedures for common tasks
- ✅ **Convention docs** — TypeScript, testing, React, and comment standards

## Quick Start

### 1. Copy to your new project

```bash
# Clone this template
git clone <this-repo-url> my-new-project
cd my-new-project

# Remove the template git history
rm -rf .git
git init
```

### 2. Customize AGENTS.md

Edit `AGENTS.md` to add project-specific context:
- Build & test commands
- Architecture overview
- Project-specific conventions

### 3. Start coding with AI

The agent will automatically read `AGENTS.md` and follow the established patterns.

## Structure

```
.
├── AGENTS.md                          # 🧠 Master instructions for AI agents
├── README.md                          # This file
├── .gitignore                         # Git ignore rules
│
├── .agent/
│   ├── skills/                        # 🛠️ Specialized AI skills
│   │   ├── pr-review-expert/          # PR review with blast radius analysis
│   │   ├── security-auditor/          # Security vulnerability scanning
│   │   ├── dependency-auditor/        # Dependency health & license check
│   │   ├── performance-profiler/      # Performance bottleneck detection
│   │   ├── ci-cd-pipeline-builder/    # CI/CD pipeline generation
│   │   ├── tech-debt-tracker/         # Tech debt scoring & tracking
│   │   ├── web-design-guidelines/     # UI/UX and web design review
│   │   └── react-useeffect/           # React hooks best practices
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
│       └── tech-docs.md               # Technical documentation writing
│
└── docs/                              # 📖 Convention documentation
    ├── typescript-conventions.md       # TypeScript standards
    ├── testing-conventions.md          # Testing patterns
    ├── react-best-practices.md        # React/Next.js optimization (45 rules)
    └── comment-policy.md              # Comment standards
```

## Skills

Each skill in `.agent/skills/` has a `SKILL.md` that the AI reads automatically when relevant. Available skills:

| Skill | What it does |
|-------|-------------|
| **pr-review-expert** | 30+ item checklist, blast radius analysis, security scan, test coverage delta |
| **security-auditor** | Code execution risks, prompt injection, supply chain, file system abuse |
| **dependency-auditor** | CVE scanning, license compliance, upgrade planning, bloat analysis |
| **performance-profiler** | CPU/memory profiling, bundle analysis, N+1 detection, load testing |
| **ci-cd-pipeline-builder** | Stack detection → GitHub Actions/GitLab CI generation |
| **tech-debt-tracker** | Debt scanning, scoring, prioritization, trend tracking |
| **web-design-guidelines** | Fetch and apply modern web semantic and aesthetic rules |
| **react-useeffect** | React hooks anti-patterns detection and state synchronization fixes |

## Workflows

Trigger workflows by referencing them:

| Workflow | Trigger |
|----------|---------|
| Code Review | "do a code review" or `/code-review` |
| Dependency Audit | "audit dependencies" or `/dependency-audit` |
| Deploy Check | "pre-deploy check" or `/deploy-check` |
| Interview | "interview me" or `/interview` |
| New Project | "setup a new project" or `/new-project` |
| OSS Research | "research library" or `/oss-research` |
| Planning | "create a plan" or `/planning` |
| PRD | "write a PRD" or `/prd` |
| Tech Docs | "write technical docs" or `/tech-docs` |

## Credits

Resources adapted from:
- [jarrodwatts/claude-code-config](https://github.com/jarrodwatts/claude-code-config) — Rules, skills, agents
- [mar_antaya](https://twitter.com/mar_antaya) — Production skills
- [Manus Context Engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents) — Planning principles
- [steveyegge/beads](https://github.com/steveyegge/beads) — Issue tracking

## License

MIT
