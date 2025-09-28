"""
Test 3: E-commerce Database Analysis & SQL Queries
"""

import streamlit as st
import pandas as pd
import sqlite3
from setup_database import setup_database

# Configure page
st.set_page_config(
    page_title="Test 3: SQL Database",
    page_icon=":file_cabinet:",
    layout="wide"
)

# Hide Streamlit default elements
hide_streamlit_style = """
<style>
/* Hide the fork button */
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
.styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
.viewerBadge_text__1JaDK {
    display: none !important;
}

/* Hide "Made with Streamlit" */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hide the hamburger menu */
.css-9s5bis.edgvbvh3 {
    display: none;
}

/* Hide "Deploy" button */
.css-1rs6os.edgvbvh3 {
    display: none;
}

/* Hide GitHub icon and fork button */
.css-1544g2n.e1fqkh3o4 {
    display: none;
}

/* Hide the entire header bar if needed */
.css-18e3th9 {
    padding-top: 0rem;
}

/* Additional selectors for different Streamlit versions */
.stDeployButton {display: none;}
.deployButton {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add Leadtech logo (adaptive to theme)
def get_leadtech_logo():
    """Get appropriate Leadtech logo based on Streamlit theme"""
    return """
    <style>
    .leadtech-logo-light {
        display: block;
    }
    .leadtech-logo-dark {
        display: none;
    }
    @media (prefers-color-scheme: dark) {
        .leadtech-logo-light {
            display: none;
        }
        .leadtech-logo-dark {
            display: block;
        }
    }
    /* Streamlit dark theme detection */
    [data-theme="dark"] .leadtech-logo-light {
        display: none;
    }
    [data-theme="dark"] .leadtech-logo-dark {
        display: block;
    }
    </style>
    <div>
        <img src="https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-1.svg" 
             class="leadtech-logo-light" width="200" alt="Leadtech Logo">
        <img src="https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-light.svg" 
             class="leadtech-logo-dark" width="200" alt="Leadtech Logo Light">
    </div>
    """

st.sidebar.markdown(get_leadtech_logo(), unsafe_allow_html=True)
st.sidebar.markdown("---")

st.markdown("# Test 3: SQL Database")
st.sidebar.header("Test 3: SQL Database")

st.markdown("## Test 3")
st.markdown("""In a database there are 3 tables: one with the orders made by customers, another with the items in each order, and a third with information about each customer. 

The relationships/information are defined as follows:

-The Orders table contains an order ID (orderId) and a customer ID (customerId)						
-The Items table contains the item ID (itemId) and the order ID (orderId). There's also a field with the item price (price).						
-The Customers table has the customer ID (customerId)""")

st.markdown("## IN database_schema.sql have the queries to create and insert data in the database sqlite")
st.markdown("#### execute")
st.code("sqlite3 ecommerce.db < database_schema.sql")

st.markdown("Please answer the following questions. For open-ended questions, feel free to use any language you're comfortable with (SQL Server, MySQL, etc.) or even Excel or pseudocode.")

try:
    # Setup database if it doesn't exist
    setup_database()
    
    # Connect to database
    conn = sqlite3.connect('ecommerce.db')
    
    st.markdown("### Database Connection")
    st.code("""import pandas as pd
import sqlite3
conn = sqlite3.connect('ecommerce.db')""")
    
    # Query 1: Customers who purchased item 3543
    st.markdown("### 1. What query would you use to find out how many customers purchased item ID ='3543'?")
    
    query1 = """SELECT COUNT(DISTINCT C.customerId) 
FROM Items I 
INNER JOIN Orders O ON I.orderId = O.orderId 
INNER JOIN Customers C ON O.customerId = C.customerId 
WHERE I.itemId = '3543'"""
    
    result1 = pd.read_sql(query1, conn)
    
    st.code(f"""df_1 = pd.read_sql(\"\"\"
{query1}
\"\"\", conn)""")
    
    st.dataframe(result1)
    
    st.markdown("## OPTION C:")
    st.markdown("Correct syntax, use DISTINCT TO DROP DUPLICATES")
    
    st.markdown("""itemId ambiguity.
If itemId is unique (line ID), it can't repeat across orders and there's no link to a product catalog.
If itemId is a product ID, repetition is expected, but the model lacks a Products table and a line PK. but in the question you said The Items table contains the item ID (itemId) and the order ID (orderId). There's also a field with the item price (price).""")
    
    # Query 2: Top 5 orders by total price
    st.markdown("### 2. How do you obtain the following? Give the total price of the 5 orders with the highest total price.")
    
    query2 = """SELECT SUM(I.price), O.orderId 
FROM Orders O 
INNER JOIN Items I ON I.orderId = O.orderId 
GROUP BY O.orderId 
ORDER BY SUM(I.price) DESC 
LIMIT 5"""
    
    result2 = pd.read_sql(query2, conn)
    
    st.code(f"""df_2 = pd.read_sql(\"\"\"
{query2}
\"\"\", conn)""")
    
    st.dataframe(result2)
    
    # Query 3: Customer 3265 orders with item 223
    st.markdown("### 3. Write a query that allows you to find the number of orders placed by customer ID = '3265' that contain item ID = '223'")
    
    query3 = """SELECT COUNT(DISTINCT o.orderId) as number_of_orders
FROM Orders o
INNER JOIN Items i ON o.orderId = i.orderId
WHERE o.customerId = '3265' 
  AND i.itemId = '223'"""
    
    result3 = pd.read_sql(query3, conn)
    
    st.code(f"""df_3 = pd.read_sql(\"\"\"
{query3}
\"\"\", conn)""")
    
    st.dataframe(result3)
    
    # Query 4: Item 113 impact analysis
    st.markdown("### 4. To determine whether the presence of a particular item in an order (in this case, item ID = '113') increases the amount spent on that order, we want to check the average price of orders that contain item ID = '113' and those that don't. Write a query to find this information.")
    
    query4 = """SELECT 
    CASE 
        WHEN i.itemId IS NOT NULL THEN 'With Item 113'
        ELSE 'Without Item 113'
    END as order_type,
    AVG(o.totalAmount) as average_amount,
    COUNT(DISTINCT o.orderId) as order_count
FROM Orders o
LEFT JOIN Items i ON o.orderId = i.orderId AND i.itemId = '113'
GROUP BY 
    CASE 
        WHEN i.itemId IS NOT NULL THEN 'With Item 113'
        ELSE 'Without Item 113'
    END"""
    
    result4 = pd.read_sql(query4, conn)
    
    st.code(f"""df_4 = pd.read_sql(\"\"\"
{query4}
\"\"\", conn)""")
    
    st.dataframe(result4)
    
    conn.close()
    
except Exception as e:
    st.error(f"❌ Database connection error: {e}")
    st.info("💡 Make sure to run: `sqlite3 ecommerce.db < database_schema.sql` first")
