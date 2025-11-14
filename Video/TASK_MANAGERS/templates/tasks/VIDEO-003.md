# VIDEO-003: Update Profile Status for Departed Employee

**Department:** Video
**Status:** Active
**Reusability:** Medium
**Automation Potential:** Low <40%

---

## Quick Info

- **Action:** Update
- **Object:** Profile Status
- **Tool:** HR System + Documentation

---

## Full Template

```yaml
template_id: VIDEO-003
task_template_name: Update Profile Status for Departed Employee
metadata:
  status: Active
  reusability_score: Medium
  extraction_date: '2025-11-10'
ownership:
  department: Video / HR
  assigned_role: Department Lead
taxonomy:
  action: Update
  object: Profile Status
  object_type: Employee Status Change
  tool: HR System + Documentation
  context: Employee-Offboarding
automation_potential:
  ranking: Low <40%
  reasoning: Status updates involve multiple systems and manual verification. Access
    revocation requires security considerations. Documentation updates need human
    review. Notifications require personalized communication.
structure:
  steps:
  - VIDEO-003-01
  - VIDEO-003-02
  - VIDEO-003-03
  - VIDEO-003-04
  - VIDEO-003-05
  - VIDEO-003-06
dependencies:
  prerequisites:
  - Departure notification received
  - HR approval obtained
  - Access to all systems
  related_tasks:
  - 'TASK-HR-005: Review Employee Status Accuracy'
deliverables:
- Updated HR status
- Updated documentation
- Access revocation confirmation
- Archived employee files
- Team notification sent
source_tracking:
  source_file: Department_Operations_Nov06_2025.md
  extraction_date: '2025-11-10'
```

---

## Navigation

- [Back to Video Tasks](../../Tasks_VIDEO.md)
- [All Tasks Listing](../../TASKS_LISTING.md)
- [Master Index](../../INDEX.md)

---

**Source:** Extracted from Tasks_VIDEO.md
**Date:** 2025-11-10
