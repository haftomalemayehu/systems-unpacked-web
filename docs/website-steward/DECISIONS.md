# Website Steward — Decision and Audit Log

## 2026-11-21 — Agent established
- Baseline: `main` includes the five-stage modernization via merged PR #22.
- Existing URL: https://systems-unpacked.com/
- Governance: review-only PRs; no merges or deployments without explicit approval.
- Known verification gap: live production, accessibility, security headers and browser CI pass status not established in this record.
- Next review: inspect current main, CI and production independently; propose evidence-backed improvements.
- Open decisions: confirm preferred review cadence and which changes may be proposed automatically.

## 2026-11-23 — Weekly evidence review (proposed; pending PR)
- Baseline: main at `c30bf940dfac4a8fcf75ff83f9a14dc9cd88a201`; PR #27 merged, no open PRs at start of audit.
- GitHub Actions: main static checks succeeded on 2026-11-22 (run 45051623417). Browser smoke workflow only triggers on pull requests, leaving final merged main without browser verification. This PR adds a main-push trigger; no new browser run is claimed.
- Source: static HTML/CSS, one local JPG (~134 KB), local SVG assets, resume PDF (~40 KB) and QR SVG (~6 KB); no root package.json/lockfile in inspected tree. Browser test installs Playwright 1.58.2 without a committed lockfile; Node 22, Python 3.12; actions/checkout@v4, setup-node@v4, setup-python@v5. Workflow token scope contents:read. Full dependency/advisory/license review not completed.
- Production: website homepage and resume URL inaccessible to web inspection; TLS, headers, live links, PDF delivery, QR scan, 390px/1440px rendering, Lighthouse and real-user LCP/INP/CLS **not verified**.
- Security: GitHub Dependabot/code/secret scanning alerts endpoints inaccessible through current connector (not a clean scan); third-party scripts, HTTP headers, external link rel attributes and privacy-policy accuracy require further verification.
- Editorial: existing IDP article remains in repository with “EDITORIAL DRAFT” marker; actual publication status unverified. New Terraform module contracts draft prepared separately as PR #28.

### Risk register (open)
| ID | Severity | Evidence | Proposed mitigation | Validation | Owner/status |
| --- | --- | --- | --- | --- | --- |
| SU-01 | P1 | Main-push browser checks absent from browser-smoke workflow | Trigger browser checks on main after merge | New main-push workflow success and 390px/1440px smoke results | Steward; this PR pending |
| SU-02 | P1 | Live domain inaccessible to web inspection; previous Safari DNS error reported | Verify Cloudflare Pages custom domain, DNS, TLS, production deployment | Public DNS resolution, HTTP status, headers, homepage and resume URL | Owner; pending |
| SU-03 | P2 | No measured performance baseline or verified production QR scan | Run mobile/desktop Lighthouse and real-device resume QR test | Record dated LCP/INP/CLS and test artifacts | Steward/owner; pending |
| SU-04 | P2 | GitHub alert endpoints not available through connector; Playwright installed without lockfile | Owner review of Security tab; consider lockfile/reproducible browser test installation | Alert inventory, npm audit/lock validation, passing CI | Steward/owner; pending |

### Decisions and guardrails
- Propose only; no merge, deploy, DNS, secret or policy changes without owner approval.
- Keep original public URLs and resume artifacts intact.
- Follow up on dependency release/EOL advisories using verified official changelogs before proposing upgrades.
