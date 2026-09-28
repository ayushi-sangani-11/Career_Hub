import logging
import json
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.text_extractor import extract_text_from_pdf_bytes
from services.skill_analyzer import extract_skills_from_text, analyze_resume_text, analyze_skill_gap, analyze_job_specific_resume
from services.job_matcher import calculate_job_match, rank_recommended_jobs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart_careerhub_ai")

app = FastAPI(
    title="Smart CareerHub AI & NLP Engine",
    description="Python FastAPI Microservice for Job-Specific Resume & Skill Gap Analysis",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextPayload(BaseModel):
    text: str

class SkillGapPayload(BaseModel):
    skills: List[str]
    targetRole: Optional[str] = "Software Developer"

class JobMatchPayload(BaseModel):
    userSkills: List[str]
    requiredSkills: List[str]
    preferredSkills: Optional[List[str]] = []

class RecommendPayload(BaseModel):
    userSkills: List[str]
    targetRole: Optional[str] = "Software Developer"
    jobs: List[Dict[str, Any]]

class JobResumeAnalysisPayload(BaseModel):
    resumeText: str
    jobTitle: str
    requiredSkills: List[str]
    preferredSkills: Optional[List[str]] = []
    jobDescription: Optional[str] = ""

@app.get("/")
def health_check():
    return {
        "service": "Smart CareerHub AI & NLP Microservice",
        "status": "online",
        "version": "2.0.0"
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
        analysis_result["extractedText"] = extracted_text[:1000]
        return analysis_result

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error analyzing resume: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to analyze resume: {str(e)}")

@app.post("/analyze-resume-job")
async def analyze_resume_job(
    file: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None),
    job_title: str = Form("Target Role"),
    required_skills: Optional[str] = Form("[]"),
    preferred_skills: Optional[str] = Form("[]"),
    job_description: Optional[str] = Form("")
):
    """
    Primary Endpoint: Analyzes candidate resume specifically against a target job's requirements.
    Supports both file upload and text input, along with form fields or JSON payload.
    """
    try:
        extracted_text = ""
        if file:
            contents = await file.read()
            extracted_text = extract_text_from_pdf_bytes(contents)
        elif resume_text:
            extracted_text = resume_text.strip()

        if not extracted_text:
            extracted_text = "Experienced candidate seeking role."

        req_list = json.loads(required_skills) if isinstance(required_skills, str) and required_skills.startswith("[") else ([s.strip() for s in required_skills.split(",")] if required_skills else [])
        pref_list = json.loads(preferred_skills) if isinstance(preferred_skills, str) and preferred_skills.startswith("[") else ([s.strip() for s in preferred_skills.split(",")] if preferred_skills else [])

        result = analyze_job_specific_resume(
            resume_text=extracted_text,
            job_title=job_title,
            required_skills=req_list,
            preferred_skills=pref_list,
            job_description=job_description or ""
        )
        return result

    except Exception as e:
        logger.error(f"Error analyzing job resume: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to analyze resume against job: {str(e)}")

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
