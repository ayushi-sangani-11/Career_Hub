import re
from typing import List, Dict, Any
from data.skill_taxonomy import SKILL_TAXONOMY, ROLE_REQUIREMENTS, SKILL_SYNONYMS

def normalize_skill(skill: str) -> str:
    """
    Normalizes skill name using SKILL_SYNONYMS map or standard title case.
    """
    if not skill:
        return ""
    clean = skill.strip().lower()
    if clean in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[clean]
    return skill.strip()

def extract_skills_from_text(text: str) -> List[str]:
    """
    Extracts known skills from raw text using boundary-sensitive regex matching and synonym normalization.
    """
    if not text:
        return []

    text_lower = text.lower()
    detected = set()

    for category, skill_list in SKILL_TAXONOMY.items():
        for skill in skill_list:
            skill_escaped = re.escape(skill.lower())
            if len(skill) <= 2:
                pattern = r'(?<![a-zA-Z0-9])' + skill_escaped + r'(?![a-zA-Z0-9])'
            else:
                pattern = r'\b' + skill_escaped + r'\b'
            
            if re.search(pattern, text_lower):
                normalized = normalize_skill(skill)
                detected.add(normalized)

    # Sort alphabetically
    result = sorted(list(detected))
    return result

def analyze_resume_text(text: str) -> Dict[str, Any]:
    """
    Performs comprehensive analysis of resume text.
    Computes overall score (0-100) and section breakdown scores.
    """
    text_lower = text.lower() if text else ""
    detected_skills = extract_skills_from_text(text)

    # Skills Score
    skill_count = len(detected_skills)
    if skill_count >= 10:
        skills_score = 95
    elif skill_count >= 7:
        skills_score = 85
    elif skill_count >= 5:
        skills_score = 75
    elif skill_count >= 3:
        skills_score = 60
    elif skill_count >= 1:
        skills_score = 45
    else:
        skills_score = 25

    # Projects Score
    project_keywords = ["project", "developed", "built", "created", "implemented", "system", "app", "application", "github", "designed", "architecture"]
    project_hits = sum(1 for kw in project_keywords if kw in text_lower)
    projects_score = min(100, max(30, project_hits * 12))

    # Education Score
    edu_keywords = ["bachelor", "b.tech", "degree", "university", "college", "gpa", "cgpa", "computer science", "engineering", "b.e", "m.tech", "diploma"]
    edu_hits = sum(1 for kw in edu_keywords if kw in text_lower)
    education_score = min(100, max(40, edu_hits * 25))

    # Experience Score
    exp_keywords = ["internship", "experience", "work", "role", "developer", "engineer", "lead", "responsibilities", "collaborated", "contributed"]
    exp_hits = sum(1 for kw in exp_keywords if kw in text_lower)
    experience_score = min(100, max(35, exp_hits * 18))

    # Keywords Score
    action_keywords = ["optimized", "managed", "scaled", "deployed", "integrated", "automated", "tested", "rest", "agile", "database", "cloud"]
    keyword_hits = sum(1 for kw in action_keywords if kw in text_lower)
    keywords_score = min(100, max(30, keyword_hits * 14))

    # Weighted Overall Score
    overall_score = round(
        (skills_score * 0.35) +
        (projects_score * 0.20) +
        (education_score * 0.15) +
        (experience_score * 0.15) +
        (keywords_score * 0.15)
    )

    # Detect Sections
    sections = []
    if any(k in text_lower for k in ["education", "academic", "qualification"]):
        sections.append("Education")
    if any(k in text_lower for k in ["skill", "technologies", "tech stack", "expertise"]):
        sections.append("Skills")
    if any(k in text_lower for k in ["project", "portfolio", "work done"]):
        sections.append("Projects")
    if any(k in text_lower for k in ["experience", "employment", "internship", "work history"]):
        sections.append("Experience")
    if any(k in text_lower for k in ["certification", "certificates", "license"]):
        sections.append("Certifications")

    suggestions = []
    if skills_score < 75:
        suggestions.append("Add more specific technical skills and tools relevant to your target career role.")
    if projects_score < 70:
        suggestions.append("Highlight 2-3 key technical projects with measurable outcomes.")
    if experience_score < 60:
        suggestions.append("Include internship experiences, open-source contributions, or freelance projects.")

    if not suggestions:
        suggestions.append("Great resume! Keep updating it with your latest accomplishments.")

    return {
        "score": overall_score,
        "categoryScores": {
            "skills": skills_score,
            "projects": projects_score,
            "education": education_score,
            "experience": experience_score,
            "keywords": keywords_score
        },
        "detectedSkills": detected_skills,
        "detectedSections": sections,
        "suggestions": suggestions,
        "wordCount": len(text.split()) if text else 0
    }

def analyze_job_specific_resume(
    resume_text: str,
    job_title: str,
    required_skills: List[str],
    preferred_skills: List[str] = None,
    job_description: str = ""
) -> Dict[str, Any]:
    """
    Central Logic: RESUME + SPECIFIC JOB REQUIREMENTS = JOB-SPECIFIC SKILL GAP REPORT.
    Compares candidate's resume against a specific job's requirements and produces tailored results.
    """
    if preferred_skills is None:
        preferred_skills = []

    resume_skills = extract_skills_from_text(resume_text)
    
    # Also extract any additional skills mentioned directly in job description
    extracted_job_skills = extract_skills_from_text(job_description) if job_description else []

    # Merge required skills & normalize
    normalized_req = [normalize_skill(s) for s in required_skills]
    # If required_skills is empty, use extracted job skills
    if not normalized_req and extracted_job_skills:
        normalized_req = extracted_job_skills[:6]

    normalized_pref = [normalize_skill(s) for s in preferred_skills]

    user_skills_lower = {s.lower() for s in resume_skills}
    # Also check raw text for skills that might be written in specific context
    resume_text_lower = resume_text.lower() if resume_text else ""

    matched_skills = []
    missing_skills = []
    partial_skills = []

    for req in normalized_req:
        req_lower = req.lower()
        if req_lower in user_skills_lower or (len(req) > 2 and req_lower in resume_text_lower):
            matched_skills.append(req)
        else:
            # Check for partial match (e.g. "Cloud" if "AWS" is present)
            if any(req_lower in u or u in req_lower for u in user_skills_lower):
                partial_skills.append(req)
            else:
                missing_skills.append(req)

    for pref in normalized_pref:
        pref_lower = pref.lower()
        if pref_lower in user_skills_lower or (len(pref) > 2 and pref_lower in resume_text_lower):
            if pref not in matched_skills:
                matched_skills.append(pref)
        elif pref not in missing_skills and pref not in partial_skills:
            missing_skills.append(pref)

    total_req = len(normalized_req) if normalized_req else 1
    matched_req_count = sum(1 for req in normalized_req if req in matched_skills or req in partial_skills)
    
    # Match percentage calculation
    raw_pct = (matched_req_count / total_req) * 100.0
    match_percentage = min(99, max(15, round(raw_pct)))

    # Detailed advice & improvement recommendations
    recommendations = []
    if missing_skills:
        for skill in missing_skills[:4]:
            recommendations.append(f"Learn {skill}: Listed as a key requirement in the {job_title} job description.")
    else:
        recommendations.append("You match all key required skills for this job! Review your project experience before applying.")

    return {
        "jobTitle": job_title,
        "matchPercentage": match_percentage,
        "matchedCount": len(matched_skills),
        "totalRequired": len(normalized_req),
        "matchedSkills": matched_skills,
        "missingSkills": missing_skills,
        "partialSkills": partial_skills,
        "detectedResumeSkills": resume_skills,
        "recommendations": recommendations,
        "disclaimer": "This match percentage is an AI-assisted comparison based on available job requirements and resume text, not a guarantee of employment or hiring."
    }
