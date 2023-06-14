#lib for database connection and executing
import psycopg2

class LogDataBase:
    #singleton pattern for only one variable to connect db
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(LogDataBase,cls).__new__(cls)
        return cls.instance
    
    #__init__ contains data that we need to connect database
    def __init__(self,host,port,user,db_name,password) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.db_name = db_name
        self.password = password
        self.conn = None
        try:
            self.conn=psycopg2.connect(
                host=self.host,
                port = self.port,
                user = self.user,
                password=self.password,
                database = self.db_name
            )
            self.conn.autocommit=True
            print("Database has been connected successfully")
        except Exception as e:
            print("ERROR:",e)

    # create table method 
    def create_table(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS logs(
                        id SERIAL PRIMARY KEY,
                        first_value DECIMAL NOT NULL,
                        second_value DECIMAL NOT NULL,
                        action VARCHAR(32) NOT NULL,
                        result DECIMAL NOT NULL 
                    )
                ''')
                print('Table "logs" successfully created')
                return 0
        except Exception as e:
            print('Table creating error:',e)
            return 1
        
