# symptom_translation.py

symptom_translation = {
    "fever": "bukhar",
    "cough": "khaansi",
    "cold": "sardi",
    "headache": "sir dard",
    "nausea": "ji michlana",
    "vomiting": "ulti",
    "diarrhea": "dast",
    "fatigue": "thakaan",
    "sore throat": "gale mein kharash",
    "body ache": "shareer mein dard",
    "runny nose": "bahti naak",
    "sneezing": "chheenk aana",
    "itching": "khujli",
    "rash": "chakate",
    "shortness of breath": "saans phoolna",
    "chest pain": "seene mein dard",
    "joint pain": "jodon ka dard",
    "abdominal pain": "pet dard",
    "dizziness": "chakkar aana",
    "weight loss": "vajan kam hona",
    "dry skin": "sookhi twacha",
    "swelling": "soojan",
    "blurry vision": "dhundhli nazar",
    "irritability": "chidhchidhapan",
    "sweating": "paseena aana",
    "itchy skin": "khujli wali twacha",
    "scaly skin": "papdi wali twacha",
    "hoarseness": "aawaz bhari hona",
    "difficulty sleeping": "neend mein dikkat",
    "loss of appetite": "bhookh mein kami",
    "persistent sadness": "lagataar udaasi",
    "restlessness": "bechaini",
    "blurred vision": "dhundhli drishti",
    "confusion": "uljhan"
}

# Reverse map: Hinglish to English
reverse_symptom_translation = {
    v: k for k, v in symptom_translation.items()
}
