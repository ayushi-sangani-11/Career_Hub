import logging
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.text_extractor import extract_text_from_pdf_bytes
from services.skill_analyzer import extract_skills_from_text, analyze_resume_text, analyze_skill_gap
from services.job_matcher import calculate_job_match, rank_recommended_jobs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart_careerhub_ai")

app = FastAPI(
    title="Smart CareerHub AI & NLP Engine",
    description="Python FastAPI Microservice for Resume Analysis, Skill Extraction, Skill Gap Analysis & Job Recommendation",
    version="1.0.0"
)

# Enable CORS for Node.js backend and React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Schemas
class TextPayload(BaseModel):
    text: str

class SkillGapPayload(BaseModel):
    skills: List[str]
    targetRole: Optional[str] = "Full Stack Developer"

class JobMatchPayload(BaseModel):
    userSkills: List[str]
    requiredSkills: List[str]
    preferredSkills: Optional[List[str]] = []

class RecommendPayload(BaseModel):
    userSkills: List[str]
    targetRole: Optional[str] = "Full Stack Developer"
    jobs: List[Dict[str, Any]]

@app.get("/")
def health_check():
    return {
        "service": "Smart CareerHub AI & NLP Microservice",
        "status": "online",
        "version": "1.0.0"
    }

@app.post("/analyze-resume")
async def analyze_resume(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    try:
        extracted_text = ""
        if file:
            contents = await file.read()
            extracted_text = extract_text_from_pdf_bytes(contents)
        elif text:
            extracted_text = text.strip()
        else:
            raise HTTPException(status_code=400, detail="Either PDF file or text body must be provided.")

        if not extracted_text:
            raise HTTPException(status_code=400, detail="Unable to extract text from provided input.")

        analysis_result = analyze_resume_text(extracted_text)
        analysis_result["extractedText"] = extracted_text[:1000] # preview snippet
        return analysis_result

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error analyzing resume: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to analyze resume: {str(e)}")

@app.post("/extract-skills")
def extract_skills(payload: TextPayload):
    skills = extract_skills_from_text(payload.text)
    return {"skills": skills, "count": len(skills)}

@app.post("/skill-gap")
def skill_gap(payload: SkillGapPayload):
    result = analyze_skill_gap(payload.skills, payload.targetRole)
    return result

@app.post("/job-match")
def job_match(payload: JobMatchPayload):
    result = calculate_job_match(
        user_skills=payload.userSkills,
        required_skills=payload.requiredSkills,
        preferred_skills=payload.preferredSkills
    )
    return result

@app.post("/recommend")
def recommend_jobs(payload: RecommendPayload):
    recommendations = rank_recommended_jobs(
        user_skills=payload.userSkills,
        target_role=payload.targetRole,
        jobs=payload.jobs
    )
    return {"recommendations": recommendations, "total": len(recommendations)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
