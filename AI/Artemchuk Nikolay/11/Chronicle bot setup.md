Here is a step-by-step guide on how to add and configure Chronicle Bot (v1.0) to link Discord events with Google Calendar.

---

### Part 1: Adding Chronicle Bot to Your Discord Server

1.  **Open Server Settings:** Right-click on your Discord server's icon in the server list.
2.  **Go to App Directory:** From the dropdown menu, select **Server Settings** → **App Directory**.
3.  **Find the Bot:** In the App Directory search bar, type **Chronicle Bot**.
4.  **Add the Bot:** Click on Chronicle Bot in the search results to go to its page, then click the **Add App** button.
5.  **Authorize:** A browser window will open. Follow the prompts to authorize and add the bot to your server (click **Authorize**, **Accept**, etc.).
6.  **Login:** After authorization, click the **Login** button on the Chronicle Bot website to access its settings panel.

---

### Part 2: Creating and Connecting Your Google Calendar

1.  **Navigate to Notifiers:** Once logged into the Chronicle Bot dashboard, you will see the **Event Notifiers** page. Click the **Add Notifier** button.
2.  **Start Calendar Connection:** You will land on the **Calendar Connection** page. You need to log in to the Google Account that holds the calendar you want to use.
3.  **Go to Google Calendar:** Open Google Calendar in a separate tab (calendar.google.com) using the *same account* you just logged in with.
4.  **Create a New Calendar:**
    * On the left sidebar, find "Other Calendars" and click the **plus icon (+)**.
    * Select **Create New Calendar**.
    * Fill in the **Name** (e.g., "Discord Events"), **Description**, and select the correct **Time Zone**.
    * Click **Create Calendar**.
5.  **Connect in Chronicle Bot:** Return to the Chronicle Bot browser page.
    * Select the **Google Calendar** you just created from the dropdown menu.
    * Select the target **Discord Server**.
    * Select the **Text Channel** where notifications should be posted.
    > **Important:** This channel must be public. If the channel is private, you must manually grant Chronicle Bot access to it in Discord's channel settings.

---

### Part 3: Configuring the Notifier Settings

On the same setup page, scroll down to configure the notification details.

#### 1. Reminders Tab

1.  **Days to Search:** Set the number of days ahead the bot should check for events in the Google Calendar.
2.  **Mention Role:** Choose a role (e.g., `@Events`) that the bot will ping when sending a notification.
3.  **Clean Up:** For **Clean up reminder messages**, select **No clean up** (this keeps a log of all notifications).
4.  **Reminder Times:**
    * Enable the toggle for **Use calendar event reminder times**.
    * Set the time (e.g., 30 minutes, 1 hour) for when the bot should remind users *before* the event starts.
5.  **Activity Messages:** Check (enable) all the following boxes:
    * **Notify on creation of new calendar event**
    * **Notify on update of existing calendar event**
    * **Notify on removal of existing calendar event**
6.  **Recurring Events:** For **Recurring Event Messages**, select **Combined**. This groups recurring events into a single message to prevent spam.

#### 2. Summaries Tab

1.  **Toggle Settings:** Enable (toggle ON) the following three options:
    * **Clean up last summary**
    * **Pin new summary messages**
    * **Skip empty summaries**
2.  **Schedule Summaries:**
    * **Group by:** Day
    * **Frequency:** Daily
    * **Time of day:** Select a convenient time for the daily summary (e.g., 9:30 AM).
    * **Days:** Set how many upcoming days the summary should include (e.g., 7).

#### 3. Event Sync Tab

1.  **Enable Sync:** Check the box for **Sync Google calendars to Discord events**. This will automatically create Discord events from your Google Calendar entries.

#### 4. Settings Tab

1.  **Event Link:** Leave this set to **Automatic**.
2.  **Language:** Select **English**.
3.  **Notifier Time Zone:** Select your server's primary time zone (e.g., **Europe/Kyiv**).

---

### Part 4: Saving and Verification

1.  **Save:** Scroll to the bottom of the page and click the **Save Notifier** button.
2.  **Check Status:** You will be redirected to the "Current Notifiers" list, where your new notifier should appear with an **Enabled** status.
3.  **Check Discord:** Go to the channel you selected in Discord. You should see a message from Chronicle Bot confirming that a new notifier has been created and linked to that channel.

