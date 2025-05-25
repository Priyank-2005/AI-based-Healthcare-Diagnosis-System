import sys
import os
from datetime import datetime
from database import disease_database
from symptom_translation import symptom_translation, reverse_symptom_translation
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Encoding fix for Windows
if os.name == "nt":
    sys.stdout.reconfigure(encoding="utf-8")

# Language Selection
print("Choose your language / Apni bhasha chunein:")
print("1. English")
print("2. Hinglish (Hindi in English letters)")
lang_choice = input("Enter choice (1 or 2): ")

LANG = "hindi" if lang_choice == "2" else "english"
print("\nWelcome!" if LANG == "english" else "Swagat hai aapka Healthcare AI mein!")

#  Ask for Name and Age
print("\nPlease enter your details:" if LANG == "english" else "\nApna naam aur umar batayein:")
user_name = input("Name: " if LANG == "english" else "Naam: ")
user_age = input("Age: " if LANG == "english" else "Umar: ")

# Translate Hinglish inputs
def translate_symptom(symptom, lang):
    return symptom_translation.get(symptom.lower(), symptom) if lang == "hindi" else symptom

def normalize_symptoms(symptom_list):
    normalized = []
    for s in symptom_list:
        s = s.lower().strip()
        normalized.append(reverse_symptom_translation.get(s, s))
    return normalized

# Disease matching logic
def match_diseases(user_symptoms):
    disease_scores = {}

    for disease, data in disease_database.items():
        symptom_dict = data["symptoms"]
        matched = [s for s in user_symptoms if s in symptom_dict]

        if matched:
            matched_score = sum(symptom_dict[s] for s in matched)
            total_score = sum(symptom_dict.values())
            confidence = int((matched_score / total_score) * 100)

            disease_scores[disease] = {
                "confidence": confidence,
                "matched": matched
            }

    return dict(sorted(disease_scores.items(), key=lambda x: x[1]["confidence"], reverse=True))

# Display Results
def display_results(results, lang):
    if not results:
        print("\nNo disease matched with given symptoms.")
        return

    top_results = list(results.items())[:3]
    for disease, info in top_results:
        data = disease_database[disease]
        name = data["hindi_name"] if lang == "hindi" else disease
        confidence = info["confidence"]
        matched = info["matched"]

        print(f"\nDiagnosis: {name}")
        print(f"Confidence: {confidence}%")
        print("Symptoms:")
        for s in matched:
            print(f"  {translate_symptom(s, lang)}")

        print("\n", "Kya karein:" if lang == "hindi" else "What to do:")
        for d in data["recommendations"]["do"]:
            print(f"  {d}")
        print("Kya na karein:" if lang == "hindi" else "What not to do:")
        for d in data["recommendations"]["dont"]:
            print(f"  {d}")
        print("-" * 40)

# Save to text file
def save_to_history(user_symptoms, results, name, age):
    with open("diagnosis_history.txt", "a", encoding="utf-8") as f:
        f.write(f"--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        f.write(f"Name: {name}, Age: {age}\n")
        f.write(f"Symptoms: {', '.join(user_symptoms)}\n")
        for disease, info in list(results.items())[:3]:
            f.write(f"- {disease} ({info['confidence']}%)\n")
        f.write("\n")
    print("Diagnosis saved to diagnosis_history.txt")

# 📄 Export to PDF
def export_to_pdf(results, lang, user_symptoms, name, age):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"diagnosis_{now}.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Healthcare AI Diagnosis Report")

    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}")
    y -= 20
    c.drawString(50, y, f"Name: {name}, Age: {age}")
    y -= 20
    c.drawString(50, y, f"Symptoms: {', '.join(user_symptoms)}")
    y -= 30

    for disease, info in list(results.items())[:3]:
        data = disease_database[disease]
        name = data["hindi_name"] if lang == "hindi" else disease

        c.setFont("Helvetica-Bold", 13)
        c.drawString(50, y, f"Disease: {name} ({info['confidence']}%)")
        y -= 20

        c.setFont("Helvetica", 11)
        c.drawString(60, y, f"Matched Symptoms: {', '.join(info['matched'])}")
        y -= 20

        c.drawString(60, y, "Do:")
        for item in data["recommendations"]["do"]:
            y -= 15
            c.drawString(80, y, f"✔ {item}")
        y -= 20
        c.drawString(60, y, "Don't:")
        for item in data["recommendations"]["dont"]:
            y -= 15
            c.drawString(80, y, f"❌ {item}")
        y -= 30

    c.save()
    print(f"PDF saved as: {file_name}")

# Run the diagnosis
while True:
    print("\n" + ("Enter your symptoms (comma-separated):" if LANG == "english" else "Apne lakshan batayein (comma se alag karein):"))
    raw_input = input(">> ")

    if raw_input.strip().lower() in ["exit", "quit"]:
        print("Goodbye! Stay healthy!" if LANG == "english" else "Alvida! Swasth rahiye!")
        break

    raw_symptoms = [s.strip() for s in raw_input.split(",")]
    user_symptoms = normalize_symptoms(raw_symptoms)

    results = match_diseases(user_symptoms)
    display_results(results, LANG)
    save_to_history(user_symptoms, results, user_name, user_age)
    export_to_pdf(results, LANG, user_symptoms, user_name, user_age)
