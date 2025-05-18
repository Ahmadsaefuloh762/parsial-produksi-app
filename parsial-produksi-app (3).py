import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Aplikasi Turunan Parsial")

# Input dari pengguna
f_input = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
x_val = st.number_input("Nilai x pada titik evaluasi:", value=1.0)
y_val = st.number_input("Nilai y pada titik evaluasi:", value=1.0)

# Simbol
x, y = sp.symbols('x y')

try:
    # Konversi input jadi ekspresi simbolik
    f = sp.sympify(f_input)

    # Turunan parsial
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Evaluasi nilai fungsi dan turunannya di titik (x_val, y_val)
    f_val = f.subs({x: x_val, y: y_val})
    fx_val = fx.subs({x: x_val, y: y_val})
    fy_val = fy.subs({x: x_val, y: y_val})

    st.write("Nilai fungsi di titik (x₀, y₀):", f_val)
    st.write("Gradien di titik (x₀, y₀):", f"({fx_val}, {fy_val})")

    st.subheader("Grafik Permukaan & Bidang Singgung")

    x_vals = np.linspace(x0 - 2, x0 + 2, 50)
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = sp.lambdify((x, y), f, 'numpy')(X, Y)
    z_tangent = f_val + fx_val * (x - x_val) + fy_val * (y - y_val)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')
    ax.set_title("Permukaan f(x, y) dan bidang singgungnya")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
