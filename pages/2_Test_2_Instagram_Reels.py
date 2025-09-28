"""
Test 2: Instagram Reels vs TikTok Analysis
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="Test 2: Instagram Reels",
    page_icon=":mobile_phone:",
    layout="wide"
)

# Add Leadtech logo
st.sidebar.image("https://leadtech.com/user/themes/leadtech/assets/images/logo/logo-leadtech-1.svg", width=200)
st.sidebar.markdown("---")

st.markdown("# Test 2: Instagram Reels")
st.sidebar.header("Test 2: Instagram Reels")

st.markdown("## Test 2")
st.markdown("""Let's let our imaginations run wild for a moment with this exercise.
You recently joined the Instagram Product team.
Your team is leading improvements to the Reels section.
But TikTok is succeeding and therefore stealing much of young people's attention. And less attention means fewer ads, and fewer ads mean less revenue. There's a lack of motivation on the team; perhaps it's too late.
It's urgent to regain leadership by putting Reels on par with TikTok. At the very least. There's even ambition to create an even better product.
As a Product Analyst, you've been assigned the mission of helping the team analyze Reels. The team has decided to launch "Prime Reels," a premium service for $9.99 per quarter. Users will no longer see ads on Reels and their videos will be shown to more users. Those without Prime membership will now see ads, and their videos will suffer a certain exposure penalty (number of views) compared to the current system. Five quarters later, we want to analyze the results.""")

try:
    # Load and process data
    st.markdown("### Data Loading and Processing")
    st.code("""df = pd.read_csv("data_test2.csv", sep=";", thousands=".")
df.rename(columns={df.columns[0]: "Cohort"}, inplace=True)
df = df.replace({"N/A": np.nan})
for c in df.columns[1:]:
    df[c] = pd.to_numeric(df[c], errors="coerce")""")
    
    df_test2 = pd.read_csv("data_test2.csv", sep=";", thousands=".")
    df_test2.rename(columns={df_test2.columns[0]: "Cohort"}, inplace=True)
    df_test2 = df_test2.replace({"N/A": np.nan})
    
    for c in df_test2.columns[1:]:
        df_test2[c] = pd.to_numeric(df_test2[c], errors="coerce")
    
    st.dataframe(df_test2)
    
    # Cohort analysis
    df_analysis = df_test2.set_index('Cohort')
    
    st.markdown("### User Numbers by Quarter and Cohort")
    st.code("""df_analysis = df.set_index('Cohort')

print("User Numbers by Quarter and Cohort:")
print(df_analysis)

quarterly_totals = df_analysis.sum(axis=0, skipna=True)
print(f"\\nTotal Active Users by Quarter:")
for quarter, total in quarterly_totals.items():
    print(f"  {quarter}: {total:,.0f} users")""")
    
    st.text("User Numbers by Quarter and Cohort:")
    st.dataframe(df_analysis)
    
    # Calculate quarterly totals
    quarterly_totals = df_analysis.sum(axis=0, skipna=True)
    
    st.text("\nTotal Active Users by Quarter:")
    for quarter, total in quarterly_totals.items():
        st.text(f"  {quarter}: {total:,.0f} users")
    
    # Cohort explanation
    st.markdown("### What \"Tenure\" Means (Cohort Analysis)")
    st.markdown("""**Tenure** is the **relative age** of a cohort measured in equal periods (here, quarters) since signup.

- **Tenure 0**: the quarter the cohort joined (diagonal of the cohort matrix).  
- **Tenure 1**: one quarter after signup.  
- **Tenure 2**: two quarters after signup, and so on.

This aligns cohorts by **lifecycle stage** (Quarter 0, 1, 2, …) rather than by calendar labels (Q1 '21, Q2 '21…), so you always compare the same point in the lifecycle across cohorts.""")
    
    st.markdown("### How Read the Cohort Matrix")
    st.markdown("""- **Rows** = cohorts (the quarter users signed up).  
- **Columns** = calendar quarters.  
- **Diagonal** = the **initial size** of each cohort (Tenure 0).  
- Cells to the **right** of the diagonal = users from that cohort active in later quarters (Tenure 1, 2, 3…).""")
    
except FileNotFoundError:
    st.error("❌ data_test2.csv file not found. Please ensure the file is in the correct directory.")
