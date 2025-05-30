﻿# AI-based-Healthcare-Diagnosis-System
A smart, multilingual, AI-powered terminal application that helps users **identify possible diseases based on their symptoms**, and provides **custom health advice and recommendations** — all from your command line!

---

## Features

-  **Symptom-to-Disease Diagnosis** using weighted matching logic.
-  **Multilingual Input** – Supports both **English** and **Hinglish (Hindi in Roman script)**.
-  **PDF Report Export** – Generates a clear and professional report of diagnosis and suggestions.
-  **Diagnosis History Log** – Saves user name, age, symptoms, and diagnosis in a log file.
-  **Treatment Guidance** – Tells you what to do and what to avoid for each predicted disease.
-  **Includes 50+ Diseases** with symptoms, severity scores, and Hindi names.

---

##  How It Works

1. User selects their preferred language (English or Hinglish).
2. They enter their **name**, **age**, and list of symptoms (comma-separated).
3. The system:
   - Translates symptoms (if in Hinglish),
   - Matches symptoms to diseases using a weighted score,
   - Calculates confidence levels,
   - Displays top 3 most likely diseases,
   - Shows helpful **do's and don’ts** for each condition.
4. Finally, it:
   - Saves the diagnosis to a log file (`diagnosis_history.txt`)
   - Creates a **PDF report** with all relevant details.

---

## Further Improvements

-Add a Graphical User Interface (GUI) using Tkinter or a web-based front-end like React.
-Voice Input Support – Allow users to speak symptoms using speech recognition.
-AI/ML Integration – Upgrade the rule-based system to use machine learning for smarter predictions.
-Mobile App Version – Develop an Android/iOS app for broader accessibility.
-More Languages – Support additional languages like Gujarati, Marathi, Tamil, etc.
-Symptom Autocomplete – Suggest symptoms as the user types, based on fuzzy matching.
-Cloud Sync and Analytics – Store diagnosis history securely online with user-friendly charts.
-Printable Reports – Export well-designed, clinic-style printable reports.
-Disease Stats Dashboard – Visualize common diseases diagnosed over time.
-User Authentication – Secure diagnosis history with login/signup support.

---

##  Files and Structure

├── diagnosis.py # Main program (input, diagnosis logic, PDF + logging)
├── database.py # Contains disease database, symptoms, weights, Hindi names
├── symptom_translation.py # English ↔ Hinglish symptom mappings
├── diagnosis_history.txt # Log of all past diagnosis results
