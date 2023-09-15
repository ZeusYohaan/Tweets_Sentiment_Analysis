import pandas as pd
import pyodbc
from sqlalchemy import create_engine


class SQL:
    def __init__(self):
        self.server = 'DESKTOP-E0NOB13'
        self.database = 'MediaAnalytics'
        self.username = 'YoUser'
        self.password = '2004'
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.conn = pyodbc.connect(self.connection_string)
        self.curr = self.conn.cursor()
        self.sql_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={self.connection_string}")

    def upload_csv_sql(self, filename, table_name):
        pd_df = pd.read_csv(filename)
        pd_df.to_sql(table_name, con=self.sql_engine, if_exists='replace', index=False)
        self.conn.close()
        self.sql_engine.dispose()

    def get_pdDf_sql(self, tablename):
        sql_query = f"SELECT * FROM {tablename}"
        pd_df = pd.read_sql(sql_query, self.conn)
        return pd_df
