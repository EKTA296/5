import streamlit as st

st.set_page_config(
    page_title="Microplastic Detection AI",
    layout="wide",
    page_icon="🏠",
)

# ---------- Styling ----------
st.markdown("""
<style>
.hero {
    padding: 2rem 2rem 1.5rem 2rem;
    border-radius: 16px;
    background: linear-gradient(135deg, #0b3d91 0%, #1f8fd6 100%);
    color: black;
    margin-bottom: 1.5rem;
}
.hero h1 { margin-bottom: 0.3rem; }
.hero p { font-size: 1.05rem; opacity: 0.9; }
.card {
    background: #f7f9fc;
    border: 1px solid #e3e8ef;
    border-radius: 12px;
    padding: 1.2rem;
    height: 100%;
}
.card h4 { margin-top: 0; }
.metric-box {
    background: #ffffff;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #e3e8ef;
}
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>🌊 AI-Based Microplastic Detection</h1>
    <p>Detecting microplastics in aquatic environments in real-time using YOLOv8 deep learning.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Nav callout ----------
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### 📌 About this project
    Microplastics are tiny plastic particles (< 5mm) that pollute water bodies and harm aquatic
    ecosystems and human health. Manually identifying them under a microscope is slow and
    error-prone. This project trains a **YOLOv8 object detection model** to automatically spot
    microplastic particles in water sample images, giving researchers and citizen scientists a
    faster way to screen samples.
    """)
    st.info("👉 Head to **Detect** in the sidebar to upload an image and run detection.", icon="🔍")



st.divider()


st.caption(
    "🔬 Under the hood: trained on a custom-labeled dataset of aquatic microplastic images "
    "using an 80/20 train-validation split, fine-tuned from YOLOv8n for fast CPU inference."
)

st.divider()
st.caption("Built as an academic project demonstrating AI-assisted environmental monitoring.")