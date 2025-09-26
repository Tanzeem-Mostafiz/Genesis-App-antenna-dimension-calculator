# Genesis Antenna Predictor

**Genesis Antenna Predictor** is a web-based tool developed as part of our undergraduate thesis and later written as a journal paper. It uses machine learning models trained on the Noah dataset to predict key microstrip patch antenna dimensions—such as patch width, patch length, and feedline width—directly from user-defined electrical specifications. Designed for the 37–40 GHz range, it provides fast, real-time predictions to support high-frequency antenna design and research.

Live Demo: [https://genesis-app.streamlit.app/](https://genesis-app.streamlit.app/)

---
## Authors
- **Tanzeem Mostafiz** – Developed the web application, contributed to model development, and co-authored the paper  
- **Anik Paul** – Contributed to research, model development and paper writing  
- **Tanvir Ibna Azaz** – Contributed to paper writing

## Features

1. You enter: Resonant Frequency, Minimum S11, and Bandwidth.

2. Genesis Wing model takes these 3 values and predicts the real (Z_real) and imaginary (Z_imag) parts of the antenna input impedance.

    - Think of it as a translator that converts your desired electrical performance into impedance characteristics.

3. Genesis Ray model takes:

    - Your original frequency & S11
    - The Z_real & Z_imag from Genesis Wing and predicts the physical design:
    - Patch Width
    - Patch Length
    - Feedline Width
    - Achievable Bandwidth

4. Streamlit simply collects your inputs, feeds them to both models in sequence, and displays the final predicted geometry + performance.

It’s basically a two-step AI pipeline: **Specs -> (Genesis Wing) -> Impedance -> (Genesis Ray) -> Geometry**


## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Tanzeem-Mostafiz/genesis-app-antenna-dimension-predictor
cd Genesis-App
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the virtual environment**
 - Windows
```bash
.venv\Scripts\activate
```
 - macOS/Linux
```bash
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage 
Run the Streamlit app locally:
```bash
streamlit run app.py
```

1. Enter your electrical specifications:
    - Resonant Frequency (GHz)
    - Minimum S11 (dB)
    - Desired Bandwidth (GHz)
2. Click Predict Antenna Parameters.
3. View predicted antenna geometry and achievable bandwidth.

## Folder Structure
```bash
Genesis-App/
│
├── assets/                # Images and icons used in the app
├── data/
│ ├── noah.csv              
├── model/                 # Trained machine learning models
│ ├── genesis_ray.pkl
│ └── genesis_wing.pkl
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License file
└── README.md              # This file

```

## Technologies Used
 - Python 3
 - Streamlit
 - Pandas, NumPy, Matplotlib, Plotly
 - CatBoost (machine learning models)

## License

This project is open-source and available under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
