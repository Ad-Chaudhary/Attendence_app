import streamlit as st

st.title("BMI Calculator & Health Advisor")
unit = st.radio("Select Height Unit:", ["Meters", "Feet & Inches"], horizontal=True)

col1, col2 = st.columns(2)

if unit == "Meters":
    height_m = col1.number_input("Enter height in meters", min_value=0.1, max_value=3.0, value=1.70, step=0.01, format="%.2f")
else:
    feet = col1.number_input("Feet", min_value=1, max_value=8, value=5, step=1)
    inches = col1.number_input("Inches", min_value=0, max_value=11, value=7, step=1)
    height_m = (feet * 0.3048) + (inches * 0.0254)


weight = col2.number_input("Enter weight in kg", min_value=1.0, max_value=300.0, value=65.0, step=0.5, format="%.1f")


c1, c2, c3 = st.columns([1, 1, 2])

if c3.button("Calculate BMI"):
    if height_m > 0 and weight > 0:
        bmi = weight / (height_m ** 2)
        min_healthy_weight = 18.5 * (height_m ** 2)
        max_healthy_weight = 24.9 * (height_m ** 2)

        st.markdown("---")
        st.subheader(f"Your BMI: **{bmi:.2f}**")

        if bmi < 18.5:
            st.info("Category: **Underweight**")
            weight_to_gain = min_healthy_weight - weight
            st.warning(f" **Suggestion:** You need to **gain around {weight_to_gain:.1f} kg** to reach a healthy weight (at least {min_healthy_weight:.1f} kg).")
            
        elif 18.5 <= bmi < 24.9:
            st.success("Category: **Normal / Healthy Weight** 🎉")
            st.write(f" Great job! Your weight is in the optimal range ({min_healthy_weight:.1f} kg – {max_healthy_weight:.1f} kg). Keep up a balanced diet and regular activity.")
            
        elif 25 <= bmi < 29.9:
            st.warning("Category: **Overweight**")
            weight_to_lose = weight - max_healthy_weight
            st.error(f" **Suggestion:** You need to **lose around {weight_to_lose:.1f} kg** to reach a normal weight (target: under {max_healthy_weight:.1f} kg).")
            
        else:
            st.error("Category: **Obesity**")
            weight_to_lose = weight - max_healthy_weight
            st.error(f" **Suggestion:** You need to **lose around {weight_to_lose:.1f} kg** to return to a healthy weight range (target: under {max_healthy_weight:.1f} kg).")

        st.caption(f" Healthy target weight range for your height: **{min_healthy_weight:.1f} kg – {max_healthy_weight:.1f} kg**")
        
    else:
        st.error("Please enter valid positive values.")