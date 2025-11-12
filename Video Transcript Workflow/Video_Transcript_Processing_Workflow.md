# Video Transcript Processing Workflow for AI Team

**Purpose**: High-level overview of how video transcripts are processed to extract and organize AI tools, LLM workflows, automation resources, and prompt engineering techniques into structured libraries.

**Version**: 1.1  
**Date**: December 12, 2025  
**Last Updated**: December 12, 2025  
**Target Audience**: AI Team (Prompt Engineers, Project Managers)  
**Format**: Process Overview (High-Level)

---

## Introduction

### What This Process Does

Video transcripts are transformed into structured, searchable tool data that populates our AI tool libraries. When videos discuss AI models, LLM integration, prompt engineering techniques, automation tools, or AI-powered workflows, this system extracts that information and makes it accessible to the AI team in an organized format.

### Why This Matters for AI Team

- **Discover New AI Tools**: Automatically surface AI models, LLM services, and automation tools mentioned in videos without manually watching hours of content
- **Access Curated Information**: Get validated, structured information about tools including use cases, workflows, and integration patterns
- **Stay Updated**: Libraries are continuously updated as new videos are processed, keeping you informed about the latest AI tools and techniques
- **Find Workflows**: Learn how tools work together through documented integration patterns and workflow examples

### High-Level Process Overview

The process flows from daily work tasks → video discovery → structured transcription → AI-powered extraction → organized library entries. The workflow starts by identifying relevant videos based on actual work processes, then processes them to extract AI tools and workflows. Each step transforms unstructured information into actionable knowledge for the AI team.

---

## Process Flow

### Step 0: Searching for Videos About Actual Processes

**What Happens**: Before transcription begins, we identify relevant videos by analyzing daily work tasks and searching for fresh, popular content that demonstrates actual AI processes and tool usage.

**Sub-Step 0.1: Process Daily Reports**
- **Input**: Daily `.md` files from team members (e.g., `daily.md` files)
- **Tool**: Process with `MAIN PROMPT v4.md` to extract:
  - Tasks and processes being worked on
  - Problems encountered
  - Tools currently in use
  - Workflows being followed
- **Output**: Structured list of tasks, processes, and tool needs extracted from daily reports

**Sub-Step 0.2: Create Perplexity Search Prompt**
- **Purpose**: Generate a search prompt for Perplexity AI to find tools that can help accomplish the defined tasks
- **Process**:
  1. Take extracted tasks and processes from Step 0.1
  2. Create a Perplexity prompt that searches for:
     - Tools that can help accomplish specific tasks
     - Popular and trending tools in relevant categories
     - Tools mentioned in recent AI workflows
- **Prompt Structure**: 
  - Include task descriptions from daily reports
  - Specify tool categories (AI models, LLM services, prompt engineering tools, automation platforms, API integrations, etc.)
  - Request YouTube video links as results
- **Output**: Perplexity search prompt ready for execution

**Sub-Step 0.3: Search for Fresh Videos**
- **Tool**: Perplexity AI (configured with specific settings)
- **Search Criteria**:
  - **Freshness**: Only videos posted "today - 1 month ago" (last 30 days)
  - **Popularity**: Focus on popular, well-viewed content
  - **Relevance**: Videos about actual processes, workflows, and tool usage
  - **Content Type**: AI tutorials, LLM demonstrations, prompt engineering walkthroughs, automation guides
- **Perplexity Configuration** (as mentioned in daily reports):
  - Creativity: 0.5
  - Enable "Structure it out" mode
  - Disable Google Search
  - Enable specific search features below Google Search
- **Output**: List of relevant YouTube video URLs with titles and descriptions

**Sub-Step 0.4: Collect Videos**
- **Process**: 
  - Review Perplexity search results
  - Filter for most relevant videos based on:
    - Task relevance
    - Video quality indicators (views, engagement)
    - Recency (within last month)
  - Collect video URLs and metadata
  - Organize by task/process category
- **Storage**: Video links saved for transcription in Step 1

**Why It Matters**: This step ensures we're processing videos that are:
- **Relevant**: Based on actual tasks and processes from daily work
- **Fresh**: Latest tools and techniques (within last month)
- **Popular**: Validated by community engagement
- **Actionable**: Focused on actual processes, not just tool introductions

**Tools Used**:
- `MAIN PROMPT v4.md` - For processing daily reports
- Perplexity AI - For searching and discovering relevant videos
- YouTube - Source platform for video content

**Output**: Curated list of relevant YouTube videos ready for transcription, organized by task/process category.

---

### Step 1: Video Transcription

**What Happens**: Videos are transcribed into text format using AI transcription tools.

**Tools Used**:
- **Google AI Studio**: For smaller videos (has size limitations)
- **Transcribe AI**: For larger videos that exceed Google AI Studio limits

**Output**: Raw transcript files saved in the `Transcribations` folder with timestamps and speaker annotations.

**Why It Matters**: Transcripts make video content searchable and processable by AI systems, enabling automated extraction of AI tools and workflows.

---

### Step 2: Prompt Processing

**What Happens**: Transcripts are processed using specialized Video Transcription/Analysis prompts that extract taxonomy elements.

**Processing Focus**:
- **Tools & Technologies**: AI models, LLM services, prompt engineering tools, automation platforms mentioned
- **Workflows**: AI integration workflows and prompt engineering patterns described
- **Actions**: AI operations and technical actions
- **Integration Patterns**: How tools connect and work together
- **Use Cases**: Specific AI applications and examples

**Location**: Processing prompts are located in `Prompts/Video_Transcription/` folder.

**Output**: Structured extraction of AI-relevant information from unstructured transcript text.

**Why It Matters**: This step identifies what AI tools and processes are mentioned, preparing them for structured storage in libraries.

---

### Step 3: Tool Data Collection

**What Happens**: Processed data identifies and extracts information about AI tools mentioned in videos.

**Data Collected**:
- Tool name, vendor, and category
- Purpose and primary use cases
- Skill level requirements
- Cost structure (Free/Freemium/Paid)
- Platform compatibility
- Integration capabilities with other tools
- Strengths and limitations
- API documentation links
- Prompt engineering examples and templates
- Integration with development environments
- Performance characteristics
- Model versions and capabilities
- AI team-specific workflows and examples

**AI Team-Relevant Focus**:
- Tools for prompt engineering, LLM integration, automation
- AI workflows and integration processes
- Tool integration patterns for AI projects
- Use cases relevant to prompt engineering, AI automation, LLM services

**Output**: Comprehensive tool profiles ready for library storage.

**Why It Matters**: This step ensures all relevant AI tool information is captured, including how AI team members actually use these tools in practice.

---

### Step 4: Library Population

**What Happens**: Extracted tool data is structured into JSON format and organized into the library system.

**Storage Structure**:
- Tools are saved in `LIBRARIES/Tools/` with category-based organization
- AI team-specific tools go to appropriate categories (e.g., `AI_Tools/`, `LLM_Services/`, `Automation_Tools/`, `Prompt_Engineering/`, `API_Integrations/`)
- Each tool gets its own JSON file with complete information
- Workflows and use cases are documented within tool entries

**File Format**: Each tool is stored as a structured JSON file containing:
- Basic information (name, vendor, category)
- Detailed description and purpose
- Usage information specific to Remote Helpers workflows
- Integration patterns with other tools
- Strengths, limitations, and tags
- API documentation links
- Prompt engineering examples and templates

**Output**: Organized, searchable library of AI tools accessible to all AI team members.

**Why It Matters**: This creates a centralized, always-updated resource where AI team members can discover and learn about tools without watching hours of video content.

---

## AI Team-Specific Focus

### What AI Team Gets from This Process

**New AI Tools Discovery**
- Automatically discover AI models, LLM services, prompt engineering tools, and automation platforms mentioned in videos
- Learn about tools you might not have known existed
- Access information about tool capabilities and use cases

**AI Workflows and Processes**
- Understand how to use tools in real AI workflows
- Learn prompt engineering patterns, LLM integration processes, and automation workflows
- See examples of how tools work together in practice

**Tool Integration Patterns**
- Learn which tools work well together
- Understand data flow between tools (e.g., LLM API → automation → integration)
- Discover tool combinations that enhance your AI stack

**Use Cases and Examples**
- See specific examples of how tools are used in AI projects
- Learn best practices from video content
- Understand tool applications in different AI contexts
- Access prompt engineering examples and implementation patterns

### Where to Find Processed Data

**Primary Location**: `LIBRARIES/Tools/` directory structure

**Categories Relevant to AI Team**:
- `AI_Tools/` - AI-powered tools and services
- `LLM_Services/` - Large Language Model services and APIs
- `Automation_Tools/` - Automation platforms and workflow tools
- `Prompt_Engineering/` - Prompt engineering tools and templates
- `API_Integrations/` - API tools and integration platforms
- `Development_Tools/` - AI development tools and frameworks

**File Format**: Each tool has a JSON file with structured information you can search and reference.

### How Processed Data Helps AI Team

**Access to Curated, Validated Information**
- Information is extracted and validated from video content
- Structured format makes it easy to find what you need
- Consistent format across all tool entries

**Time Savings**
- No need to watch entire videos to find tool information
- Quick access to tool capabilities, use cases, and workflows
- Searchable format for fast information retrieval

**Better Tool Selection**
- Compare tools based on structured information
- Understand tool strengths and limitations before trying them
- Learn integration patterns to build better AI workflows

---

## Key Concepts

### Taxonomy Elements

**What They Are**: Structured categories of information extracted from videos:
- **Tools**: Software, platforms, and services
- **Workflows**: Multi-step processes with clear objectives
- **Actions**: AI operations describing technical actions
- **Integration Patterns**: How tools connect and work together

**Why They Matter**: These elements create a structured knowledge base that makes information searchable and actionable.

### Library Structure

**Organization**: Tools are organized by category and stored as individual JSON files.

**Categories**: Tools are grouped by type (AI Tools, LLM Services, Automation Tools, etc.) to make discovery easier.

**Cross-References**: Tools reference each other when they integrate, creating a network of related resources.

### Tool JSON Format

**Structure**: Each tool is stored as a JSON file containing structured fields for:
- Basic information (name, vendor, category)
- Detailed descriptions and use cases
- Workflow examples
- Integration information
- Strengths and limitations

**Accessibility**: JSON format allows for programmatic access and easy searching, while remaining human-readable.

---

## Process Benefits

### Why This Matters for AI Team

**Continuous Discovery**
- New AI tools, LLM services, and automation platforms are automatically added as videos are processed
- No need to manually track new tool releases or updates
- Stay informed about the latest AI technology

**Validated Information**
- Tool information comes from actual usage examples in videos
- Real workflows and use cases, not just marketing materials
- Practical insights from people using tools in real projects

**Workflow Insights**
- Learn how tools are actually used together
- Understand integration patterns that work
- Discover efficient workflows used by other AI professionals

### How It Improves Tool Discovery

**Centralized Resource**
- All AI tool information in one organized location
- Easy to search and browse
- Consistent format makes comparison simple

**Context-Rich Information**
- Not just tool names, but how they're used
- Workflow examples and integration patterns
- Real-world use cases from video content
- Prompt engineering examples and implementation patterns

**Always Updated**
- Libraries grow as new videos are processed
- Information stays current with latest tool versions
- New workflows and patterns are continuously added

### How It Maintains Up-to-Date Tool Information

**Automated Processing**
- Videos are processed automatically as they're transcribed
- No manual data entry required
- Consistent extraction methodology ensures quality

**Version Tracking**
- Tool versions are noted when mentioned in videos
- Updates are captured as new videos are processed
- Historical information is preserved

**Continuous Improvement**
- Process refines based on feedback
- New extraction techniques improve coverage
- Library structure evolves to better serve AI team

---

## Related Resources

- **Video Analysis Methodology**: Detailed technical guide for processing video transcriptions (`Video_Analysis_Prompt.md`)
- **Tool Library Structure**: Explore organized tool categories in `LIBRARIES/Tools/`
- **Transcription Files**: Raw video transcriptions in `Transcribations/` folder
- **Processing Prompts**: Video transcription prompts in `Prompts/Video_Transcription/`

---

## Summary

The Video Transcript Processing Workflow transforms daily work tasks and unstructured video content into structured, searchable AI tool libraries. For the AI team, this means:

1. **Task-Driven Discovery**: Videos are identified based on actual daily work tasks and processes
2. **Fresh Content**: Only recent videos (last 30 days) are processed, ensuring up-to-date information
3. **Automatic Discovery**: New AI tools, LLM services, and automation platforms are automatically identified and documented from video content
4. **Structured Access**: Tool information is organized and easy to search
5. **Workflow Insights**: Learn how tools work together through documented integration patterns
6. **Continuous Updates**: Libraries stay current as new videos are processed

This process ensures the AI team has access to the latest AI tools, workflows, and best practices that are directly relevant to their current work, without needing to watch hours of video content manually.

---

**Maintained By**: Taxonomy Team  
**Last Updated**: December 12, 2025  
**Status**: Active  
**Version History**: 
- v1.1 (Dec 12, 2025) - Added Step 0: Video discovery process based on daily reports; Adapted for AI team
- v1.0 (Dec 12, 2025) - Initial version

