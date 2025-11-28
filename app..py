import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import multivariate_normal

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Bivariate Gaussian Visualizer",
    layout="wide",
    page_icon="📉"
)

# --- 2. Sidebar Controls ---
st.sidebar.header("Parameters")

st.sidebar.subheader("Means (Centroids)")
mu_x = st.sidebar.slider("Mean X (μₓ)", -4.0, 4.0, 0.0, 0.1)
mu_y = st.sidebar.slider("Mean Y (μᵧ)", -4.0, 4.0, 0.0, 0.1)

st.sidebar.subheader("Shape & Spread")
sigma_x = st.sidebar.slider("Std Dev X (σₓ)", 0.5, 3.0, 1.5, 0.1)
sigma_y = st.sidebar.slider("Std Dev Y (σᵧ)", 0.5, 3.0, 1.5, 0.1)
rho = st.sidebar.slider("Correlation (ρ)", -0.95, 0.95, 0.0, 0.05)

# --- 3. Mathematical Logic (Vectorized with NumPy) ---
# Create grid
x_range = 6
resolution = 60
x = np.linspace(-x_range, x_range, resolution)
y = np.linspace(-x_range, x_range, resolution)
X, Y = np.meshgrid(x, y)

# Pack positions into a 3-layer array
pos = np.dstack((X, Y))

# Create Covariance Matrix
cov_xy = rho * sigma_x * sigma_y
covariance_matrix = [[sigma_x**2, cov_xy], [cov_xy, sigma_y**2]]

# Calculate PDF using Scipy (cleaner than writing raw formula)
rv = multivariate_normal([mu_x, mu_y], covariance_matrix)
Z = rv.pdf(pos)

# --- 4. Main Layout & Visualization ---
st.title("Bivariate Gaussian Visualizer")
st.markdown("Explore the geometry of **2D Normal Distributions** using Python and Plotly.")

col1, col2 = st.columns([3, 1])

with col1:
    # Initialize Subplots: 1 Row, 2 Columns (3D Surface | 2D Contour)
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'surface'}, {'type': 'contour'}]],
        subplot_titles=('3D Surface Density', '2D Contour Projection')
    )

    # 3D Surface Trace
    fig.add_trace(
        go.Surface(z=Z, x=x, y=y, colorscale='Viridis', showscale=False, opacity=0.9),
        row=1, col=1
    )

    # 2D Contour Trace
    fig.add_trace(
        go.Contour(z=Z, x=x, y=y, colorscale='Viridis', showscale=False),
        row=1, col=2
    )

    # Update Layout
    fig.update_layout(
        height=600,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Density',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

# --- 5. Covariance Matrix Display (Right Column) ---
with col2:
    st.markdown("### Covariance Matrix Σ")
    st.info(f"""
    **Matrix Values:**
    
    | | X | Y |
    |---|---|---|
    | **X** | {covariance_matrix[0][0]:.2f} | {covariance_matrix[0][1]:.2f} |
    | **Y** | {covariance_matrix[1][0]:.2f} | {covariance_matrix[1][1]:.2f} |
    """)
    
    st.write("---")
    st.markdown(f"**Covariance:** `{cov_xy:.2f}`")
    st.markdown(f"**Correlation:** `{rho:.2f}`")
    st.caption("Note: Cov(X,Y) = ρ * σₓ * σᵧ")