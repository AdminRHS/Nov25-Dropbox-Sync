#### **Detailed Daily Plan**

**Morning Session: Strategic Preparation and Building the System's "Brain" (9:00 AM - 12:30 PM)**

**Context:** The morning is dedicated to two tasks: a quick but crucial reconfiguration of the old process and building the intellectual core for the new one.

* **9:00 AM - 10:30 AM: Revisiting the Approach to Scraping Job Sites.**
* **What will be done:**
1. Visit each of the main job sites used for scraping one by one.
2. Using the advanced search, set and configure detailed filters to select **only targeted and relevant professions**.
3. **Critically important:** Save these search settings (if the site allows it) or save the resulting URLs with all filter parameters in a separate document.
* **Expected Result:** A completed and saved set of settings/links for each job site. Future scraping will be faster and more targeted, producing much higher-quality data.

* **10:30 - 12:30: Stage 4 - Completing the "Problem Dictionary" creation.**
* **Context:** Based on the 1,000+ negative reviews collected on Friday, a structured analytical tool must be created.
* **What will be done (according to your plan):**
1. Analyze the dataset, manually or using an AI assistant, identify keywords and phrases that indicate problems (e.g., "slow response," "outdated design," "hard to navigate").
2. Group the found phrases into categories corresponding to the company's services (e.g., 'Support_Issues', 'Design_Issues', 'Marketing_Weakness').
3. Fill out and finalize the _ANALYSIS_Keywords sheet in the master table.
* **Expected Result:** A fully operational "problem dictionary." The system's "brain" has been created, capable of understanding and classifying customer complaints.

**Afternoon Session: Assembly and Integration – From Analysis to Final Result (1:30 PM - 6:00 PM)**

**Context:** The "problem dictionary" is complete. Now we need to write the code that will use it and integrate all parts of the project into a single, easy-to-run process.

* **1:30 PM - 6:00 PM: Stage 5 — Developing an analytics script and building the `main` file.**
* **What will be done (according to your plan):**
1. **Writing the analytics module (`lead_analyzer.py`):**
* A Python script will be written that reads all reviews (`_RAW_Reviews`) and the "problem dictionary" (`_ANALYSIS_Keywords`).
* In a loop for each company, it will analyze their reviews for keywords, calculate metrics (`Problem_Score`, `Review_Velocity`, `Sentiment_Score`), and generate a brief summary of the issues found.
* The analysis results will be written to the `FINAL_Leads` summary sheet.
2. **Creating the control file (`main.py`):**
* The main `main.py` file will be created. * Logic from all previous scripts will be imported and integrated into this script:
* Data cleaning script (created last week).
* Review collection script (`review_scraper.py`).
* A new analysis script (`lead_analyzer.py`).
* A main function, `main()`, will be created that sequentially calls all of these modules, ensuring the entire process is executed from start to finish in a single command.
3. **Testing:** A test run of the `main.py` file will be performed on a small data set to ensure that the entire chain works without errors.
* **Expected Result:** A complete, working, single `main.py` script that runs the entire data processing pipeline: `cleaning -> review collection -> analysis -> writing results`. The project is technically complete and ready to be run on the full data set.