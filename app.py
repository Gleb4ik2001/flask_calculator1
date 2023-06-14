# Flask
from flask import Flask,render_template,request

# python-decouple
from decouple import config

# Local
from database.log_db import LogDataBase
from database.inserting import Inserting

# database connection variable - connection
connection :LogDataBase=LogDataBase(
    host=config('DB_HOST',str),
    port=config('DB_PORT',int),
    user=config('DB_USER',str),
    db_name=config('DB_NAME',str),
    password=config('DB_PASSWORD',str)
)

# Flask variable - app
app = Flask(__name__)

# "/" route
@app.route('/',methods=['POST','GET'])
def index():
    #if button submit has pushed we are taking values from form and looking what action user has chosen
    # depend on what action had chosen firstly we are insertind data in database, secondly posting the result in Jinja form
    if request.method=="POST":
        first_digit = float(request.form.get('first_digit'))
        second_digit = float(request.form.get('second_digit'))
        action = request.form.get('action')
        if action == "plus":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit+second_digit
            ))
            return render_template('index.html',answer = first_digit+second_digit)
        elif action =="minus":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit-second_digit
            ))
            return render_template('index.html',answer = first_digit-second_digit)
        elif action =="multiply":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit*second_digit
            ))
            return render_template('index.html',answer = first_digit*second_digit)
        elif action =="divide":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit/second_digit
            ))
            return render_template('index.html',answer = first_digit/second_digit)
        elif action =="exponentiate":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit**second_digit
            ))
            return render_template('index.html',answer = first_digit**second_digit)
        elif action =="extract_the_root":
            print(Inserting.insert_data(
                conn=connection.conn,
                first_value=first_digit,
                second_value=second_digit,
                action=action,
                result=first_digit**(1/second_digit)
            ))
            return render_template('index.html',answer = first_digit**(1/second_digit))
    return render_template('index.html')

# method only for create table

# @app.route('/api/v1/createTable',methods=["GET"])
# def create_table():
#     return connection.create_table()

#check for main file
if __name__=="__main__":
    app.run(debug=False)