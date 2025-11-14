
---

# Task Breakdown - 11.11.2025

## Instructions

**What:** Detailed, actionable tasks for improving and finalizing the portfolio website (v1.1).
**Include:**

* Clear, step-by-step actions
* Links to relevant docs, tools, and resources
* Execution guidance for each task

---

## Task 1: Refine Header & Navigation

### Steps:

1. Add smooth scroll functionality using the `scroll-behavior: smooth` property or `react-scroll`.
2. Implement active link highlighting using Intersection Observer API.
3. Adjust spacing, padding, and alignment in the `Header` component.
4. Test and fix mobile menu scroll-lock behavior.
5. Verify navigation works on all screen sizes.

### Resources and Links:

* [MDN: Scroll-behavior CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior)
* [React Scroll library](https://www.npmjs.com/package/react-scroll)
* [Intersection Observer Guide](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)

### Instructions:

Open `Header.tsx` and implement smooth scrolling between sections. Use Intersection Observer to highlight the currently visible section in the navigation bar.
Ensure the mobile menu disables background scrolling when active. Test on both mobile and desktop to confirm responsiveness and UX consistency.

---

## Task 2: UI Polish & Section Transitions

### Steps:

1. Add fade-in or slide-up animations for sections using **Framer Motion** or **AOS (Animate On Scroll)**.
2. Refine typography, margins, and paddings for consistent spacing.
3. Add hover and focus animations for buttons, links, and project cards.
4. Test all transitions across browsers for smooth performance.

### Resources and Links:

* [Framer Motion Docs](https://www.framer.com/motion/)
* [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/)
* [Tailwind CSS Transition Utilities](https://tailwindcss.com/docs/transition-property)

### Instructions:

Enhance user experience with subtle motion effects. Start by wrapping each section in a Framer Motion `<motion.div>` and applying staggered fade-in effects.
Adjust Tailwind spacing classes to improve visual balance. Finally, test hover and focus states for accessibility and clarity.

---

## Task 3: Add Real Project Data

### Steps:

1. Replace all placeholder GitHub URLs in `projects.json` with actual repository links.
2. Add project descriptions and tech stack for each entry.
3. Capture screenshots of each project (desktop & mobile views).
4. Save screenshots to `src/assets/projects/` and reference them in JSON.
5. Test image rendering and responsive layout in the Projects section.

### Resources and Links:

* [GitHub Profile](https://github.com/artem-skichko)
* [React Docs: Using Images](https://react.dev/learn/importing-and-exporting-components#adding-images-css-and-other-files)
* [Tailwind Responsive Design](https://tailwindcss.com/docs/responsive-design)

### Instructions:

Open `projects.json` and replace all placeholder data. Capture screenshots with Chrome DevTools Device Toolbar (Ctrl+Shift+M).
Update paths in your component to display project images dynamically. Commit changes once all projects render properly with their real data and links.

---

## Task 4: Update README.md

### Steps:

1. Add screenshots to the “Screenshots” section using Markdown image syntax.
2. Include the live demo link and version badge (`v1.1`).
3. Update Features and Future Improvements lists.
4. Verify all markdown formatting and internal links.
5. Run a preview in VS Code or GitHub before committing.

### Resources and Links:

* [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
* [Shields.io Badges](https://shields.io/)
* [GitHub Pages URL](https://artem-skichko.github.io/your-repo-name/)

### Instructions:

Open `README.md`, replace placeholder links and images with real data.
Insert version badge and deployment URL.
Ensure headings, lists, and links are properly formatted for readability.
Run preview and fix layout issues before committing.

---

## Task 5: Accessibility & Performance Review

### Steps:

1. Run Lighthouse audit (Ctrl + Shift + I → Lighthouse tab).
2. Review and address accessibility issues (`alt`, `aria-label`, semantic HTML).
3. Compress large images with TinyPNG or Squoosh.
4. Review `vite.config.js` and optimize build output if needed.
5. Re-run audit until scores exceed 90 in all categories.

### Resources and Links:

* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
* [TinyPNG Image Optimizer](https://tinypng.com/)
* [Web.dev Accessibility Guide](https://web.dev/accessible/)

### Instructions:

Perform Lighthouse tests on both localhost and deployed versions.
Add missing accessibility attributes and compress all heavy assets.
Document improvements in `CHANGELOG.md` once scores reach target values.

---

## Task 6: Documentation Updates

### Steps:

1. Update `CHANGELOG.md` with today’s commits and improvements.
2. Create `DEVELOPER_NOTES.md` explaining AI-assisted workflow (Cursor, Gemini, Claude, ChatGPT).
3. Link `CONTRIBUTING.md` in README under “How to Contribute.”
4. Review for grammar and structure consistency.

### Resources and Links:

* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
* [Markdown Table Reference](https://www.markdownguide.org/extended-syntax/#tables)

### Instructions:

Summarize today’s changes in `CHANGELOG.md` using commit messages as references.
Document your AI-assisted workflow in `DEVELOPER_NOTES.md` (tools used, benefits, best practices).
Ensure all documentation links are valid and easily navigable.

---

## Task 7: Final Verification & Deployment

### Steps:

1. Run a production build (`npm run build`).
2. Push updates to GitHub and trigger GitHub Pages deployment.
3. Verify the deployed version on desktop and mobile.
4. Check all links, animations, and assets in production.
5. Tag release `v1.1` and commit final changes.

### Resources and Links:

* [GitHub Pages Deployment Guide](https://vitejs.dev/guide/static-deploy.html#github-pages)
* [Vite Build Command Reference](https://vitejs.dev/guide/cli.html#build)
* [GitHub Tagging Docs](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

### Instructions:

Ensure no build errors occur.
Once deployed, test navigation, responsiveness, and animations in the live environment.
Tag the final version (`v1.1`) and confirm the demo link in the README is active and up-to-date.

---

## Reminder

* Break down each task into clear, achievable steps.
* Use provided resources for guidance and troubleshooting.
* Document all significant changes in `CHANGELOG.md`.
* Review deployment before tagging release.

---
