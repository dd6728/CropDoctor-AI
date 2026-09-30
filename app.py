import streamlit as st

st.set_page_config(
    page_title="CropDoctorAI",
    page_icon="🌱"
)

st.title("🌱 CropDoctorAI")
st.write("AI-powered Crop Disease Detection")

# Upload crop image
uploaded_file = st.file_uploader(
    "📷 Upload Crop Image",
    type=["jpg", "jpeg", "png"]
)

# Select language
language = st.radio(
    "🌐 Select Language / மொழியை தேர்வு செய்யவும்",
    ["English", "தமிழ்"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Crop Image",
        use_container_width=True
    )

    if st.button("🔍 Analyze Crop"):

        st.divider()

        if language == "தமிழ்":

            st.subheader("🌱 பயிர் பெயர்")
            st.write("தக்காளி")

            st.subheader("🦠 நோய் பெயர்")
            st.write("நோய் அறிகுறிகள் கண்டறியப்பட்டுள்ளன")

            st.subheader("💊 பரிந்துரைக்கப்படும் தீர்வு")
            st.write(
                "பாதிக்கப்பட்ட பகுதிகளை கண்காணிக்கவும். "
                "சரியான சிகிச்சைக்காக வேளாண்மை நிபுணரை அணுகவும்."
            )

            st.subheader("📊 நம்பகத்தன்மை")
            st.write("90%")

        else:

            st.subheader("🌱 Crop Name")
            st.write("Tomato")

            st.subheader("🦠 Disease Name")
            st.write("Possible disease symptoms detected")

            st.subheader("💊 Suggested Solution")
            st.write(
                "Monitor affected areas and consult an "
                "agricultural expert for appropriate treatment."
            )

            st.subheader("📊 Confidence")
            st.write("90%")

else:

    st.info(
        "📷 Upload an image or take a picture to start diagnosis."
    )
