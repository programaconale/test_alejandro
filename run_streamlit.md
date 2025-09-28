# How to Run the Streamlit Multipage App

## Prerequisites

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup the database (for Test 3):**
   ```bash
   sqlite3 ecommerce.db < database_schema.sql
   ```

## Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at: `http://localhost:8501`

## Multipage Structure

Following [Streamlit's official multipage documentation](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app), the app is structured as:

```
├── streamlit_app.py                   # Main page (Test 1: Web Analytics)
├── pages/
│   ├── 1_Test_2_Instagram_Reels.py    # Test 2: Instagram Reels Analysis
│   └── 2_Test_3_SQL_Database.py       # Test 3: SQL Database Analysis
├── data_test1.csv                     # Data for Test 1
├── data_test2.csv                     # Data for Test 2
├── database_schema.sql                # SQL schema for Test 3
└── ecommerce.db                       # SQLite database (created after setup)
```

## Features

### Test 1: Web Analytics (Main Page)
- **WedInvites Inc. conversion funnel analysis**
- Exact notebook content reproduction
- Mathematical formulas with LaTeX
- Step-by-step data analysis
- All 4 questions (A, B, C, D) with detailed answers

### Test 2: Instagram Reels
- **Prime Reels premium service analysis**
- Complete business context explanation
- Cohort analysis methodology
- Data loading and processing steps
- Tenure and cohort matrix explanations

### Test 3: SQL Database
- **E-commerce database analysis**
- All 4 SQL questions with complete queries
- Database connection examples
- Query results and explanations
- Comments and insights from notebook

## App Features

- **Official Streamlit multipage structure** following documentation
- **Exact notebook content** without additional analytics
- **Original markdown comments** and code blocks
- **Mathematical formulas** rendered with LaTeX
- **DataFrames and results** as shown in notebooks

## Troubleshooting

- **Database not found**: Make sure to run the database setup command
- **CSV files not found**: Ensure `data_test1.csv` and `data_test2.csv` are in the same directory
- **Import errors**: Check that all dependencies are installed correctly

## Required Files

Make sure these files are in the same directory:
- `streamlit_app.py`
- `data_test1.csv`
- `data_test2.csv`
- `database_schema.sql`
- `ecommerce.db` (created after running the SQL setup)
- `requirements.txt`
