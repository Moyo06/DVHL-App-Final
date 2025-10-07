import streamlit as st
import pandas as pd
from datetime import datetime

# --- PAGE CONFIG ---

st.set_page_config(page_title="Domestic Violence Helpline Locator", page_icon="📞", layout="wide")

# --- SIDEBAR ---

st.sidebar.header("🚨 Emergency Contacts")
st.sidebar.markdown("""
**Call Emergency:** 112
**Helpline:** +234-815-577-0000
**Email:** [womenhelpng@gmail.com](mailto:womenhelpng@gmail.com)
""")

st.sidebar.info("If you or someone you know is in danger, please reach out immediately.")

# --- PAGE HEADER ---

st.title("Domestic Violence Helpline Locator")
st.caption("Find verified help centers, reach out instantly, and share your experience to inspire others.")

# --- HELP CENTERS DATA ---

help_centers = pd.DataFrame([
{"Center": "Mirabel Centre", "Location": "LASUTH, Ikeja, Lagos", "Phone": "+2348155770000"},
{"Center": "Project Alert", "Location": "Ikeja, Lagos", "Phone": "+2348180091072"},
{"Center": "WARDC", "Location": "Yaba, Lagos", "Phone": "+2347012345678"},
{"Center": "Women’s Rights Watch", "Location": "Enugu", "Phone": "+2348032221111"},
])

# --- SECTION 1: HELP CENTERS ---

st.subheader("📍 Nearby Help Centers")
st.dataframe(help_centers, use_container_width=True)

# --- SECTION 2: SOS MESSAGE ---

st.subheader("🚨 Send SOS Message")
with st.form("sos_form"):
st.subheader("💬 Comments & Experiences")
st.write("Share your experience or advice to help others feel supported.")

name = st.text_input("Your Name")
comment = st.text_area("Your Comment")

if st.button("Submit Comment"):
    if name and comment:
        with open("comments.csv", "a") as f:
            f.write(f"{name}: {comment}\n")
        st.success("Thank you for sharing your experience! 💜")
    else:
        st.warning("Please fill in both fields before submitting.")

location = st.text_input("Your Location")
situation = st.text_area("Describe the situation briefly")
submitted_sos = st.form_submit_button("Send SOS")
if submitted_sos:
if name and location and situation:
st.success("🚨 SOS sent successfully! A support agent will reach out shortly.")
else:
st.warning("Please fill in all fields before submitting.")

# --- SECTION 3: FEEDBACK / COMMENTS ---

st.subheader("💬 Comments & Experiences")

# File to store comments

COMMENTS_FILE = "comments.csv"

# Load existing comments

try:
comments_df = pd.read_csv(COMMENTS_FILE)
except FileNotFoundError:
comments_df = pd.DataFrame(columns=["Name", "Comment", "Timestamp"])

# Form for new comment

with st.form("comment_form"):
    st.subheader("💬 Comments & Experiences")
    st.write("Share your experience or advice to help others feel supported.")

    name = st.text_input("Your Name")
    comment = st.text_area("Your Comment")

    submitted = st.form_submit_button("Submit Comment")

    if submitted:
        if name and comment:
            with open("comments.csv", "a") as f:
                f.write(f"{name}: {comment}\n")
            st.success("Thank you for sharing your experience! 💜")
        else:
            st.warning("Please fill in both fields before submitting.")


```
if submit_comment:
    if name and comment:
        new_entry = pd.DataFrame({
            "Name": [name],
            "Comment": [comment],
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        })
        comments_df = pd.concat([comments_df, new_entry], ignore_index=True)
        comments_df.to_csv(COMMENTS_FILE, index=False)
        st.success("✅ Comment posted successfully!")
    else:
        st.warning("Please enter both your name and comment.")
```

# Display previous comments

if not comments_df.empty:
st.write("### 🗣️ Previous Comments")
for _, row in comments_df.iterrows():
st.markdown(f"**{row['Name']}** *({row['Timestamp']})*")
st.write(f"> {row['Comment']}")
st.markdown("---")
else:
st.info("No comments yet. Be the first to share your thoughts.")

# --- FOOTER ---

st.markdown("---")
st.caption("Developed by Moyo Iyanda | Domestic Violence Helpline Locator (DVHL)")
