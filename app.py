import streamlit as st

st.set_page_config(page_title="CPP Calculator", layout="centered")

st.title("🧮 CPP Calculator – Cost Per Purchase")
st.write("Calculate CPP with or without delivery rate (especially useful for COD campaigns).")

ad_spend = st.number_input("Ad Spend (EGP / USD)", min_value=0.0, value=10000.0)
orders = st.number_input("Number of Orders", min_value=1, value=100)
delivery_rate = st.slider("Delivery Rate (%)", min_value=0, max_value=100, value=80)

basic_cpp = ad_spend / orders
delivered_orders = orders * (delivery_rate / 100)
effective_cpp = ad_spend / delivered_orders if delivered_orders != 0 else 0

st.markdown("### ✅ Results")
st.write(f"**Basic CPP:** {basic_cpp:.2f}")
st.write(f"**Effective CPP (with delivery rate):** {effective_cpp:.2f}")
