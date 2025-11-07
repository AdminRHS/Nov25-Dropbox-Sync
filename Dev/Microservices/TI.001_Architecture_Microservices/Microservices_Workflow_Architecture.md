# Microservices Workflow & Architecture

## Scope
Consolidated operating model for domain microservices under LLM2.0. This is documentation-only; execution lives in external systems (web apps, MCP servers, CRMs).

## Domains
- Libraries — reference taxonomies for Actions, Objects, Tools, Responsibilities, Professions (source of truth for standardized vocabulary)
- Talents — candidate and employee lifecycle, separate from Jobs
- LRN — learning catalog, course → profession/skills/ responsibilities mappings
- Task Manager — employee allocation, tasks, milestones
- Jobs — job sites, accounts, postings
- Prospects — users, accounts, tools for outreach

## Environment Map
- Dev: `libdev.anyemp.com`, `talentsdev.anyemp.com`
- Prod: `lib.anyemp.com` (if applicable), `talents.anyemp.com`
- Internal docs: this repo (LLM context), Dropbox (archives), external CRMs

## Cross-Service Interfaces (Conceptual)
- Identity & Auth: API keys, OAuth, JWT (see `SYSTEM/Configuration/authentication_setup.md`)
- Context delivery: MCP servers for Claude/Cursor/GPT (see `DOCUMENTATION/Guides/MCP_SETUP_GUIDE.md`)
- Data references: departments JSON (`departments/*/*.json`), entity docs (`ENTITY_TYPES/*`)

## Release Workflow (No-Code)
1) Document change in relevant service README
2) Link canonical sources; avoid duplication
3) Add acceptance prompts in `Libraries/TESTS.md` (or service-specific tests)
4) Commit, PR, and merge
5) Pull into Claude/Cursor/GPT context and run acceptance tests
6) If external UI/API is updated, record URLs and versions here

## Acceptance Tests (Shared)
Use `Libraries/TESTS.md`:
- Test 1: "Give me a list of all tools used by professions" (source: `departments/*/tools.json`)
- Test 2: "Give me all professions from Department <X>" (source: `departments/<dept>/professions.json`)
- Test 3: CRUD prompts for Libraries (Actions/Objects/Responsibilities/Tools/Professions)

## Dependencies & Mappings
- LRN → Responsibilities: map course outcomes to role responsibilities
- LRN → Talents: skills acquired populate Employee CV
- Libraries → Task Manager: standardized Actions/Objects drive task templates
- Jobs ↔ Talents: separate domains, shared vocabulary via Libraries
- Prospects ↔ Task Manager: outreach tasks consume Libraries.Tools

## Backlog (High-Level)
- Define per-domain SLAs and data freshness policies (documentation)
- Add missing library slices (Actions, Objects, Responsibilities) to canonical sources
- Formalize profession → tool coverage metrics
- Expand LRN similarity features (course/lesson similarity) and mapping to responsibilities

---

**Source:** `LLM2.0/Dev DropBox/microservices/WORKFLOW.md`  
**Copied:** January 2025  
**Location:** `INFRASTRUCTURE/LIBRARY/TI/TI.001_Architecture_Microservices/`

