# Migration Guide - Consolidated Libraries

## Overview

This guide helps you integrate the consolidated library system into your applications for company context identification and location-based operations.

---

## Quick Start

### Step 1: Load the Master Index
```javascript
// Node.js / JavaScript
const fs = require('fs');
const index = JSON.parse(
  fs.readFileSync('Libs_Consolidated/library_index.json', 'utf8')
);

// Python
import json
with open('Libs_Consolidated/library_index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)
```

### Step 2: Query Specific Data
```javascript
// Get country name by ID
const countryName = index.indexes.countries[76]; // "Germany"

// Get all cities in a country
const cities = index.indexes.cities_by_country[76]; // ["Berlin"]

// Get department for a profession
const dept = index.indexes.profession_to_department[33]; // "Designers"
```

### Step 3: Load Full Data When Needed
```javascript
// Load complete country data
const countries = JSON.parse(
  fs.readFileSync('Libs_Consolidated/locations/countries.json', 'utf8')
);

// Find specific country
const germany = countries.data.find(c => c.iso2 === 'DE');
console.log(germany);
// {
//   id: 76,
//   name: "Germany",
//   iso2: "DE",
//   iso3: "DEU",
//   latitude: 52.5200,
//   longitude: 13.4050,
//   flag_url: "https://api.crm-s.com/flags/de.png"
// }
```

---

## Use Case Examples

### Use Case 1: Company Context Identification

**Scenario**: Identify a company's full business context from basic information

```javascript
// Input data
const companyInfo = {
  name: "TechStartup GmbH",
  industry: "Software Development",
  location: "Berlin, Germany",
  size: "50-100 employees"
};

// Step 1: Load necessary libraries
const industries = loadJSON('business/industries.json');
const subIndustries = loadJSON('business/sub_industries.json');
const countries = loadJSON('locations/countries.json');
const cities = loadJSON('locations/cities.json');
const departments = loadJSON('business/departments.json');

// Step 2: Identify industry
function identifyIndustry(industryName) {
  return industries.data.find(i =>
    i.name.toLowerCase().includes(industryName.toLowerCase())
  );
}

const industry = identifyIndustry("Software Development");
// Result: { id: 42, name: "Software Development", ... }

// Step 3: Identify location
function identifyLocation(cityName, countryName) {
  const country = countries.data.find(c =>
    c.name.toLowerCase() === countryName.toLowerCase()
  );

  const city = cities.data.find(c =>
    c.name.toLowerCase() === cityName.toLowerCase() &&
    c.country.id === country.id
  );

  return { country, city };
}

const location = identifyLocation("Berlin", "Germany");
// Result: {
//   country: { id: 76, name: "Germany", iso2: "DE", ... },
//   city: { id: 407, name: "Berlin", country: {...}, ... }
// }

// Step 4: Build complete context
const companyContext = {
  company: companyInfo.name,
  industry: {
    id: industry.id,
    name: industry.name,
    sub_industries: getSubIndustries(industry.id)
  },
  location: {
    city: location.city.name,
    country: location.country.name,
    iso2: location.country.iso2,
    coordinates: {
      lat: location.country.latitude,
      lng: location.country.longitude
    }
  },
  likely_departments: inferDepartments(industry.name),
  timezone: getTimezoneFromCoordinates(location.country.latitude, location.country.longitude)
};

console.log(companyContext);
// Result: Complete company context ready for CRM enrichment
```

### Use Case 2: Lead Qualification Scoring

**Scenario**: Score leads based on industry, location, and role

```javascript
function calculateLeadScore(lead) {
  let score = 0;
  const weights = {
    industry: 30,
    location: 20,
    department: 25,
    seniority: 25
  };

  // Load data
  const index = loadJSON('library_index.json');
  const industries = loadJSON('business/industries.json');
  const departments = loadJSON('business/departments.json');

  // Score by industry (target: Software Development, SaaS, Fintech)
  const targetIndustries = [42, 45, 67]; // IDs for target industries
  if (targetIndustries.includes(lead.industry_id)) {
    score += weights.industry;
  }

  // Score by location (target: EU countries)
  const euCountries = [3, 4, 5, 6, 7, 8, 9, 10]; // DE, FR, IT, ES, PL, NL, BE, SE
  if (euCountries.includes(lead.country_id)) {
    score += weights.location;
  }

  // Score by department (target: Tech roles)
  const targetDepts = ["Developers", "Designers", "Managers"];
  const leadDept = index.indexes.profession_to_department[lead.profession_id];
  if (targetDepts.includes(leadDept)) {
    score += weights.department;
  }

  // Score by seniority
  const seniorTitles = ["manager", "lead", "head", "director", "vp", "cto", "ceo"];
  if (seniorTitles.some(title => lead.job_title.toLowerCase().includes(title))) {
    score += weights.seniority;
  }

  return {
    score: score,
    grade: score >= 80 ? 'A' : score >= 60 ? 'B' : score >= 40 ? 'C' : 'D',
    qualified: score >= 60
  };
}

// Example
const lead = {
  name: "John Doe",
  job_title: "CTO",
  industry_id: 42, // Software Development
  country_id: 3,   // Germany
  profession_id: 10 // Full Stack Developer
};

const leadScore = calculateLeadScore(lead);
console.log(leadScore);
// Result: { score: 100, grade: 'A', qualified: true }
```

### Use Case 3: Geographic Market Segmentation

**Scenario**: Group leads by region for targeted campaigns

```javascript
function segmentLeadsByRegion(leads) {
  const index = loadJSON('library_index.json');
  const countries = loadJSON('locations/countries.json');

  // Define regions
  const regions = {
    'Western Europe': [1, 3, 4, 5, 6, 8, 9, 10, 36, 39], // UK, DE, FR, IT, ES, NL, BE, SE, IE, LU
    'Eastern Europe': [2, 7, 27, 28, 30, 32, 37, 38, 40, 41, 42, 43, 46, 48, 49, 51, 52], // UA, PL, BG, HR, CZ, EE, LV, LT, RO, SK, SI, RS, ME, MD, GE, BY
    'North America': [12, 13, 17], // US, CA, MX
    'Asia Pacific': [14, 15, 16, 21, 23], // AU, CN, JP, KR, PH
    'Middle East': [18, 19, 20, 24, 25], // TR, EG, UAE, MA, IL
    'Nordic': [10, 31, 33, 44], // SE, DK, FI, NO
    'Other': []
  };

  const segments = {};

  leads.forEach(lead => {
    let region = 'Other';

    for (const [regionName, countryIds] of Object.entries(regions)) {
      if (countryIds.includes(lead.country_id)) {
        region = regionName;
        break;
      }
    }

    if (!segments[region]) {
      segments[region] = [];
    }

    segments[region].push(lead);
  });

  return segments;
}

// Example
const leads = [
  { name: "Lead 1", country_id: 3 },  // Germany
  { name: "Lead 2", country_id: 2 },  // Ukraine
  { name: "Lead 3", country_id: 12 }, // USA
  { name: "Lead 4", country_id: 7 }   // Poland
];

const segments = segmentLeadsByRegion(leads);
console.log(Object.keys(segments));
// Result: ["Western Europe", "Eastern Europe", "North America"]
```

### Use Case 4: Department-Based Talent Pool Analysis

**Scenario**: Analyze available talent by department and location

```javascript
function analyzeTalentPool(candidates) {
  const departments = loadJSON('business/departments.json');
  const cities = loadJSON('locations/cities.json');
  const index = loadJSON('library_index.json');

  const analysis = {
    by_department: {},
    by_location: {},
    by_dept_and_location: {}
  };

  // Group by department
  candidates.forEach(candidate => {
    const dept = index.indexes.profession_to_department[candidate.profession_id];

    if (!analysis.by_department[dept]) {
      analysis.by_department[dept] = 0;
    }
    analysis.by_department[dept]++;

    // Group by location
    const cityName = cities.data.find(c => c.id === candidate.city_id)?.name || 'Unknown';
    const countryName = index.indexes.countries[candidate.country_id] || 'Unknown';
    const location = `${cityName}, ${countryName}`;

    if (!analysis.by_location[location]) {
      analysis.by_location[location] = 0;
    }
    analysis.by_location[location]++;

    // Combined
    const key = `${dept} in ${location}`;
    if (!analysis.by_dept_and_location[key]) {
      analysis.by_dept_and_location[key] = 0;
    }
    analysis.by_dept_and_location[key]++;
  });

  return analysis;
}

// Example
const candidates = [
  { profession_id: 9, city_id: 407, country_id: 76 },  // Backend Dev in Berlin, DE
  { profession_id: 10, city_id: 407, country_id: 76 }, // Frontend Dev in Berlin, DE
  { profession_id: 9, city_id: 450, country_id: 2 },   // Backend Dev in Kyiv, UA
];

const analysis = analyzeTalentPool(candidates);
console.log(analysis);
// Result: {
//   by_department: { "Developers": 3 },
//   by_location: { "Berlin, Germany": 2, "Kyiv, Ukraine": 1 },
//   by_dept_and_location: { "Developers in Berlin, Germany": 2, "Developers in Kyiv, Ukraine": 1 }
// }
```

### Use Case 5: Industry-Based Content Personalization

**Scenario**: Personalize content based on company industry

```javascript
function personalizeContent(company, availableContent) {
  const industries = loadJSON('business/industries.json');
  const subIndustries = loadJSON('business/sub_industries.json');
  const index = loadJSON('library_index.json');

  // Get company's industry and sub-industries
  const industryId = company.industry_id;
  const industry = industries.data.find(i => i.id === industryId);
  const companySubIndustries = index.indexes.sub_industries_by_industry[industryId] || [];

  // Score content by relevance
  const scoredContent = availableContent.map(content => {
    let relevanceScore = 0;

    // Exact industry match
    if (content.target_industries.includes(industryId)) {
      relevanceScore += 50;
    }

    // Sub-industry match
    const matchingSubIndustries = content.target_sub_industries.filter(
      sid => companySubIndustries.includes(sid)
    );
    relevanceScore += matchingSubIndustries.length * 20;

    // Related industries (same sector)
    const relatedIndustries = findRelatedIndustries(industryId);
    if (content.target_industries.some(tid => relatedIndustries.includes(tid))) {
      relevanceScore += 10;
    }

    return {
      ...content,
      relevanceScore
    };
  });

  // Return top 5 most relevant content pieces
  return scoredContent
    .sort((a, b) => b.relevanceScore - a.relevanceScore)
    .slice(0, 5);
}

// Example
const company = {
  name: "FinTech Startup",
  industry_id: 67 // Fintech
};

const content = [
  { title: "Guide to SaaS Metrics", target_industries: [42, 45], target_sub_industries: [145] },
  { title: "Fintech Compliance 2025", target_industries: [67], target_sub_industries: [189, 190] },
  { title: "Building Payment Systems", target_industries: [67], target_sub_industries: [189] }
];

const personalizedContent = personalizeContent(company, content);
// Result: Top content ranked by relevance to Fintech industry
```

---

## API Endpoints (Recommended Structure)

If building a REST API, consider these endpoints:

### Location Endpoints
```
GET /api/v1/locations/countries
GET /api/v1/locations/countries/:id
GET /api/v1/locations/countries/:id/cities
GET /api/v1/locations/cities
GET /api/v1/locations/cities/:id
```

### Business Context Endpoints
```
GET /api/v1/business/industries
GET /api/v1/business/industries/:id
GET /api/v1/business/industries/:id/sub-industries
GET /api/v1/business/sub-industries
GET /api/v1/business/departments
GET /api/v1/business/departments/:id/professions
```

### Search & Query Endpoints
```
GET /api/v1/search/countries?q=germany
GET /api/v1/search/cities?country=76&q=berlin
GET /api/v1/search/industries?q=software
GET /api/v1/context/identify
  POST body: { industry: "Software", location: "Berlin, Germany" }
  Response: { industry: {...}, location: {...}, departments: [...] }
```

---

## Database Schema (SQL Example)

### Countries Table
```sql
CREATE TABLE countries (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  iso2 CHAR(2) NOT NULL UNIQUE,
  iso3 CHAR(3) NOT NULL UNIQUE,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  flag_url VARCHAR(500),
  created_at TIMESTAMP,
  UNIQUE INDEX idx_iso2 (iso2),
  INDEX idx_name (name)
);
```

### Cities Table
```sql
CREATE TABLE cities (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  country_id INTEGER NOT NULL,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  created_at TIMESTAMP,
  FOREIGN KEY (country_id) REFERENCES countries(id),
  INDEX idx_country_id (country_id),
  INDEX idx_name (name)
);
```

### Industries Table
```sql
CREATE TABLE industries (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  color VARCHAR(50),
  status VARCHAR(50),
  created_at TIMESTAMP,
  created_by VARCHAR(255),
  INDEX idx_name (name)
);
```

### Sub-Industries Table
```sql
CREATE TABLE sub_industries (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  parent_industry_id INTEGER NOT NULL,
  description TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (parent_industry_id) REFERENCES industries(id),
  INDEX idx_parent_industry_id (parent_industry_id),
  INDEX idx_name (name)
);
```

### Departments Table
```sql
CREATE TABLE departments (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  color VARCHAR(50),
  language VARCHAR(50),
  created_at TIMESTAMP,
  INDEX idx_name (name)
);
```

### Professions Table
```sql
CREATE TABLE professions (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  department_id INTEGER NOT NULL,
  is_translated BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (department_id) REFERENCES departments(id),
  INDEX idx_department_id (department_id),
  INDEX idx_name (name)
);
```

---

## Data Import Scripts

### Import to PostgreSQL
```bash
# Import countries
psql -U username -d dbname -c "\copy countries (id, name, iso2, iso3, latitude, longitude, flag_url) FROM 'countries.csv' DELIMITER ',' CSV HEADER;"

# Import cities
psql -U username -d dbname -c "\copy cities (id, name, country_id, latitude, longitude) FROM 'cities.csv' DELIMITER ',' CSV HEADER;"

# Import industries
psql -U username -d dbname -c "\copy industries (id, name, description, color) FROM 'industries.csv' DELIMITER ',' CSV HEADER;"
```

### Import to MongoDB
```javascript
// Node.js with MongoDB
const { MongoClient } = require('mongodb');
const fs = require('fs');

async function importData() {
  const client = await MongoClient.connect('mongodb://localhost:27017');
  const db = client.db('consolidated_libs');

  // Import countries
  const countries = JSON.parse(fs.readFileSync('locations/countries.json', 'utf8'));
  await db.collection('countries').insertMany(countries.data);

  // Import cities
  const cities = JSON.parse(fs.readFileSync('locations/cities.json', 'utf8'));
  await db.collection('cities').insertMany(cities.data);

  // Import industries
  const industries = JSON.parse(fs.readFileSync('business/industries.json', 'utf8'));
  await db.collection('industries').insertMany(industries.data);

  console.log('Import complete');
  await client.close();
}

importData().catch(console.error);
```

---

## Performance Optimization

### Caching Strategy
```javascript
// In-memory cache for frequently accessed data
const cache = {
  index: null,
  countries: null,
  industries: null,
  ttl: 3600000 // 1 hour
};

function getIndex() {
  if (!cache.index || Date.now() - cache.indexLoadTime > cache.ttl) {
    cache.index = loadJSON('library_index.json');
    cache.indexLoadTime = Date.now();
  }
  return cache.index;
}

function getCountries() {
  if (!cache.countries || Date.now() - cache.countriesLoadTime > cache.ttl) {
    cache.countries = loadJSON('locations/countries.json');
    cache.countriesLoadTime = Date.now();
  }
  return cache.countries;
}
```

### Indexing for Fast Lookups
```javascript
// Build reverse indexes for O(1) lookups
function buildIndexes(data) {
  const indexes = {
    byId: {},
    byName: {},
    byIso2: {},
    byIso3: {}
  };

  data.forEach(item => {
    indexes.byId[item.id] = item;
    indexes.byName[item.name.toLowerCase()] = item;
    if (item.iso2) indexes.byIso2[item.iso2] = item;
    if (item.iso3) indexes.byIso3[item.iso3] = item;
  });

  return indexes;
}

const countryIndexes = buildIndexes(countries.data);
const germany = countryIndexes.byIso2['DE']; // O(1) lookup
```

---

## Testing & Validation

### Sample Test Cases
```javascript
describe('Company Context Identification', () => {
  it('should identify industry from partial name', () => {
    const result = identifyIndustry("software");
    expect(result.name).toContain("Software");
  });

  it('should find city by name and country', () => {
    const result = identifyLocation("Berlin", "Germany");
    expect(result.city.id).toBe(407);
    expect(result.country.iso2).toBe("DE");
  });

  it('should map profession to department', () => {
    const dept = getProfessionDepartment(9); // Backend Developer
    expect(dept).toBe("Developers");
  });
});
```

---

## Troubleshooting

### Common Issues

**Issue 1**: Cannot find city in database
- **Solution**: Check if city exists in `cities.json`. We currently have 37 major cities. For unlisted cities, fall back to country-level data.

**Issue 2**: Industry name variations
- **Solution**: Use fuzzy matching or implement industry name aliases. Example: "IT" = "Information Technology" = "Tech"

**Issue 3**: Missing coordinates for cities
- **Solution**: Some cities have `null` coordinates. Use geocoding API (Google Maps, OpenStreetMap) to populate missing data.

**Issue 4**: Profession not mapping to department
- **Solution**: Check `library_index.json` → `profession_to_department`. If profession ID not found, it may be a new profession not in consolidated data.

---

## Next Steps

1. ✅ Load master index: `library_index.json`
2. ✅ Integrate location data for geographic features
3. ✅ Integrate business context for company identification
4. ✅ Build caching layer for performance
5. ✅ Implement search/query functions
6. ✅ Add error handling and fallbacks
7. ✅ Monitor data quality and update as needed

---

## Support

For questions or issues:
- Review the main [README.md](README.md) for data structure details
- Check the consolidation script for data processing logic
- Examine sample code in this guide

---

**Version**: 1.0
**Last Updated**: 2025-11-07
