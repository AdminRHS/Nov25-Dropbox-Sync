# YELLOW CARD DASHBOARD - TECHNICAL REQUIREMENTS

## 🔗 Dashboard Prototype
**URL:** https://codepen.io/Admin-Remote-Helpers/pen/KwVXdrp

---

## 📋 OVERVIEW

The Yellow Card Dashboard is a monitoring system for workflow violations. It tracks employee compliance with workflow rules and displays violations in an easy-to-understand format.

---

## 🎯 PURPOSE

**Primary Goal:** Monitor and track workflow rule violations
**Secondary Goal:** Present violation data in a clear, visual way that encourages compliance

---

## 📊 DASHBOARD STRUCTURE

### Three Main Tabs:

#### 1. OVERVIEW
**Current:** Basic statistics on yellow card distribution
**Needed:** Introductory information panel

#### 2. YELLOW CARDS (or "Calendar")
**Purpose:** Combined view of violations
**Contains:**
- Calendar view of when violations occurred
- List of employees with violations
- Details of each violation

#### 3. TEAM
**Purpose:** Employee management
**Contains:**
- Employee list
- Profile editing
- Yellow card assignment interface

---

## 🔧 REQUIRED UPDATES

### Update 1: Intro Panel on Overview Tab

**Context from Call:**
> "Во-первых, надо будет интро в желтой карточке, то есть надо будет презентовать. Должна будет страница, ну хотя бы где-то здесь должна будет, даже если одна панелька, которая будет показывать, за что ты можешь получить желтые карточки."

**Requirements:**
- Add informational panel on Overview tab
- Explain rules of Yellow Card system
- List all violation types with brief descriptions
- Make it visually prominent
- Static content initially (can be API-driven later)

**Suggested Content:**
```
┌─────────────────────────────────────────────┐
│  YELLOW CARD SYSTEM RULES                   │
├─────────────────────────────────────────────┤
│  You can receive a yellow card for:         │
│                                              │
│  🛒 No Shopping List                         │
│     Going to work without daily plan        │
│                                              │
│  🍳 Wrong Tools                              │
│     Not using required work tools           │
│                                              │
│  📦 Product Not Delivered                    │
│     Files not stored in proper location     │
│                                              │
│  🏃 Running to Store Daily                   │
│     Not populating CRM/databases            │
│                                              │
│  📝 Didn't Write It Down                     │
│     Not logging in Daily Log                │
└─────────────────────────────────────────────┘
```

---

### Update 2: Add "Violation Type" Column

**Context from Call:**
> "Надо добавить вот сюда колонку violation type. Вот этот violation type как раз будем называть, дадим название вот этих желтых карточек, за что они бывают."

**Requirements:**
- Add new column to Yellow Cards table
- Display violation type for each entry
- Types should match those in intro panel
- Include emoji icons for quick recognition

**Column Order:**
1. Date
2. Employee Name
3. Department
4. **Violation Type** (NEW)
5. Details/Comments
6. Actions

---

### Update 3: Add "Details" Field in Yellow Card Popup

**Context from Call:**
> "А, но еще комментарии нужно в этот попа ты вот этом добавить текстовое поле. А, понял, детали."

**Requirements:**
- Add textarea field to "Give Yellow Card" modal
- Label: "Details" or "Comments"
- Make it REQUIRED field
- Store and display with violation record

**Form Structure:**
```
Give Yellow Card
├── Employee: [Dropdown]
├── Violation Type: [Dropdown]
└── Details: [Textarea - REQUIRED]
```

---

### Update 4: Add "Discord" Field to Team Profile

**Context from Call:**
> "Также тоже есть edit, можно будет изменить имя, профессию, департамент, email. Дискорд еще можем добавить."

**Requirements:**
- Add Discord field to employee profile
- Optional field (not required)
- Display in Team tab
- Editable in profile edit mode

**Profile Fields:**
- Name
- Profession
- Department
- Email
- **Discord** (NEW - optional)

---

### Update 5: Calendar Functionality

**Requirements:**
- Calendar shows daily violations
- Each date is clickable
- Click reveals: who, what profession, what violation, when
- Modal or expandable view for date details

**Date Detail View Should Show:**
```
October 14, 2025
────────────────────────────
• John Doe (Developer)
  Violation: 🍳 Wrong Tools
  Time: 10:30 AM
  Details: Used personal GPT instead of company Cursor

• Jane Smith (Designer)  
  Violation: 📦 Product Not Delivered
  Time: 2:15 PM
  Details: Files saved locally, not in Dropbox
```

---

### Update 6: Microservices Integration

**Context from Call:**
> "Но, в принципе, перспективе это то, что подтягивает из микросхем."

**Requirements:**
- Connect to central user microservice
- Sync employee data (name, email, department, profession, Discord)
- Auto-update when changes occur in master system
- Reduce manual data entry

**Data Flow:**
```
Master User Service
        ↓
   Yellow Card Dashboard
        ↓
   Display/Track Violations
```

---

### Update 7: (Consideration) Tab Naming

**Context from Call:**
> "Может, стоит переименовать календарь вместо елу карт? Она комбинированная вкладка получается."

**Current:** Tab named "Yellow Cards"
**Contains:** Both calendar and violation list

**Options:**
- "Calendar & Violations"
- "Violation Log"
- "History"
- Keep "Yellow Cards"

**Decision:** To be finalized after review

---

## 📊 DATA MODEL

### Yellow Card Record:
```javascript
{
  id: string,
  employeeId: string,
  employeeName: string,
  profession: string,
  department: string,
  violationType: string,  // NEW FIELD
  violationEmoji: string, // NEW FIELD
  details: string,        // NEW FIELD
  issuedBy: string,
  issuedAt: datetime,
  cardNumber: integer     // 1st, 2nd, or 3rd card
}
```

### Employee Profile:
```javascript
{
  id: string,
  name: string,
  profession: string,
  department: string,
  email: string,
  discord: string,        // NEW FIELD
  yellowCardCount: integer,
  yellowCards: [array of card objects]
}
```

---

## 🎨 VIOLATION TYPES (Standardized)

These should be consistent across:
- Dashboard intro panel
- Dropdown options
- Presentation materials
- Training documents

### Official Violation Types:

1. **🛒 No Daily Plan / No Shopping List**
   - Short: "No Shopping List"
   - Description: "Went to work without daily plan"

2. **🍳 Not Using Required Tools**
   - Short: "Wrong Tools"
   - Description: "Not using required work tools (Cursor, VS Code, etc.)"

3. **📦 Files Not Stored Properly**
   - Short: "Product Not Delivered"
   - Description: "Files not stored in Dropbox/Google Drive"

4. **🏃 Not Populating CRM/Objects**
   - Short: "Running to Store Daily"
   - Description: "Not maintaining databases, redoing research"

5. **📝 Not Logging in Daily Log**
   - Short: "Didn't Write It Down"
   - Description: "Not recording work in Daily Log file"

---

## 🎯 USER EXPERIENCE GOALS

### For Employees:
- Understand violations immediately
- See clear path to compliance
- Feel violations are fair and explained
- Know exactly what led to each card

### For Managers:
- Quick overview of team compliance
- Easy violation assignment
- Clear violation tracking
- Data-driven conversations

### For System:
- Reduce repeat violations through clarity
- Encourage self-monitoring
- Provide accountability
- Support fair enforcement

---

## 🔄 WORKFLOW INTEGRATION

### When Employee Receives Yellow Card:

1. **Assignment:**
   - Manager fills out form
   - Selects employee, violation type, adds details
   - System records timestamp

2. **Notification:**
   - Employee sees card in dashboard
   - Receives notification (email/Discord)
   - Can view details and violation type

3. **Tracking:**
   - Card count increments (1st, 2nd, 3rd)
   - Calendar updated
   - Statistics refreshed

4. **Follow-up:**
   - Employee reviews violation details
   - Understands what to improve
   - Has access to training materials

---

## ✅ IMPLEMENTATION CHECKLIST

### Phase 1: UI Updates
- [ ] Add intro panel to Overview
- [ ] Add Violation Type column
- [ ] Add Details field to form
- [ ] Add Discord field to profiles
- [ ] Update calendar interaction

### Phase 2: Data Structure
- [ ] Update database schema
- [ ] Create violation types enum
- [ ] Implement details storage
- [ ] Add Discord field to user model

### Phase 3: Integration
- [ ] Connect to user microservice
- [ ] Sync employee data
- [ ] Test data flow
- [ ] Handle edge cases

### Phase 4: Testing
- [ ] Test all CRUD operations
- [ ] Verify data consistency
- [ ] Check mobile responsiveness
- [ ] User acceptance testing

### Phase 5: Training
- [ ] Create dashboard user guide
- [ ] Train managers on assignment
- [ ] Explain violation types to team
- [ ] Launch communication

---

## 📱 MOBILE CONSIDERATIONS

Dashboard should be:
- Responsive on all devices
- Easy to assign cards on mobile
- Calendar functional on touch screens
- Forms easy to complete on mobile

---

## 🔒 PERMISSIONS & ACCESS

### Role-Based Access:

**Employees:**
- View their own cards
- View violation types/rules
- No assignment ability

**Managers:**
- View team cards
- Assign cards to team
- View all violations

**Admins:**
- Full access
- System settings
- Violation type management

---

## 📈 FUTURE ENHANCEMENTS

### Potential Features:
- Violation trend analysis
- Team comparison charts
- Automated notifications
- Violation appeal system
- Training material links
- Gamification elements
- Monthly/quarterly reports
- Export functionality

---

## 🎨 VISUAL CONSISTENCY

Dashboard should:
- Match overall company design
- Use same emoji system as training
- Consistent color coding:
  - 🟢 Green: Good standing
  - 🟡 Yellow: Warning
  - 🔴 Red: Critical
- Professional but friendly
- Clear data visualization

---

**Related Documents:**
- Presentation Requirements
- Violation Types List (in Analogies doc)
- Design Guidelines

**Source:** `1310 task Dashboard edits.md`
**Last Updated:** October 14, 2025
