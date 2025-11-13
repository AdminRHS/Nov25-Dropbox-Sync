#### **Detailed Daily Plan**

**Morning Session: Code Stabilization and Hardening (9:00 AM - 1:00 PM)**

**Context:** An unstable tool is a useless tool. The morning will be entirely devoted to solving the most critical issue—ensuring the reliability and fault tolerance of the scraper.

* **9:00 AM - 1:00 PM: Resolving the issue with constant errors and crashes.**
* **What will be done (step by step):**
1. **Diagnostics (9:00 AM - 10:00 AM):**
* Run the script in normal (non-headless) mode to visually track which company and which action is causing the failure.
* Carefully examine the error text in the console. Is it a Selenium "element not found" error or something else?
2. Implementing "masking" measures (10:00 - 12:00):**
* **Slowdown and randomization:** Add longer and, importantly, **random delays** (`time.sleep(random.uniform(3, 7))`) between actions (link clicks, clicks, scrolls) to the code to simulate human behavior.
* **User-Agent rotation:** Add user-agent rotation to Selenium settings so that each launch looks like a new browser.
* **Fault tolerance:** Wrap critical sections of code (e.g., clicking the "Reviews" button) in `try-except` blocks with multiple retries and logging. If the button isn't found the first time, the script should wait and try again instead of crashing. 3. **Stress Testing (12:00 - 1:00 PM):**
* Run the revised script on a long list of 20-30 companies and ensure it runs from start to finish without any fatal errors.
* **Expected Result:** A significantly more stable script, capable of processing dozens of companies in a row without crashing. The issue of constant crashes has been resolved or minimized.

**Afternoon Session: Final Functionality and Full Build (2:00 PM - 6:00 PM)**

**Context:** Once the system core is reliable, the final functionality can be added and everything can be put together.

* **2:00 PM - 5:00 PM: Writing and testing a script for searching social networks and contacts.**
* **What will be done:**
1. **Development (`enrichment_scraper.py`):**
* Write a function that takes a company name and website as input.
* Implement a search via `duckduckgo-search` or the Google Search API for queries like `"[Company Name] LinkedIn"`.
* Implement parsing of the company's website homepage for social media links (`href` containing `linkedin.com`, etc.) and email addresses.
2. **Integration into `main.py`:**
* Import the new function into the main control file.
* Add its call to the main processing loop so that the data is enriched with contacts after NLP analysis. 3. **Testing:** Test the updated `main.py` on 5-10 companies and ensure that the new fields in the final table are populated correctly.
* **5:00 PM - 6:00 PM: Final revision and cleanup.**
* **What will be done:**
1. Conduct a final review of the "anchor dictionary", adding 5-10 new synonyms or phrases, if necessary.
2. Clean up the code: add comments, remove unnecessary `print()` statements, ensure the project structure is logical.
3. Run the full cycle on 2-3 companies to ensure everything works as a single unit.
* **Expected result:** A fully finished, stable, and functionally complete project. The `main.py` script executes the entire chain – from data collection to analysis and contact enrichment – ​​without errors.