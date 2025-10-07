```python
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- PAGE SETUP ---
st.set_page_config(page_title="Domestic Violence Helpline Locator", page_icon="📱", layout="centered")

st.title("📱 Domestic Violence Helpline Locator")
st.write("Find help centers near you or send an SOS alert in emergencies.")

# --- EMERGENCY SECTION ---
st.markdown("### 🚨 Emergency Options")
col1, col2 = st.columns(2)
with col1:
    st.button("📞 Call Emergency (Nigeria Police - 112)")
with col2:
    st.button("🆘 Send SOS Alert")

# --- HELP CENTERS DATA ---
data = [
    {"name": "Mirabel Centre", "location": "LASUTH, Ikeja, Lagos", "phone": "0815 577 0000"},
    {"name": "Project Alert on Violence Against Women", "location": "Ikeja, Lagos", "phone": "0818 009 1072"},
    {"name": "Women at Risk International Foundation (WARIF)", "location": "Yaba, Lagos", "phone": "0809 210 0009"},
    {"name": "The Cece Yara Foundation", "location": "Lagos", "phone": "0800 800 8001"},
]

df = pd.DataFrame(data)

st.markdown("### 📍 Nearby Help Centers")
st.dataframe(df)

# --- MAP SECTION ---
st.markdown("### 🗺️ Map View")
m = folium.Map(location=[6.5244, 3.3792], zoom_start=11)
for _, row in df.iterrows():
    folium.Marker(
        location=[6.5244, 3.3792],
        popup=f"{row['name']} - {row['phone']}",
        icon=folium.Icon(color="purple", icon="info-sign"),
    ).add_to(m)

st_folium(m, width=700, height=400)

# --- COMMENTS SECTION ---
st.markdown("### 💬 Share Your Experience")
with st.form("comment_form"):
    name = st.text_input("Your Name (optional)")
    comment = st.text_area("Write your experience or advice here:")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if comment.strip():
            st.success("Thank you for sharing your thoughts. Your comment has been submitted.")
        else:
            st.warning("Please write something before submitting.")

# --- SAMPLE COMMENTS ---
st.markdown("### 💭 Recent Comments")
sample_comments = [
    {"name": "Ada", "comment": "Mirabel Centre helped me when I needed it most. I’m grateful!"},
    {"name": "Tolu", "comment": "Please, no one should stay silent. Help is out there!"},
    {"name": "Ngozi", "comment": "I love how easy this app makes finding help."},
]
for c in sample_comments:
    st.markdown(f"**{c['name']}**: {c['comment']}")

# --- CONTACT INFO ---
st.markdown("---")
st.subheader("📞 Contact & Support")
st.write("If you or someone you know is in danger, please reach out immediately.")
st.write("**Helpline:** 0815 577 0000 | **Email:** support@dvhl.org.ng")
st.write("Together, we can create a safer community for women in Nigeria. 💜")
```
