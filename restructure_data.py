import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs('_output', exist_ok=True)

# Load CSV and clean column names (optional: uppercase and strip)
data = pd.read_csv('data/lightcast_job_postings.csv')
data.columns = data.columns.str.strip()

# --- 1. Job Postings Table ---
job_postings = data[['ID', 'TITLE_RAW', 'TITLE_CLEAN', 'POSTED', 'EXPIRED',
                     'SALARY_FROM', 'SALARY_TO', 'MIN_YEARS_EXPERIENCE',
                     'MAX_YEARS_EXPERIENCE', 'SOFTWARE_SKILLS',
                     'EMPLOYMENT_TYPE', 'COMPANY']]
job_postings.to_csv('_output/job_postings.csv', index=False)

# --- 2. Company Table ---
company = data[['COMPANY', 'COMPANY_NAME', 'COMPANY_RAW', 'COMPANY_IS_STAFFING']].drop_duplicates()
company.to_csv('_output/company.csv', index=False)

# --- 3. Location Table ---
location = data[['ID', 'CITY', 'STATE', 'COUNTY', 'LOCATION']]
location.to_csv('_output/location.csv', index=False)

# --- 4. SOC Table ---
soc = data[['ID', 'SOC_2', 'SOC_2_NAME', 'SOC_3', 'SOC_3_NAME',
            'SOC_4', 'SOC_4_NAME', 'SOC_5', 'SOC_5_NAME']]
soc.to_csv('_output/soc.csv', index=False)

# --- 5. LOT Table ---
lot = data[['ID', 'LOT_CAREER_AREA', 'LOT_CAREER_AREA_NAME',
            'LOT_OCCUPATION', 'LOT_OCCUPATION_NAME',
            'LOT_SPECIALIZED_OCCUPATION', 'LOT_SPECIALIZED_OCCUPATION_NAME']]
lot.to_csv('_output/lot.csv', index=False)

# --- 6. NAICS Table ---
naics = data[['ID', 'NAICS2', 'NAICS2_NAME', 'NAICS3', 'NAICS3_NAME',
              'NAICS4', 'NAICS4_NAME', 'NAICS5', 'NAICS5_NAME',
              'NAICS6', 'NAICS6_NAME']]
naics.to_csv('_output/naics.csv', index=False)

print("✅ All relational tables exported successfully!")

