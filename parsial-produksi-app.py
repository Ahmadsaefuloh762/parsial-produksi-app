import sympy as sp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Konfigurasi Streamlit
st.title("Aplikasi Interaktif: Turunan Parsial dan Bidang Singgung")

# Input fungsi dan titik
f_input = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
x_val = st.number_input("Nilai x pada titik evaluasi:", value=1.0)
y_val = st.number_input("Nilai y pada titik evaluasi:", value=1.0)

x, y = sp.symbols('x y')
try:
    f = sp.sympify(f_input)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    fx_val = fx.subs({x: x_val, y: y_val})
    fy_val = fy.subs({x: x_val, y: y_val})
    f_val = f.subs({x: x_val, y: y_val})

    st.write(f"Turunan parsial terhadap x di titik ({x_val}, {y_val}) = {fx_val}")
    st.write(f"Turunan parsial terhadap y di titik ({x_val}, {y_val}) = {fy_val}")

    # Persamaan bidang singgung
    z_tangent = float(f_val) + float(fx_val)*(x - x_val) + float(fy_val)*(y - y_val)
    st.latex(f"\\text{{Bidang Singgung: }} z = {z_tangent}")

    # Visualisasi
    x_range = np.linspace(x_val - 2, x_val + 2, 50)
    y_range = np.linspace(y_val - 2, y_val + 2, 50)
    X, Y = np.meshgrid(x_range, y_range)
    f_lambd = sp.lambdify((x, y), f, "numpy")
    tangent_lambd = sp.lambdify((x, y), z_tangent, "numpy")

    Z = f_lambd(X, Y)
    Z_tangent = tangent_lambd(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.4, color='red')
    ax.scatter(x_val, y_val, f_val, color='black', s=50)
    ax.set_title('Grafik Permukaan dan Bidang Singgung')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
