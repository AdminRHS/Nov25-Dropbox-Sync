# Task Manager Database Structure Documentation

## Overview

This document provides a comprehensive overview of the Task Manager database structure, including table schemas, relationships, parameters, and data types used throughout the system.

## Database Architecture

The Task Manager system follows a hierarchical structure:
- **Projects** → **Milestones** → **Tasks** → **Steps**

With supporting template structures:
- **Project Templates** → **Milestone Templates** → **Task Templates** → **Step Templates**

---

## Core Tables

### 1. Projects (`projects`)

The top-level container for organizing work.

#### Table Structure

```sql
CREATE TABLE projects (
  id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  entity_id tinyint(3) unsigned DEFAULT NULL,
  inner_client_id tinyint(3) unsigned DEFAULT NULL,
  project_template_id smallint(5) unsigned DEFAULT NULL,
  start_date date NOT NULL,
  end_date date DEFAULT NULL,
  created_by smallint(5) unsigned DEFAULT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | smallint(5) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `name` | varchar(100) | Project name | NOT NULL |
| `entity_id` | tinyint(3) unsigned | Reference to entities table | FOREIGN KEY → entities(id) |
| `inner_client_id` | tinyint(3) unsigned | Reference to inner clients | FOREIGN KEY → inner_clients(id) |
| `project_template_id` | smallint(5) unsigned | Reference to project template | FOREIGN KEY → project_templates(id) |
| `start_date` | date | Project start date | NOT NULL |
| `end_date` | date | Project end date | NULLABLE |
| `created_by` | smallint(5) unsigned | User who created the project | FOREIGN KEY → users(id) |
| `created_at` | timestamp | Creation timestamp | DEFAULT current_timestamp() |

#### Relationships

- **Belongs to**: `entities`, `inner_clients`, `project_templates`, `users`
- **Has many**: `milestones`

---

### 2. Milestones (`milestones`)

Major checkpoints or phases within a project.

#### Table Structure

```sql
CREATE TABLE milestones (
  id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  description varchar(500) NOT NULL,
  milestone_template_id bigint(20) unsigned DEFAULT NULL,
  project_id smallint(5) unsigned DEFAULT NULL,
  start_date date DEFAULT NULL,
  end_date date DEFAULT NULL,
  expected_hours time NOT NULL DEFAULT '00:00:00',
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | bigint(20) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `name` | varchar(100) | Milestone name | NOT NULL |
| `description` | varchar(500) | Milestone description | NOT NULL |
| `milestone_template_id` | bigint(20) unsigned | Reference to milestone template | FOREIGN KEY → milestone_templates(id) |
| `project_id` | smallint(5) unsigned | Reference to parent project | FOREIGN KEY → projects(id) |
| `start_date` | date | Milestone start date | NULLABLE |
| `end_date` | date | Milestone end date | NULLABLE |
| `expected_hours` | time | Expected duration | DEFAULT '00:00:00' |

#### Relationships

- **Belongs to**: `projects`, `milestone_templates`
- **Has many**: `tasks`

---

### 3. Tasks (`tasks`)

Individual work items that belong to milestones.

#### Table Structure

```sql
CREATE TABLE tasks (
  id mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  entity_id tinyint(3) unsigned DEFAULT NULL,
  `order` mediumint(8) unsigned NOT NULL DEFAULT 0,
  task_queue mediumint(8) unsigned NOT NULL DEFAULT 0,
  title varchar(100) NOT NULL,
  task_template_id smallint(5) unsigned DEFAULT NULL,
  status_id tinyint(3) unsigned DEFAULT NULL,
  milestone_id bigint(20) unsigned DEFAULT NULL,
  project_id smallint(5) unsigned DEFAULT NULL,
  start_date datetime DEFAULT NULL,
  due_date datetime DEFAULT NULL,
  priority_id tinyint(3) unsigned DEFAULT NULL,
  total_time time DEFAULT '00:00:00',
  is_completed tinyint(1) NOT NULL DEFAULT 0,
  created_by smallint(5) unsigned DEFAULT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  note varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | mediumint(8) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `entity_id` | tinyint(3) unsigned | Reference to entities | FOREIGN KEY → entities(id) |
| `order` | mediumint(8) unsigned | Display order | DEFAULT 0 |
| `task_queue` | mediumint(8) unsigned | Queue position | DEFAULT 0 |
| `title` | varchar(100) | Task title | NOT NULL |
| `task_template_id` | smallint(5) unsigned | Reference to task template | FOREIGN KEY → task_templates(id) |
| `status_id` | tinyint(3) unsigned | Task status | FOREIGN KEY → statuses(id) |
| `milestone_id` | bigint(20) unsigned | Reference to parent milestone | FOREIGN KEY → milestones(id) |
| `project_id` | smallint(5) unsigned | Reference to parent project | FOREIGN KEY → projects(id) |
| `start_date` | datetime | Task start date/time | NULLABLE |
| `due_date` | datetime | Task due date/time | NULLABLE |
| `priority_id` | tinyint(3) unsigned | Task priority | FOREIGN KEY → priorities(id) |
| `total_time` | time | Total time spent | DEFAULT '00:00:00' |
| `is_completed` | tinyint(1) | Completion flag | DEFAULT 0 |
| `created_by` | smallint(5) unsigned | User who created task | FOREIGN KEY → users(id) |
| `created_at` | timestamp | Creation timestamp | DEFAULT current_timestamp() |
| `note` | varchar(500) | Additional notes | NULLABLE |

#### Task Status Types (Frontend)

```typescript
export type TaskStatus =
  | 'todo'
  | 'in_progress'
  | 'in_review'
  | 'done'
  | 'cancelled';
```

#### Task Priority Types (Frontend)

```typescript
export type TaskPriority = 'low' | 'medium' | 'high';
```

#### Relationships

- **Belongs to**: `entities`, `task_templates`, `statuses`, `milestones`, `projects`, `priorities`, `users`
- **Has many**: `steps`, `task_assignees`, `task_comments`, `task_history_events`
- **Has many (through)**: `parent_tasks` (via `tasks_parent_task`)

---

### 4. Steps (`steps`)

Individual actions or sub-tasks within a task.

#### Table Structure

```sql
CREATE TABLE steps (
  id mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `order` tinyint(3) unsigned NOT NULL DEFAULT 0,
  step_template_id smallint(5) unsigned NOT NULL,
  assignee_id smallint(5) unsigned DEFAULT NULL,
  name varchar(200) NOT NULL,
  entity_id tinyint(3) unsigned DEFAULT NULL,
  task_id mediumint(8) unsigned DEFAULT NULL,
  is_completed tinyint(1) NOT NULL DEFAULT 0,
  completed_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | mediumint(8) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `order` | tinyint(3) unsigned | Step order within task | DEFAULT 0 |
| `step_template_id` | smallint(5) unsigned | Reference to step template | FOREIGN KEY → step_templates(id), NOT NULL |
| `assignee_id` | smallint(5) unsigned | Assigned user | FOREIGN KEY → users(id) |
| `name` | varchar(200) | Step name | NOT NULL |
| `entity_id` | tinyint(3) unsigned | Reference to entities | FOREIGN KEY → entities(id) |
| `task_id` | mediumint(8) unsigned | Reference to parent task | FOREIGN KEY → tasks(id) |
| `is_completed` | tinyint(1) | Completion flag | DEFAULT 0 |
| `completed_at` | timestamp | Completion timestamp | NULLABLE |

#### Relationships

- **Belongs to**: `step_templates`, `users`, `entities`, `tasks`
- **Has many**: `checklist_items` (via step checklists)

---

## Template Tables

### 5. Task Templates (`task_templates`)

Reusable task definitions that can be instantiated as actual tasks.

#### Table Structure

```sql
CREATE TABLE task_templates (
  id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  action_id bigint(20) unsigned DEFAULT NULL,
  object_id bigint(20) unsigned DEFAULT NULL,
  is_draft tinyint(1) NOT NULL DEFAULT 0,
  description varchar(500) DEFAULT NULL,
  cost smallint(6) NOT NULL DEFAULT 0,
  frequency_id tinyint(3) unsigned DEFAULT NULL,
  entity_id tinyint(3) unsigned DEFAULT NULL,
  task_quantity smallint(6) NOT NULL DEFAULT 0,
  expected_hours time NOT NULL DEFAULT '00:00:00',
  created_by smallint(5) unsigned DEFAULT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | smallint(5) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `name` | varchar(100) | Template name | NOT NULL |
| `action_id` | bigint(20) unsigned | Reference to actions library | FOREIGN KEY → actions(id) |
| `object_id` | bigint(20) unsigned | Reference to objects library | FOREIGN KEY → objects(id) |
| `is_draft` | tinyint(1) | Draft status flag | DEFAULT 0 |
| `description` | varchar(500) | Template description | NULLABLE |
| `cost` | smallint(6) | Estimated cost | DEFAULT 0 |
| `frequency_id` | tinyint(3) unsigned | Reference to frequencies | FOREIGN KEY → frequencies(id) |
| `entity_id` | tinyint(3) unsigned | Reference to entities | FOREIGN KEY → entities(id) |
| `task_quantity` | smallint(6) | Expected quantity | DEFAULT 0 |
| `expected_hours` | time | Expected duration | DEFAULT '00:00:00' |
| `created_by` | smallint(5) unsigned | Creator user | FOREIGN KEY → users(id) |
| `created_at` | timestamp | Creation timestamp | DEFAULT current_timestamp() |

#### TypeScript Interface

```typescript
export interface TaskTemplate {
  id: number;
  name: string;
  task_template_type_id: number | null;
  action_id: number | null;
  object_id: number | null;
  description: string | null;
  cost: number | null;
  frequency_id: number | null;
  task_quantity: number | null;
  expected_hours: number | null;
  entity_id: number | null;
  is_draft: boolean;
  created_at: string;
  step_templates: StepTemplate[];
  parent_task_templates: ParentTaskTemplate[];
  task_template_type: TaskTemplateType | null;
  created_by: number | null;
}
```

#### Draft vs Full Template

**Draft Template** (minimal requirements):
- `name`: Required
- `is_draft`: Must be `1`
- All other fields optional

**Full Template** (production ready):
- `name`: Required
- `is_draft`: Must be `0`
- `task_template_type_id`: Required
- `action_id`: Required
- `object_id`: Required
- Other fields optional

#### Relationships

- **Belongs to**: `actions`, `objects`, `entities`, `frequencies`, `users`, `task_template_types`
- **Has many**: `step_templates` (via `task_template_step_template`)
- **Has many**: `parent_task_templates` (via `task_temp_parent_task_temp`)

---

### 6. Step Templates (`step_templates`)

Reusable step definitions used in task templates.

#### Table Structure

```sql
CREATE TABLE step_templates (
  id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  action_id bigint(20) unsigned DEFAULT NULL,
  object_id bigint(20) unsigned DEFAULT NULL,
  tool_id smallint(5) unsigned DEFAULT NULL,
  is_draft tinyint(1) NOT NULL DEFAULT 0,
  description varchar(2000) DEFAULT NULL,
  entity_id tinyint(3) unsigned NOT NULL,
  hours_planned time NOT NULL DEFAULT '00:00:00',
  created_by smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | smallint(5) unsigned | Primary key | AUTO_INCREMENT, NOT NULL |
| `name` | varchar(100) | Template name | NOT NULL |
| `action_id` | bigint(20) unsigned | Reference to actions library | FOREIGN KEY → actions(id) |
| `object_id` | bigint(20) unsigned | Reference to objects library | FOREIGN KEY → objects(id) |
| `tool_id` | smallint(5) unsigned | Reference to tools library | FOREIGN KEY → tools(id) |
| `is_draft` | tinyint(1) | Draft status flag | DEFAULT 0 |
| `description` | varchar(2000) | Template description | NULLABLE |
| `entity_id` | tinyint(3) unsigned | Reference to entities | FOREIGN KEY → entities(id), NOT NULL |
| `hours_planned` | time | Planned duration | DEFAULT '00:00:00' |
| `created_by` | smallint(5) unsigned | Creator user | FOREIGN KEY → users(id) |

#### TypeScript Interface

```typescript
export interface StepTemplate {
  id: number;
  name: string;
  description?: string | null;
  is_draft: boolean;
  action_id?: number | null;
  entity_id?: number | null;
  object_id?: number | null;
  tool_id?: number | null;
  hours_planned?: number | null;
  created_at: string;
  updated_at: string;
}
```

#### Relationships

- **Belongs to**: `actions`, `objects`, `tools`, `entities`, `users`
- **Has many**: `task_templates` (via `task_template_step_template`)

---

## Junction/Pivot Tables

### 7. Task Template - Step Template (`task_template_step_template`)

Links task templates to their step templates with ordering.

#### Table Structure

```sql
CREATE TABLE task_template_step_template (
  task_template_id smallint(5) unsigned NOT NULL,
  step_template_id smallint(5) unsigned NOT NULL,
  `order` mediumint(8) unsigned DEFAULT NULL,
  PRIMARY KEY (task_template_id, step_template_id)
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `task_template_id` | smallint(5) unsigned | Reference to task template | FOREIGN KEY → task_templates(id), PRIMARY KEY |
| `step_template_id` | smallint(5) unsigned | Reference to step template | FOREIGN KEY → step_templates(id), PRIMARY KEY |
| `order` | mediumint(8) unsigned | Execution order | NULLABLE |

---

### 8. Task Assignee (`task_assignee`)

Many-to-many relationship between tasks and users (assignees).

#### Table Structure

```sql
CREATE TABLE task_assignee (
  task_id mediumint(8) unsigned NOT NULL,
  assignee_id smallint(5) unsigned NOT NULL
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `task_id` | mediumint(8) unsigned | Reference to task | FOREIGN KEY → tasks(id) |
| `assignee_id` | smallint(5) unsigned | Reference to user | FOREIGN KEY → users(id) |

---

### 9. Task Template - Parent Task Template (`task_temp_parent_task_temp`)

Defines parent-child relationships between task templates.

#### Table Structure

```sql
CREATE TABLE task_temp_parent_task_temp (
  parent_task_template_id smallint(5) unsigned NOT NULL,
  task_template_id smallint(5) unsigned NOT NULL
)
```

#### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `parent_task_template_id` | smallint(5) unsigned | Reference to parent template | FOREIGN KEY → task_templates(id) |
| `task_template_id` | smallint(5) unsigned | Reference to child template | FOREIGN KEY → task_templates(id) |

---

## Supporting Data Structures

### 10. Checklist Items (`checklist_items`)

Items within steps that can be checked off.

#### TypeScript Interface

```typescript
export interface ChecklistItem {
  id: number;
  checklist_item_id: number;
  is_completed: boolean;
  is_correct: boolean;
  name: string;
  order: number;
  placement_id: number;
  completed_by: number;
  completed_at: string;
  step_id: number;
  created_at: string;
  updated_at: string;
}
```

---

### 11. Task Comments (`task_comments`)

Comments attached to tasks.

#### TypeScript Interface

```typescript
export interface TaskComment {
  id: number;
  content: string;
  createdAt: string;
  user: User;
}
```

---

### 12. Task History Events (`task_history_events`)

Audit trail of changes to tasks.

#### TypeScript Interface

```typescript
export interface TaskHistoryEvent {
  id: number;
  description: string;
  details: string | null;
  createdAt: string;
  user: User;
}
```

---

## API Response Structures

### Standard API Response

```typescript
export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
  links?: PaginationLinks;
  meta?: PaginationMeta;
}
```

### Pagination Structure

```typescript
interface PaginationMeta {
  current_page: number;
  from: number;
  last_page: number;
  links: PaginationLink[];
  path: string;
  per_page: number;
  to: number;
  total: number;
}

interface PaginationLinks {
  first: string;
  last: string;
  prev: string | null;
  next: string | null;
}
```

---

## Frontend Type Definitions

### Task Interface (Frontend)

```typescript
export interface Task {
  id: number;
  title: string;
  description: string;
  note: string;
  is_completed: boolean;
  steps: TaskStep[];
  parent_tasks: { id: number; title: string; steps: TaskStep[] }[];
  project: { id: number; name: string };
  previous_id: number | null;
  next_id: number | null;
  status: TaskStatus;
  priority: TaskPriority;
  createdAt: string;
  updatedAt: string;
  dueDate: string;
  estimatedHours: number;
  template?: {
    id: number;
    name: string;
  };
  assignees: User[];
}
```

### Task Step Interface

```typescript
export interface TaskStep {
  id: number;
  name: string;
  description: string;
}
```

---

## Validation Schemas

### Task Template Validation (Zod)

```typescript
// Draft schema - only name required
const draftSchema = z.object({
  name: z.string().min(1, 'Name is required'),
  is_draft: z.literal(1),
  task_template_type_id: z.number().optional(),
  action_id: z.number().optional(),
  object_id: z.number().optional(),
  description: z.string().nullable().optional(),
  cost: z.number().nullable().optional(),
  frequency_id: z.number().nullable().optional(),
  task_quantity: z.number().nullable().optional(),
  expected_hours: z.number().nullable().optional(),
  entity_id: z.number().nullable().optional(),
});

// Full schema - additional fields required
const fullSchema = z.object({
  name: z.string().min(1, 'Name is required'),
  is_draft: z.literal(0),
  task_template_type_id: z.number({
    required_error: 'Task template type is required',
  }),
  action_id: z.number({
    required_error: 'Action is required',
  }),
  object_id: z.number({
    required_error: 'Object is required',
  }),
  description: z.string().nullable().optional(),
  cost: z.number().nullable().optional(),
  frequency_id: z.number().nullable().optional(),
  task_quantity: z.number().nullable().optional(),
  expected_hours: z.number().nullable().optional(),
  entity_id: z.number().nullable().optional(),
});

// Union schema
export const taskTemplateSchema = z.discriminatedUnion('is_draft', [
  draftSchema,
  fullSchema,
]);
```

---

## API Endpoints

### Task Templates

- `GET /task-templates` - List all task templates (with filters)
- `GET /task-templates/:id` - Get single task template
- `POST /task-templates` - Create new task template
- `PUT /task-templates/:id` - Update task template
- `DELETE /task-templates/:id` - Delete task template

### Tasks

- `GET /tasks/:id` - Get single task
- `POST /tests/:taskId/start` - Start a test for a task

### Step Templates

- `GET /step-templates` - List all step templates (with filters)
- `GET /step-templates/:id` - Get single step template
- `POST /step-templates` - Create new step template
- `PUT /step-templates/:id` - Update step template
- `DELETE /step-templates/:id` - Delete step template

---

## Key Relationships Summary

```
Projects
  └── Milestones
      └── Tasks
          ├── Steps
          ├── Task Assignees (many-to-many)
          ├── Task Comments
          └── Task History Events

Project Templates
  └── Milestone Templates
      └── Task Templates
          ├── Step Templates (via junction table)
          └── Parent Task Templates (self-referential)
```

---

## Data Flow

1. **Template Creation**: Create step templates → Create task templates → Link step templates to task templates
2. **Project Creation**: Create project from template → Generate milestones → Generate tasks from task templates
3. **Task Execution**: Assign users → Create steps from step templates → Track completion → Update status

---

## Notes

- All timestamps use MySQL `timestamp` type with `DEFAULT current_timestamp()`
- Foreign keys use `ON DELETE CASCADE` or `ON DELETE SET NULL` depending on relationship
- Draft templates allow incomplete data for work-in-progress templates
- The system supports hierarchical task structures through parent-child relationships
- Tasks can be linked sequentially via `previous_id` and `next_id` (not shown in DB schema but used in frontend)

---

*Last Updated: 2025-01-27*
*Document Version: 1.0*

