import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import csv
import os
from datetime import datetime

# ---------------- Page config ----------------

st.set_page_config(page_title="DVHL - Domestic Violence Helpline Locator",
page_icon="📞",
layout="wide")

# ---------------- Header / Sidebar ----------------

st.title("📱 Domestic Violence Helpline Locator")
st.write("Find verified help centers near you, send an SOS if needed, and share experiences to help others.")

st.sidebar.header("🚨 Emergency Contacts")
st.sidebar.markdown("[📞 Call Emergency (Nigeria - 112)](tel:+234112)")
st.sidebar.markdown("[📞 Helpline: +2348155770000](tel:+2348155770000)")
st.sidebar.markdown("[✉️ Email Support](mailto:support@dvhl.org.ng)")
st.sidebar.markdown("---")
st.sidebar.info("If you are in immediate danger, call emergency services first. If safe, use the SOS form below.")

st.divider()

# ---------------- Helplines (built-in dataset) ----------------

helplines = [
{"Name": "Mirabel Centre", "City": "Lagos", "Address": "LASUTH, Ikeja", "Phone": "+2348155770000", "Latitude": 6.6018, "Longitude": 3.3515},
{"Name": "Project Alert on Violence Against Women", "City": "Lagos", "Address": "PO Box 15456, Ikeja", "Phone": "+2348180091072", "Latitude": 6.6051, "Longitude": 3.3490},
{"Name": "WARIF (Women at Risk International Foundation)", "City": "Lagos", "Address": "Yaba", "Phone": "+2348092100009", "Latitude": 6.5174, "Longitude": 3.3763},
{"Name": "Cece Yara Foundation", "City": "Lagos", "Address": "Ikeja", "Phone": "+2348008008001", "Latitude": 6.5850, "Longitude": 3.3450},
]

df = pd.DataFrame(helplines)

# Search/filter UI

st.header("📋 Helplines Directory")
q = st.text_input("Search helplines by city, name or address (leave empty to show all):")

def filter_helplines(df_, query):
if not query:
return df_
qlow = query.lower()
mask = df_.apply(
lambda r: qlow in str(r.get("Name","")).lower()
or qlow in str(r.get("City","")).lower()
or qlow in str(r.get("Address","")).lower(),
axis=1
)
return df_[mask]

filtered = filter_helplines(df, q)

if filtered.empty:
st.warning("No helplines match your search.")
else:
for _, r in filtered.iterrows():
with st.expander(f"{r['Name']} — {r['City']}"):
st.write(f"**Address:** {r['Address']}")
phone = r.get("Phone","")
if phone:
# produce a tel: link with digits only and leading +
digits = "".join(ch for ch in phone if ch.isdigit())
tel = f"+{digits}" if not phone.strip().startswith("+") else phone.strip()
st.markdown(f"**Phone:** [📞 {phone}](tel:{tel})")
else:
st.write("**Phone:** Not available")
st.markdown("[✉️ Email Support](mailto:support@dvhl.org.ng)")

# Download helplines CSV

csv_bytes = df.to_csv(index=False).encode("utf-8")
st.download_button("💾 Download Helplines CSV", data=csv_bytes, file_name="helplines.csv", mime="text/csv")

st.divider()

# ---------------- Map ----------------

st.header("📍 Helpline Locations on Map")

# center map on average location if available

if df["Latitude"].notna().any() and df["Longitude"].notna().any():
avg_lat = float(df["Latitude"].dropna().astype(float).mean())
avg_lon = float(df["Longitude"].dropna().astype(float).mean())
else:
avg_lat, avg_lon = 6.5244, 3.3792  # Lagos fallback

m = folium.Map(location=[avg_lat, avg_lon], zoom_start=10, tiles="CartoDB positron")

for _, r in filtered.iterrows():
lat = r.get("Latitude")
lon = r.get("Longitude")
if pd.notna(lat) and pd.notna(lon):
try:
folium.Marker(
location=[float(lat), float(lon)],
popup=f"{r.get('Name','')}<br/>{r.get('Address','')}<br/>📞 {r.get('Phone','')}",
tooltip=r.get("Name",""),
icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)
except Exception:
continue

st_folium(m, width="100%", height=450)

st.divider()

# ---------------- SOS Form (writes to sos_reports.csv) ----------------

st.header("🚨 Send SOS (Optional)")
with st.form("sos_form"):
sos_name = st.text_input("Your name (optional)")
sos_location = st.text_input("Your location (only if safe)")
sos_message = st.text_area("Briefly describe the situation")
send_sos = st.form_submit_button("Send SOS")

```
if send_sos:
    if not sos_message.strip():
        st.warning("Please describe the situation briefly before sending.")
    else:
        sos_file = "sos_reports.csv"
        file_exists = os.path.exists(sos_file)
        with open(sos_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Timestamp","Name","Location","Message"])
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "Timestamp": datetime.utcnow().isoformat(),
                "Name": sos_name or "Anonymous",
                "Location": sos_location or "",
                "Message": sos_message.strip()
            })
        st.success("✅ SOS submitted. If this is an emergency, call your local emergency number immediately.")
```

st.divider()

# ---------------- Comments (persist to comments.csv) ----------------

st.header("💬 Comments & Community Voices")

comments_file = "comments.csv"
if not os.path.exists(comments_file):
# create file with sample comments
with open(comments_file, "w", newline="", encoding="utf-8") as f:
writer = csv.DictWriter(f, fieldnames=["Name","Comment","Timestamp"])
writer.writeheader()
writer.writerow({"Name":"Ada","Comment":"This app helped me find a center quickly.","Timestamp":datetime.utcnow().isoformat()})
writer.writerow({"Name":"Tolu","Comment":"Please add more centers across states.","Timestamp":datetime.utcnow().isoformat()})

# load comments

comments = []
with open(comments_file, "r", encoding="utf-8") as f:
reader = csv.DictReader(f)
for row in reader:
comments.append(row)

# comment submission form

with st.form("comment_form"):
commenter = st.text_input("Name (optional)")
comment_text = st.text_area("Share your experience or a supportive message")
post = st.form_submit_button("Post Comment")
if post:
if not comment_text.strip():
st.warning("Please write something before posting.")
else:
with open(comments_file, "a", newline="", encoding="utf-8") as f:
writer = csv.DictWriter(f, fieldnames=["Name","Comment","Timestamp"])
writer.writerow({"Name": commenter or "Anonymous", "Comment": comment_text.strip(), "Timestamp": datetime.utcnow().isoformat()})
st.success("✅ Your comment was posted.")
st.experimental_rerun()

# display comments (most recent first)

if comments:
st.subheader("Recent messages")
for row in reversed(comments[-50:]):  # show up to last 50
name = row.get("Name","Anonymous")
text = row.get("Comment","")
ts = row.get("Timestamp","")
st.markdown(f"**{name}** — *{ts}*")
st.write(text)
st.markdown("---")
else:
st.info("No comments yet. Be the first to share a message of hope.")

st.divider()

# ---------------- Resources & Footer ----------------

st.header("📚 Resources & Safety Tips")
with st.expander("Know your rights"):
st.write("Learn about legal protections, contact local legal aid organizations for assistance.")
with st.expander("Safety planning"):
st.write("Consider a safety plan: emergency bag, trusted contacts, and safe exits.")
with st.expander("Counselling & support"):
st.write("Seek counseling from verified organizations and support lines.")

st.markdown("---")
st.markdown("<div style='text-align:center; color: #666;'>Created by <strong>Moyo Iyanda</strong> ❤️ | Share to raise awareness</div>", unsafe_allow_html=True)
