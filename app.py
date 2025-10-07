import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Domestic Violence Helpline Locator", page_icon="📞", layout="wide")

# Title

st.title("📞 Domestic Violence Helpline Locator")
st.write("Find help centers near you or send an SOS alert in emergencies.")

# Emergency buttons

col1, col2 = st.columns(2)
with col1:
st.button("🚨 Send SOS Alert")
with col2:
st.button("📞 Call Emergency")

# Map

st.header("📍 Nearby Help Centers")

centers = [
{"name": "Mirabel Centre - Lagos", "address": "LASUTH, Ikeja", "phone": "08155770000"},
{"name": "Project Alert on Violence Against Women", "address": "Ikeja, Lagos", "phone": "08180091072"},
{"name": "Women at Risk International Foundation (WARIF)", "address": "Yaba, Lagos", "phone": "08092100009"}
]

m = folium.Map(location=[6.5244, 3.3792], zoom_start=11)
for center in centers:
folium.Marker(
location=[6.5244, 3.3792],
popup=f"{center['name']}<br>{center['address']}<br>{center['phone']}",
icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)

st_data = st_folium(m, width=700, height=450)

# Search feature

st.header("🔍 Search for a Help Center")
query = st.text_input("Enter center name or location")

def search_centers(query):
if not query:
return centers
return [c for c in centers if query.lower() in c["name"].lower() or query.lower() in c["address"].lower()]

results = search_centers(query)
for c in results:
st.write(f"**{c['name']}** — {c['address']} — 📞 {c['phone']}")

# Feedback section

st.header("💬 Share Your Experience or Feedback")

with st.form("comment_form"):
name = st.text_input("Your Name")
comment = st.text_area("Your Comment or Experience")
submitted = st.form_submit_button("Submit")

if submitted:
if name and comment:
st.success(f"Thank you, {name}, for sharing your experience!")
# (Optional: store data locally if allowed)
else:
st.warning("Please fill in both your name and comment before submitting.")

# Contact info

st.header("📧 Contact Support")
st.write("For more help, reach out to us:")
st.write("- 📞 Hotline: 0810 123 4567")
st.write("- 📧 Email: [support@dvhlapp.ng](mailto:support@dvhlapp.ng)")
st.write("- 🌐 Website: [www.dvhlapp.ng](http://www.dvhlapp.ng)")

st.caption("© 2025 Domestic Violence Helpline Locator | Built with ❤️ in Nigeria")
