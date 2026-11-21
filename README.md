# Systems Unpacked Website

Public, static HTML/CSS website for **Systems Unpacked**, a cloud architecture, platform engineering, and AI systems publication and professional portfolio.

Production site: https://systems-unpacked.com/

## Site structure

- `index.html` — homepage and featured engineering topics
- `about/index.html` — publication mission and engineering approach
- `projects/index.html` — reference architectures, project concepts, and guides
- `blog/index.html` — upcoming technical article topics (not published full articles)
- `resume/index.html` — public resume viewer and PDF download
- `contact/index.html` — public contact information
- `privacy/index.html` and `terms/index.html` — legal information
- `assets/styles.css` — shared styling
- `assets/resume/` — intentionally public resume PDF and QR SVG

## Local preview

This site has no build step or frontend package dependencies. From the repository root, run:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/`. Use an HTTP server rather than opening files directly, because links use root-relative paths.

## Validation

Run the dependency-free source checks:

```sh
python3 scripts/check_site.py
```

The same checks run in GitHub Actions for pull requests and pushes to `main`. They verify local links, referenced assets, metadata, page headings, and public crawler files. They do **not** replace a browser-based accessibility audit, Lighthouse audit, security-header inspection, or production smoke test.

## Deployment and change control

The repository is intended to be served as a static site by Cloudflare Pages. Verify the actual Cloudflare Pages project settings before changing deployment configuration. Open a pull request, review the diff and CI results, and obtain human approval before merging to `main`. A merge may trigger automatic production deployment depending on Cloudflare settings. Confirm the deployed commit and check key pages and assets afterward.

Do not commit API keys, OAuth tokens, secrets, private contact details, or private resume versions. The PDF under `assets/resume/` is publicly accessible by design. Changes to publishing integrations and Google OAuth controls are outside the scope of this static site.

## Content standards

- Distinguish **reference designs**, **prototypes**, and **implemented projects**.
- Do not claim production deployments or outcomes without verifiable evidence.
- Publish full articles only when their complete content exists; label planned topics accordingly.
- Review technical guidance and provider-specific details regularly.
- Keep the sitemap and canonical URLs consistent with the public domain.

## Browser verification

Pull requests also run Playwright smoke checks on desktop and mobile viewports. These check page responses, headings, horizontal overflow, mobile menu behavior and the inline CI/CD SVG dimensions. To run locally, install Node.js 22 and Playwright, serve the repository on port 8000, then run `node scripts/browser-smoke.cjs`. Production Cloudflare security headers, accessibility audits, external links and live deployment status require separate verification.
