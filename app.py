# app.py
import streamlit as st
import pickle
import numpy as np
from pathlib import Path
import base64

# ==============================
# Load Models
# ==============================
@st.cache_resource
def load_models():
    with open("model/genesis_wing.pkl", "rb") as f:
        genesis_wing = pickle.load(f)
    with open("model/genesis_ray.pkl", "rb") as f:
        genesis_ray = pickle.load(f)
    return genesis_wing, genesis_ray

genesis_wing, genesis_ray = load_models()

# ==============================
# Streamlit Page Config
# ==============================
st.set_page_config(page_title="Genesis Antenna Predictor", page_icon="", layout="centered")

#===============================

# Simple background image from local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            opacity: 0.95;
        }}
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local("assets/background.png")

#===============================
# Display top-right image
def display_right_side(image_path, width=80, top_percent=40):
    """
    Display an image floating on the right side of the page.
    :param image_path: Path to image
    :param width: Width in pixels
    :param top_percent: Top position as percentage (0-100)
    """
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(f'''
        <img src="data:image/png;base64,{encoded}" 
        style="position: fixed; top: {top_percent}%; right: 50px; 
               width: {width}px; transform: translateY(-50%); z-index:1000;">
    ''', unsafe_allow_html=True)

display_right_side("assets/back.png", width=300, top_percent=33)  # vertically centered

# Display constant values box under the right-side image
def display_constants_box():
    constants_html = """
    <div style="
        position: fixed;
        top: 52%;
        right: 50px;
        width: 270px;
        background-color: rgba(0, 0, 0, 0.35);
        padding: 10px 0 10px 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 15px;
        line-height: 1.7;
        color: white;
        z-index: 1001;
    ">
        <b style='font-size: 16px'>Constant Values of the Antenna:</b><br><br>
        Substrate: Rogers RT5880 (εr)<br>
        Dielectric contant, εr: 2.2<br>
        Substrate Thickness: 0.254 mm<br>
        Substrate Width: 4.602 mm<br>
        Substrate Length: 3.996 mm<br>
        Ground Width: Full<br>
        Inset Width: 0.395 mm<br>
        Inset Length: 0.6 mm
    </div>
    """
    st.markdown(constants_html, unsafe_allow_html=True)

display_constants_box()


# ==============================

# Custom title
st.markdown("<h1 class='big-title'>Genesis Antenna Predictor <br><span style='font-size:30px; color:cyan;'>37 to 40 GHz Range</span></h1>", unsafe_allow_html=True)


# ==============================
# Input Fields
# ==============================

st.markdown("""
    <style>
    .big-title {
        font-size: 50px !important;
        font-weight: bold;
        color: #333333;
    }
    .custom-label {
        font-size:18px;
        margin-bottom:-58px; /* Pull input box closer */
        display:block;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Section heading with larger font
st.markdown(

    "<h3 style='font-size:22px; font-weight:bold; color: yellow; margin-bottom: 5px;'>Enter Electrical Specifications</h3>",
    unsafe_allow_html=True
)

# Resonant Frequency
st.markdown("<span class='custom-label'>Resonant Frequency (GHz)</span>", unsafe_allow_html=True)
freq = st.number_input(
    "",
    min_value=37.0, max_value=40.0,
    value=38.0, step=0.1, format="%.3f"
)

# Minimum S11
st.markdown("<span class='custom-label'>Minimum S11 (dB)</span>", unsafe_allow_html=True)
s11 = st.number_input(
    "",
    min_value=-60.0, max_value=-10.0,
    value=-20.0, step=0.1, format="%.3f"
)

# Desired Bandwidth
st.markdown("<span class='custom-label'>Desired Bandwidth (GHz)</span>", unsafe_allow_html=True)
bandwidth = st.number_input(
    "",
    min_value=0.1, max_value=10.0,
    value=1.0, step=0.1, format="%.3f"
)


# ==============================
# Prediction
# ==============================
if st.button("PREDICT DIMENSIONS"):
    # Step 1: Genesis Wing predicts Z_real & Z_imag
    z_pred = genesis_wing.predict(np.array([[freq, s11, bandwidth]]))
    z_real, z_imag = z_pred[0]

    # Step 2: Genesis Ray predicts geometry & achievable bandwidth
    geom_pred = genesis_ray.predict(np.array([[freq, s11, z_real, z_imag]]))
    patch_length, patch_width, feed_width, final_bw = geom_pred[0]

    # ==============================
    # Show Results in a clean table
    # ==============================
    st.success("Prediction Complete ✅")

    st.markdown("""
        <style>
        .clean-table {
            border-collapse: collapse;
            margin-top: 1px;
        }
        .clean-table td {
            padding: 4px 16px;
            color: white;
            font-size: 16.5px;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <table class="clean-table">
        <tr><td>Patch Length:</td><td>{patch_length:.4f} mm</td></tr>
        <tr><td>Patch Width:</td><td>{patch_width:.4f} mm</td></tr>
        <tr><td>Feedline Width:</td><td>{feed_width:.4f} mm</td></tr>
        <tr><td>Achievable Bandwidth:</td><td>{final_bw:.4f} GHz</td></tr>
    </table>
    """, unsafe_allow_html=True)
