# Bivariate Gaussian Visualizer 📉

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bivariate-gaussian-visualizer.streamlit.app/)

An interactive web application to explore and visualize **Bivariate (2D) Gaussian Distributions**. Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/), this tool allows you to manipulate statistical parameters in real-time and observe the resulting geometric changes in 3D surface plots and 2D contour projections.

## ✨ Features

*   **Interactive Controls**: Adjust the Mean ($\mu$), Standard Deviation ($\sigma$), and Correlation ($\rho$) for both X and Y variables using intuitive sliders.
*   **Real-time Visualization**:
    *   **3D Surface Density Plot**: Visualize the probability density function (PDF) as a 3D surface.
    *   **2D Contour Projection**: View the distribution from above to understand the spread and orientation.
*   **Covariance Matrix Display**: See the dynamically calculated Covariance Matrix ($\Sigma$) and correlation values.
*   **Mathematical Insights**: Helps users understand concepts like variance, covariance, and correlation in a visual manner.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/A7med-Foly/Bivariate-Gaussian-Visualizer.git
    cd Bivariate-Gaussian-Visualizer
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`.

## 🛠️ Technologies Used

*   **[Streamlit](https://streamlit.io/)**: For creating the web interface.
*   **[NumPy](https://numpy.org/)**: For efficient numerical operations and matrix calculations.
*   **[SciPy](https://scipy.org/)**: specifically `multivariate_normal` for calculating the Probability Density Function.
*   **[Plotly](https://plotly.com/)**: For interactive 3D and 2D graphing.

## 📊 Mathematical Context

The Bivariate Gaussian distribution is defined by:
*   **Mean Vector ($\mu$)**: Determines the center of the distribution.
*   **Covariance Matrix ($\Sigma$)**: Determines the shape, spread, and orientation.

$$
\Sigma = \begin{bmatrix} \sigma_x^2 & \rho \sigma_x \sigma_y \\ \rho \sigma_x \sigma_y & \sigma_y^2 \end{bmatrix}
$$

Where $\rho$ is the correlation coefficient between $X$ and $Y$.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
