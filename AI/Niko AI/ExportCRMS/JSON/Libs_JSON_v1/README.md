# Libs JSON v1 - Library Data Structure Documentation

## Overview

This directory contains library reference data exported from the CRM system in JSON format. These libraries serve as lookup tables for various entities used throughout the CRM application including statuses, departments, languages, professions, and more.

## Data Structure

All library JSON files follow a consistent structure with a root `data` array containing library items. Each library type has specific fields relevant to its purpose.

### Common Fields

Most library items share these common fields:

```json
{
  "id": number,                    // Unique identifier
  "name": string,                  // Display name
  "color": string,                 // RGB color code for UI
  "status": object,                // Status metadata
  "translation": object,           // Translation/language info
  "priority": object,              // Priority level
  "created_at": string,            // ISO timestamp
  "created_by": object,            // User who created the entry
  "description": string | null,    // Optional description
  "image_icon": string | null,     // Optional icon URL
  "count_edits": number            // Edit counter
}
```

## Library Files

### 1. Status.json
**Purpose**: Candidate/lead status tracking

**Structure**:
```json
{
  "data": [
    {
      "id": 6,
      "name": "Application",
      "color": "rgb(184, 9, 246)"
    }
  ]
}
```

**Statuses Include**:
- Application, Approved, Black list, Closed, Denied
- Didn't start, Follow up, Hired, Interview, New
- No answer, Not approved, Not interested, Not looking
- Not relevant, Pending, Published, Refused, Started, Video

---

### 2. Department.json
**Purpose**: Organizational departments with associated professions

**Structure**:
```json
{
  "data": [
    {
      "id": 32,
      "department_id": 4,
      "name": "Designers",
      "color": "rgb(151, 71, 255)",
      "professions": [
        {
          "id": 33,
          "profession_id": 1,
          "name": "3d designer",
          "is_translated": false,
          "department_id": 4
        }
      ],
      "progressable_type": "Modules\\Library\\Models\\Department"
    }
  ]
}
```

**Departments Include**:
- Managers (rgb: 255, 87, 87)
- Developers (rgb: 61, 183, 124)
- Marketers (rgb: 255, 64, 129)
- Designers (rgb: 151, 71, 255)
- Videographers (rgb: 126, 207, 203)

**Multi-Language Support**: Departments are available in English, Ukrainian, and Polish translations.

---

### 3. Langs.json
**Purpose**: Supported languages in the system

**Structure**:
```json
{
  "data": [
    {
      "id": 1,
      "language_id": 1,
      "name": "English",
      "iso2": "EN",
      "iso3": "ENG",
      "image": "https://api.crm-s.com/flags/gb.png",
      "progressable_type": "Modules\\Library\\Models\\Language"
    }
  ]
}
```

**Languages Include**:
- English, French, German, Spanish, Italian, Portuguese
- Dutch, Polish, Swedish, Danish, Russian, Romanian
- Czech, Bulgarian, Ukrainian, Turkish, Chinese
- Azerbaijani, Kazakh

---

### 4. Proffessions.json
**Purpose**: Job positions/roles

**Note**: This is a detailed list of professions linked to departments. Each profession includes:
- Unique ID
- Profession name
- Department association
- Translation status

---

### 5. cities.json
**Purpose**: City locations for addressing

Expected structure similar to countries with city-specific data.

---

### 6. countries.json
**Purpose**: Country reference data

Expected to include country names, codes, and regional information.

---

### 7. industry.json & sub-industry.json
**Purpose**: Industry classifications

Hierarchical structure where industries can have sub-industries for detailed categorization.

---

### 8. action.json
**Purpose**: System actions/activities tracking

Large file containing action definitions and metadata.

---

### 9. formats.json
**Purpose**: Data format specifications

File format types supported in the system.

---

### 10. objects.json
**Purpose**: System object definitions

Object types and their properties.

---

### 11. tool-type.json & tools.json
**Purpose**: Tool classifications and specific tools

Reference data for tools used in projects or workflows.

---

## Sample Data Examples

### Sample_Candidate_Profile.json

Example candidate record structure showing:
- Personal information (name, age, contact details)
- Professional details (department, position, expected salary)
- Application status and tracking
- HR manager assignment
- Interview scheduling
- Portfolio and resume links
- Social media handles (Instagram, Telegram, Viber)

```json
{
  "id": 100001,
  "name_candidate": "Sarah Johnson",
  "department_id": "5",
  "position_id": "45",
  "status_candidate_id": "11",
  "expected_salary": 1500,
  "expected_salary_currency_id": "1",
  "email": "sarah.johnson@example.com",
  "phone": "+12345678901"
}
```

### Sample_LeadAccount_Profile.json

Example lead/account record structure for B2B tracking.

---

## Usage Notes

1. **Color Codes**: All colors are in RGB format (e.g., `"rgb(255, 87, 87)"`) for consistent UI rendering
2. **Relationships**: Many libraries reference each other via ID fields (e.g., `department_id`, `language_id`)
3. **Translations**: Multi-language support is built-in via the `translation` object
4. **Status Tracking**: Most entities include status and priority for workflow management
5. **Audit Trail**: `created_by`, `created_at`, and `count_edits` provide audit information

## Integration

These library files are meant to be:
- Imported into application databases as reference tables
- Used for dropdown/select field population in forms
- Cached for performance in frontend applications
- Synchronized across system modules

## Version History

**v1**: Initial export from old CRM system
- Date: 2025-11-07
- Source: C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\Libs
- Conversion: Python script `convert_libs_to_json.py`

## Related Documentation

- See `Sample_Candidate_Profile.json` for candidate data structure
- See `Sample_LeadAccount_Profile.json` for lead/account structure
- Original source: `Libs_JSON_old` directory

---

**Last Updated**: 2025-11-07
