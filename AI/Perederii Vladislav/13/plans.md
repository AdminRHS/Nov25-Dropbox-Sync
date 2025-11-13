#### **Detailed Daily Plan**

**Morning Session: Code Stabilization and Optimization – Solving the "Reviews" Button Issue (9:00 AM - 12:30 PM)**

**Context:** Before launching a multi-hour processing cycle across hundreds of companies, we need to fix a known issue that is slowing down the process and reducing reliability. The morning will be entirely dedicated to this engineering task.

* **9:00 AM - 12:30 PM: Reworking the search and click logic for the "Reviews" tab.**
* **What will be done (step by step):**
1. **Diagnostics (9:00 AM - 9:45 AM):** Run the script in normal (non-headless) mode on several "problem" companies to visually understand why the current method isn't working. Is the button not visible? Is it obscured by another element? Is it delayed in appearing?
2. **Finding and implementing alternative solutions (9:45 - 12:00):**
* **Option A (Most likely): Explicit Wait.** Remove the current "Json-click" and implement the standard Selenium construct with `WebDriverWait` and `element_to_be_clickable`. This will force the script to wait until the button becomes visible and clickable, but no longer than the specified timeout (e.g., 10-15 seconds).
* **Option B: A more robust selector.** Analyze the HTML code and find a more stable selector for the button, such as XPath based on text or attributes that don't change dynamically.
* **Option C (Fallback): Direct URL navigation.** Try to see if it's possible to create a direct link to the reviews tab to avoid the need for a click altogether. 3. **Testing and Verification (12:00 - 12:30):** Run the updated script on 15-20 different companies to ensure the new solution works quickly and reliably 100% of the time.
* **Expected Result:** The bottleneck in the code has been eliminated. The script runs significantly faster and more reliably, which is critical for processing large data sets.

**Afternoon Session: Final "Production" Run – Processing All 450 Companies (1:30 - 6:00 PM)**

**Context:** The tool has been debugged and optimized. It's time to use it to complete the most important production task of this phase.

* **1:30 PM - 6:00 PM: Completing processing of the full list of 450 companies.**
* **What will be done:**
1. **Preparing for restart (1:30 PM - 2:00 PM):**
* Ensure that `main.py` implements the logic for skipping already processed companies (check if the company is in the `FINAL_Leads` sheet).
* Check that all API keys and access permissions are in place.
2. **Running on the full array (2:00 PM):**
* Run the main `main.py` file.
3. **Background monitoring (2:00 PM - 6:00 PM):**
* While the script is running, periodically monitor the console output to catch any unexpected errors.
* Watch the `FINAL_Leads` summary table in Google Sheets update in real time.
* **Expected result:** The first "combat" run of the project is **fully completed**. The final table contains **450 fully processed, analyzed, and enriched leads**. The project has officially moved from the development stage to a finished, well-established tool that has already delivered its first large-scale results.