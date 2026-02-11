import streamlit as st
import qrcode
from utils import password_strength, suggest_password
from PIL import Image
import io

st.set_page_config(page_title="WiFi QR Generator", page_icon="📶")

st.title("📶 WiFi QR Code Generator (AI Powered)")
st.write("Generate secure WiFi QR codes instantly")

ssid = st.text_input("WiFi Name (SSID)")
password = st.text_input("Password", type="password")
security = st.selectbox("Security Type", ["WPA", "nopass"])

if password:
    strength = password_strength(password)
    if strength == "Weak":
        st.error(f"Password Strength: {strength}")
        st.info(f"Suggested Password: {suggest_password()}")
    elif strength == "Medium":
        st.warning(f"Password Strength: {strength}")
    else:
        st.success(f"Password Strength: {strength}")

if st.button("Generate QR Code"):
    if ssid:
        wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
        qr = qrcode.make(wifi_data)

        buf = io.BytesIO()
        qr.save(buf)
        buf.seek(0)

        img = Image.open(buf)
        st.image(img, caption="Scan to Connect 📲")

        st.download_button(
            "Download QR Code",
            data=buf,
            file_name="wifi_qr.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter WiFi name")
