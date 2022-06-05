import streamlit as st
import math
st.set_page_config(page_title="This is my page", layout="wide")

#st.title Използваме за да направим заглавие на нашата страница

st.title("Beam Divergence")
st.subheader("Gaussian Beams Calculator")


#полета за въвеждане на числа


left_column,right_column = st.columns(2)
with left_column:

    a = st.number_input("Axial Distance, z (mm)")

    b = st.number_input("Beam Waist, ω‸0 (mm):")

    c = st.number_input("Wavelength, λ (μm):")

# Резултат

with right_column:
    result=0
    if a != 0 and b != 0 and c != 0:
        ZR=3.14*(b**2)/c

        result = a*(1+(ZR/a))**2

        st.markdown(f"Rayleigh Range: {ZR:.3f} mm")
        st.markdown(f"Radius of Curvature: {result:.3f} mm ")
