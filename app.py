from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------- QUIZ ----------------
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# ---------------- SUBMIT ----------------
@app.route('/submit', methods=['POST'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    stream = request.form['stream']

    love = request.form['love']
    skill = request.form['skill']
    mission = request.form['mission']
    money = request.form['money']

    # -------- SIMPLE IKIGAI LOGIC --------
    if love == "Technology" and skill == "Problem Solving":
        career = "Software Developer / Data Analyst"
    elif love == "Helping People" and skill == "Communication":
        career = "Teacher / Counselor"
    elif love == "Business" and skill == "Leadership":
        career = "Entrepreneur / Manager"
    elif love == "Art & Creativity":
        career = "Designer / Content Creator"
    else:
        career = "Explore multidisciplinary careers"

    # -------- SAVE TO CSV --------
    file_exists = os.path.isfile('data.csv')

    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        # Add header if file is empty
        if not file_exists:
            writer.writerow([
                "Age", "Gender", "Stream",
                "Love", "Skill", "Mission", "Money",
                "Career"
            ])

        writer.writerow([
            age, gender, stream,
            love, skill, mission, money,
            career
        ])

    return render_template('result.html', career=career)


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    data = []

    try:
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
    except:
        data = []

    total = len(data) - 1 if len(data) > 0 else 0  # remove header

    return render_template('dashboard.html', data=data, total=total)


# ---------------- REPORT ----------------
@app.route('/report')
def report():
    return render_template('report.html')


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)