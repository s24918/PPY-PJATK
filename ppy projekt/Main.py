import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import joblib

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
df = pd.read_csv(url)

# One-hot encode the categorical columns
# One-hot encoding is a process of converting categorical variables into binary representations.
# It creates additional columns (dummy variables) for each unique value in the categorical column and assigns a value
# of 1 or 0 to indicate the presence or absence of that value in the original column.
df_encoded = pd.get_dummies(df, columns = ["Month", "VisitorType", "Weekend"], drop_first = True)

# Split data into features (X) and labels (y)
X = df_encoded.drop("Revenue", axis = 1)
y = df_encoded["Revenue"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Connect to SQLite database
conn = sqlite3.connect('online_shoppers.db')
cursor = conn.cursor()

# Create a table in the database
create_table_query = """
CREATE TABLE IF NOT EXISTS online_shoppers (
    id INTEGER PRIMARY KEY,
    Administrative INTEGER,
    Informational INTEGER,
    ProductRelated INTEGER,
    BounceRates REAL,
    ExitRates REAL,
    PageValues REAL,
    SpecialDay REAL,
    Month TEXT,
    OperatingSystems INTEGER,
    Browser INTEGER,
    Region INTEGER,
    TrafficType INTEGER,
    VisitorType TEXT,
    Weekend TEXT,
    Revenue TEXT
)
"""
#execute an SQL query on a SQLite database using a cursor object.
cursor.execute(create_table_query)


def save_data_to_db():
    data = X.copy()
    data["Revenue"] = y
    data.to_sql('online_shoppers', conn, if_exists = 'replace', index = False)
    messagebox.showinfo("Data Saved", "Data has been saved in the SQLite database.")


def load_data_from_db():
    global X, y
    data = pd.read_sql('SELECT * FROM online_shoppers', conn)
    X = data.drop("Revenue", axis = 1)
    y = data["Revenue"]
    messagebox.showinfo("Data Loaded", "Data has been loaded from the SQLite database.")


def train_model():
    global model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    messagebox.showinfo("Model Trained", "Mean Squared Error: {:.4f}".format(mse))


def predict_new_data():
    new_data_str = new_data_entry.get()
    new_data_list = list(map(float, new_data_str.split(",")))
    new_data_df = pd.DataFrame([new_data_ist], columns = X.columns)
    prediction = model.predict(new_data_df)
    messagebox.showinfo("Prediction for New Data", f"Prediction: {prediction}")


def save_model():
    joblib.dump(model, "online_shoppers_model.pkl")
    messagebox.showinfo("Model Saved", "Model has been saved to disk.")


def load_model():
    global model
    model = joblib.load("online_shoppers_model.pkl")
    messagebox.showinfo("Model Loaded", "Model has been loaded from disk.")


def create_bar_chart():
    fig = plt.figure(figsize = (10, 6))
    revenue_counts = df["Revenue"].value_counts()
    revenue_counts.plot(kind = "bar")
    plt.xlabel("Revenue")
    plt.ylabel("Count")
    plt.title("Revenue Distribution")
    fig.show()


# Generowanie pliku PDF z wykresami
def generate_pdf():
    with PdfPages("wykresy.pdf") as pdf:
        fig = create_bar_chart()
        pdf.savefig(fig)
        plt.close(fig)

# Create the main window
window = tk.Tk()
window.title("Online Shopper Intention")
window.geometry("400x400")

# Create a scrollable container
scrollpane = tk.Frame(window)
scrollpane.pack(fill="both", expand=True, padx=10, pady=10)

# Data table for browsing the data
data_table = ttk.Treeview(scrollpane)
data_table["columns"] = list(df.columns)
data_table.pack(side="left", fill="y")

# Set table headers
for header in df.columns:
    data_table.heading(header, text=header)

# Set column widths
column_widths = [80] * len(df.columns)
for header, width in zip(df.columns, column_widths):
    data_table.column(header, width=width)

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(scrollpane, orient="vertical", command=data_table.yview)
scrollbar.pack(side="right", fill="y")

# Configure the scrollbar to scroll the table
data_table.configure(yscrollcommand=scrollbar.set)

# Insert data into the table
for index, row in df.iterrows():
    data_table.insert("", "end", text=index, values=row.tolist())

# Create a scrollable container for buttons and text fields
form_scrollpane = tk.Frame(window)
form_scrollpane.pack(fill="both", expand=True, padx=10, pady=10)

# Buttons and text fields
save_data_button = tk.Button(form_scrollpane, text="Save Data to Database", command=save_data_to_db)
save_data_button.pack(pady=10)

load_data_button = tk.Button(form_scrollpane, text="Load Data from Database", command=load_data_from_db)
load_data_button.pack(pady=10)

train_model_button = tk.Button(form_scrollpane, text="Train Model", command=train_model)
train_model_button.pack(pady=10)

save_model_button = tk.Button(form_scrollpane, text="Save Model", command=save_model)
save_model_button.pack(pady=10)

load_model_button = tk.Button(form_scrollpane, text="Load Model", command=load_model)
load_model_button.pack(pady=10)

new_data_label = tk.Label(form_scrollpane, text="New Data (separated by commas):")
new_data_label.pack()
new_data_entry = tk.Entry(form_scrollpane)
new_data_entry.pack()

predict_button = tk.Button(form_scrollpane, text="Predict for New Data", command=predict_new_data)
predict_button.pack(pady=10)

bar_chart_button = tk.Button(form_scrollpane, text="Generate Bar Chart", command=create_bar_chart)
bar_chart_button.pack(pady=10)

pdf_button = tk.Button(form_scrollpane, text="Generuj PDF", command=generate_pdf)
pdf_button.pack(pady=10)

# Run the main application loop
window.mainloop()