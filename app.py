from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import joblib
import os

# --------------------------------------------
# Initialize Flask App
# --------------------------------------------
app = Flask(__name__)
app.secret_key = "macha_secret_key"

# --------------------------------------------
# Load ML Model and Vectorizer
# --------------------------------------------
MODEL_PATH = os.path.join("IBM", "model.pkl")
VECTORIZER_PATH = os.path.join("IBM", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# --------------------------------------------
# Routes
# --------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')

    if not url:
        return render_template('index.html', error="Please enter a valid URL.")

    # Transform the URL input into model features
    features = vectorizer.transform([url])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # Probability of being malicious

    # Convert probability to percentage
    malicious_percentage = round(probability * 100, 2)
    safe_percentage = 100 - malicious_percentage

    # Save data to session
    session['scan_data'] = {
        'url': url,
        'safe': safe_percentage,
        'malicious': malicious_percentage
    }

    return redirect(url_for('front'))

@app.route('/front')
def front():
    data = session.get('scan_data', None)
    return render_template('front.html', data=data)

# --------------------------------------------
# Run Flask
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
