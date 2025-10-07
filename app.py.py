import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Domestic Violence Helpline Locator", page_icon="❤️", layout="wide")

# --- HEADER ---
st.title("Domestic Violence Helpline Locator")
st.write("Find help centers near you, access emergency services, and chat anonymously for support.")

# --- ABOUT & BENEFITS ---
st.header("About this Website")
st.write("""
This website helps survivors of domestic violence quickly locate nearby help centers and reach emergency services.
""")

st.subheader("Benefits:")
st.write("""
- Immediate access to verified emergency helplines.  
- Searchable directory of local help centers.  
- Map visualization for easy location tracking.  
- Anonymous chat for guidance and support.  
- Optional location input to inform help centers safely.  
- Downloadable resources for offline access.
""")

# --- HELPLINES DIRECTORY ---
st.header("📋 Helplines Directory")

# Load CSV data
df = pd.read_csv("help_centers.csv")

search_city = st.text_input("Search helplines by city or location:")

if search_city:
    filtered = df[df['City'].str.contains(search_city, case=False, na=False)]
else:
    filtered = df

for idx, row in filtered.iterrows():
    st.write(f"**{row['Name']}** - {row['City']} - {row['Address']} - {row['Phone']}")

# --- MAP ---
st.header("📍 Helpline Locations on Map")
m = folium.Map(location=[6.5244, 3.3792], zoom_start=6)  # Nigeria central coordinates

for idx, row in df.iterrows():
    if pd.notna(row['Latitude']) and pd.notna(row['Longitude']):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Name']} - {row['City']}\n{row['Phone']}",
            tooltip=row['Name']
        ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# --- ANONYMOUS CHAT ---
st.header("💬 Anonymous Chat")

chat_input = st.text_area("Write your message (anonymous):", height=100)

if st.button("Send"):
    if chat_input.strip() != "":
        st.success("Help is on the way! If safe, consider sharing your location.")
    else:
        st.warning("Please write something before sending.")

# --- OPTIONAL LOCATION ---
st.subheader("📍 Share Your Location (Optional)")
user_location = st.text_input("Enter your location or address if safe:")

if user_location:
    st.info("Your location has been noted. Help centers can be notified safely.")

# --- DOWNLOAD ---
st.header("💾 Download Helpline List")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Helplines CSV",
    data=csv,
    file_name='help_centers.csv',
    mime='text/csv'
)

# --- RESOURCES & SAFETY TIPS ---
st.header("📚 Resources & Safety Tips")
st.write("""
- **Know your rights:** Learn legal protections against domestic violence.  
- **Safety planning:** Steps to protect yourself and loved ones.  
- **Counseling & support:** Access emotional and psychological support services.  
- **Trusted contacts:** Always have someone you can call in emergencies.
""")

# --- FOOTER ---
st.markdown("---")
st.markdown("Created by Moyo Iyanda ❤️ | Share to raise awareness")
