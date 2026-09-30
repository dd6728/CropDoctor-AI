import streamlit as st

st.set_page_config(
    page_title="CropDoctorAI",
    page_icon="🌱"
)

st.title("🌱 CropDoctorAI")
st.subheader("Plant Disease Detection and Solution")

st.write("Select a plant and disease to get the solution.")

plant = st.selectbox(
    "🌱 Select Plant",
    ["Tomato", "Rice", "Potato", "Chilli"]
)

if plant == "Tomato":
    diseases = ["Early Blight", "Late Blight"]

elif plant == "Rice":
    diseases = ["Rice Blast", "Bacterial Leaf Blight"]

elif plant == "Potato":
    diseases = ["Early Blight", "Late Blight"]

else:
    diseases = ["Leaf Curl"]

disease = st.selectbox(
    "🦠 Select Disease",
    diseases
)

if disease == "Early Blight":
    solution = "Remove infected leaves and follow recommended disease-management practices."

elif disease == "Late Blight":
    solution = "Remove affected plant parts and follow recommended treatment."

elif disease == "Rice Blast":
    solution = "Use healthy seeds and follow recommended disease-management practices."

elif disease == "Bacterial Leaf Blight":
    solution = "Use resistant varieties and maintain proper field sanitation."

else:
    solution = "Monitor the plant regularly and manage insect vectors."

st.write("### 🌱 Plant Name")
st.write(plant)

st.write("### 🦠 Disease Name")
st.write(disease)

st.write("### 💊 Solution")
st.success(solution)
