# Task Breakdown - November 5, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Fix Card Disappearance Bug in Account Management

**Priority:** HIGH
**Timeline:** Tomorrow (Nov 6)
**Status:** In Progress

### Steps:
1. Review the code where edit mode is activated in Account Management tab
2. Identify where cards are being cleared or hidden (check for .innerHTML = '', display:none, or container clearing)
3. Change logic to use class-based state management instead of DOM manipulation
4. Ensure cards remain in DOM and simply toggle edit state via CSS class
5. Test edit mode activation/deactivation multiple times
6. Verify "+ Add Account" card appears correctly without affecting existing cards
7. Test account creation while edit mode is active
8. Confirm no temporary disappearances during any action

### Resources and Links:
- Account Management section code
- Edit mode toggle logic
- Card rendering functions
- Browser DevTools for debugging DOM changes

### Instructions:
The bug occurs because edit mode activation is clearing the container or applying display:none. Instead of manipulating the DOM directly, use a state class (e.g., 'edit-mode-active') on the container and handle visibility through CSS. This preserves the cards while allowing mode switching. Test thoroughly with all account types (Free/Freemium/Paid) to ensure stability.

---

## Task 2: Complete Cropper.js Visual Markers

**Priority:** HIGH
**Timeline:** 2 days
**Status:** Not Started

### Steps:
1. Review Cropper.js documentation for visual marker configuration
2. Enable crop box and corner handles in Cropper.js initialization options
3. Style crop markers to match macOS/Telegram aesthetic (white borders, subtle shadows)
4. Configure crop area background dimming/overlay
5. Add visual feedback for draggable corners (cursor changes, hover states)
6. Implement grid lines or rule-of-thirds overlay (optional)
7. Test crop manipulation with various image sizes and aspect ratios
8. Ensure Apply button correctly captures cropped region

### Resources and Links:
- Cropper.js official documentation: https://github.com/fengyuanchen/cropperjs
- Current crop modal implementation
- macOS and Telegram crop UI references
- CSS styling for crop markers

### Instructions:
Cropper.js has built-in visual markers, but they need to be properly configured and styled. Initialize with options like `viewMode`, `dragMode`, `cropBoxResizable`, and `cropBoxMovable`. Style the crop box (.cropper-crop-box) and handles (.cropper-point) to match the white-border aesthetic established in the modal. Ensure users can clearly see and manipulate the crop boundaries.

---

## Task 3: Finalize Account Creation Flow

**Priority:** HIGH
**Timeline:** 2 days
**Status:** In Progress

### Steps:
1. Test complete flow: Click "+ Add Account" → Fill form → Select tool type → Create
2. Verify all three tool types (Free/Freemium/Paid) create correctly
3. Ensure new account card appears immediately in the grid
4. Check that edit mode stays active after account creation
5. Test form validation (required fields, proper error messages)
6. Verify form clears after successful creation
7. Test account creation with image upload
8. Ensure no conflicts with existing accounts

### Resources and Links:
- Account creation form code
- Card rendering logic
- Tool type selection UI
- Form validation functions

### Instructions:
Walk through the entire account creation flow multiple times with different scenarios: with/without images, different tool types, required vs optional fields. Ensure smooth transitions and no UI glitches. The "+ Add Account" card should remain clickable after creation, and the modal should close cleanly. Test edge cases like rapidly creating multiple accounts or canceling mid-creation.

---

## Task 4: Manual Code Cleanup and Restructuring

**Priority:** MEDIUM
**Timeline:** End of week
**Status:** Not Started

### Steps:
1. Create full backup of current working code
2. Identify duplicate HTML blocks (search for repeated IDs or similar structures)
3. Remove unused CSS classes and styles (use DevTools coverage tool)
4. Consolidate redundant JavaScript functions
5. Clean one section at a time (e.g., modal HTML first, then styles, then scripts)
6. Test functionality after each cleanup pass
7. Document what was removed and why
8. Commit changes incrementally with descriptive messages

### Resources and Links:
- Chrome DevTools CSS Coverage tool
- Version control (Git)
- Code comparison/diff tools
- HTML/CSS validator

### Instructions:
After the Gemini AI cleanup was too aggressive, manual cleanup is safer. Work methodically: backup, clean one small section, test, commit, repeat. Use browser DevTools Coverage tool to identify unused CSS. Search for duplicate IDs or class names in HTML. Comment out code before deleting to make reverting easier. Prioritize removing truly unused code rather than optimizing existing code structure.

---

## Task 5: Test and Polish All Edit Mode Features

**Priority:** MEDIUM
**Timeline:** End of week
**Status:** Not Started

### Steps:
1. Create comprehensive test checklist for both AI Catalog and Account Management tabs
2. Test edit mode activation/deactivation with checkmark and X buttons
3. Verify dashed card highlighting appears correctly
4. Test all card actions: create, edit, delete on both tabs
5. Check image upload, crop, and delete functionality
6. Test tag autocomplete in all relevant fields
7. Verify modal windows open/close smoothly
8. Test keyboard navigation and accessibility

### Resources and Links:
- Both tab implementations (AI Catalog and Account Management)
- Edit mode toggle controls
- All modal windows
- User acceptance testing checklist

### Instructions:
Create a systematic testing checklist covering all features across both tabs. Test not just happy paths but also edge cases: rapid clicking, keyboard shortcuts, browser back button, refreshing during edit mode. Document any inconsistencies between AI Catalog and Account Management implementations. Ensure visual consistency (colors, spacing, animations) across all components.

---

## Task 6: Implement Beautiful Confirmation Window

**Priority:** MEDIUM
**Timeline:** 1 week
**Status:** Not Started

### Steps:
1. Design confirmation window in Figma matching macOS/Telegram style
2. Create HTML structure for confirmation modal
3. Style with white borders, smooth dimming, and balanced spacing
4. Add clear action buttons (Confirm/Cancel or Yes/No)
5. Implement smooth fade-in/fade-out animations
6. Add appropriate confirmation messages for different actions
7. Test confirmation flow for various actions (delete card, exit edit mode, etc.)
8. Ensure keyboard support (Enter to confirm, Esc to cancel)

### Resources and Links:
- Existing modal window styles
- Figma mockups for confirmation dialogs
- macOS system dialog references
- Animation/transition CSS

### Instructions:
The confirmation window should match the established macOS/Telegram aesthetic: white borders, soft shadows, smooth background dimming. Keep the message clear and concise. Provide obvious action buttons with appropriate colors (blue for confirm, gray for cancel). The window should feel lightweight and non-intrusive. Consider adding icons for different confirmation types (warning, info, success).

---

## Task 7: Enhance Hover Effects and Animations

**Priority:** LOW
**Timeline:** 1 week
**Status:** Not Started

### Steps:
1. Audit all interactive elements for current hover states
2. Add smooth CSS transitions to buttons and icons (0.2-0.3s)
3. Implement card hover effects (subtle lift or shadow increase)
4. Add smooth animations for modal open/close
5. Animate card appearance when creating new items
6. Add loading states with smooth spinners or progress indicators
7. Implement smooth scrolling where appropriate
8. Test animations performance on slower devices

### Resources and Links:
- CSS transition and animation documentation
- Current hover effect implementations
- Animation best practices guides
- Performance testing tools

### Instructions:
Subtle animations enhance perceived quality without slowing the interface. Use CSS transitions for simple state changes (hover, focus) and CSS animations or JavaScript for complex sequences. Keep durations short (200-300ms for most transitions). Add easing functions (ease-in-out) for natural motion. Test on lower-end devices to ensure animations don't cause jank or stuttering.

---

## Task 8: Cross-Browser Compatibility Testing

**Priority:** LOW
**Timeline:** 2 weeks
**Status:** Not Started

### Steps:
1. Set up testing environment with Chrome, Firefox, Safari, and Edge
2. Test all core functionality in each browser
3. Check CSS rendering (Flexbox, Grid, custom properties)
4. Verify JavaScript features work (ES6+, Cropper.js library)
5. Test image upload and cropping in all browsers
6. Check modal window behavior and positioning
7. Document any browser-specific issues
8. Implement polyfills or fallbacks for compatibility issues

### Resources and Links:
- BrowserStack or CrossBrowserTesting for remote testing
- Can I Use website for feature compatibility checks
- Browser-specific debugging tools
- Polyfill resources (if needed)

### Instructions:
Modern browsers are generally compatible, but test thoroughly especially in Safari which can have quirks. Pay attention to CSS custom properties, Flexbox/Grid, and newer JavaScript features. Test Cropper.js specifically as it manipulates DOM and Canvas. Check file input behavior across browsers. Document any visual differences and decide if they're acceptable or need fixing.

---

## Task 9: Create Design System Documentation

**Priority:** LOW
**Timeline:** 2 weeks
**Status:** Not Started

### Steps:
1. Catalog all UI components (buttons, modals, cards, forms, icons)
2. Document color palette and usage guidelines
3. Document typography (fonts, sizes, weights, line heights)
4. Document spacing system (margins, padding, grid)
5. Create component usage examples and code snippets
6. Document interaction patterns (hover, click, drag, etc.)
7. Capture Figma mockups as reference images
8. Create README or wiki page with all documentation

### Resources and Links:
- Current Figma designs
- All implemented components
- Design system examples (Material Design, IBM Carbon, etc.)
- Project documentation repository

### Instructions:
Good design system documentation makes future development faster and more consistent. Organize by component type (buttons, forms, modals, etc.). For each component, include: visual example, code snippet, usage guidelines, and variations. Document the reasoning behind design decisions (why macOS/Telegram style, why square photo frames, etc.). Include do's and don'ts with examples.

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
