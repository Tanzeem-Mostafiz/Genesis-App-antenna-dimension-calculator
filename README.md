# Genesis Antenna Predictor

**Genesis Antenna Predictor** is a web-based tool that predicts microstrip patch antenna dimensions based on user-defined electrical specifications. This app leverages machine learning models trained with the Noah dataset to provide **real-time predictions** for antenna design in the 37-40 GHz range.

Live Demo: [https://genesis-app.streamlit.app/](https://genesis-app.streamlit.app/)

---

## Features

1. Predicts **Z_real** and **Z_imaginary** of antenna input impedance using the **Genesis Wing** model.  
2. Predicts physical design parameters using the **Genesis Ray** model:
  - Patch Width  
  - Patch Length  
  - Feedline Width  
  - Achievable Bandwidth  
3. Dynamic interface built with **Streamlit**.   

---

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
