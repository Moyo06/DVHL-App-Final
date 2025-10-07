import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# ---------------- App Title ----------------
st.set_page_config(page_title="DVHL - Domestic Violence Helpline Locator", page_icon="📞", layout="centered")

st.title("📱 Domestic Violence Helpline Locator")
st.caption("Find help centers near you or send an SOS alert in emergencies.")

# ---------------- Emergency Buttons ----------------
st.markdown("### 🚨 Emergency Options")
col1, col2 = st.columns(2)
with col1:
    st.button("📞 Call Emergency", help="Simulate a call to emergency helpline (for demo)")
with col2:
    st.button("🚨 Send SOS", help="Simulate sending an SOS alert (for demo)")

st.divider()

# ---------------- Map Section ----------------
st.markdown("### 📍 Nearby Help Centers")

# Example data of verified centers
data = pd.DataFrame({
    'Center': ['Mirabel Centre - Lagos', 'Project Alert on Violence Against Women - Lagos', 'WARIF Centre - Lagos'],
    'Location': ['LASUTH, Ikeja', 'PO Box 15456, Ikeja', 'No. 6 Turton Street, Yaba'],
    'Phone': ['08155770000', '08180091072', '08092100009'],
    'Latitude': [6.6018, 6.6051, 6.5174],
    'Longitude': [3.3515, 3.3490, 3.3763]
})

# Display table
st.dataframe(data[['Center', 'Location', 'Phone']])

# Create map
m = folium.Map(location=[6.5244, 3.3792], zoom_start=11)

for i, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Center']}<br>{row['Location']}<br>📞 {row['Phone']}",
        icon=folium.Icon(color="purple", icon="heart")
    ).add_to(m)

st_folium(m, width=700, height=400)

st.divider()

# ---------------- Comments Section ----------------
st.subheader("💬 Comments & Experiences")

if "comments" not in st.session_state:
    st.session_state["comments"] = [
        {"name": "Ada", "message": "This app can truly save lives. Thank you for building it!"},
        {"name": "Blessing", "message": "I didn’t know these centers existed, this is so helpful."},
        {"nam
