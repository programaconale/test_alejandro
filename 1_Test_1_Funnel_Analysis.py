"""
Test Alejandro Marcano - Main Page (Test 1: Web Analytics)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

# Add Leadtech logo (adaptive to theme - corrected)
def get_leadtech_logo():
    """Get appropriate Leadtech logo based on Streamlit theme"""
    return """
    <style>
    .leadtech-logo-for-light {
        display: block;
    }
    .leadtech-logo-for-dark {
        display: none;
    }
    @media (prefers-color-scheme: dark) {
        .leadtech-logo-for-light {
            display: none;
        }
        .leadtech-logo-for-dark {
            display: block;
        }
    }
    /* Streamlit dark theme detection */
    [data-theme="dark"] .leadtech-logo-for-light {
        display: none;
    }
    [data-theme="dark"] .leadtech-logo-for-dark {
        display: block;
    }
    </style>
    <div>
        <img src="https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-1.svg" 
             class="leadtech-logo-for-light" width="200" alt="Leadtech Logo Dark">
        <img src="https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-light.svg" 
             class="leadtech-logo-for-dark" width="200" alt="Leadtech Logo Light">
    </div>
    """

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
    
    # Calculate average funnel steps
    avg_home = df_test1['home pageviews'].mean()
    avg_form = df_test1['page with form pageviews'].mean()
    avg_payment = df_test1['Payment page pageviews'].mean()
    avg_accepted = df_test1['Accepted payment page pageviews'].mean()
    
    
    # 2. Site Comparison Funnel
    st.markdown("#### Conversion Rates by Site")
    
    # Create a comparison chart of conversion rates
    fig_comparison = go.Figure()
    
    # Add bars for each conversion step
    fig_comparison.add_trace(go.Bar(
        name='Home → Form (%)',
        x=df_test1['Sites of WedInvites Inc.'],
        y=df_test1['home_to_form_%'],
        marker_color='#1f77b4'
    ))
    
    fig_comparison.add_trace(go.Bar(
        name='Form → Payment (%)',
        x=df_test1['Sites of WedInvites Inc.'],
        y=df_test1['form_to_payment_%'],
        marker_color='#ff7f0e'
    ))
    
    fig_comparison.add_trace(go.Bar(
        name='Payment → Accepted (%)',
        x=df_test1['Sites of WedInvites Inc.'],
        y=df_test1['payment_to_accepted_%'],
        marker_color='#2ca02c'
    ))
    
    fig_comparison.update_layout(
        title='Conversion Rates by Funnel Step and Site',
        xaxis_title='Sites',
        yaxis_title='Conversion Rate (%)',
        barmode='group',
        height=500,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig_comparison, use_container_width=True)
    
   # Create funnel chart
    fig_funnel = go.Figure(go.Funnel(
        y = ["Home Page Visits", "Form Page Views", "Payment Page Views", "Accepted Payments"],
        x = [avg_home, avg_form, avg_payment, avg_accepted],
        textposition = "inside",
        textinfo = "value+percent initial+percent previous",
        opacity = 0.65,
        marker = {"color": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"],
                 "line": {"width": 2, "color": "white"}},
        connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}}
    ))
    
    fig_funnel.update_layout(
        title="Average Conversion Funnel Across All Sites",
        font_size=12,
        height=500
    )
    
    st.plotly_chart(fig_funnel, use_container_width=True)
    
    st.markdown("---")
    
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
    
    st.markdown("---")
    
    # Question E
    st.markdown("## QUESTION E")
    st.markdown("It is discovered with the team that the Google Analytics script has not been firing correctly on site 5 for some time.")
    
    st.markdown("You check Mixpanel and see that it is tracking:")
    st.markdown("a) The overall funnel conversion rate: 1.4%")
    st.markdown("b) The conversion from the home page to the form: 30%")
    st.markdown("c) The conversion from the form to the payment page: 20%")
    st.markdown("d) The conversion from the payment page to the payment accepted page is not being tracked.")
    
    st.markdown("**Based on the Mixpanel data, what is the conversion rate for the funnel step from the payment page to payment accepted?**")
    
    st.markdown("### Solution")
    st.markdown("We can calculate the missing conversion rate using the funnel formula:")
    st.markdown("**Overall Conversion = Home→Form × Form→Payment × Payment→Accepted**")
    
    st.code("""# Given Mixpanel data for Site 5
overall = 0.014  # 1.4%
home_to_form = 0.30  # 30%
form_to_payment = 0.20  # 20%

# Calculate payment -> accepted
payment_to_accepted = overall / (home_to_form * form_to_payment)

print(f"Payment → Accepted conversion rate: {payment_to_accepted:.2%}")""")
    
    # Calculate the missing conversion rate
    overall = 0.014  # 1.4%
    home_to_form = 0.30  # 30%
    form_to_payment = 0.20  # 20%
    
    payment_to_accepted = overall / (home_to_form * form_to_payment)
    
    st.text(f"Payment → Accepted conversion rate: {payment_to_accepted:.2%}")
    
    st.markdown("### Verification")
    st.markdown(f"**Check:** {home_to_form:.1%} × {form_to_payment:.1%} × {payment_to_accepted:.1%} = {(home_to_form * form_to_payment * payment_to_accepted):.1%} ✅")
    
    st.markdown("---")
    
    # Question F
    st.markdown("## QUESTION F")
    st.markdown("The average ticket price for each site is $125. What is the profit for each site, taking into account the CPA? Assuming a price test is being conducted by increasing the average ticket price for each site by 30%, resulting in a 10% drop in CR(Conversion rate) and a 40% increase in CPA, what would the new profit be for each domain? What is the % difference between the previous profit and the profit with the price increase applied to each site?")
    
    st.markdown("### Baseline Profit")
    st.markdown("- Price = $125")
    st.markdown("- Profit = Accepted × (Price – CPA)")
    
    st.markdown("### Price Test Scenario")
    st.markdown("- Price ↑30% → $162.50")
    st.markdown("- Accepted ↓10%")
    st.markdown("- CPA ↑40%")
    
    st.markdown("Profit (new) = (Accepted × 0.9) × (162.50 – CPA × 1.4)")
    
    st.markdown("### % Difference")
    st.markdown("%Diff = (Profit_new – Profit_baseline) / Profit_baseline × 100")
    
    st.code("""# Config
AVG_TICKET = 125.0
PRICE_UP = 1.30
CR_DROP = 0.90
CPA_UP = 1.40

# Profit baseline
df_test1["profit_baseline"] = df_test1["Accepted payment page pageviews"] * (
    AVG_TICKET - df_test1["CPA (Cost per Conversion)"]
)

# Nuevo escenario con test
df_test1["accepted_new"] = df_test1["Accepted payment page pageviews"] * CR_DROP
df_test1["cpa_new"] = df_test1["CPA (Cost per Conversion)"] * CPA_UP
df_test1["price_new"] = AVG_TICKET * PRICE_UP

df_test1["profit_new"] = df_test1["accepted_new"] * (
    df_test1["price_new"] - df_test1["cpa_new"]
)

# % Difference
df_test1["profit_diff_%"] = (
    (df_test1["profit_new"] - df_test1["profit_baseline"]) / df_test1["profit_baseline"] * 100
).round(1)""")
    
    # Calculate profits
    AVG_TICKET = 125.0
    PRICE_UP = 1.30
    CR_DROP = 0.90
    CPA_UP = 1.40
    
    # Profit baseline
    df_test1["profit_baseline"] = df_test1["Accepted payment page pageviews"] * (
        AVG_TICKET - df_test1["CPA (Cost per Conversion)"]
    )
    
    # Nuevo escenario con test
    df_test1["accepted_new"] = df_test1["Accepted payment page pageviews"] * CR_DROP
    df_test1["cpa_new"] = df_test1["CPA (Cost per Conversion)"] * CPA_UP
    df_test1["price_new"] = AVG_TICKET * PRICE_UP
    
    df_test1["profit_new"] = df_test1["accepted_new"] * (
        df_test1["price_new"] - df_test1["cpa_new"]
    )
    
    # % Difference
    df_test1["profit_diff_%"] = (
        (df_test1["profit_new"] - df_test1["profit_baseline"]) / df_test1["profit_baseline"] * 100
    ).round(1)
    
    # Display results
    profit_analysis = df_test1[[
        "Sites of WedInvites Inc.",
        "Accepted payment page pageviews",
        "CPA (Cost per Conversion)",
        "profit_baseline",
        "profit_new",
        "profit_diff_%"
    ]].round(2)
    
    st.markdown("### 📊 Profit Analysis Results")
    st.dataframe(profit_analysis)
    
    st.markdown("### Interpretation")
    st.markdown("1. The **baseline profit** shows how much each site currently earns with a $125 average ticket.")
    st.markdown("2. The **new profit** simulates the impact of raising the price (fewer buyers, higher CPA, but more revenue per conversion).")
    st.markdown("3. The **% difference** highlights whether the strategy increases or decreases profit for each site.")
    
    # Example calculation for Site 1
    site1_data = df_test1.iloc[0]
    st.markdown("### Example: Site 1")
    st.markdown(f"- Accepted = {site1_data['Accepted payment page pageviews']:,.0f}")
    st.markdown(f"- CPA = ${site1_data['CPA (Cost per Conversion)']:.0f}")
    
    st.markdown(f"**Baseline Profit** = {site1_data['Accepted payment page pageviews']:,.0f} × (125 – {site1_data['CPA (Cost per Conversion)']:.0f}) = **${site1_data['profit_baseline']:,.0f}**")
    st.markdown(f"**New Profit** = ({site1_data['Accepted payment page pageviews']:,.0f} × 0.9) × (162.5 – {site1_data['CPA (Cost per Conversion)']:.0f} × 1.4) = **${site1_data['profit_new']:,.0f}**")
    st.markdown(f"**% Difference** = **{site1_data['profit_diff_%']:+.1f}%**")
    
    # Summary insights
    positive_sites = df_test1[df_test1['profit_diff_%'] > 0]
    negative_sites = df_test1[df_test1['profit_diff_%'] < 0]
    
    st.markdown("### 🔍 Key Insights")
    if len(positive_sites) > 0:
        st.success(f"✅ **{len(positive_sites)} sites benefit** from the price increase:")
        for _, site in positive_sites.iterrows():
            st.text(f"  • {site['Sites of WedInvites Inc.']}: {site['profit_diff_%']:+.1f}% profit increase")
    
    if len(negative_sites) > 0:
        st.warning(f"⚠️ **{len(negative_sites)} sites lose profit** with the price increase:")
        for _, site in negative_sites.iterrows():
            st.text(f"  • {site['Sites of WedInvites Inc.']}: {site['profit_diff_%']:+.1f}% profit decrease")
    
    avg_profit_change = df_test1['profit_diff_%'].mean()
    if avg_profit_change > 0:
        st.success(f"📈 **Overall impact:** {avg_profit_change:+.1f}% average profit increase across all sites")
    else:
        st.error(f"📉 **Overall impact:** {avg_profit_change:+.1f}% average profit decrease across all sites")
    
    st.markdown("👉 **Conclusion:** The price test should be implemented selectively on sites that show positive profit impact, while maintaining current pricing on sites where the test reduces profitability.")
    
except FileNotFoundError:
    st.error("❌ data_test1.csv file not found. Please ensure the file is in the correct directory.")