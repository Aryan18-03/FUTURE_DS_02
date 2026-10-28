import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="📊Customer Retention & Churn Analysis",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Cyber-analytics visual system: deep navy, electric cyan, violet, and signal coral.
st.markdown("""
<style>
:root {
    --bg: #07111F;
    --panel: #0D1B2A;
    --panel-2: #102338;
    --line: #203A53;
    --cyan: #36E4F5;
    --blue: #4D8DFF;
    --violet: #A78BFA;
    --coral: #FF6B81;
    --mint: #4DE2B1;
    --text: #EAF4FF;
    --muted: #91A9C2;
}
.stApp {
    background:
      radial-gradient(ellipse at 12% 0%, rgba(54,228,245,.10), transparent 34%),
      radial-gradient(ellipse at 88% 8%, rgba(167,139,250,.10), transparent 32%),
      var(--bg);
    color: var(--text);
}
[data-testid="stHeader"] { display: none !important; height: 0 !important; }
[data-testid="stToolbar"] { display: none !important; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.block-container { padding-top: .8rem !important; }
[data-testid="stSidebar"] {
    background: radial-gradient(ellipse at 10% 0%, rgba(54,228,245,.12), transparent 38%), linear-gradient(180deg, #0B1B2B 0%, #091522 100%);
    border-right: 1px solid rgba(54,228,245,.22);
}
[data-testid="stSidebar"] [data-testid="stExpander"] {
    background: linear-gradient(145deg, rgba(16,35,56,.92), rgba(8,21,35,.92));
    border: 1px solid rgba(77,141,255,.28) !important;
    border-radius: 14px !important;
    margin-bottom: .55rem;
}
[data-testid="stSidebar"] [data-testid="stExpander"] summary { font-weight: 750; }
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { color: #A8C5E0 !important; font-size: .9rem; font-weight: 700; }
.sidebar-kicker { color: var(--cyan); font-size: .72rem; font-weight: 850; letter-spacing: .16em; }
.sidebar-reset button { min-height: 44px; background: linear-gradient(100deg, rgba(54,228,245,.22), rgba(167,139,250,.20)); border: 1px solid rgba(54,228,245,.65); box-shadow: 0 5px 18px rgba(54,228,245,.09); }
[data-testid="stSidebar"] * { color: var(--text); }
.block-container { padding-top: 1.5rem; padding-bottom: 2.5rem; max-width: 1500px; }
h1, h2, h3 { color: var(--text) !important; letter-spacing: -.025em; }
h1 { font-weight: 800 !important; }\n[data-testid="stPlotlyChart"] iframe { overflow: hidden !important; }\n[data-testid="stPlotlyChart"] { overflow: visible !important; }\n[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { font-size: .95rem !important; font-weight: 800 !important; color: #EAF4FF !important; }\n[data-testid="stSidebar"] [data-baseweb="select"] { min-height: 42px; }
p, label, .stMarkdown { color: var(--text); }
[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(16,35,56,.98), rgba(10,25,41,.98));
    border: 1px solid var(--line);
    border-top: 2px solid var(--cyan);
    padding: 1rem 1.05rem;
    border-radius: 15px;
    box-shadow: 0 8px 28px rgba(0,0,0,.14);
    min-height: 112px;
}
[data-testid="stMetricLabel"] { color: #C7D8EA !important; font-size: 1.12rem !important; font-weight: 800 !important; }
[data-testid="stMetricValue"] { color: var(--cyan) !important; font-size: 1.85rem !important; font-weight: 850 !important; }
[data-testid="stMetricDelta"] { font-size: .8rem; }
div[data-testid="stPlotlyChart"] {
    background: rgba(13,27,42,.74);
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: .35rem;
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--line) !important;
    border-radius: 14px !important;
}
.stButton > button, .stDownloadButton > button {
    border: 1px solid rgba(54,228,245,.45);
    background: linear-gradient(100deg, rgba(54,228,245,.14), rgba(77,141,255,.16));
    color: var(--text);
    border-radius: 10px;
    font-weight: 650;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    border-color: var(--cyan);
    color: var(--cyan);
}
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
    background: #102338;
    border-color: #294660;
}
[data-testid="stExpander"] { border: 1px solid var(--line); border-radius: 12px; overflow: visible !important; }\n[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: .55rem; }\n[data-testid="stSidebar"] [data-baseweb="popover"] { max-height: none !important; }
hr { border-color: var(--line); }
.hero {
    padding: 1.4rem 1.5rem;
    border: 1px solid rgba(54,228,245,.27);
    border-radius: 18px;
    background: linear-gradient(115deg, rgba(16,35,56,.96), rgba(12,24,42,.83));
    margin-bottom: 1rem;
}
.eyebrow {
    color: var(--cyan);
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: .16em;
    text-transform: uppercase;
}
.hero-sub { color: var(--muted); margin-bottom: 0; }
.insight-card {
    padding: 1rem 1.05rem;
    border: 1px solid var(--line);
    border-left: 3px solid var(--cyan);
    background: rgba(13,27,42,.82);
    border-radius: 12px;
    margin-bottom: .7rem;
}
.insight-card strong { color: var(--cyan); }
.small-note { color: var(--muted); font-size: .83rem; }
@media (max-width: 768px) {
    .block-container { padding: 1rem .8rem 2rem .8rem; }
    .hero { padding: 1rem; }
    h1 { font-size: 1.7rem !important; }
    [data-testid="stMetric"] { padding: .75rem; min-height: 90px; }
    [data-testid="stMetricValue"] { font-size: 1.35rem; }
    div[data-testid="stPlotlyChart"] { padding: 0; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">Customer intelligence / retention signals</div>
  <h1>📊Customer Retention &amp; Churn Analysis</h1>
  <p class="hero-sub">Spot retention risks, explore customer segments, and turn churn patterns into practical actions.</p>
</div>
""", unsafe_allow_html=True)
st.caption("FUTURE INTERNS • DATA SCIENCE & ANALYTICS • TASK 2")

DATA_FILE = "Telco-Customer-Churn.csv"

@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()
    data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    data["tenure"] = pd.to_numeric(data["tenure"], errors="coerce")
    data["MonthlyCharges"] = pd.to_numeric(data["MonthlyCharges"], errors="coerce")
    data = data.dropna(subset=["TotalCharges", "tenure", "MonthlyCharges"]).copy()
    return data

try:
    df = load_data(DATA_FILE)
except FileNotFoundError:
    st.error(f"Dataset not found: {DATA_FILE}. Keep the CSV in the same folder as app.py.")
    st.stop()
except Exception as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()

required_columns = [
    "customerID", "Churn", "Contract", "InternetService", "PaymentMethod",
    "SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"
]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    st.error(f"The dataset is missing these columns: {missing_columns}")
    st.stop()

# Sidebar controls use keyed widgets so the reset button truly restores defaults.
contract_options = sorted(df["Contract"].dropna().unique().tolist())
internet_options = sorted(df["InternetService"].dropna().unique().tolist())
payment_options = sorted(df["PaymentMethod"].dropna().unique().tolist())
senior_options = ["All customers", "Senior citizens", "Non-senior citizens"]
min_tenure = int(df["tenure"].min())
max_tenure = int(df["tenure"].max())

def reset_filters():
    st.session_state["contract_filter"] = contract_options
    st.session_state["internet_filter"] = internet_options
    st.session_state["payment_filter"] = payment_options
    st.session_state["senior_filter"] = "All customers"
    st.session_state["tenure_filter"] = (min_tenure, max_tenure)

st.sidebar.markdown('<div class="sidebar-kicker">CUSTOMER INTELLIGENCE</div>', unsafe_allow_html=True)
st.sidebar.markdown("## 🎛️ Segment controls")
st.sidebar.caption("Explore customer groups while keeping churn-rate comparisons meaningful.")
st.sidebar.markdown('<div class="sidebar-reset">', unsafe_allow_html=True)
st.sidebar.button("↺  Reset all filters", on_click=reset_filters, use_container_width=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")
with st.sidebar.expander("▦  Contract & service", expanded=True):
    selected_contracts = st.multiselect("Contract type", contract_options, default=contract_options, key="contract_filter")
    selected_internet = st.multiselect("Internet service", internet_options, default=internet_options, key="internet_filter")
with st.sidebar.expander("◈  Billing & customer profile", expanded=True):
    selected_payments = st.multiselect("Payment method", payment_options, default=payment_options, key="payment_filter")
    selected_senior = st.selectbox("Customer profile", senior_options, index=0, key="senior_filter")
with st.sidebar.expander("◷  Customer tenure", expanded=True):
    tenure_range = st.slider("Tenure range (months)", min_tenure, max_tenure, (min_tenure, max_tenure), key="tenure_filter")
st.sidebar.markdown('<p class="small-note">Tip: compare contract, billing, and tenure segments to identify where retention support may help.</p>', unsafe_allow_html=True)

filtered_df = df[
    df["Contract"].isin(selected_contracts)
    & df["InternetService"].isin(selected_internet)
    & df["PaymentMethod"].isin(selected_payments)
    & df["tenure"].between(tenure_range[0], tenure_range[1])
].copy()
if selected_senior == "Senior citizens":
    filtered_df = filtered_df[filtered_df["SeniorCitizen"] == 1].copy()
elif selected_senior == "Non-senior citizens":
    filtered_df = filtered_df[filtered_df["SeniorCitizen"] == 0].copy()

total_customers = len(filtered_df)
churned_customers = int((filtered_df["Churn"] == "Yes").sum())
retained_customers = int((filtered_df["Churn"] == "No").sum())
churn_rate = churned_customers / total_customers * 100 if total_customers else 0
retention_rate = retained_customers / total_customers * 100 if total_customers else 0
avg_monthly_charges = filtered_df["MonthlyCharges"].mean() if total_customers else 0

st.subheader("📈 Customer Retention Performance KPIs")
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Customers in view", f"{total_customers:,}")
k2.metric("Churned customers", f"{churned_customers:,}")
k3.metric("Churn rate", f"{churn_rate:.2f}%")
k4.metric("Retention rate", f"{retention_rate:.2f}%")
k5.metric("Avg. monthly charge", f"${avg_monthly_charges:,.2f}")
st.caption(f"Filtered view: {total_customers:,} customers. Churn and retention rates include both churn outcomes in the selected segment.")

if filtered_df.empty:
    st.warning("No customers match the selected filters. Widen one or more filters to continue.")
    st.stop()

def style_chart(fig, height=350):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#DCEBFA", family="Arial"),
        height=height,
        margin=dict(l=14, r=14, t=76, b=28),
        title=dict(font=dict(size=15, color="#FFFFFF", family="Arial"), x=0.02, pad=dict(b=10)),
        legend=dict(
            bgcolor="rgba(0,0,0,0)", orientation="h",
            yanchor="bottom", y=1.02, xanchor="left", x=0
        ),
        hoverlabel=dict(bgcolor="#102338", font_color="#EAF4FF"),
    )
    fig.update_xaxes(showgrid=False, zeroline=False, automargin=True)
    fig.update_yaxes(gridcolor="rgba(145,169,194,.13)", zeroline=False, automargin=True)
    return fig

CHURN_COLORS = {"No": "#36E4F5", "Yes": "#FF6B81"}

st.markdown("---")
st.subheader("01 / Churn pulse")
left, right = st.columns(2, gap="medium")
churn_summary = (
    filtered_df["Churn"].value_counts().reindex(["No", "Yes"], fill_value=0)
    .rename_axis("Churn").reset_index(name="Customers")
)
with left:
    fig = px.bar(
        churn_summary, x="Churn", y="Customers", color="Churn",
        color_discrete_map=CHURN_COLORS, text="Customers",
        title="Retained vs. churned customers"
    )
    fig.update_traces(textposition="outside", cliponaxis=False)
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})
with right:
    fig = px.pie(
        churn_summary, names="Churn", values="Customers", hole=.66,
        color="Churn", color_discrete_map=CHURN_COLORS, title="Share of customers"
    )
    fig.update_traces(textinfo="percent+label", marker=dict(line=dict(color="#0D1B2A", width=3)))
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})

st.markdown("---")
st.subheader("02 / Risk signals")
left, right = st.columns(2, gap="medium")
with left:
    contract_summary = (
        filtered_df.groupby(["Contract", "Churn"], observed=False).size()
        .reset_index(name="Customers")
    )
    fig = px.bar(
        contract_summary, x="Contract", y="Customers", color="Churn",
        barmode="group", color_discrete_map=CHURN_COLORS,
        title="Customer count by contract"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})
with right:
    contract_rate = (
        filtered_df.groupby("Contract", observed=False)
        .agg(Customers=("customerID", "count"), Churned=("Churn", lambda x: (x == "Yes").sum()))
        .reset_index()
    )
    contract_rate["Churn Rate (%)"] = contract_rate["Churned"].div(contract_rate["Customers"]).mul(100).fillna(0)
    fig = px.bar(
        contract_rate, x="Contract", y="Churn Rate (%)",
        text=contract_rate["Churn Rate (%)"].map(lambda x: f"{x:.1f}%"),
        color="Churn Rate (%)", color_continuous_scale=["#36E4F5", "#4D8DFF", "#FF6B81"],
        title="Churn rate by contract", hover_data=["Customers", "Churned"]
    )
    fig.update_traces(textposition="outside", cliponaxis=False)
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})

left, right = st.columns(2, gap="medium")
with left:
    fig = px.box(
        filtered_df, x="Churn", y="tenure", color="Churn",
        color_discrete_map=CHURN_COLORS, points="outliers",
        title="Tenure by churn status"
    )
    fig.update_yaxes(title="Tenure (months)")
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})
with right:
    fig = px.box(
        filtered_df, x="Churn", y="MonthlyCharges", color="Churn",
        color_discrete_map=CHURN_COLORS, points="outliers",
        title="Monthly charges by churn status"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})

left, right = st.columns(2, gap="medium")
with left:
    payment_summary = (
        filtered_df.groupby(["PaymentMethod", "Churn"], observed=False).size()
        .reset_index(name="Customers")
    )
    fig = px.bar(
        payment_summary, x="PaymentMethod", y="Customers", color="Churn",
        barmode="group", color_discrete_map=CHURN_COLORS,
        title="Customers by payment method and churn status"
    )
    fig.update_xaxes(tickangle=-25)
    st.plotly_chart(style_chart(fig, 430), use_container_width=True, config={"displayModeBar": False, "responsive": True})
with right:
    internet_summary = (
        filtered_df.groupby(["InternetService", "Churn"], observed=False).size()
        .reset_index(name="Customers")
    )
    fig = px.bar(
        internet_summary, x="InternetService", y="Customers", color="Churn",
        barmode="group", color_discrete_map=CHURN_COLORS,
        title="Customers by internet service and churn status"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True, config={"displayModeBar": False, "responsive": True})

# Evidence-based insights update with the selected segment.
st.markdown("---")
st.subheader("03 / Insights & recommended actions")
st.caption("These are associations in the selected data, not proof that one factor causes churn.")

def churn_rate_table(frame, group_col):
    summary = frame.groupby(group_col, observed=False).agg(
        total=("Churn", "size"),
        churned=("Churn", lambda values: (values == "Yes").sum())
    )
    summary["rate"] = summary["churned"].div(summary["total"]).mul(100).fillna(0)
    return summary

contract_rates = churn_rate_table(filtered_df, "Contract")
payment_rates = churn_rate_table(filtered_df, "PaymentMethod")
internet_rates = churn_rate_table(filtered_df, "InternetService")

insight_col, action_col = st.columns(2, gap="medium")
with insight_col:
    st.markdown("#### 🔎 Signals in this segment")
    st.markdown(f'<div class="insight-card"><strong>{churn_rate:.1f}% churn rate</strong><br>There are {churned_customers:,} churned customers in the current filtered view.</div>', unsafe_allow_html=True)
    if not contract_rates.empty:
        high_contract = contract_rates["rate"].idxmax()
        st.markdown(f'<div class="insight-card"><strong>Contract signal: {high_contract}</strong><br>Highest observed contract-level churn rate in this view: {contract_rates.loc[high_contract, "rate"]:.1f}%.</div>', unsafe_allow_html=True)
    if not payment_rates.empty:
        high_payment = payment_rates["rate"].idxmax()
        st.markdown(f'<div class="insight-card"><strong>Payment signal: {high_payment}</strong><br>Highest observed payment-method churn rate in this view: {payment_rates.loc[high_payment, "rate"]:.1f}%.</div>', unsafe_allow_html=True)
    if not internet_rates.empty:
        high_internet = internet_rates["rate"].idxmax()
        st.markdown(f'<div class="insight-card"><strong>Service signal: {high_internet}</strong><br>Highest observed internet-service churn rate in this view: {internet_rates.loc[high_internet, "rate"]:.1f}%.</div>', unsafe_allow_html=True)
with action_col:
    st.markdown("#### 🧭 Suggested actions")
    st.markdown("""
    <div class="insight-card"><strong>1 / Support new customers</strong><br>Review the first months of the customer journey, check onboarding issues, and follow up after service setup.</div>
    <div class="insight-card"><strong>2 / Test retention offers</strong><br>Consider clear, optional longer-term plans or loyalty benefits for month-to-month customers; measure results before scaling.</div>
    <div class="insight-card"><strong>3 / Review billing friction</strong><br>Investigate payment-method and billing-related complaints, and make payment options and invoices easy to understand.</div>
    <div class="insight-card"><strong>4 / Improve service experience</strong><br>Review service reliability, support response time, and customer feedback for segments with elevated churn.</div>
    <div class="insight-card"><strong>5 / Measure impact</strong><br>Track churn rate and retention over time, and compare test groups before and after each action.</div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("04 / Customer records")
with st.expander("Preview filtered customer data"):
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download filtered data (CSV)",
    data=csv_data,
    file_name="filtered_customer_churn.csv",
    mime="text/csv",
    use_container_width=True,
)
st.markdown("---")
st.markdown('<p class="small-note">FUTURE INTERNS · Customer Retention & Churn Analysis · Built with Streamlit, Pandas and Plotly</p>', unsafe_allow_html=True)
