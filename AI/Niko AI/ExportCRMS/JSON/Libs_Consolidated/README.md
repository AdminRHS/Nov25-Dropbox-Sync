# Consolidated Libraries - Complete Reference

## Overview

This consolidated library system combines semantic framework data from **Libs 25** with rich business context and location data from **Libs_JSON_old**, creating a unified reference system optimized for:

- **Company Context Identification** - Industry, sub-industry, and department classifications
- **Location-Based Operations** - Countries and cities with coordinates and ISO codes
- **Semantic Workflow Modeling** - Actions, objects, tools, and responsibilities
- **Multi-Language Support** - International business operations

**Version**: 1.0
**Consolidated Date**: 2025-11-07
**Total Entities**: 863 (Countries: 54, Cities: 37, Industries: 151, Sub-Industries: 376, Departments: 15, Professions: 230)

---

## Directory Structure

```
Libs_Consolidated/
├── README.md                           # This file
├── library_index.json                  # Master index with cross-references
├── locations/
│   ├── countries.json                  # 54 countries with ISO codes & coordinates
│   └── cities.json                     # 37 major cities worldwide
├── business/
│   ├── industries.json                 # 151 industry classifications
│   ├── sub_industries.json             # 376 detailed sub-categories
│   └── departments.json                # 15 departments with 230 professions
└── MIGRATION_GUIDE.md                  # Integration instructions
```

---

## File Descriptions

### Master Index

#### library_index.json
**Purpose**: Central registry with quick lookups and cross-references

**Contains**:
- Statistics summary (total counts for all entity types)
- Country index (ID → Name mapping)
- Cities grouped by country
- Industry index with sub-industry relationships
- Department index with profession mappings
- File location references

**Use Cases**:
- Fast entity lookups without loading full files
- Understanding relationships between entities
- Navigation to specific data files
- API endpoint routing

**Example Query Patterns**:
```javascript
// Get all cities in Germany (country_id: 76)
index.indexes.cities_by_country[76]  // ["Berlin"]

// Get department name for profession ID
index.indexes.profession_to_department[33]  // "Designers"

// Get all sub-industries for an industry
index.indexes.sub_industries_by_industry[5]  // ["Software Development", ...]
```

---

## Location Data

### countries.json
**Purpose**: Global country reference with geographic data

**Structure**:
```json
{
  "version": "1.0",
  "source": "Libs_JSON_old/countries.json",
  "consolidated_date": "2025-11-07",
  "total_countries": 54,
  "data": [
    {
      "id": 1,
      "name": "United Kingdom",
      "iso2": "GB",
      "iso3": "GBR",
      "latitude": 51.5074,
      "longitude": -0.1278,
      "flag_url": "https://api.crm-s.com/flags/gb.png",
      "metadata": {
        "created_at": "2024-09-10T17:07:40.000000Z",
        "translation_language": "English"
      }
    }
  ]
}
```

**Key Fields**:
- `id`: Unique country identifier
- `name`: Official country name
- `iso2`: ISO 3166-1 alpha-2 code (2 letters)
- `iso3`: ISO 3166-1 alpha-3 code (3 letters)
- `latitude/longitude`: Geographic coordinates (capital city)
- `flag_url`: Country flag image URL

**Coverage**: 54 countries across all continents
- **Europe**: UK, Germany, France, Spain, Italy, Poland, Ukraine, etc.
- **North America**: USA, Canada, Mexico
- **Asia**: China, Japan, South Korea, Israel, UAE, Turkey
- **Oceania**: Australia, New Zealand
- **Middle East**: UAE, Israel, Egypt, Morocco
- **Other**: Various EU and non-EU European countries

**Use Cases**:
- Address validation and normalization
- Timezone determination
- Currency/locale selection
- Geographic filtering and search
- International shipping calculations
- Tax jurisdiction identification

---

### cities.json
**Purpose**: Major city locations with country associations

**Structure**:
```json
{
  "version": "1.0",
  "source": "Libs_JSON_old/cities.json",
  "consolidated_date": "2025-11-07",
  "total_cities": 37,
  "data": [
    {
      "id": 407,
      "name": "Berlin",
      "country": {
        "id": 76,
        "name": "Germany",
        "iso2": "DE",
        "iso3": "DEU"
      },
      "latitude": null,
      "longitude": null,
      "metadata": {
        "created_at": "2024-09-10T17:30:29.000000Z",
        "translation_language": "English"
      }
    }
  ]
}
```

**Key Fields**:
- `id`: Unique city identifier
- `name`: City name
- `country`: Complete country reference (id, name, ISO codes)
- `latitude/longitude`: Geographic coordinates (when available)

**Coverage**: 37 major cities including:
- **Germany**: Berlin
- **Italy**: Milan, Rome
- **Poland**: Warsaw, Krakow
- **Spain**: Madrid
- **Ukraine**: Kyiv, Lviv, Kharkiv, Odesa, Dnipro, Cherkasy, Chernihiv, Chernivtsi, and 20+ more
- **Other**: Vienna, Riga, Oslo, Izmir, and more

**Use Cases**:
- Candidate/lead location tracking
- Regional job market analysis
- Office location management
- Remote team timezone coordination
- Local market targeting

---

## Business Context Data

### industries.json
**Purpose**: Top-level industry classifications for company categorization

**Structure**:
```json
{
  "version": "1.0",
  "source": "Libs_JSON_old/industry.json",
  "consolidated_date": "2025-11-07",
  "total_industries": 151,
  "data": [
    {
      "id": 1,
      "name": "Accounting & Audit",
      "description": null,
      "color": "rgb(255, 87, 87)",
      "metadata": {
        "created_at": "2024-09-10T15:30:00.000000Z",
        "created_by": "System Admin",
        "status": "Approved"
      }
    }
  ]
}
```

**Key Fields**:
- `id`: Unique industry identifier
- `name`: Industry name
- `description`: Optional detailed description
- `color`: RGB color for UI visualization
- `metadata`: Creation info, status, author

**Major Industry Categories** (151 total):
- **Technology**: Software Development, IT Services, SaaS
- **Finance**: Banking, Investment, Insurance, Accounting
- **Healthcare**: Hospitals, Pharma, Medical Devices
- **Manufacturing**: Various production sectors
- **Services**: Professional Services, Consulting, Legal
- **Retail**: E-commerce, Physical Retail
- **Education**: Schools, Universities, EdTech
- **Real Estate**: Property Management, Construction
- **Hospitality**: Hotels, Tourism, Restaurants
- **Media**: Publishing, Broadcasting, Entertainment
- **Transportation**: Logistics, Shipping
- **Energy**: Oil & Gas, Renewable Energy
- **Government**: Public Administration, Defense

**Use Cases**:
- Company classification and categorization
- Lead qualification and scoring
- Market segmentation analysis
- Industry-specific content targeting
- Competitive intelligence gathering
- Talent pool identification by industry

---

### sub_industries.json
**Purpose**: Granular industry subcategories for precise company context

**Structure**:
```json
{
  "version": "1.0",
  "source": "Libs_JSON_old/sub-industry.json",
  "consolidated_date": "2025-11-07",
  "total_sub_industries": 376,
  "data": [
    {
      "id": 1,
      "name": "Abrasives & Nonmetallic Minerals Manufacturing",
      "parent_industry_id": 45,
      "description": null,
      "metadata": {
        "created_at": "2024-09-10T15:30:00.000000Z",
        "created_by": "System Admin"
      }
    }
  ]
}
```

**Key Fields**:
- `id`: Unique sub-industry identifier
- `name`: Sub-industry name
- `parent_industry_id`: Links to parent industry
- `description`: Optional details
- `metadata`: Creation tracking

**Hierarchical Structure**:
- 376 sub-industries map to 151 parent industries
- Average of 2-3 sub-industries per industry
- Enables 2-level categorization: Industry → Sub-Industry

**Examples by Industry**:

**Software Development Industry**:
- SaaS Platforms
- Mobile App Development
- Enterprise Software
- Open Source Projects
- Developer Tools

**Healthcare Industry**:
- Hospital Systems
- Pharmaceutical Manufacturing
- Medical Devices
- Telemedicine
- Healthcare IT

**Finance Industry**:
- Investment Banking
- Retail Banking
- Insurance Services
- Fintech
- Asset Management

**Use Cases**:
- Precise company categorization beyond broad industries
- Niche market targeting
- Specialized talent recruitment
- Competitive set definition
- M&A target identification
- Market research segmentation

---

### departments.json
**Purpose**: Organizational departments with profession hierarchies

**Structure**:
```json
{
  "version": "1.0",
  "source": "Libs_JSON_old/Department.json",
  "consolidated_date": "2025-11-07",
  "total_departments": 15,
  "total_professions": 230,
  "data": [
    {
      "id": 4,
      "name": "Designers",
      "color": "rgb(151, 71, 255)",
      "translation": {
        "language": "English",
        "iso2": "EN"
      },
      "professions": [
        {
          "id": 1,
          "name": "3d designer",
          "is_translated": false,
          "department_id": 4
        },
        {
          "id": 2,
          "name": "Graphic designer",
          "is_translated": false,
          "department_id": 4
        }
      ],
      "profession_count": 30,
      "metadata": {
        "created_at": "2024-09-10T15:22:37.000000Z",
        "created_by": "System Admin"
      }
    }
  ]
}
```

**Departments & Professions**:

1. **Managers** (40+ professions)
   - Project Manager, Product Manager, Scrum Master
   - HR Manager, Recruiter, Talent Acquisition
   - Sales Manager, Account Manager, Business Development
   - Financial Manager, Accountant, Bookkeeper
   - Event Manager, Tourism Manager
   - Personal Assistant, Executive Assistant, Secretary
   - Analyst, Data Entry Specialist
   - Lead Generator, Chat Operator
   - Prompt Engineer, AI Engineer

2. **Developers** (15+ professions)
   - Backend Developer, Frontend Developer, Full Stack Developer
   - Mobile Developer (iOS/Android)
   - QA Engineer, Test Automation
   - System Administrator, DevOps Engineer
   - UI Developer, Client-Side Developer
   - Interface Engineer

3. **Marketers** (40+ professions)
   - **SEO**: SEO Manager, SEO Specialist, SEO Strategist
   - **Content**: Content Manager, Copywriter, Content Strategist
   - **Social Media**: SMM Manager, Social Media Specialist
   - **Paid Ads**: Media Buyer, PPC Specialist, Targetologist
   - **Email**: Email Marketer
   - **PR**: PR Manager, Influencer Manager
   - **Other**: Affiliate Manager, Linkbuilder, Translator, Proofreader

4. **Designers** (30+ professions)
   - **3D/Visual**: 3D Designer, Visualizer, Concept Artist
   - **Graphics**: Graphic Designer, Brand Identity Designer
   - **UI/UX**: UI/UX Designer, Product Designer, Interaction Designer
   - **Web**: Web Designer, Wordpress Designer
   - **Other**: Illustrator, Interior Designer, Motion Designer, Character Designer

5. **Videographers** (7+ professions)
   - Video Editor, Mobile Video Editor
   - Motion Designer
   - Video Content Creator
   - Reels/Shorts Creator
   - Mobilograph

**Multi-Language Support**:
- English (primary)
- Ukrainian translations
- Polish translations
- German translations

**Use Cases**:
- Organizational structure modeling
- Role-based access control (RBAC)
- Talent pipeline segmentation
- Job posting categorization
- Team composition planning
- Skill gap analysis
- Hiring needs forecasting

---

## Integration with Libs 25

The consolidated library **complements** the existing Libs 25 semantic libraries:

### Libs 25 Original Content (Still Active):
- **actions_library.json** (600+ action verbs for workflow modeling)
- **objects_library.json** (1,000+ work deliverables and outputs)
- **tools_library.json** (200+ software tools and platforms)
- **professions_library.json** (300+ job titles with semantic tags)
- **responsibilities_library.json** (150+ job duties and tasks)

### Consolidated Library Enhancements:
- **Location Context**: Countries and cities for geographic operations
- **Business Context**: Industries, sub-industries for company classification
- **Department Hierarchies**: Organizational structure and profession groupings
- **Cross-References**: Master index linking all entities

### Recommended Usage Pattern:

```
For Semantic Queries (Tasks, Workflows, Skills):
→ Use Libs 25 (actions, objects, tools, responsibilities)

For Business Context (Company Info, Location, Industry):
→ Use Libs_Consolidated (countries, cities, industries, departments)

For Complete View (Professions with full context):
→ Combine both: Libs 25 professions + Consolidated departments
```

---

## API Query Patterns

### Example 1: Find all professions in a department
```javascript
// Load departments
const departments = loadJSON('business/departments.json');
const designers = departments.data.find(d => d.name === 'Designers');
const professions = designers.professions.map(p => p.name);
// Result: ["3d designer", "Graphic designer", "UI UX designer", ...]
```

### Example 2: Get sub-industries for a company
```javascript
// Load index
const index = loadJSON('library_index.json');
const industryId = 5; // Software Development
const subIndustries = index.indexes.sub_industries_by_industry[industryId];
// Result: ["SaaS", "Mobile Apps", "Enterprise Software", ...]
```

### Example 3: Find cities in a country
```javascript
// Load index
const index = loadJSON('library_index.json');
const germanyId = 76;
const cities = index.indexes.cities_by_country[germanyId];
// Result: ["Berlin"]
```

### Example 4: Company context identification
```javascript
// Input: Company operates in "Software Development" in "Berlin, Germany"
const context = {
  industry: findIndustry("Software Development"), // id: 5
  sub_industry: findSubIndustry("SaaS", 5),       // id: 23
  country: findCountry("Germany"),                // id: 76, iso2: "DE"
  city: findCity("Berlin", 76),                   // id: 407
  departments: ["Developers", "Designers"],       // ids: [2, 4]
  professions: ["Full Stack Developer", "UI/UX Designer"]
};
```

---

## Data Quality & Maintenance

### Current Data Quality:
- ✓ All entities have unique IDs
- ✓ Hierarchical relationships preserved
- ✓ ISO codes standardized (countries)
- ✓ Metadata includes creation dates and authors
- ✓ Multi-language support structure maintained

### Known Limitations:
- Some city coordinates are `null` (need to be populated)
- Not all sub-industries have descriptions
- Profession translations incomplete for some languages
- Industry color schemes are basic RGB

### Maintenance Recommendations:
1. **Quarterly**: Review and add new industries/sub-industries
2. **Bi-annually**: Update city coordinates using geocoding service
3. **Annually**: Audit profession lists for emerging roles
4. **As-needed**: Add new countries/cities based on business expansion

---

## Version History

### v1.0 (2025-11-07)
- Initial consolidation release
- Extracted 54 countries, 37 cities from Libs_JSON_old
- Extracted 151 industries, 376 sub-industries
- Extracted 15 departments with 230 professions
- Created master index with cross-references
- Established integration pattern with Libs 25

---

## Related Documentation

- **Libs 25**: `C:\Users\Dell\Dropbox\Nov25\Libs 25\README.md`
- **Original CRM Export**: `C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\JSON\Libs_JSON_old\`
- **Libs JSON v1 README**: `C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\JSON\Libs_JSON_v1\README.md`
- **Consolidation Script**: `C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\scripts\consolidate_libraries.py`

---

## Support & Contributions

**Questions or Issues?**
- Check the master index first: `library_index.json`
- Review the MIGRATION_GUIDE.md for integration patterns
- Examine the consolidation script for data extraction logic

**Need to Add Data?**
- Industries/Sub-industries: Edit source files in Libs_JSON_old, then re-run consolidation script
- Countries/Cities: Update Libs_JSON_old source, then consolidate
- Departments/Professions: Modify Libs_JSON_old Department.json, then consolidate

---

**Last Updated**: 2025-11-07
**Consolidated By**: Library Consolidation Script v1.0
**Total Data Size**: ~1.2 MB (consolidated from 8 MB original)
