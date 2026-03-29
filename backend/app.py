from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import extract_text_from_pdf, extract_skills, calculate_score
from skills_db import skills_db

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    text = extract_text_from_pdf(file)

    results = {}

    for role, skills in skills_db.items():
        found = extract_skills(text, skills)
        missing = list(set(skills) - set(found))
        score = calculate_score(found, skills)

        results[role] = {
            "score": score,
            "found_skills": found,
            "missing_skills": missing
        }

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)