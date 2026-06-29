# 🛡️ AI Spam Detection System

An end-to-end **Machine Learning** web application that detects whether a given **SMS message** is **Spam** or **Not Spam**. The project is built using **Flask**, **Scikit-learn**, and **Natural Language Processing (NLP)** techniques. It features a modern responsive interface and is deployed online using **Render**.

> **Live Demo:** https://spam-detection-system-bii9.onrender.com

---

## 📌 Features

* 📱 SMS Spam Detection using Machine Learning
* 📧 Email Spam Detection page (Coming Soon)
* 🤖 TF-IDF based text feature extraction
* 🧠 Logistic Regression classifier with hyperparameter tuning
* 🌐 Flask web application
* 🎨 Modern responsive UI
* 📊 Confidence score for predictions
* 🚀 Deployed on Render

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask
* Python

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* GridSearchCV
* Pandas
* NumPy

---

## 📂 Project Structure

```text
Spam-Detection/
│
├── app.py
├── requirements.txt
│
├── model/
│   ├── SMS_Model.pkl
│   └── SMS_Transformer.pkl
│
├── static/
│   ├── home.css
│   └── sms.css
│
├── templates/
│   ├── home.html
│   ├── sms.html
│   └── email.html
│
└── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Collect and combine SMS spam datasets.
2. Clean the dataset by removing duplicates and handling missing values.
3. Split the data into training and testing sets.
4. Convert text into numerical features using **TF-IDF Vectorizer**.
5. Train a **Logistic Regression** model.
6. Tune hyperparameters using **GridSearchCV**.
7. Save the trained model and vectorizer using Pickle.
8. Deploy the Flask application on Render.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Sumit-Avasthi/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd SPAM-DETECTION-SYSTEM
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* 📧 Email Spam Detection
* 📂 Upload Email (.eml) files
* 📊 Prediction history
* 🌙 Dark/Light mode
* 🔍 Suspicious keyword highlighting
* 🧠 Deep Learning based spam detection

---

## 👨‍💻 Author

**Sumit Avasthi**

B.Tech Computer Science (Data Science)

Passionate about Machine Learning, Data Science, and Full-Stack Development.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
