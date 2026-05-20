# AI NutriCare 🥗🩺

**AI NutriCare** is an advanced AI-powered health monitoring and diet recommendation system. It processes patient medical reports, predicts ICU stay lengths, and generates highly personalized clinical diet plans tailored to Indian dietary habits using state-of-the-art Machine Learning and Large Language Models.

## 🚀 Features

- **Automated Medical Report Extraction:** Extracts vitals, demographics, and lab results directly from uploaded PDF medical reports using OCR and table extraction.
- **ICU Risk Prediction (ML):** Leverages an LSTM-based deep learning model to predict the probability of long vs. short ICU stays based on patient vitals.
- **Dynamic Clinical Interpretations:** Automatically analyzes lab values (e.g., Glucose, Creatinine, Hemoglobin, Sodium) and applies clinical rules to determine dietary constraints.
- **AI-Powered Diet Generation:** Uses the Groq LLM API (Llama 3.1) to generate personalized, day-by-day nutritional diet plans with complete macronutrient breakdowns.
- **PDF Report Generation:** Compiles all findings and the generated diet plan into a comprehensive, styled PDF report for patients and doctors.

## 🛠️ Technology Stack

### Backend
- **Framework:** FastAPI (Python)
- **Machine Learning:** TensorFlow / Keras (LSTM Model), Scikit-Learn
- **Document Processing:** PDFPlumber, Camelot, PyTesseract (OCR)
- **AI / LLM:** Groq API (Llama-3.1-8b-instant)
- **PDF Generation:** ReportLab

### Frontend
- **Framework:** React + Vite
- **Styling:** CSS
- **Integration:** REST APIs for seamless communication with the backend

## 📁 Project Structure

```
AI_NutriCare/
├── App/                # React (Vite) Frontend
├── backend/            # FastAPI Backend & API endpoints
├── Data/               # Raw and Transformed datasets
├── Notebooks/          # Jupyter notebooks for Data Processing & ML modeling
├── models/             # Saved Keras LSTM models and Scalers (Pickle)
└── README.md           # Project Documentation
```

## ⚙️ Setup Instructions

### 1. Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirments.txt
   ```
4. **Environment Variables:**
   Create a `.env` file in the `backend/` folder and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
5. **Run the FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd App
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Run the development server:**
   ```bash
   npm run dev
   ```

## 🧠 Machine Learning Model
The project uses an LSTM (Long Short-Term Memory) neural network trained on MIMIC-III ICU data to analyze sequential patient vitals (Heart Rate, MAP, SpO2, Glucose, etc.) and predict the severity of the patient's condition, determining the likelihood of an extended ICU stay.

## ⚠️ Important Note
This software is intended for educational and auxiliary purposes. The generated diet plans and clinical predictions should always be verified by certified healthcare professionals and dietitians before implementation.
