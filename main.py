from flask import Flask,render_template,request
import pymysql


app = Flask(__name__)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='xxxxxxxxxx',
    database='form'
)
cursor = connection.cursor()

@app.route("/", methods=['GET', 'POST'])    #homepage
def homepage():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        role = request.form['role']
        print(first_name,last_name, email, date, role)

        insert_query = "INSERT INTO ENTRY (first_name, last_name, email, date, role) VALUES (%s, %s, %s, %s, %s)" #write into databse
        values = (first_name, last_name, email, date, role)
        cursor.execute(insert_query, values)
        connection.commit()
    

        

    return render_template('index.html')


app.run(debug=True, port=5001)