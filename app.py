import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# 1. Page setup
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Analysis | Future Interns",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# 2. Dark theme styling
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0B1020;
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stMetric"] {
        background-color: #151E32;
        border: 1px solid #26334D;
        padding: 18px;
        border-radius: 12px;
    }

    [data-testid="stMetricLabel"] {
        color: #A8B5CC;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF;
    }

    h1, h2, h3 {
        color: #F8FAFC;
    }

    div[data-testid="stPlotlyChart"] {
        background-color: #111827;
        border-radius: 12px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. Load and clean the dataset
# --------------------------------------------------
st.title("📊 Customer Retention & Churn Analysis")
st.caption("Future Interns | Data Science & Analytics | Task 2")

DATA_FILE = "Telco-Customer-Churn.csv"

@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)

    # Remove accidental spaces from column names
    data.columns = data.columns.str.strip()

    # Convert TotalCharges to numeric
    data["TotalCharges"] = pd.to_numeric(
        data["TotalCharges"], errors="coerce"
    )

    # Remove rows where TotalCharges was blank or invalid
    data = data.dropna(subset=["TotalCharges"]).copy()

    # Ensure numeric columns are numeric
    data["tenure"] = pd.to_numeric(data["tenure"], errors="coerce")
    data["MonthlyCharges"] = pd.to_numeric(
        data["MonthlyCharges"], errors="coerce"
    )

    data = data.dropna(
        subset=["tenure", "MonthlyCharges", "TotalCharges"]
    ).copy()

    return data


try:
    df = load_data(DATA_FILE)
except FileNotFoundError:
    st.error(
        f"Dataset not found: {DATA_FILE}. "
        "Place the CSV file in the same folder as app.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()

required_columns = [
    "customerID", "Churn", "Contract", "InternetService",
    "PaymentMethod", "tenure", "MonthlyCharges", "TotalCharges"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"The dataset is missing these columns: {missing_columns}")
    st.stop()

# --------------------------------------------------
# 4. Sidebar filters
# --------------------------------------------------
st.sidebar.title("🔎 Dashboard Filters")
st.sidebar.caption("Select the customer groups you want to explore.")

contract_options = sorted(df["Contract"].dropna().unique())
internet_options = sorted(df["InternetService"].dropna().unique())
payment_options = sorted(df["PaymentMethod"].dropna().unique())
churn_options = sorted(df["Churn"].dropna().unique())

selected_contracts = st.sidebar.multiselect(
    "Contract Type",
    contract_options,
    default=contract_options
)

selected_internet = st.sidebar.multiselect(
    "Internet Service",
    internet_options,
    default=internet_options
)

selected_payments = st.sidebar.multiselect(
    "Payment Method",
    payment_options,
    default=payment_options
)

selected_churn = st.sidebar.multiselect(
    "Churn Status",
    churn_options,
    default=churn_options
)

min_tenure = int(df["tenure"].min())
max_tenure = int(df["tenure"].max())

tenure_range = st.sidebar.slider(
    "Tenure (months)",
    min_value=min_tenure,
    max_value=max_tenure,
    value=(min_tenure, max_tenure)
)

# Apply filters
filtered_df = df[
    df["Contract"].isin(selected_contracts)
    & df["InternetService"].isin(selected_internet)
    & df["PaymentMethod"].isin(selected_payments)
    & df["Churn"].isin(selected_churn)
    & df["tenure"].between(tenure_range[0], tenure_range[1])
].copy()

# --------------------------------------------------
# 5. KPI cards
# --------------------------------------------------
st.subheader("Business Overview")

total_customers = len(filtered_df)
churned_customers = int((filtered_df["Churn"] == "Yes").sum())
retained_customers = int((filtered_df["Churn"] == "No").sum())

churn_rate = (
    churned_customers / total_customers * 100
    if total_customers else 0
)

retention_rate = (
    retained_customers / total_customers * 100
    if total_customers else 0
)

avg_monthly_charges = (
    filtered_df["MonthlyCharges"].mean()
    if total_customers else 0
)

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("Total Customers", f"{total_customers:,}")
k2.metric("Churned Customers", f"{churned_customers:,}")
k3.metric("Churn Rate", f"{churn_rate:.2f}%")
k4.metric("Retention Rate", f"{retention_rate:.2f}%")
k5.metric("Avg. Monthly Charges", f"{avg_monthly_charges:.2f}")

st.caption(
    f"Showing {total_customers:,} customers after applying your filters."
)

if filtered_df.empty:
    st.warning("No customers match these filters. Change your selections.")
    st.stop()

# --------------------------------------------------
# 6. Prepare chart theme
# --------------------------------------------------
def style_chart(fig, height=360):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#E5E7EB"),
        height=height,
        margin=dict(l=20, r=20, t=55, b=25),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        )
    )
    return fig


# --------------------------------------------------
# 7. Churn distribution
# --------------------------------------------------
st.markdown("---")
st.subheader("Customer Churn Overview")

left, right = st.columns(2)

churn_summary = (
    filtered_df["Churn"]
    .value_counts()
    .reindex(["No", "Yes"], fill_value=0)
    .rename_axis("Churn")
    .reset_index(name="Customers")
)

with left:
    fig = px.bar(
        churn_summary,
        x="Churn",
        y="Customers",
        color="Churn",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        text="Customers",
        title="Retained vs Churned Customers"
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(style_chart(fig), use_container_width=True)

with right:
    fig = px.pie(
        churn_summary,
        names="Churn",
        values="Customers",
        hole=0.62,
        color="Churn",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        title="Customer Churn Share"
    )
    fig.update_traces(
        textinfo="percent+label",
        hovertemplate="%{label}: %{value:,} customers (%{percent})"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True)

# --------------------------------------------------
# 8. Churn by contract
# --------------------------------------------------
st.markdown("---")
st.subheader("What Is Associated With Churn?")

left, right = st.columns(2)

with left:
    contract_summary = (
        filtered_df.groupby(["Contract", "Churn"], observed=False)
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        contract_summary,
        x="Contract",
        y="Customers",
        color="Churn",
        barmode="group",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        title="Customer Count by Contract Type"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True)

with right:
    contract_rate = (
        filtered_df.groupby("Contract", observed=False)
        .agg(
            Customers=("customerID", "count"),
            Churned=("Churn", lambda x: (x == "Yes").sum())
        )
        .reset_index()
    )

    contract_rate["Churn Rate (%)"] = (
        contract_rate["Churned"] / contract_rate["Customers"] * 100
    )

    fig = px.bar(
        contract_rate,
        x="Contract",
        y="Churn Rate (%)",
        text=contract_rate["Churn Rate (%)"].map(
            lambda value: f"{value:.1f}%"
        ),
        color="Churn Rate (%)",
        color_continuous_scale=["#22C55E", "#F59E0B", "#F43F5E"],
        title="Churn Rate by Contract Type",
        hover_data=["Customers", "Churned"]
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(style_chart(fig), use_container_width=True)

# --------------------------------------------------
# 9. Tenure and monthly charges
# --------------------------------------------------
left, right = st.columns(2)

with left:
    fig = px.box(
        filtered_df,
        x="Churn",
        y="tenure",
        color="Churn",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        points="outliers",
        title="Customer Tenure by Churn Status"
    )
    fig.update_yaxes(title="Tenure (months)")
    st.plotly_chart(style_chart(fig), use_container_width=True)

with right:
    fig = px.box(
        filtered_df,
        x="Churn",
        y="MonthlyCharges",
        color="Churn",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        points="outliers",
        title="Monthly Charges by Churn Status"
    )
    fig.update_yaxes(title="Monthly Charges")
    st.plotly_chart(style_chart(fig), use_container_width=True)

# --------------------------------------------------
# 10. Payment method and internet service
# --------------------------------------------------
left, right = st.columns(2)

with left:
    payment_summary = (
        filtered_df.groupby(["PaymentMethod", "Churn"], observed=False)
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        payment_summary,
        x="PaymentMethod",
        y="Customers",
        color="Churn",
        barmode="group",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        title="Churn by Payment Method"
    )
    fig.update_xaxes(tickangle=-20)
    st.plotly_chart(style_chart(fig, 420), use_container_width=True)

with right:
    internet_summary = (
        filtered_df.groupby(["InternetService", "Churn"], observed=False)
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        internet_summary,
        x="InternetService",
        y="Customers",
        color="Churn",
        barmode="group",
        color_discrete_map={"No": "#22C55E", "Yes": "#F43F5E"},
        title="Churn by Internet Service"
    )
    st.plotly_chart(style_chart(fig), use_container_width=True)

# --------------------------------------------------
# 11. Download filtered data
# --------------------------------------------------
st.markdown("---")
st.subheader("Explore Customer Records")

with st.expander("Preview filtered customer data"):
    st.dataframe(filtered_df, use_container_width=True)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_customer_churn.csv",
    mime="text/csv"
)

st.caption(
    "Future Interns | Customer Retention & Churn Analysis | Task 2"
)