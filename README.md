# Flask MongoDB Form API

A simple web application built using **Flask** and **MongoDB** that allows users to submit their name and email through a web form. The submitted data is stored in a MongoDB database.

## 🚀 Features

* User registration form
* Collects Name and Email
* Stores submitted data in MongoDB
* Success page after successful submission
* Error handling for database operations
* Environment variable support using `.env`

## 🛠️ Tech Stack

* **Backend:** Flask
* **Database:** MongoDB
* **Frontend:** HTML
* **Environment Management:** python-dotenv
* **Database Driver:** PyMongo

## 📂 Project Structure

```text
project/
│
├── app.py
├── .env
├── requirements.txt
│
├── templates/
│   ├── form.html
│   └── success.html
│
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/workneel2111/Devops_3
cd Devops_3
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask pymongo python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URL=your_mongodb_connection_string
```

## ▶️ Running the Application

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

## 📋 Application Workflow

1. User opens the registration form.
2. User enters their name and email.
3. Flask receives the form data.
4. Data is inserted into MongoDB.
5. User is redirected to the success page.
6. If an error occurs, an error message is displayed.

## 🗄️ Database Structure

Database:

```text
studentdb
```

Collection:

```text
students
```

Sample Document:

```json
{
  "_id": "ObjectId(...)",
  "name": "John Doe",
  "email": "john@example.com"
}
```

## 📸 Screenshots

You can add screenshots of:

* Registration Form
* Success Page
* MongoDB Collection Data

## 📚 Learning Objectives

This project demonstrates:

* Flask routing
* Handling GET and POST requests
* Working with HTML forms
* Connecting Flask with MongoDB
* Using environment variables securely
* Basic error handling

## 👨‍💻 Author

Neel Patel

## 📄 License

This project is created for learning and educational purposes.
