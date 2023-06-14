import pandas as pd
import pyodbc
import os


class AzureSQLDataExporter:
    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path

    def read_credentials_from_file(self):
        with open(self.credentials_file_path, "r") as file:
            lines = file.readlines()
            data = [line.strip() for line in lines]
        return data

    def export_data_to_excel(self):
        # Fetch the credentials from the file
        fetched_credentials = self.read_credentials_from_file()

        # Pass the fetched credentials to the AzureSQLDataExporter object
        server = fetched_credentials[1]
#         database = fetched_credentials[2]
#         username = fetched_credentials[3]
        password = fetched_credentials[4]
        

        # Establish a connection to the Azure SQL Server
        conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        conn = pyodbc.connect(conn_str)

        # Fetch all table names
        cursor = conn.cursor()
        query = "SELECT name FROM sys.tables"
        table_names = [row[0] for row in cursor.execute(query)]

        # Create an empty DataFrame to store the combined data
        combined_data = pd.DataFrame()

        # Fetch data from each table and combine it
        for table_name in table_names:
            # Retrieve the data from the table
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, conn)

            # Add the table name as a column in the DataFrame
            df['Table'] = table_name

            # Append the data to the combined DataFrame
            combined_data = combined_data.append(df, ignore_index=True)

        # Export the combined data to an Excel file
        excel_file = 'combined_data.xlsx'
        combined_data.to_excel(excel_file, index=False)
        print(f"All data exported to '{excel_file}'")

        # Close the connection
        conn.close()


# Usage:
credentials_file_path = os.path.join('cred.txt')
data_exporter = AzureSQLDataExporter(credentials_file_path)
data_exporter.export_data_to_excel()
