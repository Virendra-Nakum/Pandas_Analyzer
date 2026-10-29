# Data Analysis & Visualization Program

### A Python-Based Project for Data Analysis, Statistical Operations, and Data Visualization

## 📌 Project Overview

The **Data Analysis & Visualization Program** is a Python-based application that uses Pandas and Matplotlib to analyze CSV datasets, handle missing values, calculate descriptive statistics, perform DataFrame operations, and generate visualizations.

The project provides a menu-driven interface that allows users to perform different data analysis tasks easily.

## ✨ Features

- Load datasets from CSV files.
- Explore the first and last five rows of a dataset.
- Display column names, data types, and basic information.
- Identify and handle missing values.
- Calculate minimum, maximum, mean, median, and standard deviation of sales.
- Perform DataFrame operations such as total sales and product-wise quantity analysis.
- Identify regions with the highest sales.
- Generate bar plots, line plots, scatter plots, pie charts, histograms, and area plots.
- Save generated visualizations as PNG images.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **Pandas** — Data manipulation and analysis.
- **Matplotlib** — Data visualization.
- **CSV** — Dataset file format.

## ⚙️ Process

1. **Load Dataset:** The user enters the path of a CSV file, which is loaded into a Pandas DataFrame.
2. **Explore Data:** The user examines rows, column names, data types, and dataset information.
3. **Perform DataFrame Operations:** The program calculates sales totals, identifies high- and low-sales records, analyzes regional sales, and summarizes product quantities.
4. **Handle Missing Data:** The user can display missing values, fill missing numerical values with the mean, replace missing values with a specific value, or remove incomplete rows.
5. **Generate Statistics:** The program calculates descriptive statistics for the `Sales` column.
6. **Visualize Data:** The user selects a chart type and the required columns to generate a visualization.
7. **Save Visualization:** The generated graph can be saved as a PNG file.
8. **Exit:** The user exits the program through the main menu.

## 📂 Project Structure

text

```
├── main.py
├── output.png
├── data/
│   └── sales_data.csv
├── graph/
│   └── sales.png
└── README.md
```

**Note:** `main.py` contains the Python program. The `data/` folder stores CSV datasets, and the `graph/` folder stores generated visualizations. Create these folders as needed. The example CSV and image files are optional and should be added separately.

## ▶️ How to Run Project

### 1\. Install Python

Download and install Python from the official website:

[https://www.python.org/downloads/](<https://www.python.org/downloads/>)

### 2\. Install Required Libraries

Open a terminal or command prompt and run:

bash

```
pip install pandas matplotlib
```

### 3\. Create the Project Files

Save the Python code in a file named `main.py`.

Create the following folders in the project directory:

text

```
data/
graph/
```

Place your CSV dataset inside the `data/` folder.

### 4\. Run the Program

Open the terminal in the project directory and execute:

bash

```
python main.py
```

### 5\. Load the Dataset

When prompted, enter the CSV file path:

text

```
data/sales_data.csv
```

Make sure the dataset exists at the specified path.

### 6\. Select an Operation

Enter the corresponding menu number to explore the dataset, handle missing values, calculate statistics, generate charts, or save a visualization.

## 📊 Sample Output

The following is an illustrative example of the program's console output.

text

```
=============== Data Analysis & Visualization Program ===============
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
======================================================================

Enter Your Choice: 1

Enter Dataset Path (e.g. data/sales_data.csv): data/sales_data.csv

Dataset Loaded Successfully!
```

### Example: Statistical Analysis

text

```
=== Statistical Analysis ===
1. Minimum Sales
2. Maximum Sales
3. Average Sales
4. Median Sales
5. Standard Deviation of Sales

Enter Your Choice: 3

Average Sales: 2500.0
```

_The numerical result above is an example only; actual output depends on the dataset._

### Example: Data Visualization

text

```
===== Data Visualization =====
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Area Plot

Enter Your Choice: 1

Enter the X-axis Column Name: Product
Enter the Y-axis Column Name: Sales
```

The program displays the selected chart using Matplotlib.

### Example: Saving a Visualization

text

```
Enter File Name (e.g. sales.png): sales.png

Graph Saved Successfully in the graph Folder!
```

The graph is saved in the `graph/` directory when that folder exists and the file can be written successfully.

## 🎯 Objectives

- Understand practical data analysis using Python.
- Learn how to manipulate CSV datasets with Pandas.
- Identify and handle missing data.
- Calculate useful statistical measures.
- Represent data visually using different chart types.
- Develop a menu-driven Python application.

## 🔮 Future Improvements

- Add support for Excel files.
- Allow users to select different statistical columns dynamically.
- Add interactive dashboards.
- Improve input validation and error messages.
- Automatically create output directories.
- Export analysis results to CSV or Excel files.

## Output

![Programe Output](output.png)

## 👨‍💻 Author

** Virendra Nakum** 

**Project:** Data Analysis & Visualization Program

**Language:** Python

## 📝 Conclusion

The Data Analysis & Visualization Program demonstrates how Python libraries such as Pandas and Matplotlib can be used to process, analyze, and visualize datasets. It combines data exploration, missing-value handling, statistical calculations, and graphical representation in a single menu-driven application, making it a useful beginner-level data analytics project.

Before submitting: Replace `Virendra Nakum` with your actual name, and ensure your Python file is named `main.py` or update the README instructions to match your filename.
