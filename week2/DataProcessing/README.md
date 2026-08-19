# Week 2 – Data Analysis & EDA

## Topics Covered

- JupyterLab Setup
- KDE (Kernel Density Estimation)
- Normal Distribution
- Interquartile Range (IQR)
- Contour Plots
- Pandas
- Exploratory Data Analysis (EDA)
- NumPy

---

<<<<<<< HEAD
=======
---

>>>>>>> origin/main
## Technologies & Libraries

- Python
- JupyterLab
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

<<<<<<< HEAD
---

=======
>>>>>>> origin/main
## Repository Structure

```text
week2/
│
├── notebook/
│   ├── contour.ipynb
│   ├── distribution.ipynb
│   ├── eda.ipynb
│   ├── iqr.ipynb
│   ├── kde.ipynb
│   ├── numpy.ipynb
│   ├── pandas.ipynb
│   └── WineQT.csv
│
├── README.md
└── .gitignore
```
<<<<<<< HEAD

---

=======
---


>>>>>>> origin/main
# JupyterLab Setup

## Installation

To install JupyterLab, open **Command Prompt (CMD)** or **PowerShell** and run:

1. Install JupyterLab:

<<<<<<< HEAD
   ```bash
   pip install jupyterlab
   ```
2. Navigate to the project directory:

   ```bash
   cd C:\Users\palak\python_Vc
   ```
3. Start JupyterLab:

   ```bash
   python -m jupyterlab
   ```
=======
   ```bash
   pip install jupyterlab
   ```
2. Navigate to the project directory:

   ```bash
   cd C:\Users\palak\python_Vc
   ```
3. Start JupyterLab:

   ```bash
   python -m jupyterlab
   ```
>>>>>>> origin/main
4. JupyterLab will open in your browser.

# KDE (Kernel Density Estimation)

Kernel Density Estimation (KDE) is a non-parametric technique used in Exploratory Data Analysis (EDA) to estimate the probability density distribution of a continuous numerical variable.

KDE produces a smooth curve that shows where the data is concentrated. It can be thought of as a smoother alternative to a histogram.

## How KDE Works

KDE (Kernel Density Estimation) estimates the distribution of data by placing a small, smooth curve called a **kernel** around each data point.

These individual curves are then combined to create one **overall density curve**.

* **Higher peaks** → More data points are concentrated in that region.
* **Lower regions** → Fewer data points are present.
* **Multiple peaks** → May indicate different groups or patterns in the data.
* **Bandwidth** → Controls the smoothness of the KDE curve.

<<<<<<< HEAD

## KDE vs Histogram

| **Histogram**                          | **KDE (Kernel Density Estimation)**     |
| -------------------------------------- | --------------------------------------- |
| Divides data into **bins**             | Creates a **smooth density curve**      |
| Depends on **bin size**                | Depends on **bandwidth**                |
| Shows **frequency/counts**             | Shows **estimated probability density** |
| Less smooth and can look discontinuous | Smooth and continuous                   |
=======
## KDE vs Histogram

| **Histogram**                          | **KDE (Kernel Density Estimation)**     |
| -------------------------------------- | --------------------------------------- |
| Divides data into **bins**             | Creates a **smooth density curve**      |
| Depends on **bin size**                | Depends on **bandwidth**                |
| Shows **frequency/counts**             | Shows **estimated probability density** |
| Less smooth and can look discontinuous | Smooth and continuous                   |
>>>>>>> origin/main

# Normal Distribution Properties

A **normal distribution** is a continuous probability distribution with a characteristic **bell-shaped curve**.

### 1. Bell-Shaped Curve

The distribution has a symmetric, bell-shaped curve.

### 2. Symmetric

The curve is perfectly symmetric around the **mean (μ)**.

* Left side = Right side
* Equal distances from the mean have equal probabilities.

### 3. Mean = Median = Mode

For a perfectly normal distribution:

**Mean = Median = Mode**

All three occur at the center of the distribution.

### 4. Total Area = 1

The entire area under the curve represents probability.

[
P(-\infty < X < \infty) = 1
]

Therefore, the total probability is **100%**.

### 5. Determined by Mean and Standard Deviation

A normal distribution is described by:

* **μ (mean)** → determines the center
* **σ (standard deviation)** → determines the spread

A larger standard deviation produces a wider and flatter distribution, while a smaller standard deviation produces a narrower and taller distribution.

### 6. 68–95–99.7 Rule

One of the most important properties of a normal distribution is the **Empirical Rule**:


| Range  | Approx. Data |
| ------ | -----------: |
| μ ± 1σ |      **68%** |
| μ ± 2σ |      **95%** |
| μ ± 3σ |    **99.7%** |


For example, if the **mean = 50** and **standard deviation = 10**:

* 68% → **40 to 60**
* 95% → **30 to 70**
* 99.7% → **20 to 80**

### 7. Tails Approach Zero

The curve extends infinitely in both directions, but it **never actually touches the x-axis**.

### 8. Zero Skewness

A normal distribution has **zero skewness** because it is perfectly symmetric.

### 9. Unimodal

A normal distribution has **one peak**, which represents the mode.

# Interquartile Range in Statistics

<<<<<<< HEAD

=======
>>>>>>> origin/main
The *Interquartile Range (IQR)* tells us how spread out the middle 50% of the data is. It is less affected by extreme values and gives a better idea of how tightly or loosely the central data points are grouped. It is calculated using the first quartile (Q1) and third quartile (Q3).

## Key Features of IQR
- Focuses only on the central portion of the data.
- Not affected much by outliers, unlike the full range.
- Gives a clear view of how values are arranged around the median.

## Quartiles
Quartiles divide the dataset into four equal parts:
- **Q1 (First Quartile):** Separates the lowest 25% of the data.
- **Q2 (Second Quartile / Median):** Middle value of the dataset.
- **Q3 (Third Quartile):** Separates the highest 25% of the data.

The IQR captures the range between Q1 and Q3, representing the middle 50% of the distribution.

---

## Formula of IQR
The data is sorted in ascending order and split into four equal parts: Q1, Q2, Q3 — called first, second, and third quartiles respectively.

The IQR is simply calculated as:

```math
Interquartile Range = Q3 - Q1
```

It indicates how spread out this middle 50% is, helping gauge variability without influence from outliers.

---

## Applications of the Interquartile Range (IQR)

The Interquartile Range (IQR) has a variety of applications across different fields, including:

- **Outlier Detection:** IQR is used in finance, healthcare, and quality control to detect outliers. Data points that fall outside the range:

- Q1 − 1.5 × IQR
- Q3 + 1.5 × IQR

are considered outliers.

- **Measure of Variability for Skewed Distributions:** Unlike the range, IQR is not sensitive to extreme values or outliers. It is useful for measuring variability in skewed datasets and helps in providing a better representation of spread.

- **Data Summary and Comparison:** It acts as a tool for summarizing data when the dataset is non-normally distributed. It provides a focused view of the data's central 50%, which offers valuable insights into data spread and central tendency.

- **Predictive Data Analysis:** IQR can be applied in predictive analytics where understanding the distribution of data plays an important role in model accuracy and prediction reliability.

- **Central Tendency:** While the mean can be skewed by extreme values, focusing on the central 50% of the data provides a clearer understanding of its true distribution.

---

# Contour Plots

A contour plot is a graphical method to visualize the 3-D surface by plotting constant Z slices called contours in a 2-D format. The contour plot is an alternative to a 3-D surface plot.

A contour plot uses:

- **X-axis** → X variable
- **Y-axis** → Y variable
- **Contour lines / colors** → Z value

## What are Contour Lines?

A contour line connects points that have the **same Z value**.

## Components of a Contour Plot
- **Vertical axis:** Independent variable 2
- **Horizontal axis:** Independent variable 1
- **Lines:** Iso-response values, which can be calculated with the help of (x,y).

The independent variable is usually restricted to a regular grid. The techniques for determining the correct iso-response values are complex and almost always computer-generated.

## Usage
The contour plot depicts changes in Z values relative to X and Y. If data do not form a regular grid, 2-D interpolation is typically necessary.

For one-variable data, a run sequence or histogram is considered necessary. For two-variable data, a scatter plot is recommended. Contour plots can also use polar coordinates (r, theta) instead of traditional rectangular coordinates (x, y, z).

## Types of Contour Plots:
- **Rectangular Contour Plot:** A projection of a 2D plot on a rectangular canvas; the most common form.
- **Polar Contour Plot:** Uses polar coordinates r and theta; r is the distance from origin, theta is the angle from the positive x-axis.
- **Ternary Contour Plot:** Represents relationships between three explanatory variables and response variable within a filled triangle.

---
## Pandas

**Pandas** is a popular Python library used for **data manipulation, data analysis, and data cleaning**. It provides powerful data structures such as **Series** and **DataFrame** for working with structured data.

### Installation

Install Pandas using:

<<<<<<< HEAD
    ```bash
        pip install pandas
    ```
=======
    ```bash
        pip install pandas
    ```
>>>>>>> origin/main

---

# Exploratory Data Analysis (EDA)

**Exploratory Data Analysis (EDA)** is the process of understanding and analyzing a dataset before building models or making conclusions.

### Key Objectives

- Understand the **structure and characteristics** of the data.
- Identify **missing values** and **duplicate data**.
- Analyze **distributions and relationships** between variables.
- Detect **outliers** and unusual values.
- Calculate **statistical measures** such as mean, median, and standard deviation.
- Find patterns and trends using **visualizations**.

### Techniques Used

- **Pandas & NumPy** → Data cleaning and statistical analysis.
- **Matplotlib & Seaborn** → Data visualization.
- **Histogram & KDE** → Understand data distributions.
- **IQR** → Detect outliers.
- **Contour Plots** → Visualize relationships between variables.
- **GroupBy & Aggregation** → Compare statistics across groups.

### Key Idea

EDA helps us **understand the data, identify problems, discover patterns, and prepare the dataset for further analysis or machine learning**.

---

# NumPy

**NumPy (Numerical Python)** is a Python library used for **numerical computing and data analysis**.

### Key Features

- Provides fast and efficient **arrays**.
- Supports **mathematical and statistical operations**.
- Useful for **random number generation**.
- Provides functions for **mean, median, standard deviation, variance**, etc.
- Works efficiently with **large numerical datasets**.
- Commonly used with **Pandas, Matplotlib, and Seaborn**.

### Key Idea

NumPy provides the fundamental tools needed for **numerical calculations and data analysis in Python**.

## NumPy Array

A **NumPy array** is a collection of values stored in a structured and efficient format for **numerical operations**.

### Key Features

- Stores multiple values in a single array.
- Supports **1D, 2D, and multidimensional** arrays.
- Faster and more memory-efficient than Python lists for numerical data.
- Allows mathematical operations directly on arrays.

### Key Idea

NumPy arrays are mainly used for **storing and performing calculations on numerical data**.

---

## Practice Notebooks

### 1. KDE
Learn about Kernel Density Estimation and practice creating KDE plots.

<<<<<<< HEAD
 [Open KDE Notebook](notebook/kde.ipynb)
=======
 [Open KDE Notebook](notebook/kde.ipynb)
>>>>>>> origin/main

### 2. Normal Distribution
Practice generating and visualizing normally distributed data.

<<<<<<< HEAD
 [Open Normal Distribution Notebook](notebook/distribution.ipynb)
=======
 [Open Normal Distribution Notebook](notebook/distribution.ipynb)
>>>>>>> origin/main

### 3. IQR
Practice calculating Q1, Q3, IQR and identifying outliers.

<<<<<<< HEAD
 [Open IQR Notebook](notebook/iqr.ipynb)
=======
 [Open IQR Notebook](notebook/iqr.ipynb)
>>>>>>> origin/main

### 4. Contour Plots
Practice creating contour plots and visualizing relationships between variables.

<<<<<<< HEAD
 [Open Contour Plot Notebook](notebook/contour.ipynb)
=======
 [Open Contour Plot Notebook](notebook/contour.ipynb)
>>>>>>> origin/main

### 5. Pandas
Practice DataFrame creation, data manipulation and basic analysis.

<<<<<<< HEAD
 [Open Pandas Notebook](notebook/pandas.ipynb)
=======
 [Open Pandas Notebook](notebook/pandas.ipynb)
>>>>>>> origin/main

### 6. NumPy
Practice NumPy arrays, mathematical operations and random data generation.

<<<<<<< HEAD
 [Open NumPy Notebook](notebook/numpy.ipynb)
=======
 [Open NumPy Notebook](notebook/numpy.ipynb)
>>>>>>> origin/main

### 7. EDA
Practice performing Exploratory Data Analysis on a dataset.

<<<<<<< HEAD
 [Open EDA Notebook](notebook/eda.ipynb)
=======
 [Open EDA Notebook](notebook/eda.ipynb)
>>>>>>> origin/main

---

## Dataset

The practical notebooks use the Wine Quality dataset:

👉 [WineQT.csv](notebook/WineQT.csv)

---

<<<<<<< HEAD
=======
---

>>>>>>> origin/main
## Conclusion

Week 2 focused on building a strong foundation in data analysis and Exploratory Data Analysis (EDA). I learned how to work with NumPy and Pandas, understand data distributions using KDE and normal distribution concepts, detect outliers using IQR, and visualize relationships using contour plots. I also applied these concepts practically through Jupyter notebooks and the Wine Quality dataset.

<<<<<<< HEAD
These concepts provide a foundation for understanding datasets, identifying patterns and anomalies, and preparing data for further analysis and machine learning.

---
=======
These concepts provide a foundation for understanding datasets, identifying patterns and anomalies, and preparing data for further analysis and machine learning.
>>>>>>> origin/main
