from database.log_db import LogDataBase

# class for inserting and findind data 
class Inserting:
    first_value:float
    second_value:float
    action:str
    result:float

    @staticmethod
    def insert_data(
        conn:LogDataBase,
        first_value:float,
        second_value:float,
        action:str,
        result:float
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO logs(
                    first_value,
                    second_value,
                    action,
                    result
                    )VALUES(
                        {first_value},
                        {second_value},
                        '{action}',
                        {result}
                    )
                """)
            print("Log successfully inserted")
        except Exception as e:
            print('Log inserting ERROR:',e)
        
    @staticmethod
    def select_full_data(conn:LogDataBase):
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM logs
                """)
                result = cur.fetchall()
                print(result)
        except Exception as e:
            print('Selecting data ERROR:',e)