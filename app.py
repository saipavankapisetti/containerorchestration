import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM paddy_calculator')
    result = cur.fetchone()
    cur.close()
    return render_template('index.html', result=result)

@app.route('/calculate', methods=['POST'])
def calculate():
    num_bags = int(request.form['num_bags'])
    bag_weight = float(request.form['bag_weight'])
    price_per_bag = float(request.form['price_per_bag'])

    total_weight_kg = (num_bags * bag_weight) / 75.0
    total_amount = price_per_bag * total_weight_kg

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO paddy_calculator (num_bags, bag_weight, price_per_bag, total_weight_kg, total_amount) VALUES (%s, %s, %s, %s, %s)",
                (num_bags, bag_weight, price_per_bag, total_weight_kg, total_amount))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
