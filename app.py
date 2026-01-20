import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive UAV Performance Analyzer")

# User Inputs in the Sidebar
mass = st.sidebar.slider("UAV Mass (kg)", 1.0, 10.0, 3.5)
root_chord = st.sidebar.number_input("Root Chord (m)", value=0.9)
velocity = st.sidebar.slider("Flight Velocity (m/s)", 5, 50, 20)

# Calculations (Based on your MATLAB logic)
W = mass * 9.81
# ... Insert your aerodynamic math here ...

# Display Result
st.write(f"At {velocity} m/s, the Thrust Required is: {calculated_Tr} N")

# Plotting
fig, ax = plt.subplots()
ax.plot(V_range, Tr_range)
st.pyplot(fig)
