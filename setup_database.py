"""
Setup script to initialize the SQLite database for the Streamlit app
This script will be called automatically when the app starts
"""

import sqlite3
import os

def setup_database():
    """Initialize the SQLite database if it doesn't exist"""
    
    if not os.path.exists('ecommerce.db'):
        print("Creating database...")
        
        try:
            # Create database connection
            conn = sqlite3.connect('ecommerce.db')
            
            # Read and execute the SQL schema
            with open('database_schema.sql', 'r', encoding='utf-8') as f:
                sql_script = f.read()
            
            # Execute the SQL script
            conn.executescript(sql_script)
            conn.close()
            
            print("✅ Database created successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error creating database: {e}")
            return False
    else:
        print("✅ Database already exists")
        return True

if __name__ == "__main__":
    setup_database()
