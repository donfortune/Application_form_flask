from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])    #homepage
def homepage():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        role = request.form['role']
        print(first_name,last_name, email, date, role)

        

    return render_template('index.html')


app.run(debug=True, port=5001)