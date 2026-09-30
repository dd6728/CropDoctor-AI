import streamlit as st
import torch
from PIL import Image
from transformers import ViTImageProcessor, ViTForImageClassification

st.set_page_config(
    page_title="CropDoctorAI",
    page_icon="🌱"
)

st.title("🌱 CropDoctorAI")
st.write("AI-based Preliminary Crop Health Screening")

MODEL_ID = "ayerr/plant-disease-classification"
MODEL_SUBFOLDER = "ayerr/plant-disease-classification"


@st.cache_resource
def load_model():

    processor = ViTImageProcessor.from_pretrained(
        MODEL_ID,
        subfolder=MODEL_SUBFOLDER
    )

    model = ViTForImageClassification.from_pretrained(
        MODEL_ID,
        subfolder=MODEL_SUBFOLDER
    )

    model.eval()

    return processor, model


# Load AI model
try:
    processor, model = load_model()
    st.success("✅ AI model loaded successfully!")

except Exception as e:
    st.error("❌ AI model loading failed.")
    st.exception(e)
    st.stop()


# Language
language = st.radio(
    "🌐 Select Language / மொழியை தேர்வு செய்யவும்",
    ["English", "தமிழ்"]
)


# Upload image
uploaded_file = st.file_uploader(
    "📷 Upload Crop Image / பயிர் படத்தை பதிவேற்றவும்",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Crop Image",
        use_container_width=True
    )

    if st.button("🔍 Analyze Crop", type="primary"):

        with st.spinner("🔬 Analyzing crop..."):

            inputs = processor(
                images=image,
                return_tensors="pt"
            )

            with torch.no_grad():
                outputs = model(**inputs)

            probabilities = torch.softmax(
                outputs.logits,
                dim=-1
            )

            predicted_class = torch.argmax(
                probabilities,
                dim=-1
            ).item()

            label = model.config.id2label[
                predicted_class
            ]

            confidence = probabilities[
                0,
                predicted_class
            ].item()


        st.divider()

        # Result
        if language == "தமிழ்":

            st.subheader("🌱 பயிர் பெயர்")
            st.write("இந்த model பயிர் பெயரை தனியாக கண்டறியாது.")

            st.subheader("🦠 நோய் நிலை")
            st.write(
                "ஆரோக்கியமானது"
                if label.lower() == "healthy"
                else "நோய் அறிகுறிகள் இருக்கலாம்"
            )

            st.subheader("💊 பரிந்துரைக்கப்படும் தீர்வு")

            if label.lower() == "healthy":
                st.write(
                    "🌱 தொடர்ந்து செடியை கண்காணிக்கவும். "
                    "சரியான நீர்ப்பாசனம் மற்றும் பராமரிப்பை தொடரவும்."
                )
            else:
                st.write(
                    "⚠️ பாதிக்கப்பட்ட பகுதிகளை கண்காணிக்கவும். "
                    "சரியான சிகிச்சைக்காக வேளாண்மை நிபுணரை அணுகவும்."
                )

            st.subheader("📊 நம்பகத்தன்மை")
            st.write(f"{confidence * 100:.2f}%")

        else:

            st.subheader("🌱 Crop Name")
            st.write(
                "This model does not identify the crop name separately."
            )

            st.subheader("🦠 Disease Status")

            if label.lower() == "healthy":
                st.write("Healthy")
            else:
                st.write("Possible disease symptoms detected")

            st.subheader("💊 Suggested Solution")

            if label.lower() == "healthy":
                st.write(
                    "Continue regular crop monitoring, "
                    "proper watering and general plant care."
                )
            else:
                st.write(
                    "Monitor affected areas and consult "
                    "an agricultural expert for appropriate treatment."
                )

            st.subheader("📊 Confidence")
            st.write(f"{confidence * 100:.2f}%")

        st.info(
            "⚠️ This is preliminary AI screening only, "
            "not a guaranteed diagnosis."
        )

else:

    st.info(
        "📷 Upload an image to start diagnosis."
    )
