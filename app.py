import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter and Material Density Checker",
    page_icon="⚙️",
    layout="centered"
)

# Header
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

st.markdown("""
### Student Information
**Full Name:** Muhammad aqib  
**Roll Number:** 25-ME-103
""")

st.markdown("---")

# =========================
# UNIT CONVERTER SECTION
# =========================
st.header("🔄 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Force", "Pressure", "Temperature"]
)

# Length Converter
if conversion_type == "Length":
    st.subheader("Length Converter")

    meter_value = st.number_input("Enter value in meters", min_value=0.0)

    cm = meter_value * 100
    mm = meter_value * 1000
    inch = meter_value * 39.3701
    feet = meter_value * 3.28084

    st.success(f"{meter_value} m = {cm:.2f} cm")
    st.success(f"{meter_value} m = {mm:.2f} mm")
    st.success(f"{meter_value} m = {inch:.2f} inches")
    st.success(f"{meter_value} m = {feet:.2f} feet")

# Force Converter
elif conversion_type == "Force":
    st.subheader("Force Converter")

    newton_value = st.number_input("Enter value in Newton", min_value=0.0)

    kn = newton_value / 1000
    dyne = newton_value * 100000
    lbf = newton_value * 0.224809

    st.success(f"{newton_value} N = {kn:.4f} kN")
    st.success(f"{newton_value} N = {dyne:.2f} dyne")
    st.success(f"{newton_value} N = {lbf:.4f} pound-force")

# Pressure Converter
elif conversion_type == "Pressure":
    st.subheader("Pressure Converter")

    pa_value = st.number_input("Enter value in Pascal", min_value=0.0)

    kpa = pa_value / 1000
    bar = pa_value / 100000
    atm = pa_value / 101325

    st.success(f"{pa_value} Pa = {kpa:.4f} kPa")
    st.success(f"{pa_value} Pa = {bar:.6f} bar")
    st.success(f"{pa_value} Pa = {atm:.6f} atm")

# Temperature Converter
elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")

    celsius = st.number_input("Enter temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"{celsius} °C = {fahrenheit:.2f} °F")
    st.success(f"{celsius} °C = {kelvin:.2f} K")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================
st.header("🧱 Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Concrete": 2400,
    "Wood": 700
}

selected_material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[selected_material]

st.info(f"Density of {selected_material} = {density} kg/m³")

# Volume and Mass Calculation
st.subheader("Mass Calculator")

volume = st.number_input(
    "Enter Volume (m³)",
    min_value=0.0,
    value=1.0
)

mass = density * volume

st.success(f"Mass = {mass:.2f} kg")

st.markdown("---")

# Footer
st.caption("Developed using Streamlit and GitHub for Mechanical Engineering Application")
