import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Page title

st.title("📞 Domestic Violence Helpline Locator")
st.write("Find help centers near you or send an SOS alert in emergencies.")

# Sidebar SOS alert

with st.sidebar:
st.header("🚨 Emergency Options")
st.button("📞 Call Emergency")
st.button("🚨 Send SOS Alert")

# Load help centers

data = pd.read_csv("help_centers.csv")

# Display help centers

st.subheader("📍 Nearby Help Centers")
for _, row in data.iterrows():
st.markdown(f"**{row['Name']}** - {row['Location']}")
st.markdown(f"📞 {row['Phone']}")
st.write("")

# Search help centers

st.subheader("🔍 Search Help Centers")
query = st.text_input("Enter center name to search")
if query:
results = data[data["Name"].str.contains(query, case=False, na=False)]
if not results.empty:
for _, row in results.iterrows():
st.markdown(f"**{row['Name']}** - {row['Location']}")
st.markdown(f"📞 {row['Phone']}")
else:
st.warning("No help center found with that name.")

# Comments & experiences

st.subheader("💬 Comments & Experiences")
with st.form("comment_form"):
name = st.text_input("Your Name")
comment = st.text_area("Your Experience or Comment")
submitted = st.form_submit_button("Submit")

```
if submitted and name and comment:
    st.success("✅ Thank you for sharing your experience!")
```

# Sample comments (static)

st.write("### Recent Comments")
sample_comments = [
{"name": "Ada", "comment": "Mirabel Centre helped me feel safe again."},
{"name": "Zainab", "comment": "The volunteers were so kind and supportive."},
{"name": "Ngozi", "comment": "I was guided through the process of getting help."},
]

for item in sample_comments:
st.markdown(f"**{item['name']}**: {item['comment']}")

# Contact details

st.divider()
st.write("📧 **Contact Us:** [womenhelpline.ng@gmail.com](mailto:womenhelpline.ng@gmail.com)")
st.write("📞 **Support Line:** +234 815 577 0000")
