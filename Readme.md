# ImportSQL GUI Application

## Purpose

This project provides a graphical user interface (GUI) for importing CSV files into a MySQL database. It simplifies the process by automating the creation of database tables and inserting data from CSV files located in a specified folder.

## Installation and Dependencies

### Prerequisites

- Python 3.x
- MySQL Server
- Pip (Python package manager)

### Dependencies

The application requires the following Python packages:

- `mysql-connector-python`
- `pandas`

These dependencies will be installed automatically when you run the GUI application. Alternatively, you can install them manually:

```bash
pip install mysql-connector-python pandas
```

### Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

## How to Use

1. **Run the GUI Application**

   ```bash
   python gui.py
   ```

2. **Enter Required Information**

   - **Username**: Your MySQL username.
   - **Password**: Your MySQL password.
   - **Database Name**: The name of the database to import data into.
   - **Folder Path**: The directory containing your CSV files.

3. **Import Data**

   - Click the **Submit** button.
   - The application will install any missing dependencies.
   - It will then execute `importsql.py` to import data from the CSV files into your database.

## Error Cases and Troubleshooting

- **Missing Fields**: Ensure all input fields are filled. The application will display an error message if any fields are missing.

- **Dependency Installation Failed**: If automatic installation fails, install dependencies manually:

  ```bash
  pip install mysql-connector-python pandas
  ```

- **Database Connection Errors**: Verify that your MySQL server is running and the credentials are correct. Common errors include:

  - **Access Denied**: Incorrect username or password.
  - **Database Does Not Exist**: The specified database name is incorrect or doesn't exist.

- **File Errors**: If the folder path is incorrect or inaccessible, the application will raise a `FileNotFoundError`.

- **Unexpected Errors**: Any other exceptions will be displayed in an error message. Check the console output for more details.

## How It Works

- **`gui.py`**: Launches a Tkinter GUI that collects user inputs and runs `importsql.py` with the provided information.

- **`importsql.py`**:

  - Reads environment variables set by `gui.py` for database credentials and folder path.
  - Connects to the MySQL database using `mysql.connector`.
  - Iterates over each CSV file in the specified folder:
    - Creates a table for each CSV file (if it doesn't already exist).
    - Inserts the data from the CSV file into the corresponding table using Pandas.

- **Data Import Process**:

  - For each CSV file:
    - The table name is derived from the CSV file name.
    - Columns are created based on the CSV headers.
    - Data types default to `VARCHAR(255)`.
    - Data is inserted row by row into the table.

## Notes

- Ensure that the MySQL user has the necessary permissions to create tables and insert data.
- The application uses `mysql_native_password` authentication plugin; make sure your MySQL server supports it.