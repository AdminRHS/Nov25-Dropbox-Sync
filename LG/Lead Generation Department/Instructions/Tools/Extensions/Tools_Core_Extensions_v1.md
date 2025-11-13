# Core Extensions Guide (Google Scrape + RE Extension)

Use this playbook to install, pin, log into, and operate the two internal Chrome extensions the LG team relies on daily.

---

## 1. Download packages
1. Go to Discord `#lg-hub` (or `#test-app` for new builds).
2. Download both archives:
   - **Google Scrape** (a.k.a. Google Search Extension)
   - **RE Extension for LinkedIn**
3. Extract each ZIP (Right-click → `Extract here`). Store them in a stable folder (e.g., `~/RemoteHelpers/Extensions`). Deleting or moving the folder after installation will break the extension.

---

## 2. Install in Chrome
1. Open Chrome → menu (⋮) → `Extensions` → `Manage extensions`.
2. Enable **Developer mode** (top-right toggle).
3. Click `Load unpacked` (top-left) and select the extracted Google Scrape folder → `Select folder`.
4. Repeat for the RE Extension folder.
5. Pin both extensions: click the puzzle icon → pin icons (`📌`) for Google Scrape and RE Extension so they stay visible.

---

## 3. Log in
### Google Scrape
1. Click the extension icon.
2. Enter your CRM email + password, then `Sign in`. Wait until your name appears at the bottom of the panel—do not click elsewhere until the login success message appears.

### RE Extension
1. Open [linkedin.com/feed](https://www.linkedin.com/feed) first.
2. Click the extension icon → `Visit LinkedIn page` if prompted.
3. Sign in with the same CRM credentials; wait for the confirmation banner.

---

## 4. Google Scrape usage
1. Fill the search fields (country, city, industry, company size, keyword). Example query:
   ```
   site:linkedin.com "headquarters:Berlin" AND Industry:"Marketing" AND "company size:11-50"
   ```
2. Click `Search` and let the scraper run (don’t touch the browser until it finishes).
3. Results appear in two places:
   - Discord `#google-extension-unique-lead` channel (filter by your name in the search bar).
   - A new Chrome tab listing unique companies (blue = unchecked, red = already opened).
4. Check each company’s location/fit before logging it in the CRM.
5. When starting a new search, change the parameters, click the `Reset` icon, then `Search`. Always finish reviewing the previous page before launching another search.
6. Track every query in the [Search Extension Tracker](https://docs.google.com/spreadsheets/d/1v-caMlLDYgAKJyPzYksi9rst9onV1VZtrmpOF_BHPi0/):
   - Query, Manager, Date, Country, City, Industry, Size.

---

## 5. RE Extension workflow
1. Copy the email/phone number from SalesQL (or another enrichment tool) before running the extension.
2. On a lead’s LinkedIn profile, click the RE icon.
3. Review/edit fields before submitting:
   - **Lead position** (match CRM naming).
   - **Company name** (select correct option from the dropdown).
   - **Industry**.
   - **Company location** (must match the country you’re sourcing).
4. Click **Add New Lead to CRM** for the first contact at a company. For additional contacts, use **Add Lead to Existing Company**.
5. Open the newly created CRM card (`Visit Him`) and fix any warnings listed in the **Notes** section (wrong position, missing industry, etc.).
6. If the extension could not find social links, email, or phone, open the company website manually afterward and update the CRM card.

---

## 6. Quick reference
| Task | Google Scrape | RE Extension |
| --- | --- | --- |
| Primary use | Discover unique companies | Create leads/companies in CRM |
| Data source | Google SERP scraping | LinkedIn profile parsing |
| Output | Discord + HTML results | Direct CRM record |
| Credentials | CRM email/password | Same as Google Scrape |

Keep both extensions updated via the Discord releases and re-run `Load unpacked` if we ship a new version. Report bugs with screenshots in `#lg-hub` so the automation team can patch them quickly.
