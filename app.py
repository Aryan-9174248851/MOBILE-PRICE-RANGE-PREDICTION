import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Mobile Price Range Prediction")
st.title("📱 Mobile Price Range Prediction")

st.write("Enter mobile specifications")

# Numeric inputs
battery_power = st.number_input("Battery Power (mAh)", 500, 6000, 800)
clock_speed = st.number_input("Clock Speed (GHz)", 0.5, 5.0, 1.0)
fc = st.number_input("Front Camera (MP)", 0, 50, 5)
int_memory = st.number_input("Internal Memory (GB)", 2, 512, 32)
m_dep = st.number_input("Mobile Depth (cm)", 0.1, 1.5, 0.5)
mobile_wt = st.number_input("Mobile Weight (grams)", 80, 300, 150)
n_cores = st.number_input("Number of Cores", 1, 16, 8)
pc = st.number_input("Primary Camera (MP)", 0, 108, 12)
px_height = st.number_input("Pixel Height", 0, 3000, 800)
px_width = st.number_input("Pixel Width", 0, 3000, 1200)
ram = st.number_input("RAM (MB)", 256, 12000, 2048)
sc_h = st.number_input("Screen Height (cm)", 5, 20, 14)
sc_w = st.number_input("Screen Width (cm)", 5, 20, 7)
talk_time = st.number_input("Talk Time (hours)", 2, 24, 10)

# Binary inputs
blue = st.selectbox("Bluetooth", [0, 1])
dual_sim = st.selectbox("Dual SIM", [0, 1])
four_g = st.selectbox("4G Support", [0, 1])
three_g = st.selectbox("3G Support", [0, 1])
touch_screen = st.selectbox("Touch Screen", [0, 1])
wifi = st.selectbox("WiFi", [0, 1])

# Prediction
if st.button("🔍 Predict Price Range"):
    input_data = np.array([[battery_power, blue, clock_speed, dual_sim,
                             fc, four_g, int_memory, m_dep, mobile_wt,
                             n_cores, pc, px_height, px_width, ram,
                             sc_h, sc_w, talk_time, three_g,
                             touch_screen, wifi]])

    prediction = model.predict(input_data)[0]

    price_map = {
        0: "Low Cost 📉",
        1: "Medium Cost 📊",
        2: "High Cost 📈",
        3: "Very High Cost 💎"
    }

    st.success(f"Predicted Price Range: **{price_map[prediction]}**")
