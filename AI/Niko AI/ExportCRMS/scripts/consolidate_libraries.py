"""
Script to consolidate library data from Libs_JSON_old and Libs 25.
Extracts location data, business context, and creates a unified structure.
"""
import json
import os
from pathlib import Path
from collections import defaultdict


def load_json(file_path):
    """Load JSON file and return data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, file_path):
    """Save data to JSON file with proper formatting."""
    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  [OK] Created: {output_path}")


def extract_countries(source_file, output_file):
    """Extract and clean countries data."""
    print("\nExtracting countries data...")
    data = load_json(source_file)

    countries = []
    for item in data.get('data', []):
        country = {
            'id': item['country_id'],
            'name': item['name'],
            'iso2': item['iso2'],
            'iso3': item['iso3'],
            'latitude': item.get('latitude'),
            'longitude': item.get('longitude'),
            'flag_url': item.get('image'),
            'metadata': {
                'created_at': item.get('created_at'),
                'translation_language': item.get('translation', {}).get('name', 'English')
            }
        }
        countries.append(country)

    output_data = {
        'version': '1.0',
        'source': 'Libs_JSON_old/countries.json',
        'consolidated_date': '2025-11-07',
        'total_countries': len(countries),
        'data': sorted(countries, key=lambda x: x['name'])
    }

    save_json(output_data, output_file)
    return len(countries)


def extract_cities(source_file, output_file):
    """Extract and clean cities data."""
    print("\nExtracting cities data...")
    data = load_json(source_file)

    cities = []
    for item in data.get('data', []):
        city = {
            'id': item.get('city_id', item.get('id')),
            'name': item['name'],
            'country': {
                'id': item.get('country', {}).get('id'),
                'name': item.get('country', {}).get('name'),
                'iso2': item.get('country', {}).get('iso2'),
                'iso3': item.get('country', {}).get('iso3')
            },
            'latitude': item.get('latitude'),
            'longitude': item.get('longitude'),
            'metadata': {
                'created_at': item.get('created_at'),
                'translation_language': item.get('translation', {}).get('name', 'English')
            }
        }
        cities.append(city)

    output_data = {
        'version': '1.0',
        'source': 'Libs_JSON_old/cities.json',
        'consolidated_date': '2025-11-07',
        'total_cities': len(cities),
        'data': sorted(cities, key=lambda x: (x['country']['name'] or '', x['name']))
    }

    save_json(output_data, output_file)
    return len(cities)


def extract_industries(source_file, output_file):
    """Extract and clean industries data."""
    print("\nExtracting industries data...")
    data = load_json(source_file)

    industries = []
    for item in data.get('data', []):
        industry = {
            'id': item.get('industry_id', item.get('id')),
            'name': item['name'],
            'description': item.get('description'),
            'color': item.get('color'),
            'metadata': {
                'created_at': item.get('created_at'),
                'created_by': item.get('created_by', {}).get('name') if item.get('created_by') else None,
                'status': item.get('status', {}).get('name') if item.get('status') else None
            }
        }
        industries.append(industry)

    output_data = {
        'version': '1.0',
        'source': 'Libs_JSON_old/industry.json',
        'consolidated_date': '2025-11-07',
        'total_industries': len(industries),
        'data': sorted(industries, key=lambda x: x['name'])
    }

    save_json(output_data, output_file)
    return len(industries)


def extract_sub_industries(source_file, output_file):
    """Extract and clean sub-industries data."""
    print("\nExtracting sub-industries data...")
    data = load_json(source_file)

    sub_industries = []
    for item in data.get('data', []):
        sub_industry = {
            'id': item.get('sub_industry_id', item.get('id')),
            'name': item['name'],
            'parent_industry_id': item.get('industry_id'),
            'description': item.get('description'),
            'metadata': {
                'created_at': item.get('created_at'),
                'created_by': item.get('created_by', {}).get('name') if item.get('created_by') else None
            }
        }
        sub_industries.append(sub_industry)

    output_data = {
        'version': '1.0',
        'source': 'Libs_JSON_old/sub-industry.json',
        'consolidated_date': '2025-11-07',
        'total_sub_industries': len(sub_industries),
        'data': sorted(sub_industries, key=lambda x: x['name'])
    }

    save_json(output_data, output_file)
    return len(sub_industries)


def extract_departments(source_file, output_file):
    """Extract and clean departments data."""
    print("\nExtracting departments data...")
    data = load_json(source_file)

    departments = []
    for item in data.get('data', []):
        # Extract professions
        professions = []
        for prof in item.get('professions', []):
            profession = {
                'id': prof.get('profession_id', prof.get('id')),
                'name': prof.get('name'),
                'is_translated': prof.get('is_translated', False),
                'department_id': prof.get('department_id')
            }
            professions.append(profession)

        department = {
            'id': item.get('department_id', item.get('id')),
            'name': item['name'],
            'color': item.get('color'),
            'translation': {
                'language': item.get('translation', {}).get('name'),
                'iso2': item.get('translation', {}).get('iso2')
            },
            'professions': professions,
            'profession_count': len(professions),
            'metadata': {
                'created_at': item.get('created_at'),
                'created_by': item.get('created_by', {}).get('name') if item.get('created_by') else None
            }
        }
        departments.append(department)

    output_data = {
        'version': '1.0',
        'source': 'Libs_JSON_old/Department.json',
        'consolidated_date': '2025-11-07',
        'total_departments': len(departments),
        'total_professions': sum(d['profession_count'] for d in departments),
        'data': sorted(departments, key=lambda x: x['name'])
    }

    save_json(output_data, output_file)
    return len(departments)


def create_master_index(base_dir, output_file):
    """Create master index with cross-references."""
    print("\nCreating master index...")

    # Load all consolidated data
    countries_data = load_json(base_dir / 'locations' / 'countries.json')
    cities_data = load_json(base_dir / 'locations' / 'cities.json')
    industries_data = load_json(base_dir / 'business' / 'industries.json')
    sub_industries_data = load_json(base_dir / 'business' / 'sub_industries.json')
    departments_data = load_json(base_dir / 'business' / 'departments.json')

    # Build cross-references
    country_index = {c['id']: c['name'] for c in countries_data['data']}
    cities_by_country = defaultdict(list)
    for city in cities_data['data']:
        country_id = city['country']['id']
        if country_id:
            cities_by_country[country_id].append(city['name'])

    industry_index = {i['id']: i['name'] for i in industries_data['data']}
    sub_industries_by_industry = defaultdict(list)
    for sub_ind in sub_industries_data['data']:
        parent_id = sub_ind.get('parent_industry_id')
        if parent_id:
            sub_industries_by_industry[parent_id].append(sub_ind['name'])

    department_index = {}
    profession_to_department = {}
    for dept in departments_data['data']:
        department_index[dept['id']] = {
            'name': dept['name'],
            'color': dept['color'],
            'profession_count': dept['profession_count']
        }
        for prof in dept['professions']:
            profession_to_department[prof['id']] = dept['name']

    master_index = {
        'version': '1.0',
        'consolidated_date': '2025-11-07',
        'description': 'Master index for consolidated library system with cross-references',
        'statistics': {
            'total_countries': len(country_index),
            'total_cities': cities_data['total_cities'],
            'total_industries': len(industry_index),
            'total_sub_industries': sub_industries_data['total_sub_industries'],
            'total_departments': len(department_index),
            'total_professions': departments_data['total_professions']
        },
        'indexes': {
            'countries': country_index,
            'cities_by_country': dict(cities_by_country),
            'industries': industry_index,
            'sub_industries_by_industry': dict(sub_industries_by_industry),
            'departments': department_index,
            'profession_to_department': profession_to_department
        },
        'file_locations': {
            'locations': {
                'countries': 'locations/countries.json',
                'cities': 'locations/cities.json'
            },
            'business': {
                'industries': 'business/industries.json',
                'sub_industries': 'business/sub_industries.json',
                'departments': 'business/departments.json'
            },
            'semantic': {
                'professions': '../Libs 25/professions_library.json',
                'actions': '../Libs 25/actions_library.json',
                'objects': '../Libs 25/objects_library.json',
                'tools': '../Libs 25/tools_library.json',
                'responsibilities': '../Libs 25/responsibilities_library.json'
            }
        }
    }

    save_json(master_index, output_file)
    print(f"\n  Total entities indexed: {sum(master_index['statistics'].values())}")


def main():
    """Main consolidation process."""
    print("="*70)
    print("LIBRARY CONSOLIDATION SCRIPT")
    print("="*70)

    # Define paths
    base_dir = Path(__file__).parent.parent
    source_dir = base_dir / 'JSON' / 'Libs_JSON_old'
    output_dir = base_dir / 'JSON' / 'Libs_Consolidated'

    # Create output directories
    locations_dir = output_dir / 'locations'
    business_dir = output_dir / 'business'

    print(f"\nSource directory: {source_dir}")
    print(f"Output directory: {output_dir}")

    # Phase 1: Extract Location Data
    print("\n" + "="*70)
    print("PHASE 1: EXTRACTING LOCATION DATA")
    print("="*70)

    countries_count = extract_countries(
        source_dir / 'countries.json',
        locations_dir / 'countries.json'
    )

    cities_count = extract_cities(
        source_dir / 'cities.json',
        locations_dir / 'cities.json'
    )

    # Phase 2: Extract Business Context Data
    print("\n" + "="*70)
    print("PHASE 2: EXTRACTING BUSINESS CONTEXT DATA")
    print("="*70)

    industries_count = extract_industries(
        source_dir / 'industry.json',
        business_dir / 'industries.json'
    )

    sub_industries_count = extract_sub_industries(
        source_dir / 'sub-industry.json',
        business_dir / 'sub_industries.json'
    )

    departments_count = extract_departments(
        source_dir / 'Department.json',
        business_dir / 'departments.json'
    )

    # Phase 3: Create Master Index
    print("\n" + "="*70)
    print("PHASE 3: CREATING MASTER INDEX")
    print("="*70)

    create_master_index(
        output_dir,
        output_dir / 'library_index.json'
    )

    # Summary
    print("\n" + "="*70)
    print("CONSOLIDATION COMPLETE!")
    print("="*70)
    print(f"\nExtracted Data:")
    print(f"  Countries:       {countries_count}")
    print(f"  Cities:          {cities_count}")
    print(f"  Industries:      {industries_count}")
    print(f"  Sub-Industries:  {sub_industries_count}")
    print(f"  Departments:     {departments_count}")
    print(f"\nOutput directory: {output_dir}")
    print(f"\nNext Steps:")
    print(f"  1. Review consolidated files in: {output_dir}")
    print(f"  2. Check master index: {output_dir / 'library_index.json'}")
    print(f"  3. Update Libs 25 libraries with enhanced metadata")
    print(f"  4. Update documentation")
    print("="*70)


if __name__ == "__main__":
    main()
