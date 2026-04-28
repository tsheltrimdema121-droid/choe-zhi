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
    age = request.form.get('age')
    gender = request.form.get('gender')
    stream = request.form.get('stream')

    answers = []
    for i in range(1, 21):
        answers.append(request.form.get(f"q{i}"))

    # IKIGAI LOGIC
    tech_score = sum(1 for a in answers if a == "Technology")
    help_score = sum(1 for a in answers if a == "Helping")
    business_score = sum(1 for a in answers if a == "Business")
    creative_score = sum(1 for a in answers if a == "Creative")
    science_score = sum(1 for a in answers if a == "Science")

    scores = {
        "Technology": tech_score,
        "Helping": help_score,
        "Business": business_score,
        "Creative": creative_score,
        "Science": science_score
    }

    career_type = max(scores, key=scores.get)

    if career_type == "Technology":
        career = "Software Developer / Data Analyst"
    elif career_type == "Helping":
        career = "Teacher / Counselor"
    elif career_type == "Business":
        career = "Entrepreneur / Manager"
    elif career_type == "Creative":
        career = "Designer / Content Creator"
    else:
        career = "Scientist / Researcher"

    # SAVE CSV
    file_exists = os.path.isfile('data.csv')

    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            header = ["Age", "Gender", "Stream"] + [f"Q{i}" for i in range(1, 21)] + ["Career"]
            writer.writerow(header)

        writer.writerow([age, gender, stream] + answers + [career])

    return render_template('result.html', career=career)


# ---------------- REPORT ----------------
@app.route('/report')
def report():
    return render_template('report.html')


# ---------------- RESEARCH ----------------
@app.route('/research')
def research():
    data = []

    try:
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
    except:
        data = []

    total = len(data) - 1 if len(data) > 0 else 0

    return render_template('research.html', data=data, total=total)


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)