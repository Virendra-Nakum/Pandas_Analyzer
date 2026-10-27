import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzer:

    def __init__(self):
        self.data = None
        self.graph = None

    def load_data(self):
        try:
            path = input("Enter Dataset Path (e.g. data/sales_data.csv): ").strip()
            self.data = pd.read_csv(path)
            print("Dataset Loaded Successfully!")
            print(self.data.head())
            return self.data
        except :
            print("Invalid File Name:")
            return

    def explore_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return
        elif self.data.empty:
            print("Dataset Is Empty!")
            return

        print("=== Explore Data ===")
        print("1. Display the First 5 Rows")
        print("2. Display the Last 5 Rows")
        print("3. Display Column Names")
        print("4. Display Data Types")
        print("5. Display Basic Information")

        try:
            choice = int(input("Enter Your Choice: "))
        except :
            print("Enter a Valid Choice!")
            return

        if choice == 1:
            print(self.data.head())
        elif choice == 2:
            print(self.data.tail())
        elif choice == 3:
            print(self.data.columns)
        elif choice == 4:
            print(self.data.dtypes)
        elif choice == 5:
            self.data.info()
        else:
            print("Enter a Valid Choice!")

    def missing_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return

        elif self.data.empty:
            print("Dataset Is Empty!")
            return

        print("=== Handle Missing Data ===")
        print("1. Display Rows with Missing Values")
        print("2. Fill Missing Values with Mean")
        print("3. Drop Rows with Missing Values")
        print("4. Replace Missing Values with a Specific Value")

        try:
            choice = int(input("Enter Your Choice: "))
        except :
            print("Enter a Valid Choice!")
            return

        if choice == 1:
            missing = self.data.isnull().sum()
            if not self.data.isnull().values.any():
                print("No Missing Values Found!")
            else:
                print(self.data[self.data.isnull().any(axis=1)])
                print("Missing Values in Each Column:")
                print(missing)

        elif choice == 2:
            if "Product" in self.data.columns:
                self.data["Product"] = self.data["Product"].fillna("Unknown")

            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing Values Filled Where Possible!")
            print(self.data.isnull().sum())

        elif choice == 3:
            print("===== Before =====")
            print(self.data.isnull().sum())
            self.data.dropna(inplace=True)
            print("===== After =====")
            print(self.data.isnull().sum())
            print("Rows with Missing Values Removed!")

        elif choice == 4:
            value = input("Enter a Value to Replace Missing Values: ")
            self.data.fillna(value, inplace=True)
            print("Missing Values Replaced Successfully!")
            print(self.data.isnull().sum())

        else:
            print("Enter a Valid Choice!")

    def visualization_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return

        if self.data.empty:
            print("Dataset Is Empty!")
            return

        print("===== Data Visualization =====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Area Plot")

        try:
            choice = int(input("Enter Your Choice: "))
        except :
            print("Enter a Valid Choice!")
            return

        try:
            if choice == 1:
                x = input("Enter the X-axis Column Name: ")
                y = input("Enter the Y-axis Column Name: ")
                self.graph = self.data.plot.bar(x=x, y=y)
                plt.title(f"Bar Plot of {y} vs {x}")
                plt.xlabel(x)
                plt.ylabel(y)

            elif choice == 2:
                x = input("Enter the X-axis Column Name: ")
                y = input("Enter the Y-axis Column Name: ")
                self.graph = self.data.plot.line(x=x, y=y)
                plt.title(f"Line Plot of {y} vs {x}")
                plt.xlabel(x)
                plt.ylabel(y)

            elif choice == 3:
                x = input("Enter the X-axis Column Name: ")
                y = input("Enter the Y-axis Column Name: ")
                self.graph = self.data.plot.scatter(x=x, y=y)
                plt.title(f"Scatter Plot of {y} vs {x}")
                plt.xlabel(x)
                plt.ylabel(y)

            elif choice == 4:
                column = input("Enter the Column Name for Pie Chart: ")
                self.graph = self.data[column].value_counts().plot.pie(autopct="%1.1f%%")
                plt.title(f"Pie Chart of {column}")
                plt.ylabel("")

            elif choice == 5:
                column = input("Enter the Column Name for Histogram: ")
                self.graph = self.data[column].plot.hist()
                plt.title(f"Histogram of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")

            elif choice == 6:
                x = input("Enter the X-axis Column Name: ")
                y = input("Enter the Y-axis Column Name: ")
                self.graph = self.data.plot.area(x=x, y=y)
                plt.title(f"Area Plot of {y} vs {x}")
                plt.xlabel(x)
                plt.ylabel(y)

            else:
                print("Enter a Valid Choice!")
                return

            plt.tight_layout()
            plt.show()

        except :
            self.graph = None
            print("Unable to Create Graph. Check Column Names and Data Types.")
            print("Error:")

    def save_visualization(self):
        if self.graph is None:
            print("Please Create a Graph First!")
            return

        name = input("Enter File Name (e.g. sales.png): ").strip()

 

        if not name.lower().endswith(".png"):
            name += ".png"

        try:
            self.graph.figure.savefig("graph/" + name)
            print("Graph Saved Successfully in the graph Folder!")

        except  :
            print("Error Saving Graph. Check Whether the graph Folder Exists.")
            print("Error:")

    def statistics_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return
 
        elif "Sales" not in self.data.columns:
            print("Sales Column Not Found in the Dataset!")
            return

        sales = pd.to_numeric(self.data["Sales"], errors="coerce").dropna()

        if sales.empty:
            print("No Valid Numerical Sales Data Found!")
            return

        print("=== Statistical Analysis ===")
        print("1. Minimum Sales")
        print("2. Maximum Sales")
        print("3. Average Sales")
        print("4. Median Sales")
        print("5. Standard Deviation of Sales")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Enter a Valid Choice!")
            return

        if choice == 1:
            print("Minimum Sales:", sales.min())
        elif choice == 2:
            print("Maximum Sales:", sales.max())
        elif choice == 3:
            print("Average Sales:", sales.mean())
        elif choice == 4:
            print("Median Sales:", sales.median())
        elif choice == 5:
            print("Standard Deviation of Sales:", sales.std())
        else:
            print("Enter a Valid Choice!")

    def performance_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return

        print("=== DataFrame Operations ===")
        print("1. Sum of Sales")
        print("2. Top 5 Products with Highest Sales")
        print("3. Top 5 Products with Lowest Sales")
        print("4. Region with Highest Sales")
        print("5. Total Quantity Sold by Each Product")

        try:
            choice = int(input("Enter Your Choice: "))
        except :
            print("Enter a Valid Choice!")
            return

        if choice == 1:
            print("Total Sales:", self.data["Sales"].sum())

        elif choice == 2 :
            print("Higest Sales :",self.data['Sales'].nlargest(5))

        elif choice == 3 :
            print("Lowest Sales :",self.data['Sales'].nsmallest(5))

        elif choice == 4:
            sales = self.data.groupby("Region")["Sales"].sum()
            print("Region with Highest Sales:", sales.idxmax())

        elif choice == 5:
            print(self.data.groupby("Product")["Quantity"].sum())

        else:
            print("Enter a Valid Choice!")

    def main_menu(self):
        print()
        print("=" * 15, "Data Analysis & Visualization Program", "=" * 15)
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 70)

    def start_Programe(self):
        while True:
            self.main_menu()

            try:
                choice = int(input("Enter Your Choice: "))
            except :
                print("Enter a Valid Choice!")
                continue

            print()

            if choice == 1:
                self.load_data()

            elif choice == 2:
                self.explore_data()

            elif choice == 3:
                self.performance_data()

            elif choice == 4:
                self.missing_data()

            elif choice == 5:
                self.statistics_data()

            elif choice == 6:
                self.visualization_data()

            elif choice == 7:
                self.save_visualization()

            elif choice == 8:
                print("Exiting the Program. Goodbye!")
                
                break
            else:
                print("Invalid Choice!")


obj = DataAnalyzer()
obj.start_Programe()