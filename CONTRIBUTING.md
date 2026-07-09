# Contributing to code-security-research

This project uses a strict commit and pull request policy. The goal is to keep history easy to review, easy to bisect, and useful for future AI-assisted maintenance.

## Branch Rules

- `main` must stay deployable.
- Do not push directly to `main`.
- Create topic branches from `main`:
  - `feature/<short-name>` for features or new sub-genres
  - `fix/<short-name>` for bug fixes in scripts or content
  - `docs/<short-name>` for documentation-only work
  - `chore/<short-name>` for maintenance or vault reorganization
- Keep branches short-lived. Rebase on `main` before opening a PR if the branch is stale.

## Commit Format

Every commit must use Conventional Commits:

```text
<type>(<scope>): <description>
```

Examples:
```text
feat(vault): add 2.9 mutation testing sub-genre
fix(script): resolve syntax error in setup_vault
docs(readme): update obsidian vault usage guide
feat(papers): add raven program repair paper note
```

## Commit Types

| Type | Use for |
| --- | --- |
| `feat` | New user-facing capability, category, or major note |
| `fix` | Bug fix in script or content corrections |
| `refactor` | Internal restructuring (e.g. script cleanup) with no behavior change |
| `docs` | Documentation only |
| `test` | Tests and test validation scripts |
| `chore` | Tooling, config, repository maintenance |
| `style` | Formatting only, no behavior change |
| `perf` | Performance improvement (e.g. script runtime optimization) |
| `security` | Security or privacy hardening |

## Commit Scopes

The allowed scopes for this repository are:

| Scope | Area |
| --- | --- |
| `vault` | Category notes, markdown pages, index, vault directory structure |
| `script` | Code security research scripts (e.g. `setup_vault.py`) |
| `template` | Note templates (e.g. `Paper Template.md`) |
| `papers` | New research paper markdown files |
| `ci` | CI pipeline and repository policy config |
| `docs` | Repository general documentation (`README.md`, `CONTRIBUTING.md`) |
| `deps` | Environment, dependencies, package management |

Use a new scope only when none of the above is accurate.

## Commit Message Rules

- Use English.
- Keep the subject under 72 characters (per Conventional Commits official recommendation).
- Use lowercase after the colon.
- Do not end the subject with a period.
- Do not use vague subjects like `update files`, `fix bug`, or `misc changes`.
- Reference issues in the body, not the subject.

## Atomic Commit Rules

One commit must represent one logical change.
- Separate unrelated category edits.
- Separate script updates from manual markdown changes.
- Separate example papers from category structure updates.

## Pull Request Rules

PR titles must also follow Conventional Commits:

```text
<type>(<scope>): <description>
```

PR descriptions must include:
- Summary
- Key Changes
- Verification
- Data/Privacy Impact

## Verification Expectations

Before requesting review, include the checks you ran. At minimum:
- **Vault changes**: Verify all double bracket links work and point to existing category files.
- **Script changes**: Run `python setup_vault.py` and verify all categories are generated cleanly with no Python errors.
- **Paper entries**: Check that YAML frontmatter is well-formed and categories contain links.

## Privacy Rules

- Never commit real API keys, personal access tokens, or private research findings.
- Use placeholders for templates.
