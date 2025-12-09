import streamlit as st
import pandas as pd
import plotly.express as px

# --- Title ---
st.title("FEMA Disaster Relief Dashboard")

# --- Load FEMA dataset ---
df = pd.read_csv("fema_sample.csv")

# --- Data Preview ---
st.subheader("Data Preview")
st.write(df.head())

# --- Histogram of Repair Amount ---
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(df, x="repairAmount", nbins=30,
                        title="Distribution of Repair Amounts")
st.plotly_chart(fig_hist)

st.markdown("*Insight:* Most TSA Eligible recepients received 1000 to 3000 dollars in aid money, with the highest aid amount being 35 to 37 thousand dollars, "

            "signifying that most recipients don't receive enough money for major repairs.")
# --- Boxplot of Repair Amount by TSA Eligibility ---
st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(df, x="tsaEligible", y="repairAmount",
                 title="Repair Amount by TSA Eligibility",
                 labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)",
                         "repairAmount": "Repair Amount"})
st.plotly_chart(fig_box)

st.markdown("*Insight:* TSA-eligible households tend to have higher repair amounts, "

            "but variability is large.")

# --- Authors ---
st.write("Authors: Darren Cantor")
