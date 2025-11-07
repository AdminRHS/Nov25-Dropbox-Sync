# Task Breakdown - November 6, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Fix Crop Modal Window Opening

### Steps:
1. Open smt.js file and locate the crop button click event handler
2. Add console.log statements to debug the click event flow
3. Check if event.preventDefault() or event.stopPropagation() is blocking the modal
4. Verify the modal initialization code runs before the button click
5. Test the modal opening function independently to isolate the issue
6. Ensure no CSS display properties are preventing modal visibility
7. Check for JavaScript errors in browser console that might interrupt execution
8. Validate that the crop button has correct data attributes and IDs
9. Test across different scenarios (new upload vs existing image)
10. Commit working solution to GitHub

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Cropper.js Documentation](https://github.com/fengyuanchen/cropperjs)
- [JavaScript Event Handling Reference](https://developer.mozilla.org/en-US/docs/Web/API/Event)

### Instructions:

Start by identifying where the crop button click handler is defined in smt.js. Add debugging statements to trace the execution flow from button click to modal open attempt. Common issues include:
- Event bubbling conflicts with other click handlers
- Modal initialization happening after click event
- CSS z-index or display issues hiding the modal
- Missing or incorrect element selectors

Test the modal.show() or equivalent function directly in the console to verify it works independently. Once identified, implement the fix and test thoroughly before committing.


---

## Task 2: Resolve Edit Mode Card Disappearing Issue

### Steps:
1. Locate the renderAccountsView function in smt.js
2. Add console.log to track when cards are rendered and removed
3. Check the edit mode state management logic
4. Verify the card array is not being cleared during edit mode activation
5. Inspect DOM to see if cards exist but are hidden vs actually removed
6. Review CSS rules that might hide cards during edit mode
7. Check if event listeners are triggering unwanted re-renders
8. Ensure the Add Account card stays first without affecting other cards
9. Test edit mode toggle multiple times to reproduce the issue
10. Implement fix and verify cards persist across edit mode toggles

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [DOM Manipulation Best Practices](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [JavaScript State Management Patterns](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

### Instructions:

The issue likely stems from how the renderAccountsView function rebuilds the card display. Check if the function completely replaces the DOM content or updates it selectively. Ensure that:
- The accounts array maintains its data during edit mode
- The rendering logic doesn't filter out cards based on edit state
- CSS classes are applied correctly without hiding cards
- Event listeners don't trigger multiple renders that clear content

Add a persistent state flag to track edit mode and ensure the render function respects this flag when displaying cards.


---

## Task 3: Fix Add Account Button Modal Behavior

### Steps:
1. Find the Add Account button click handler in smt.js
2. Verify the button element selector is correct and unique
3. Check if multiple event listeners are attached to the same button
4. Add debugging to see if the click event fires consistently
5. Verify modal initialization code runs on page load
6. Check for conditional logic that might prevent modal opening
7. Test if the edit mode state affects the button's functionality
8. Ensure the modal HTML element exists in the DOM
9. Verify no CSS is hiding or disabling the button
10. Test the fix across different states (edit mode on/off)

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Modal Component Patterns](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/dialog_role)
- [Event Delegation](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_delegation)

### Instructions:

Investigate why the modal doesn't open consistently. Common causes include:
- Button being re-rendered, losing event listeners
- Multiple handlers causing conflicts
- Modal not properly initialized before button click
- Edit mode state interfering with modal display

Use event delegation if the button is dynamically created. Ensure the modal initialization happens in DOMContentLoaded or similar early event. Test by directly calling the modal open function to confirm the modal itself works.


---

## Task 4: Refine Fill/Fit/Crop Mode Logic

### Steps:
1. Review Figma's image display behavior for reference
2. Document expected behavior for each mode (Fill, Fit, Crop)
3. Locate the mode switching code in smt.js
4. Implement Fill mode: scale image to cover container, maintain aspect ratio
5. Implement Fit mode: scale image to fit within container, maintain aspect ratio
6. Implement Crop mode: enable Cropper.js for manual cropping
7. Add smooth CSS transitions between modes
8. Ensure image positioning is centered in all modes
9. Handle edge cases (very wide, very tall, square images)
10. Test with various image dimensions and aspect ratios

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Figma Design Reference](https://www.figma.com)
- [CSS object-fit Property](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
- [Cropper.js API](https://github.com/fengyuanchen/cropperjs#options)

### Instructions:

Study how Figma handles image display modes as your UX reference. Implement:

**Fill Mode**: Use CSS `object-fit: cover` to fill the container completely, cropping overflow
**Fit Mode**: Use CSS `object-fit: contain` to show the entire image within bounds
**Crop Mode**: Initialize Cropper.js with appropriate options for manual editing

Add mode toggle buttons with active state styling. Ensure transitions are smooth (CSS transition: all 0.3s ease). Store the selected mode in state to persist user preference.


---

## Task 5: Implement Crop Application Processing

### Steps:
1. Create a crop apply button in the crop modal
2. Get the cropped canvas data from Cropper.js using getCroppedCanvas()
3. Convert canvas to blob or data URL
4. Update the image preview with cropped result
5. Store cropped image data for form submission
6. Close the crop modal after applying
7. Update the card with the new cropped image
8. Ensure the original image is preserved (for re-cropping if needed)
9. Add loading state during crop processing
10. Handle errors gracefully with user feedback

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Cropper.js getCroppedCanvas](https://github.com/fengyuanchen/cropperjs#getcroppedcanvasoptions)
- [Canvas to Blob API](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob)

### Instructions:

The crop application workflow should:
1. User clicks "Apply" button in crop modal
2. Call `cropper.getCroppedCanvas()` to get the cropped image as canvas
3. Convert to data URL: `canvas.toDataURL('image/jpeg', 0.9)`
4. Update the preview image src with the data URL
5. Store data in form field or state for backend submission
6. Close modal and destroy cropper instance
7. Re-initialize cropper if user wants to edit again

Add visual feedback (spinner or progress indicator) during processing. Implement error handling for large images or browser limitations.


---

## Task 6: Fix Preview Update After Cropping

### Steps:
1. Identify the preview image element in the DOM
2. Create a function to update preview with new image data
3. Call this function after crop is applied
4. Ensure the preview container refreshes/re-renders
5. Check if image caching is preventing updates
6. Add cache-busting to image URLs if needed (timestamp parameter)
7. Verify the correct preview element is being updated
8. Test with multiple crop operations in sequence
9. Ensure preview maintains correct aspect ratio and sizing
10. Add smooth transition animation for preview updates

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Image Loading and Caching](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
- [CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

### Instructions:

After cropping, the preview must immediately reflect the changes. Implement:

```javascript
function updatePreview(croppedDataURL) {
  const preview = document.querySelector('#image-preview');
  preview.src = croppedDataURL;
  preview.classList.add('updated'); // trigger animation
}
```

If the preview doesn't update, the browser might be caching. Add a timestamp:
```javascript
preview.src = croppedDataURL + '?t=' + Date.now();
```

Ensure the preview element dimensions accommodate the new image. Add CSS transitions for smooth visual updates.


---

## Task 7: Verify Image Insertion into Cards

### Steps:
1. Locate the account card rendering function
2. Find where image data is inserted into card HTML
3. Test image insertion with new uploads
4. Test image insertion with cropped images
5. Verify image data is properly encoded (base64 or URL)
6. Check if card template includes correct image placeholder
7. Ensure image aspect ratio is maintained in card display
8. Test with various image formats (JPG, PNG, WebP)
9. Add fallback image for missing or failed loads
10. Validate final card appearance matches design specifications

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Base64 Image Encoding](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL)
- [Image Error Handling](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/error_event)

### Instructions:

Ensure the card rendering function properly inserts images:

```javascript
function renderCard(account) {
  const img = account.image || '/path/to/placeholder.png';
  return `
    <div class="account-card">
      <img src="${img}" alt="${account.name}" onerror="this.src='/fallback.png'">
      ...
    </div>
  `;
}
```

Test the complete flow: upload → crop → apply → card render. Verify:
- Image displays correctly in card
- Aspect ratio is preserved
- No broken image icons
- Fallback works for errors


---

## Task 8: Complete Cropper.js Behavior Integration

### Steps:
1. Review all Cropper.js configuration options
2. Set appropriate initial aspect ratio (or free crop)
3. Configure view mode for optimal display
4. Enable/disable features based on UX requirements (zoom, rotate, etc.)
5. Style Cropper.js controls to match light theme
6. Add custom toolbar with Figma-like controls
7. Implement keyboard shortcuts for common actions
8. Add touch/gesture support for mobile devices
9. Test cropper performance with large images
10. Optimize initialization and destroy lifecycle

### Resources and Links:
- [Project Repository](https://github.com/AdminRHS/AdminRHS-AI-Catalog-4)
- [Cropper.js Full API Documentation](https://github.com/fengyuanchen/cropperjs)
- [Cropper.js Examples](https://fengyuanchen.github.io/cropperjs/)
- [Custom Cropper Styling](https://github.com/fengyuanchen/cropperjs#styling)

### Instructions:

Initialize Cropper.js with optimal configuration:

```javascript
const cropper = new Cropper(imageElement, {
  viewMode: 1, // restrict crop box to canvas
  dragMode: 'move',
  aspectRatio: NaN, // free aspect ratio
  autoCropArea: 1,
  restore: false,
  guides: true,
  center: true,
  highlight: false,
  cropBoxMovable: true,
  cropBoxResizable: true,
  toggleDragModeOnDblclick: false,
  background: false, // matches light theme
});
```

Customize CSS to match your light theme (Figma/Telegram style). Override default Cropper.js styles in your stylesheet. Add custom controls for common operations (reset, rotate, flip). Ensure smooth performance by properly destroying cropper instances when modals close.


---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
