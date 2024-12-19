import pyodbc
class DBConnection:
    def __init__(self):
        self.conn = None
        self.stmt = None

    def open(self):
        try:
            connection_string = ( "Driver={ODBC  Server};"
                                "Server=YOURSERVER;"
                                "Database=Courier Management System;"
                                "TrustServerCertificate=yes;"
                                "Trusted_Connection=yes;"
            )
            self.conn = pyodbc.connect(connection_string)
            self.stmt = self.conn.cursor()
            print('--Database Is Connected:--')
        except Exception as e:
            print(str(e) + ' --Database Is Not Connected:--')
            sys.exit(1)

    def close(self):
        if self.stmt:
            self.stmt.close()
        if self.conn:
            self.conn.close()
            print('--Connection Is Closed:--')

