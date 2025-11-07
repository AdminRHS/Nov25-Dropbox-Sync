#### **Detailed Daily Plan**

**Morning Session: Functionality Finalization — "Data Enrichment" (9:00 AM - 12:30 PM)**

**Context:** Start the day by finalizing the last remaining code fragments. This will allow the entire afternoon to be dedicated exclusively to testing and debugging the fully assembled system.

* **9:00 AM - 12:30 PM: Finalizing, debugging, and integrating contact and social media search scripts.**
* **What will be accomplished:**
1. **Finalizing and debugging scripts:** Take yesterday's draft versions of the scripts. Add error handling (try-except), improve the search results parsing logic, and test them individually on 5-10 companies to ensure their functionality.
2. **Integration into `main.py`:** Import the final, debugged social media and contact search functions into the main control file (`main.py`). Integrate their calls into the main data processing loop so that they are triggered at the last stage, after NLP analysis.
3. **Integration Testing:** Run the full `main.py` cycle on a small sample (3-5 companies) and verify that new columns (`Social_Links`, `Decision_Maker_Info`, etc.) in the final table are correctly created and populated.
* **Expected Result:** A fully functional `main.py`. All planned features are implemented and integrated into a single process.

**Afternoon Session: Pre-Release Preparation – Hardening and Optimization (1:30 PM - 5:00 PM)**

**Context:** The code is completely written, but is it ready for production? This block is dedicated to comprehensive testing and polishing of the entire project.

* **1:30 PM - 5:00 PM: Comprehensive diagnostics, optimization, and debugging of the entire system.**
* **What will be done:**
1. **Comprehensive diagnostics (E2E Test):** Run the full `main.py` on a larger and more diverse data sample (e.g., 30-50 companies from different niches). Closely monitor the process, logging, and results.
2. **Bottleneck analysis and optimization:** During the test, pay attention to which stages take the most time. If possible, make minor optimizations (e.g., reduce the number of unnecessary queries, optimize data handling in Pandas).
3. **Debugging and code polishing:** Fix any errors or illogical behavior identified during the comprehensive test. Add comments to complex sections of code, remove debug `print()` statements, and finalize the project structure.
* **Expected Result:** A stable, reliable, and optimized version of the code, ready for production use.

**Evening Session: Preparing for the "Production" Launch (5:00 PM - 6:00 PM)**

**Context:** The code is ready and debugged. Now we need to prepare a "clean testing ground" for tomorrow's large-scale test.

* **5:00 PM - 6:00 PM: Preparing data and environment for the real test.**
* **What will be done:**
1. **Creating a test list:** Select and compile a list of 50-100 real companies on which the test will be conducted tomorrow.
2. **Preparing a "Clean" Spreadsheet:** Create a new, empty copy of the master spreadsheet in Google Sheets. Fill only the very first sheet (`_RAW_Company_List`) with data from the generated list.
3. **Final check:** Ensure that all configuration files and credentials (`credentials.json`) are in place and correct.
* **Expected result:** A fully prepared environment for tomorrow's test. You can come in the morning, click the "play" button, and run the process on real data without any additional preparation.