from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

print("Current Directory:", os.getcwd())

app = Flask(__name__)

client = MongoClient(
"mongodb+srv://neel:neel123@cluster0.3nwaelx.mongodb.net/?appName=Cluster0"
)

db = client["studentdb"]
collection = db["students"]

@app.route('/', methods=['GET','POST'])
def form():

    if request.method == 'POST':

        try:

            data = {
                "name": request.form['name'],
                "email": request.form['email']
            }

            collection.insert_one(data)

            return redirect(url_for('success'))

        except Exception as e:

            return render_template(
                'form.html',
                error=str(e)
            )

    return render_template('form.html')

@app.route('/success')
def success():

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)