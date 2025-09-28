"""
Test 2: Instagram Reels vs TikTok Analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configure page
st.set_page_config(
    page_title="Test 2: Instagram Reels",
    page_icon=":mobile_phone:",
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
    
    st.markdown("> Example: For a cohort that started in Q1 '21, the cells (Q1 '21, Q1 '21), (Q1 '21, Q2 '21), (Q1 '21, Q3 '21) correspond to Tenure 0, 1, 2 respectively.")
    
    # Mathematical Formulas
    st.markdown("## Retention by Cohort and Tenure")
    
    st.markdown("**Retention at tenure $t$ for a given cohort:**")
    st.latex(r"""
    \mathrm{Retention}_{\text{cohort},\,t}
    =
    \frac{\text{Active users of that cohort at tenure } t}
    {\text{Initial cohort size (Tenure 0)}}
    """)
    
    st.markdown("**Average retention curve across cohorts (by tenure):**")
    st.latex(r"""
    \overline{\mathrm{Retention}}(t)
    =
    \frac{1}{N_t}
    \sum_{i \in \text{cohorts with data at } t}
    \mathrm{Retention}_{i,\,t}
    """)
    
    st.markdown("Where $N_t$ is the number of cohorts that have a valid observation at tenure $t$.")
    
    st.markdown("## From Retention to LTV and Profitable CAC")
    
    st.markdown("""- Price = **$9.99 per quarter**.  
- Breakeven LTV assumes **~100% gross margin** (ignoring payment fees/opex).  
- Observation window = **5 quarters** (Tenure 0..4). If users stay longer, true LTV increases.""")
    
    st.markdown("**Expected paying quarters (within observed window):**")
    st.latex(r"""
    \mathbb{E}[\text{paying quarters}]
    =
    \sum_{t=0}^{T}
    \overline{\mathrm{Retention}}(t)
    """)
    
    st.markdown("**Breakeven LTV:**")
    st.latex(r"""
    \mathrm{LTV}_{\text{breakeven}}
    =
    (\$9.99)\times
    \mathbb{E}[\text{paying quarters}]
    """)
    
    st.markdown("**CAC guidance:**")
    st.markdown("- **Max profitable CAC (breakeven)**:")
    st.latex(r"""
    \mathrm{CAC}_{\max} \approx \mathrm{LTV}_{\text{breakeven}}
    """)
    
    st.markdown("- **Target CAC** (leave room for fees/opex/ad opportunity cost), e.g. **70% of LTV**:")
    st.latex(r"""
    \mathrm{CAC}_{\text{target}} \approx 0.7 \times \mathrm{LTV}_{\text{breakeven}}
    """)
    
    st.markdown("> If you model payment fees, support cost/user, content costs, or the opportunity cost of removing ads for Prime users, subtract them from LTV before setting your CAC cap.")
    
    st.markdown("## Simple Competitive Growth Analysis vs TikTok")
    
    st.markdown("**Quarter-over-quarter (QoQ) growth of total active users:**")
    st.markdown("1) Approximate total active users per quarter by summing each column of the cohort matrix:")
    st.markdown("   - Let $U_q$ be total active users in quarter $q$.")
    st.markdown("2) QoQ growth rate:")
    st.latex(r"""
    \mathrm{Growth}_{q} \;(\%)
    =
    \left(
    \frac{U_{q}-U_{q-1}}{U_{q-1}}
    \right)\times 100
    """)
    
    st.markdown("**Pre–Post impact (Prime Reels effect):**")
    st.markdown("- Define **Pre-Prime** quarters (e.g., Q1 '21–Q3 '21) and **Post-Prime** quarters (e.g., Q4 '21–Q1 '22).")
    st.markdown("- Compute average users in each period, $\\overline{U}_{\\text{pre}}$ and $\\overline{U}_{\\text{post}}$.")
    
    st.markdown("**Impact percentage:**")
    st.latex(r"""
    \mathrm{Impact}\;(\%)
    =
    \left(
    \frac{\overline{U}_{\text{post}} - \overline{U}_{\text{pre}}}
    {\overline{U}_{\text{pre}}}
    \right)\times 100
    """)
    
    st.markdown("**Interpretation:**")
    st.markdown("- Higher QoQ growth and a positive Pre–Post impact indicate stronger competitive momentum.")
    st.markdown("- If growth slows or turns negative, investigate retention, acquisition, and product value drivers.")
    
    st.markdown("> As you extend the time window (more quarters) or refine margin assumptions, **recalculate LTV and CAC** accordingly.")
    
    # Build Retention by Tenure
    st.markdown("## Build Retention by Tenure")
    st.markdown("""- **Tenure 0** corresponds to the cohort's start quarter (diagonal in the cohort table).
- **Tenure 1, 2, …** are subsequent quarters for that same cohort.
- **Retention** at each tenure is computed as `active users at that tenure / initial cohort size`.""")
    
    st.code("""quarters = list(df.columns[1:])
cohorts = df["Cohort"].tolist()

values = df.set_index("Cohort")[quarters].to_numpy()

# Diagonal = initial size per cohort
initial_sizes = []
for i in range(len(cohorts)):
    if i < len(quarters):
        initial_sizes.append(values[i, i])
    else:
        initial_sizes.append(np.nan)
initial_sizes = np.array(initial_sizes, dtype=float)

max_tenure = len(quarters) - 1

retention_rows = []
for r, cohort in enumerate(cohorts):
    row = []
    n0 = initial_sizes[r]
    for t in range(0, max_tenure+1):
        c = r + t
        if np.isnan(n0) or c >= len(quarters):
            row.append(np.nan)
            continue
        val = values[r, c]
        row.append(np.nan if (pd.isna(val) or pd.isna(n0) or n0 == 0) else val / n0)
    retention_rows.append(row)

retention = pd.DataFrame(
    retention_rows,
    index=cohorts,
    columns=[f"Tenure {t}" for t in range(0, max_tenure+1)]
)""")
    
    # Calculate retention
    quarters = list(df_test2.columns[1:])
    cohorts = df_test2["Cohort"].tolist()
    
    values = df_test2.set_index("Cohort")[quarters].to_numpy()
    
    # Diagonal = initial size per cohort
    initial_sizes = []
    for i in range(len(cohorts)):
        if i < len(quarters):
            initial_sizes.append(values[i, i])
        else:
            initial_sizes.append(np.nan)
    initial_sizes = np.array(initial_sizes, dtype=float)
    
    max_tenure = len(quarters) - 1
    
    retention_rows = []
    for r, cohort in enumerate(cohorts):
        row = []
        n0 = initial_sizes[r]
        for t in range(0, max_tenure+1):
            c = r + t
            if np.isnan(n0) or c >= len(quarters):
                row.append(np.nan)
                continue
            val = values[r, c]
            row.append(np.nan if (pd.isna(val) or pd.isna(n0) or n0 == 0) else val / n0)
        retention_rows.append(row)
    
    retention = pd.DataFrame(
        retention_rows,
        index=cohorts,
        columns=[f"Tenure {t}" for t in range(0, max_tenure+1)]
    )
    
    st.dataframe(retention.round(4))
    
    # Average Retention Curve
    st.markdown("## Average Retention Curve")
    st.markdown("We average retention **across cohorts** for each tenure to estimate a typical lifecycle. This gives us the share of the original cohort still active (and paying) in each subsequent quarter.")
    
    st.code("""avg_retention = retention.mean(axis=0, skipna=True)
pd.DataFrame({
    "Tenure": retention.columns,
    "Avg Retention": avg_retention.values
}).round(4)""")
    
    avg_retention = retention.mean(axis=0, skipna=True)
    avg_retention_df = pd.DataFrame({
        "Tenure": retention.columns,
        "Avg Retention": avg_retention.values
    }).round(4)
    
    st.dataframe(avg_retention_df)
    
    # LTV and CAC Calculations
    st.markdown("## LTV and Profitable CAC")
    st.markdown("""**Assumptions** :
- Revenue per active quarter: **$9.99** (Prime Reels price)
- Gross margin: **~100%** (ignoring fees and opex) to compute *breakeven* CAC
- Lifetime limited to the **observed 5 quarters**. If retention continues beyond, true LTV would be higher.

**Method**:  
Expected paying quarters = sum of average retention at each tenure.  
LTV (breakeven) = $9.99 × (expected paying quarters).

You should target CAC **below** LTV to maintain margins (e.g., 60–80% of LTV).""")
    
    st.code("""price_per_quarter = 9.99
expected_paying_quarters = float(np.nansum(avg_retention.values))
ltv_breakeven = price_per_quarter * expected_paying_quarters
recommended_cac = 0.7 * ltv_breakeven""")
    
    price_per_quarter = 9.99
    expected_paying_quarters = float(np.nansum(avg_retention.values))
    ltv_breakeven = price_per_quarter * expected_paying_quarters
    recommended_cac = 0.7 * ltv_breakeven
    
    summary = {
        "Expected Paying Quarters (within observed window)": round(expected_paying_quarters, 4),
        "LTV Breakeven ($)": round(ltv_breakeven, 2),
        "Recommended CAC Target (70% of LTV, $)": round(recommended_cac, 2)
    }
    
    st.text("Summary:")
    for key, value in summary.items():
        st.text(f"  {key}: {value}")
    
    # Visualizations
    st.markdown("## 📊 Visualizations")
    
    # 1. Retention Curve
    st.markdown("### Average Retention Curve by Tenure")
    
    fig_retention = go.Figure()
    fig_retention.add_trace(go.Scatter(
        x=list(range(len(avg_retention))),
        y=avg_retention.values,
        mode='lines+markers',
        name='Average Retention',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8, color='#1f77b4')
    ))
    
    fig_retention.update_layout(
        title="Average Retention by Tenure (Prime Reels)",
        xaxis_title="Tenure (quarters since signup)",
        yaxis_title="Retention (share of original cohort)",
        height=500,
        showlegend=False
    )
    
    # Add annotations for key points
    for i, val in enumerate(avg_retention.values):
        if not np.isnan(val):
            fig_retention.add_annotation(
                x=i,
                y=val,
                text=f"{val:.2%}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor="#1f77b4",
                font=dict(size=10)
            )
    
    st.plotly_chart(fig_retention, use_container_width=True)
    
    # 2. Cohort Heatmap
    st.markdown("### Cohort Analysis Heatmap")
    
    # Create cohort heatmap
    fig_cohort = go.Figure(data=go.Heatmap(
        z=retention.values,
        x=retention.columns,
        y=retention.index,
        colorscale='RdYlBu_r',
        text=retention.round(3).values,
        texttemplate="%{text}",
        textfont={"size": 10},
        colorbar=dict(title="Retention Rate")
    ))
    
    fig_cohort.update_layout(
        title="Cohort Retention Heatmap",
        xaxis_title="Tenure",
        yaxis_title="Cohort",
        height=500
    )
    
    st.plotly_chart(fig_cohort, use_container_width=True)
    
    # 3. User Growth Analysis
    st.markdown("### User Growth Analysis")
    
    # Calculate QoQ growth
    quarters_list = list(quarterly_totals.index)
    growth_rates = []
    for i in range(1, len(quarters_list)):
        prev_users = quarterly_totals.iloc[i-1]
        curr_users = quarterly_totals.iloc[i]
        growth_rate = ((curr_users - prev_users) / prev_users) * 100
        growth_rates.append(growth_rate)
    
    # Create subplot with two y-axes
    fig_growth = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add total users bar chart
    fig_growth.add_trace(
        go.Bar(
            x=quarters_list,
            y=quarterly_totals.values,
            name="Total Active Users",
            marker_color='lightblue',
            opacity=0.7
        ),
        secondary_y=False,
    )
    
    # Add growth rate line
    fig_growth.add_trace(
        go.Scatter(
            x=quarters_list[1:],
            y=growth_rates,
            mode='lines+markers',
            name="QoQ Growth Rate (%)",
            line=dict(color='red', width=3),
            marker=dict(size=8)
        ),
        secondary_y=True,
    )
    
    # Set y-axes titles
    fig_growth.update_yaxes(title_text="Total Active Users", secondary_y=False)
    fig_growth.update_yaxes(title_text="QoQ Growth Rate (%)", secondary_y=True)
    
    fig_growth.update_layout(
        title="User Growth Analysis: Total Users vs QoQ Growth Rate",
        xaxis_title="Quarter",
        height=500
    )
    
    st.plotly_chart(fig_growth, use_container_width=True)
    
    # Analysis Results
    st.markdown("## 📈 Analysis Results")
    
    st.markdown("### (a) Retention by cycle/quarter")
    st.markdown("Using the cohort matrix normalized by each cohort's initial size (diagonal), the average retention by tenure is:")
    
    for i, (tenure, retention_rate) in enumerate(zip(avg_retention_df['Tenure'], avg_retention_df['Avg Retention'])):
        st.text(f"{tenure}: {retention_rate:.2%}")
    
    st.markdown('("Tenure t" = t quarters after signup.)')
    
    st.markdown("### (b) Profitable CAC (using the retention chart)")
    
    st.markdown("From the chart, the average retention by tenure is approximately:")
    for i, (tenure, retention_rate) in enumerate(zip(avg_retention_df['Tenure'], avg_retention_df['Avg Retention'])):
        st.markdown(f"- {tenure}: **{retention_rate:.2f}**")
    
    st.markdown("**Expected paying quarters (area under the curve):**")
    
    retention_sum_formula = " + ".join([f"{val:.2f}" for val in avg_retention.values if not np.isnan(val)])
    st.latex(f"\\mathbb{{E}}[\\text{{quarters}}] = {retention_sum_formula} \\approx {expected_paying_quarters:.2f}")
    
    st.markdown("**Price:** $9.99 per quarter")
    
    st.markdown("**Breakeven LTV:**")
    st.latex(f"\\text{{LTV}}_{{\\text{{breakeven}}}} = 9.99 \\times {expected_paying_quarters:.2f} \\approx \\${ltv_breakeven:.2f}")
    
    st.markdown(f"**Profitable CAC (max to break even):** **${ltv_breakeven:.2f}**")
    
    st.markdown(f"**Recommended CAC target (~70% of LTV, to allow fees/opex):**")
    st.latex(f"\\text{{CAC}}_{{\\text{{target}}}} \\approx 0.7 \\times {ltv_breakeven:.2f} \\approx \\${recommended_cac:.2f}")
    
    st.markdown("> **Notes:** If Prime users remain subscribed beyond five quarters, true LTV would increase, allowing a higher CAC. Conversely, if you include payment fees, support costs, or ad-opportunity cost (Prime users remove ads), you should subtract those from LTV to get a stricter CAC cap.")
    
    # Key Insights
    st.markdown("## 🔍 Key Insights")
    
    st.markdown("**In a nutshell, the chart tells you this:**")
    
    st.markdown(f"- **A very sharp drop after the 1st quarter:** from 100% (Tenure 0) to ~{avg_retention.iloc[1]:.0%} in Tenure 1.")
    st.markdown(f"- **Sustained churn afterward:** ~{avg_retention.iloc[2]:.0%} in Tenure 2 and ~{avg_retention.iloc[3]:.1%} in Tenure 3.")
    st.markdown(f"- **Almost no one follows through to the 5th quarter:** ~{avg_retention.iloc[4]:.2%} in Tenure 4.")
    
    # Pre-Post Analysis
    pre_prime_quarters = quarterly_totals.iloc[:3]  # Q1-Q3 '21
    post_prime_quarters = quarterly_totals.iloc[3:]  # Q4 '21 - Q1 '22
    
    avg_pre = pre_prime_quarters.mean()
    avg_post = post_prime_quarters.mean()
    impact_percentage = ((avg_post - avg_pre) / avg_pre) * 100
    
    st.markdown("### Pre-Post Prime Reels Impact")
    st.markdown(f"- **Pre-Prime average users (Q1-Q3 '21):** {avg_pre:,.0f}")
    st.markdown(f"- **Post-Prime average users (Q4 '21-Q1 '22):** {avg_post:,.0f}")
    st.markdown(f"- **Impact:** {impact_percentage:+.1f}% change in average user base")
    
    if impact_percentage > 0:
        st.success(f"✅ Prime Reels shows a positive impact with {impact_percentage:.1f}% increase in user base!")
    else:
        st.warning(f"⚠️ Prime Reels shows a negative impact with {impact_percentage:.1f}% decrease in user base.")
    
except FileNotFoundError:
    st.error("❌ data_test2.csv file not found. Please ensure the file is in the correct directory.")
