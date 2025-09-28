"""
Test Alejandro Marcano - Main Page (Test 1: Web Analytics)
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="Test 1: Web Analytics",
    page_icon=":bar_chart:",
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
    # Check if dark theme is enabled
    try:
        # This is a workaround to detect theme - Streamlit doesn't provide direct theme detection
        # We'll use CSS to detect and show appropriate logo
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
    except:
        # Fallback to default logo
        return '<img src="https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-1.svg" width="200" alt="Leadtech Logo">'

st.sidebar.markdown(get_leadtech_logo(), unsafe_allow_html=True)
st.sidebar.markdown("---")

st.markdown("# Test 1: Web Analytics")
st.sidebar.header("Test 1: Web Analytics")

st.markdown("## Test 1")
st.markdown("In this notebook I answer the question of the test 1")

# Load and process data
try:
    df_test1 = pd.read_csv("data_test1.csv", sep=";", thousands=".")
    
    st.markdown("### Data Loading")
    st.code("df_test1 = pd.read_csv(\"data_test1.csv\", sep=\";\", thousands=\".\")")
    st.dataframe(df_test1.head(10))
    
    # Data info
    st.markdown("### Data Information")
    st.text(f"Shape: {df_test1.shape}")
    st.text(f"Columns: {list(df_test1.columns)}")
    st.text("\nData Types:")
    st.text(str(df_test1.dtypes))
    
    # Clean CPA data
    st.markdown("### Data Cleaning")
    st.code("""# remove € symbol and convert comma to decimal 
df_test1['CPA (Cost per Conversion)'] = df_test1['CPA (Cost per Conversion)'].str.replace('€', '').str.replace(',', '.').astype(float)""")
    
    df_test1['CPA (Cost per Conversion)'] = (df_test1['CPA (Cost per Conversion)']
                                            .str.replace('€', '')
                                            .str.replace(',', '.')
                                            .astype(float))
    
    st.markdown("Clean Data:")
    st.dataframe(df_test1.head())
    st.text(f"\nData types:")
    st.text(str(df_test1.dtypes))
    
    # Show full dataset
    st.markdown("### Full Dataset")
    st.dataframe(df_test1)
    
    # Question A
    st.markdown("## QUESTION A")
    st.markdown("What is the conversion rate(%) at each conversion step or transition point in the funnel for each site (conversion rate between funnel steps)?")
    
    st.markdown("### Formula")
    st.markdown("""For each step in the funnel, the **conversion rate** is:

$$
\\text{Conversion Rate (\\%)} = \\frac{\\text{Visitors at Step B}}{\\text{Visitors at Step A}} \\times 100
$$

Where:  
- **Step A** = the previous stage ( Home pageviews).  
- **Step B** = the next stage (Form pageviews).  

Imagine :  
1. People visit the Home page.  
2. Some move to the Form page.  
3. A smaller group goes to the Payment page.  
4. Finally, only a few finish with Accepted payment.  

The conversion rate is the percentage of people who move from one layer to the next.""")
    
    # Calculate conversion rates
    st.code("""df_test1["home_to_form_%"] = (df_test1["page with form pageviews"] / df_test1["home pageviews"] * 100).round(1)
df_test1["form_to_payment_%"] = (df_test1["Payment page pageviews"] / df_test1["page with form pageviews"] * 100).round(1)
df_test1["payment_to_accepted_%"] = (df_test1["Accepted payment page pageviews"] / df_test1["Payment page pageviews"] * 100).round(1)

conversion_rates = df_test1[[
    "Sites of WedInvites Inc.",
    "home_to_form_%",
    "form_to_payment_%",
    "payment_to_accepted_%"
]]""")
    
    df_test1["home_to_form_%"] = (df_test1["page with form pageviews"] / df_test1["home pageviews"] * 100).round(1)
    df_test1["form_to_payment_%"] = (df_test1["Payment page pageviews"] / df_test1["page with form pageviews"] * 100).round(1)
    df_test1["payment_to_accepted_%"] = (df_test1["Accepted payment page pageviews"] / df_test1["Payment page pageviews"] * 100).round(1)
    
    conversion_rates = df_test1[[
        "Sites of WedInvites Inc.",
        "home_to_form_%",
        "form_to_payment_%",
        "payment_to_accepted_%"
    ]]
    
    st.dataframe(conversion_rates)
    
    st.markdown("""In the case of Site 1
- **Home → Form:** 48% of visitors moved from the Home page (170546) to the Form page (81862).  
- **Form → Payment:** Of those, 75% continued to the Payment page (61397).  
- **Payment → Accepted:** Finally, only 5.7% of those on the Payment page completed the Accepted payment step (3500).  

In other words:  
Out of **100 people** who visited the Home page of Site 1:  
- **48 people** saw the form page,  
- **36 people** reached the payment page,  (Then, of those 48, 75% reach Payment. 48×0.75=36)
- **only 2 people** actually completed the payment.  (Then, of those 36, 5.7% go to Accepted. 36×0.057=2)

This shows that the **biggest drop happens at the last step (Payment → Accepted)**, which might indicate issues with the payment process.""")
    
    # Question B
    st.markdown("## Question B")
    st.markdown("What is the overall conversion rate of the entire funnel on each site?")
    
    st.markdown("## Overall Conversion Probability Calculation")
    st.markdown("""### Formula
To calculate the overall probability of conversion (picking a random user from any of the 10 sites):

$$
P(\\text{Conversion}) = \\frac{\\text{Total Accepted Payments}}{\\text{Total Home Pageviews}} \\times 100
$$

This gives us the probability that a randomly selected user from any site will convert into a customer.""")
    
    st.code("conversion_rates['Overall conversion rate (%)'] = (df_test1['Accepted payment page pageviews'] / df_test1['home pageviews'] * 100).round(2)")
    
    conversion_rates['Overall conversion rate (%)'] = (df_test1['Accepted payment page pageviews'] / df_test1['home pageviews'] * 100).round(2)
    st.dataframe(conversion_rates)
    
    st.markdown("""- The **highest performers** are:
  - **Site 6 (4.26%)**,  
  - **Site 10 (2.84%)**, and  
  - **Site 9 (2.40%)**.  
  These sites are converting a larger share of visitors into paying customers.

- The **lowest performers** are:
  - **Site 7 (0.93%)** and  
  - **Site 8 (0.95%)**.  
  Less than **1 in 100 visitors** completes the funnel, which suggests strong friction or issues at later steps (e.g., payment).

- Most other sites fall around **2% overall conversion**, which means roughly **2 out of every 100 homepage visitors** end up paying.

This analysis helps identify **which sites need optimization** (e.g., checkout process, form completion) and **which sites are already performing well**.""")
    
    # Question C
    st.markdown("## QUESTION C")
    st.markdown("If you pick a random user from any of the ten sites, what is the probability that they will convert into a customer (buyer)?")
    
    st.markdown("""### Formula
To calculate the overall probability of conversion (picking a random user from any of the 10 sites):

$$
P(\\text{Conversion}) = \\frac{\\text{Total Accepted Payments}}{\\text{Total Home Pageviews}} \\times 100
$$""")
    
    # Calculate overall conversion probability
    st.code("""# Calculate overall conversion probability
# This calculates the probability that a random user from any site will convert

print("OVERALL CONVERSION PROBABILITY CALCULATION")
print("=" * 50)

# Step 1: Calculate totals
total_home_pageviews = df_test1['home pageviews'].sum()
total_accepted_payments = df_test1['Accepted payment page pageviews'].sum()

print("Step 1 - Calculate Totals:")
print("-" * 30)
print(f"Total Home Pageviews: {total_home_pageviews:,}")
print(f"Total Accepted Payments: {total_accepted_payments:,}")

# Step 2: Calculate overall conversion probability
overall_conversion_probability = (total_accepted_payments / total_home_pageviews) * 100

print(f"\\nStep 2 - Calculate Probability:")
print("-" * 30)
print(f"P(Conversion) = Total Accepted Payments / Total Home Pageviews × 100")
print(f"P(Conversion) = {total_accepted_payments:,} / {total_home_pageviews:,} × 100")
print(f"P(Conversion) = {overall_conversion_probability:.2f}%")

print(f"\\n✅ FINAL ANSWER:")
print("=" * 20)
print(f"If you pick a random user from any of the ten sites,")
print(f"the probability that they will convert into a customer is:")
print(f"\\n🎯 {overall_conversion_probability:.1f}%")

print(f"\\n📊 INTERPRETATION:")
print("-" * 20)
print(f"Out of every 100 visitors across all sites,")
print(f"only about {int(overall_conversion_probability)} actually complete the funnel and become customers.")""")
    
    # Execute the calculation
    total_home_pageviews = df_test1['home pageviews'].sum()
    total_accepted_payments = df_test1['Accepted payment page pageviews'].sum()
    overall_conversion_probability = (total_accepted_payments / total_home_pageviews) * 100
    
    st.text("OVERALL CONVERSION PROBABILITY CALCULATION")
    st.text("=" * 50)
    st.text("Step 1 - Calculate Totals:")
    st.text("-" * 30)
    st.text(f"Total Home Pageviews: {total_home_pageviews:,}")
    st.text(f"Total Accepted Payments: {total_accepted_payments:,}")
    st.text(f"\nStep 2 - Calculate Probability:")
    st.text("-" * 30)
    st.text(f"P(Conversion) = Total Accepted Payments / Total Home Pageviews × 100")
    st.text(f"P(Conversion) = {total_accepted_payments:,} / {total_home_pageviews:,} × 100")
    st.text(f"P(Conversion) = {overall_conversion_probability:.2f}%")
    st.text(f"\n✅ FINAL ANSWER:")
    st.text("=" * 20)
    st.text(f"If you pick a random user from any of the ten sites,")
    st.text(f"the probability that they will convert into a customer is:")
    st.text(f"\n🎯 {overall_conversion_probability:.1f}%")
    st.text(f"\n📊 INTERPRETATION:")
    st.text("-" * 20)
    st.text(f"Out of every 100 visitors across all sites,")
    st.text(f"only about {int(overall_conversion_probability)} actually complete the funnel and become customers.")
    
    # Question D
    st.markdown("## QUESTION D")
    st.markdown("Let's say a partner offers us a special service that we can only offer on one site, and we know it will help us increase the site's sales by 10%. All sites sell a product at the same price. We want to achieve the highest financial return. On which site would you offer the partner's service?")
    
    st.markdown("I calculated the absolute increase in conversions (10%) for each site. Since they all sell at the same price, the site with the most additional conversions will generate the greatest return.")
    
    # Rename columns and calculate incremental buyers
    df_analysis = df_test1.copy()
    df_analysis = df_analysis.rename(columns={
        "Sites of WedInvites Inc.": "site",
        "home pageviews": "home",
        "page with form pageviews": "form",
        "Payment page pageviews": "payment",
        "Accepted payment page pageviews": "accepted",
        "CPA (Cost per Conversion)": "CPA"
    })
    
    df_analysis["incremental_buyers"] = (df_analysis["accepted"] * 0.10).round().astype(int)
    
    st.code("""df_test1 = df_test1.rename(columns={
    "Sites of WedInvites Inc.": "site",
    "home pageviews": "home",
    "page with form pageviews": "form",
    "Payment page pageviews": "payment",
    "Accepted payment page pageviews": "accepted",
    "CPA (Cost per Conversion)": "CPA"
})

df_test1["incremental_buyers"] = (df_test1["accepted"] * 0.10).round().astype(int)

best_site = df_test1.loc[df_test1["incremental_buyers"].idxmax()]

print("Incremental buyers per site with +10% lift:")
print(df_test1[["site", "accepted", "incremental_buyers"]])

print("\\nBest site to offer the partner's service:")
print(f"Site: {best_site['site']}, Incremental buyers: {best_site['incremental_buyers']}")""")
    
    best_site = df_analysis.loc[df_analysis["incremental_buyers"].idxmax()]
    
    st.text("Incremental buyers per site with +10% lift:")
    st.dataframe(df_analysis[["site", "accepted", "incremental_buyers"]])
    
    st.text(f"\nBest site to offer the partner's service:")
    st.text(f"Site: {best_site['site']}, Incremental buyers: {best_site['incremental_buyers']}")
    
except FileNotFoundError:
    st.error("❌ data_test1.csv file not found. Please ensure the file is in the correct directory.")