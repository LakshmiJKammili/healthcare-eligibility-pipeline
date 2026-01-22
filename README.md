## Healthcare Eligibility Ingestion Pipeline

### How to Run
1. Install dependencies:
   pip install pandas
2. Place partner files in the `data/` directory
3. Run:
   python main.py
4. Output will be written to `output/unified_eligibility.csv`

### Design Overview
- The pipeline is configuration-driven
- Partner-specific details (delimiter, column names, date formats) are stored in a config file
- Core ingestion and transformation logic is generic and reusable

### Adding a New Partner
1. Add a new entry to `PARTNER_CONFIG`
2. Specify:
   - File path
   - Delimiter
   - Column mapping
   - Date format
   - Partner code
3. No changes to processing logic are required

### Error Handling & Validation
- Rows missing `external_id` are dropped
- Invalid date or phone formats result in null values
- This design can easily be extended to log errors for auditing
