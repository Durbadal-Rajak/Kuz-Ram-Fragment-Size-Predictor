import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# Kuz-Ram mean fragment size
def kuz_ram(A, V, Q):
    X = A * (V / Q)**0.8 * Q**(1/6)
    return X


# Rosin-Rammler distribution
def rosin_rammler(x, xc, n):
    R = 1 - np.exp(-(x / xc)**n)
    return R


# Title
st.title("Kuz-Ram Fragment Size Predictor")

# Inputs
A = st.number_input("Rock Factor (A)", value=10.0)

V = st.number_input(
    "Rock Volume per Hole (V, m³)",
    value=300.0
)

Q = st.number_input(
    "Explosive Charge per Hole (Q, kg)",
    value=150.0
)

# Mean fragment size
X = kuz_ram(A, V, Q)

# Results
st.subheader("Results")
st.write(f"Mean Fragment Size = {X:.2f} cm")

# Rosin-Rammler parameters
xc = X
n = 1.5

# Generate sizes from 1 to 100 cm
sizes = np.linspace(1, 100, 200)

# Calculate percent passing
passing = rosin_rammler(sizes, xc, n) * 100

# Calculate P20, P50, P80
P20 = np.interp(20, passing, sizes)
P50 = np.interp(50, passing, sizes)
P80 = np.interp(80, passing, sizes)

# Create graph
fig, ax = plt.subplots()

# Plot curve
ax.plot(sizes, passing)

# Mark P20, P50, P80
ax.scatter(P20, 20, label=f"P20 = {P20:.2f} cm")
ax.scatter(P50, 50, label=f"P50 = {P50:.2f} cm")
ax.scatter(P80, 80, label=f"P80 = {P80:.2f} cm")

# Labels
ax.set_xlabel("Fragment Size (cm)")
ax.set_ylabel("Percent Passing (%)")
ax.set_title("Rosin-Rammler Distribution")
ax.legend()

# Show graph
st.pyplot(fig)


# -------------------------------
# Results
# -------------------------------
st.subheader("Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("P20", f"{P20:.2f} cm")

with col2:
    st.metric("P50", f"{P50:.2f} cm")

with col3:
    st.metric("P80", f"{P80:.2f} cm")

st.metric(
    "Mean Fragment Size",
    f"{X:.2f} cm"
)

# -------------------------------
# Blast Quality
# -------------------------------
if P80 < 30:
    verdict = "Good Fragmentation ✅"

elif P80 < 60:
    verdict = "Coarse Fragmentation ⚠️"

else:
    verdict = "Very Coarse Fragmentation ❌"

st.subheader("Blast Quality")

if P80 < 30 : 
    st.success(verdict)
elif P80 < 60 :
    st.success(verdict)
else :
    st.error(verdict)    
    