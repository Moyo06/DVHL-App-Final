import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import datetime

# ------------------ PAGE CONFIG ------------------

st.set_page_config(page_title="Domestic Violence Helpline Locator", page_icon="📞", layout="wide")

st.title("📞 Domestic Violence Helpline Locator")
st.markdown("Find help centers near you, share your experience, or send an SOS alert.")

# ------------------ LOAD HELP CENTERS ------------------

data = {
"Center Name": ["Mirabel Centre", "Project Alert on Violence Against Women", "WARIF Centre"],
"Address": ["LASUTH, Ikeja, Lagos", "PO Box 15456, Ikeja, Lagos", "6 Turton Street, Lagos"],
"Phone": ["08155770000", "08180091072", "08092100009"],
"Latitude": [6.6018, 6.6010, 6.5498],
"Longitude": [3.3515, 3.3457, 3.3675],
}
centers = pd.DataFrame(data)

# ------------------ SEARCH BAR ------------------

st.sidebar.header("🔍 Search for a Help Center")
query = st.sidebar.text_input("Enter a center name or location")

if not query:
st.sidebar.info("Type a name or location to begin your search.")
else:
results = centers[centers["Center Name"].str.contains(query, case=False)]
if not results.empty:
st.sidebar.success(f"Found {len(results)} center(s):")
st.sidebar.dataframe(results[["Center Name", "Address", "Phone"]])
else:
st.sidebar.warning("No results found. Try another keyword.")

# ------------------ MAP ------------------

st.header("🗺️ Nearby Help Centers")
m = folium.Map(location=[6.6, 3.35], zoom_start=11)
for _, row in centers.iterrows():
folium.Marker(
[row["Latitude"], row["Longitude"]],
popup=f"{row['Center Name']}<br>{row['Address']}<br>📞 {row['Phone']}",
tooltip=row["Center Name"],
icon=folium.Icon(color="purple", icon="heart"),
).add_to(m)
st_folium(m, width=700, height=400)

# ------------------ COMMENT SECTION ------------------

st.subheader("💬 Share Your Experience")
comment_file = "comments.csv"

if "comments" not in st.session_state:
try:
st.session_state.comments = pd.read_csv(comment_file).to_dict("records")
except FileNotFoundError:
st.session_state.comments = []

with st.form("comment_form", clear_on_submit=True):
name = st.text_input("Your Name")
message = st.text_area("Your Comment or Experience")
submitted = st.form_submit_button("Submit Comment")

```
if submitted:
    if name and message:
        new_comment = {"name": name, "message": message, "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
        st.session_state.comments.append(new_comment)
        pd.DataFrame(st.session_state.comments).to_csv(comment_file, index=False)
        st.success("Your comment has been submitted!")
    else:
        st.error("Please fill in all fields.")
```

if st.session_state.comments:
for c in reversed(st.session_state.comments):
st.write(f"**{c['name']}** ({c['time']}): {c['message']}")

# ------------------ SOS SECTION ------------------

st.subheader("🚨 Emergency SOS Alert")
st.warning("If you're in immediate danger, call the nearest helpline or submit an SOS below.")

sos_file = "sos_reports.csv"
if "sos_reports" not in st.session_state:
try:
st.session_state.sos_reports = pd.read_csv(sos_file).to_dict("records")
except FileNotFoundError:
st.session_state.sos_reports = []

with st.form("sos_form", clear_on_submit=True):
location = st.text_input("Enter your location (e.g., Ikeja, Lagos)")
phone = st.text_input("Your phone number (optional)")
sos_button = st.form_submit_button("Send SOS 🚨")

```
if sos_button:
    if location:
        report = {
            "location": location,
            "phone": phone,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        st.session_state.sos_reports.append(report)
        pd.DataFrame(st.session_state.sos_reports).to_csv(sos_file, index=False)
        st.success("🚨 SOS alert sent successfully! Help is on the way.")
    else:
        st.error("Please enter your location before sending SOS.")
```

# ------------------ CONTACT INFO ------------------

st.markdown("---")
st.markdown("📧 **Email:** [support@dvhlapp.ng](mailto:support@dvhlapp.ng) | ☎️ **Helpline:** 0815-577-0000")
st.markdown("© 2025 Domestic Violence Helpline Locator | Built with ❤️ in Nigeria")
