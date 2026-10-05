:root {
  --bg: #071116;
  --bg-soft: #0d1b24;
  --panel: rgba(12, 20, 27, 0.85);
  --panel-strong: #0d1b24;
  --panel-border: rgba(152, 182, 209, 0.18);
  --text: #edf4fb;
  --muted: #9ab0c2;
  --line: rgba(158, 195, 236, 0.16);
  --grid: rgba(144, 183, 242, 0.08);
  --brand: #8ec7ff;
  --brand-2: #6fe7d6;
  --brand-3: #b498ff;
  --shadow: rgba(5, 12, 18, 0.7);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: Inter, "Segoe UI", sans-serif;
  line-height: 1.65;
  color: var(--text);
  background:
    linear-gradient(rgba(7, 17, 22, 0.88), rgba(7, 17, 22, 0.97)),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px),
    linear-gradient(var(--grid) 1px, transparent 1px),
    var(--bg);
  background-size: auto, 26px 26px, 26px 26px, cover;
}

img {
  max-width: 100%;
  display: block;
}

a {
  color: var(--brand);
  text-decoration: none;
}

a:hover {
  color: var(--brand-2);
}

button,
input,
textarea {
  font: inherit;
}

.page-shell {
  min-height: 100vh;
}

.container {
  width: min(1180px, calc(100% - 2rem));
  margin: 0 auto;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(10px);
  background: rgba(7, 17, 22, 0.8);
  border-bottom: 1px solid var(--line);
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 78px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.7rem;
  color: var(--text);
  font-weight: 700;
  letter-spacing: 0.02em;
}

.brand-mark {
  color: var(--brand-2);
  font-size: 1.1rem;
  text-shadow: 0 0 18px rgba(111, 231, 214, 0.5);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-links a {
  color: var(--muted);
  position: relative;
  font-size: 0.96rem;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--text);
}

.nav-links a.active::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -0.5rem;
  height: 2px;
  background: linear-gradient(90deg, var(--brand), var(--brand-2));
}

.hero {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  align-items: center;
  gap: 3rem;
  min-height: 720px;
  padding-top: 2.5rem;
  padding-bottom: 2rem;
}

.eyebrow {
  margin: 0 0 1rem;
  color: var(--brand-2);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-size: 0.72rem;
  font-weight: 700;
}

.hero-copy h1 {
  margin: 0;
  font-size: clamp(3rem, 5vw, 5rem);
  line-height: 0.96;
  letter-spacing: -0.08em;
}

.lede {
  max-width: 640px;
  margin-top: 1.4rem;
  font-size: 1.12rem;
  color: var(--muted);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2rem;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--panel-border);
  border-radius: 999px;
  padding: 0.9rem 1.35rem;
  font-weight: 700;
  transition: transform 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
}

.button:hover {
  transform: translateY(-1px);
  border-color: rgba(142, 199, 255, 0.7);
}

.button-primary {
  background: linear-gradient(135deg, var(--brand), var(--brand-3));
  color: #071116;
  box-shadow: 0 14px 30px rgba(142, 199, 255, 0.2);
}

.button-secondary {
  background: rgba(13, 27, 36, 0.7);
  color: var(--text);
}

.signal-list {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin: 2rem 0 0;
  padding: 0;
}

.signal-list li {
  padding: 0.5rem 0.8rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(14, 23, 30, 0.7);
  color: var(--muted);
  font-size: 0.83rem;
}

.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.system-diagram {
  position: relative;
  width: min(420px, 100%);
  aspect-ratio: 1 / 1;
  background: radial-gradient(circle at center, rgba(111, 231, 214, 0.08), rgba(142, 199, 255, 0.04) 35%, transparent 70%);
  border: 1px solid var(--line);
  border-radius: 24px;
  box-shadow: 0 22px 80px var(--shadow);
}

.node {
  position: absolute;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 118px;
  min-height: 52px;
  padding: 0.65rem 0.8rem;
  border-radius: 12px;
  background: rgba(12, 20, 27, 0.9);
  border: 1px solid var(--line);
  color: var(--text);
  box-shadow: 0 12px 26px rgba(0, 0, 0, 0.2);
}

.node-one { top: 18%; left: 12%; }
.node-two { top: 10%; right: 12%; }
.node-core {
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(135deg, rgba(142, 199, 255, 0.18), rgba(111, 231, 214, 0.12));
}
.node-four { bottom: 14%; left: 50%; transform: translateX(-50%); }

.trace {
  position: absolute;
  display: block;
  background: linear-gradient(90deg, transparent, var(--brand-2), transparent);
}

.trace-one { left: 30%; top: 31%; width: 22%; height: 2px; }
.trace-two { right: 29%; top: 31%; width: 22%; height: 2px; }
.trace-three { left: 50%; top: 36%; width: 2px; height: 18%; transform: translateX(-50%); }
.trace-four { left: 50%; bottom: 30%; width: 2px; height: 16%; transform: translateX(-50%); }

.feature-band {
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  background: rgba(9, 16, 22, 0.7);
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.25rem;
  padding: 2.25rem 0;
}

.feature-card {
  background: rgba(12, 20, 27, 0.8);
  border: 1px solid var(--panel-border);
  border-radius: 18px;
  padding: 1.6rem;
  box-shadow: 0 16px 34px rgba(0, 0, 0, 0.18);
}

.feature-kicker {
  margin: 0 0 0.9rem;
  color: var(--brand-2);
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 700;
}

.feature-card h2 {
  margin: 0 0 0.7rem;
  font-size: 1.32rem;
}

.feature-card p {
  margin: 0;
  color: var(--muted);
}

.section {
  padding-top: 5rem;
  padding-bottom: 5rem;
}

.section-header {
  margin-bottom: 2rem;
}

.section-header h2 {
  margin: 0;
  max-width: 820px;
  font-size: clamp(2rem, 4vw, 3rem);
  line-height: 1.12;
}

.narrow {
  max-width: 760px;
}

.posts-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr;
  gap: 1.5rem;
}

.post-card,
.content-panel,
.principle-card,
.blog-card {
  background: rgba(12, 20, 27, 0.88);
  border: 1px solid var(--panel-border);
  border-radius: 18px;
  box-shadow: 0 18px 32px rgba(0, 0, 0, 0.18);
}

.post-card {
  padding: 1.6rem;
}

.post-featured {
  background: linear-gradient(180deg, rgba(14, 28, 36, 0.96), rgba(12, 20, 27, 0.88));
}

.meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.9rem;
}

.meta-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  border: 1px solid rgba(111, 231, 214, 0.3);
  color: var(--brand-2);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
}

.meta-date {
  color: var(--muted);
  font-size: 0.8rem;
}

.post-card h3 {
  margin: 0 0 0.8rem;
  font-size: 1.35rem;
  line-height: 1.3;
}

.post-card p,
.principle-card p,
.content-panel p,
.content-panel li,
.footer-copy,
.site-footer li,
.site-footer a,
.story-panel p {
  color: var(--muted);
}

.post-card a {
  display: inline-block;
  margin-top: 0.7rem;
  font-weight: 700;
}

.principle-section {
  padding-top: 0;
}

.principles-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.principle-card {
  padding: 1.6rem;
}

.principle-card h3 {
  margin-top: 0;
  margin-bottom: 0.7rem;
}

.page-header {
  padding-top: 4rem;
  padding-bottom: 1rem;
  text-align: center;
}

.page-header h1 {
  margin: 0;
  font-size: clamp(2.5rem, 4vw, 4rem);
  line-height: 1.08;
  letter-spacing: -0.06em;
}

.content-layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 1.5rem;
}

.content-panel {
  padding: 2rem;
}

.content-panel h2 {
  margin-top: 0;
  margin-bottom: 1rem;
}

.bullet-list {
  margin: 0;
  padding-left: 1.2rem;
  line-height: 2;
}

.blog-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contact-form label {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  color: var(--muted);
}

.contact-form input,
.contact-form textarea {
  background: rgba(7, 17, 22, 0.9);
  border: 1px solid var(--panel-border);
  border-radius: 12px;
  color: var(--text);
  padding: 0.85rem 0.9rem;
}

.contact-form input:focus,
.contact-form textarea:focus {
  outline: 2px solid rgba(142, 199, 255, 0.18);
  border-color: rgba(142, 199, 255, 0.7);
}

.site-footer {
  border-top: 1px solid var(--line);
  background: rgba(8, 13, 18, 0.9);
  margin-top: 3rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr 0.8fr;
  gap: 2rem;
  padding-top: 2.4rem;
  padding-bottom: 1.2rem;
}

.footer-brand {
  margin-bottom: 0.7rem;
}

.site-footer h3 {
  margin-top: 0;
  margin-bottom: 0.8rem;
}

.site-footer ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.site-footer li {
  margin-bottom: 0.45rem;
}

.footer-bottom {
  border-top: 1px solid var(--line);
  color: var(--muted);
  text-align: center;
  padding: 1.1rem 0 2rem;
}

@media (max-width: 900px) {
  .hero,
  .content-layout,
  .posts-grid,
  .principles-grid,
  .blog-grid,
  .feature-grid,
  .footer-grid {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
    padding-top: 3rem;
  }

  .nav {
    flex-direction: column;
    justify-content: center;
    gap: 0.7rem;
    padding: 0.7rem 0 1rem;
  }
}

@media (max-width: 560px) {
  .nav-links {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.8rem 1rem;
  }

  .button {
    width: 100%;
  }

  .page-header h1 {
    font-size: 2.3rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
  }
}

