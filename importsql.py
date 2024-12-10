import os
import mysql.connector
import pandas as pd

def main():
    try:
        # Retrieve environment variables
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')
        folder_path = os.getenv('FOLDER_PATH')

        if not all([db_user, db_password, db_name, folder_path]):
            raise ValueError("Missing environment variables for DB configuration or folder path.")

        # Database connection
        conn = mysql.connector.connect(
            host='localhost',
            user=db_user,
            password=db_password,
            database=db_name,
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()

        # Iterate through all CSV files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                table_name = file_name.split('.')[0]
                file_path = os.path.join(folder_path, file_name)
                
                df = pd.read_csv(file_path)
                columns = ', '.join([f"`{col}` VARCHAR(255)" for col in df.columns])
                create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns});"
                cursor.execute(create_table_query)

                for _, row in df.iterrows():
                    row_values = ', '.join(["'{}'".format(str(value).replace("'", "''")) for value in row])
                    insert_query = f"INSERT INTO `{table_name}` VALUES ({row_values});"
                    cursor.execute(insert_query)

                print(f"Data imported into table: {table_name}")

        # Commit and close
        conn.commit()
        print("All data imported successfully.")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except FileNotFoundError as fnf_err:
        print(f"File Error: {fnf_err}")
    except ValueError as val_err:
        print(f"Value Error: {val_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()