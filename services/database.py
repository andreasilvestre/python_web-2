import pyodbc

SERVER = 'localhost\sqlexpress'
DATABASE = 'crud'
USERNAME = "ANDREA\\andre"
PASSWORD = ''


#connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
#cnxn = pyodbc.connect(connectionString)

cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}', server = 'localhost\sqlexpress', database = 'crud')

cursor = cnxn.cursor()