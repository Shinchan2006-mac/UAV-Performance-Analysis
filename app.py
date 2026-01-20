import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive UAV Performance Analyzer")

# 1. User Inputs in Sidebar
st.sidebar.header("Design Parameters")
mass = st.sidebar.slider("UAV Mass (kg)", 1.0, 10.0, 3.5)
velocity = st.sidebar.slider("Flight Velocity (m/s)", 5, 50, 20)
rho = 1.225 # Air density
S = 0.5     # Example Wing Area (use your actual value)

# 2. The Calculations (The "Math" part)
W = mass * 9.81
# This is where 'calculated_Tr' gets created:
calculated_Tr = W / 10 # Simplified example: Replace with your actual Tr formula

# 3. Displaying the Result
# Now that calculated_Tr is defined above, this line will work:
st.write(f"At {velocity} m/s, the Thrust Required is: {calculated_Tr:.2f} N")

# 4. Interactive Plot
v_range = np.linspace(5, 50, 100)
tr_range = W / (v_range * 0.5) # Example curve logic

fig, ax = plt.subplots()
ax.plot(v_range, tr_range, color='red')
ax.set_xlabel('Velocity (m/s)')
ax.set_ylabel('Thrust Required (N)')
ax.grid(True)

st.pyplot(fig)
