import streamlit as st

# --- APP TITLE ---
st.set_page_config(page_title="Unit Converter", page_icon="📏")
st.title("📏 Unit Converter")
st.markdown("Convert between different units of measurement!")

# --- UNIT CONVERSION DATA ---
units = {
    "Length": {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254,
    },
    "Weight": {
        "Grams": 1.0,
        "Kilograms": 1000.0,
        "Pounds": 453.592,
        "Ounces": 28.3495,
    },
    "Temperature": {
        "Celsius": {
            "to_Celsius": lambda x: x,
            "from_Celsius": lambda x: x,
        },
        "Fahrenheit": {
            "to_Celsius": lambda x: (x - 32) * 5 / 9,
            "from_Celsius": lambda x: x * 9 / 5 + 32,
        },
        "Kelvin": {
            "to_Celsius": lambda x: x - 273.15,
            "from_Celsius": lambda x: x + 273.15,
        },
    },
}

# --- SIDEBAR FOR CATEGORY SELECTION ---
st.sidebar.header("Select Category")
category = st.sidebar.selectbox("Choose a category:", list(units.keys()))

if category != "Temperature":
    # --- UNIT SELECTION ---
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit:", list(units[category].keys()))
    with col2:
        to_unit = st.selectbox("To Unit:", list(units[category].keys()))

    # --- INPUT VALUE ---
    value = st.number_input(f"Enter value in {from_unit}:", value=1.0)

    # --- CONVERSION LOGIC ---
    base_value = value * units[category][from_unit]
    converted_value = base_value / units[category][to_unit]

    # --- DISPLAY RESULT ---
    st.subheader("Result:")
    st.markdown(f"{value} {from_unit} = **{converted_value:.4f} {to_unit}**")

else:
    # --- TEMPERATURE CONVERSION ---
    col1, col2 = st.columns(2)
    with col1:
        from_temp = st.selectbox("From Unit:", list(units["Temperature"].keys()))
    with col2:
        to_temp = st.selectbox("To Unit:", list(units["Temperature"].keys()))

    # --- INPUT VALUE ---
    value = st.number_input(f"Enter value in {from_temp}:", value=0.0)

    # --- CONVERSION LOGIC ---
    celsius_value = units["Temperature"][from_temp]["to_Celsius"](value)
    converted_value = units["Temperature"][to_temp]["from_Celsius"](celsius_value)

    # --- DISPLAY RESULT ---
    st.subheader("Result:")
    st.markdown(f"{value} {from_temp} = **{converted_value:.4f} {to_temp}**")

# --- FOOTER ---
st.sidebar.markdown("Built with ❤️ using Streamlit")