from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Get MongoDB connection string from .env
mongo_url = os.getenv("MONGO_URL")

# Create MongoDB client
client = MongoClient(mongo_url)

# Database and collection
db = client["studentdb"]
collection = db["students"]

@app.route('/', methods=['GET', 'POST'])
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
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))