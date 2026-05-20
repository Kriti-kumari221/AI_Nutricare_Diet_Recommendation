from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import shutil
# ---- IMPORT YOUR EXISTING LOGIC ----
from services.pdf_pipeline import process_pdf_to_json
from services.diet_llm import generate_full_diet_plan

app = FastAPI(
    title="AI-NutriCare Backend",
    description="ICU-Aware Diet Planning System",
    version="1.0"
)

# ---- CORS (VERY IMPORTANT FOR REACT) ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- HEALTH CHECK ----
@app.get("/")
def root():
    return {"status": "AI-NutriCare backend running 🚀"}

# ---- MAIN ENDPOINT ----
@app.post("/generate-diet")
async def generate_diet(
    pdf: UploadFile = File(None),
    diet_type: str = Form("veg"),
    days: int = Form(3)
):
    """
    Receives:
    - PDF report (optional)
    - diet_type (veg / nonveg / both)
    - number of days

    Returns:
    - ICU risk prediction
    - Clinical findings
    - Multi-day diet plan
    """

    try:
        # ---------- 1. SAVE PDF ----------
        pdf_path = None
        if pdf:
            os.makedirs("temp", exist_ok=True)
            pdf_path = f"temp/{pdf.filename}"

            with open(pdf_path, "wb") as buffer:
                shutil.copyfileobj(pdf.file, buffer)

        # ---------- 2. ICU + NLP PIPELINE ----------
        patient_json = process_pdf_to_json(
            pdf_path if pdf_path else None
        )

        # ---------- 3. LLM DIET GENERATION ----------
        diet_plan = generate_full_diet_plan(
            final_patient_json=patient_json,
            diet_type=diet_type,
            days=days
        )

        # ---------- 4. CLEAN RESPONSE FOR UI ----------
        response = {
            "icu_prediction": patient_json["icu_prediction"],
            "clinical_findings": patient_json["clinical_interpretation"]["clinical_findings"],
            "diet_constraints": patient_json["clinical_interpretation"]["diet_constraints"],
            "diet_plan": diet_plan
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
