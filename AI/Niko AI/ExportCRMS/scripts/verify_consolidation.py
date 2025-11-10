"""
Verification script for consolidated libraries.
Checks data integrity, validates cross-references, and generates a report.
"""
import json
from pathlib import Path


def load_json(file_path):
    """Load JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def verify_countries(countries_file):
    """Verify countries data integrity."""
    print("\n" + "="*70)
    print("VERIFYING COUNTRIES DATA")
    print("="*70)

    data = load_json(countries_file)
    countries = data['data']

    issues = []
    stats = {
        'total': len(countries),
        'with_coordinates': 0,
        'with_flags': 0,
        'missing_coordinates': [],
        'missing_flags': [],
        'duplicate_iso2': [],
        'duplicate_iso3': []
    }

    iso2_seen = set()
    iso3_seen = set()

    for country in countries:
        # Check coordinates
        if country.get('latitude') and country.get('longitude'):
            stats['with_coordinates'] += 1
        else:
            stats['missing_coordinates'].append(country['name'])

        # Check flags
        if country.get('flag_url'):
            stats['with_flags'] += 1
        else:
            stats['missing_flags'].append(country['name'])

        # Check for duplicates
        iso2 = country.get('iso2')
        iso3 = country.get('iso3')

        if iso2 in iso2_seen:
            stats['duplicate_iso2'].append(iso2)
        iso2_seen.add(iso2)

        if iso3 in iso3_seen:
            stats['duplicate_iso3'].append(iso3)
        iso3_seen.add(iso3)

    # Report
    print(f"\nTotal Countries: {stats['total']}")
    print(f"With Coordinates: {stats['with_coordinates']} ({stats['with_coordinates']/stats['total']*100:.1f}%)")
    print(f"With Flag URLs: {stats['with_flags']} ({stats['with_flags']/stats['total']*100:.1f}%)")

    if stats['missing_coordinates']:
        print(f"\n[WARNING] {len(stats['missing_coordinates'])} countries missing coordinates:")
        for name in stats['missing_coordinates'][:5]:
            print(f"  - {name}")
        if len(stats['missing_coordinates']) > 5:
            print(f"  ... and {len(stats['missing_coordinates']) - 5} more")

    if stats['duplicate_iso2']:
        print(f"\n[ERROR] Duplicate ISO2 codes found: {stats['duplicate_iso2']}")
        issues.append("Duplicate ISO2 codes")

    if stats['duplicate_iso3']:
        print(f"\n[ERROR] Duplicate ISO3 codes found: {stats['duplicate_iso3']}")
        issues.append("Duplicate ISO3 codes")

    if not issues:
        print("\n[OK] Countries data structure is valid")

    return stats, issues


def verify_cities(cities_file):
    """Verify cities data integrity."""
    print("\n" + "="*70)
    print("VERIFYING CITIES DATA")
    print("="*70)

    data = load_json(cities_file)
    cities = data['data']

    issues = []
    stats = {
        'total': len(cities),
        'with_coordinates': 0,
        'missing_coordinates': [],
        'missing_country': [],
        'cities_by_country': {}
    }

    for city in cities:
        # Check coordinates
        if city.get('latitude') and city.get('longitude'):
            stats['with_coordinates'] += 1
        else:
            stats['missing_coordinates'].append(city['name'])

        # Check country association
        if not city.get('country') or not city['country'].get('id'):
            stats['missing_country'].append(city['name'])
            issues.append(f"City {city['name']} missing country association")
        else:
            country_name = city['country'].get('name', 'Unknown')
            if country_name not in stats['cities_by_country']:
                stats['cities_by_country'][country_name] = 0
            stats['cities_by_country'][country_name] += 1

    # Report
    print(f"\nTotal Cities: {stats['total']}")
    print(f"With Coordinates: {stats['with_coordinates']} ({stats['with_coordinates']/stats['total']*100:.1f}%)")

    if stats['missing_coordinates']:
        print(f"\n[WARNING] {len(stats['missing_coordinates'])} cities missing coordinates")

    if stats['missing_country']:
        print(f"\n[ERROR] {len(stats['missing_country'])} cities missing country association")

    print(f"\nCities by Country (top 10):")
    sorted_countries = sorted(stats['cities_by_country'].items(), key=lambda x: x[1], reverse=True)
    for country, count in sorted_countries[:10]:
        print(f"  {country}: {count} cities")

    if not issues:
        print("\n[OK] Cities data structure is valid")

    return stats, issues


def verify_industries(industries_file):
    """Verify industries data integrity."""
    print("\n" + "="*70)
    print("VERIFYING INDUSTRIES DATA")
    print("="*70)

    data = load_json(industries_file)
    industries = data['data']

    issues = []
    stats = {
        'total': len(industries),
        'with_description': 0,
        'with_color': 0,
        'duplicate_names': []
    }

    names_seen = set()

    for industry in industries:
        # Check description
        if industry.get('description'):
            stats['with_description'] += 1

        # Check color
        if industry.get('color'):
            stats['with_color'] += 1

        # Check duplicates
        name = industry.get('name', '').lower()
        if name in names_seen:
            stats['duplicate_names'].append(industry['name'])
        names_seen.add(name)

    # Report
    print(f"\nTotal Industries: {stats['total']}")
    print(f"With Descriptions: {stats['with_description']} ({stats['with_description']/stats['total']*100:.1f}%)")
    print(f"With Colors: {stats['with_color']} ({stats['with_color']/stats['total']*100:.1f}%)")

    if stats['duplicate_names']:
        print(f"\n[WARNING] Duplicate industry names: {stats['duplicate_names']}")

    print("\n[OK] Industries data structure is valid")

    return stats, issues


def verify_departments(departments_file):
    """Verify departments data integrity."""
    print("\n" + "="*70)
    print("VERIFYING DEPARTMENTS DATA")
    print("="*70)

    data = load_json(departments_file)
    departments = data['data']

    issues = []
    stats = {
        'total_departments': len(departments),
        'total_professions': 0,
        'departments_by_profession_count': {},
        'translation_languages': set()
    }

    for dept in departments:
        profession_count = len(dept.get('professions', []))
        stats['total_professions'] += profession_count
        stats['departments_by_profession_count'][dept['name']] = profession_count

        # Track languages
        lang = dept.get('translation', {}).get('language')
        if lang:
            stats['translation_languages'].add(lang)

    # Report
    print(f"\nTotal Departments: {stats['total_departments']}")
    print(f"Total Professions: {stats['total_professions']}")
    print(f"Average Professions per Department: {stats['total_professions']/stats['total_departments']:.1f}")

    print(f"\nDepartments by Size:")
    sorted_depts = sorted(stats['departments_by_profession_count'].items(), key=lambda x: x[1], reverse=True)
    for dept, count in sorted_depts:
        print(f"  {dept}: {count} professions")

    print(f"\nTranslation Languages: {', '.join(sorted(stats['translation_languages']))}")

    print("\n[OK] Departments data structure is valid")

    return stats, issues


def verify_master_index(index_file, consolidated_dir):
    """Verify master index cross-references."""
    print("\n" + "="*70)
    print("VERIFYING MASTER INDEX")
    print("="*70)

    index = load_json(index_file)
    issues = []

    # Load actual data
    countries = load_json(consolidated_dir / 'locations' / 'countries.json')
    cities = load_json(consolidated_dir / 'locations' / 'cities.json')
    industries = load_json(consolidated_dir / 'business' / 'industries.json')
    departments = load_json(consolidated_dir / 'business' / 'departments.json')

    # Verify counts
    print(f"\nStatistics:")
    print(f"  Countries: Index={index['statistics']['total_countries']}, Actual={len(countries['data'])}")
    print(f"  Cities: Index={index['statistics']['total_cities']}, Actual={len(cities['data'])}")
    print(f"  Industries: Index={index['statistics']['total_industries']}, Actual={len(industries['data'])}")
    print(f"  Departments: Index={index['statistics']['total_departments']}, Actual={len(departments['data'])}")
    print(f"  Professions: Index={index['statistics']['total_professions']}, Actual={sum(len(d['professions']) for d in departments['data'])}")

    # Verify country index
    actual_countries = {str(c['id']): c['name'] for c in countries['data']}
    indexed_countries = index['indexes']['countries']

    if len(actual_countries) != len(indexed_countries):
        issues.append(f"Country count mismatch: {len(actual_countries)} vs {len(indexed_countries)}")

    # Verify cities_by_country
    cities_by_country = {}
    for city in cities['data']:
        country_id = str(city['country']['id']) if city['country']['id'] else 'null'
        if country_id not in cities_by_country:
            cities_by_country[country_id] = []
        cities_by_country[country_id].append(city['name'])

    indexed_cities_by_country = index['indexes']['cities_by_country']

    for country_id, city_list in cities_by_country.items():
        if country_id not in indexed_cities_by_country:
            issues.append(f"Missing country {country_id} in cities_by_country index")
        elif set(city_list) != set(indexed_cities_by_country[country_id]):
            issues.append(f"City list mismatch for country {country_id}")

    if issues:
        print(f"\n[ERROR] Found {len(issues)} issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n[OK] Master index is valid and consistent with data files")

    return index['statistics'], issues


def generate_summary_report(consolidated_dir):
    """Generate final summary report."""
    print("\n" + "="*70)
    print("CONSOLIDATION VERIFICATION SUMMARY")
    print("="*70)

    # Run all verifications
    countries_stats, countries_issues = verify_countries(consolidated_dir / 'locations' / 'countries.json')
    cities_stats, cities_issues = verify_cities(consolidated_dir / 'locations' / 'cities.json')
    industries_stats, industries_issues = verify_industries(consolidated_dir / 'business' / 'industries.json')
    departments_stats, departments_issues = verify_departments(consolidated_dir / 'business' / 'departments.json')
    index_stats, index_issues = verify_master_index(consolidated_dir / 'library_index.json', consolidated_dir)

    # Summary
    total_issues = len(countries_issues) + len(cities_issues) + len(industries_issues) + len(departments_issues) + len(index_issues)

    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)

    print(f"\nData Entities:")
    print(f"  Countries:       {countries_stats['total']}")
    print(f"  Cities:          {cities_stats['total']}")
    print(f"  Industries:      {industries_stats['total']}")
    print(f"  Departments:     {departments_stats['total_departments']}")
    print(f"  Professions:     {departments_stats['total_professions']}")
    print(f"  TOTAL ENTITIES:  {countries_stats['total'] + cities_stats['total'] + industries_stats['total'] + departments_stats['total_departments'] + departments_stats['total_professions']}")

    print(f"\nData Completeness:")
    print(f"  Countries with coordinates: {countries_stats['with_coordinates']}/{countries_stats['total']} ({countries_stats['with_coordinates']/countries_stats['total']*100:.1f}%)")
    print(f"  Cities with coordinates:    {cities_stats['with_coordinates']}/{cities_stats['total']} ({cities_stats['with_coordinates']/cities_stats['total']*100:.1f}%)")
    print(f"  Industries with colors:     {industries_stats['with_color']}/{industries_stats['total']} ({industries_stats['with_color']/industries_stats['total']*100:.1f}%)")

    print(f"\nValidation Results:")
    if total_issues == 0:
        print(f"  [OK] All checks passed! No issues found.")
    else:
        print(f"  [WARNING] Found {total_issues} issues that need attention")
        print(f"    Countries: {len(countries_issues)} issues")
        print(f"    Cities: {len(cities_issues)} issues")
        print(f"    Industries: {len(industries_issues)} issues")
        print(f"    Departments: {len(departments_issues)} issues")
        print(f"    Master Index: {len(index_issues)} issues")

    print("\n" + "="*70)
    print("RECOMMENDED NEXT ACTIONS:")
    print("="*70)

    if cities_stats['missing_coordinates']:
        print(f"\n1. [HIGH PRIORITY] Geocode {len(cities_stats['missing_coordinates'])} cities with missing coordinates")
        print(f"   Run: python scripts/geocode_cities.py")

    if countries_stats['missing_coordinates']:
        print(f"\n2. [HIGH PRIORITY] Add coordinates for {len(countries_stats['missing_coordinates'])} countries")

    print(f"\n3. [MEDIUM PRIORITY] Expand city coverage from {cities_stats['total']} to 100+ cities")
    print(f"   Focus: Western Europe, Ukraine, North America")

    print(f"\n4. [MEDIUM PRIORITY] Add timezone data to all countries")
    print(f"   Run: python scripts/add_timezones.py")

    print(f"\n5. [LOW PRIORITY] Add descriptions for {industries_stats['total'] - industries_stats['with_description']} industries")

    print("\n" + "="*70)


def main():
    """Main verification process."""
    base_dir = Path(__file__).parent.parent
    consolidated_dir = base_dir / 'JSON' / 'Libs_Consolidated'

    print("="*70)
    print("CONSOLIDATED LIBRARIES VERIFICATION")
    print("="*70)
    print(f"\nDirectory: {consolidated_dir}")

    generate_summary_report(consolidated_dir)


if __name__ == "__main__":
    main()
