# 📬 Email Spam Classifier

A simple Streamlit-based web app that classifies email content as **Spam** or **Not Spam** using a logistic regression model trained on real-world data.

---

## 🎯 Features

- Input email text and get a prediction instantly
- Displays model confidence score
- Trained on a public spam dataset
- Educational and easy-to-understand interface
- Clean, modular Python code

---

## 🧠 How It Works

1. Cleans input text (removes URLs, numbers, symbols)
2. Transforms it using `CountVectorizer`
3. Predicts with a logistic regression model
4. Displays label and confidence score

---

## 🗃️ Dataset

- Used: [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)  
- ~5,500 messages labeled as spam or ham

---

## ⚙️ Installation

```bash
git clone https://github.com/santanuhaldarone/Spam-Email-Classifier.git
cd spam-classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
