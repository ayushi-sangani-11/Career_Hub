import re
from typing import List, Dict, Any
from data.skill_taxonomy import SKILL_TAXONOMY, ROLE_REQUIREMENTS

def extract_skills_from_text(text: str) -> List[str]:
    """
    Extracts known skills from raw text using boundary-sensitive regex matching.
    """
    if not text:
        return []

    text_lower = text.lower()
    detected = set()

    for category, skill_list in SKILL_TAXONOMY.items():
        for skill in skill_list:
            skill_escaped = re.escape(skill.lower())
            # For short skills like 'C', 'R', use strict word boundaries
            if len(skill) <= 2:
                pattern = r'(?<![a-zA-Z0-9])' + skill_escaped + r'(?![a-zA-Z0-9])'
            else:
                pattern = r'\b' + skill_escaped + r'\b'
            
            if re.search(pattern, text_lower):
                # Standardize display format
                detected.add(skill)

    # Clean duplicates like 'React' and 'React.js' into single representations if both present
    result = list(detected)

    # Sort alphabetically
    result.sort()
    return result

def analyze_resume_text(text: str) -> Dict[str, Any]:
    """
    Performs comprehensive analysis of resume text.
    Computes overall score (0-100) and section breakdown scores.
    """
    text_lower = text.lower() if text else ""
    detected_skills = extract_skills_from_text(text)

    # Category Scoring Logic
    # 1. Skills Score (0-100)
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

    # 2. Projects Score (0-100)
    project_keywords = ["project", "developed", "built", "created", "implemented", "system", "app", "application", "github", "designed", "architecture"]
    project_hits = sum(1 for kw in project_keywords if kw in text_lower)
    projects_score = min(100, max(30, project_hits * 12))

    # 3. Education Score (0-100)
    edu_keywords = ["bachelor", "b.tech", "degree", "university", "college", "gpa", "cgpa", "computer science", "engineering", "b.e", "m.tech", "diploma"]
    edu_hits = sum(1 for kw in edu_keywords if kw in text_lower)
    education_score = min(100, max(40, edu_hits * 25))

    # 4. Experience Score (0-100)
    exp_keywords = ["internship", "experience", "work", "role", "developer", "engineer", "lead", "responsibilities", "collaborated", "contributed"]
    exp_hits = sum(1 for kw in exp_keywords if kw in text_lower)
    experience_score = min(100, max(35, exp_hits * 18))

    # 5. Keywords & Formatting Score (0-100)
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

    # Generate Recommendations
    suggestions = []
    if skills_score < 75:
        suggestions.append("Add more specific technical skills and tools relevant to your target career role.")
    if projects_score < 70:
        suggestions.append("Highlight 2-3 key technical projects with measurable outcomes and GitHub repository links.")
    if experience_score < 60:
        suggestions.append("Include internship experiences, open-source contributions, or freelance projects.")
    if keywords_score < 70:
        suggestions.append("Use strong action verbs such as 'optimized', 'architected', 'integrated', and 'deployed'.")
    if "Certifications" not in sections:
        suggestions.append("Consider adding relevant industry certifications (e.g. AWS, Meta React, MongoDB).")

    if not suggestions:
        suggestions.append("Great resume! Keep updating it with your latest accomplishments and project metrics.")

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

def analyze_skill_gap(user_skills: List[str], target_role: str) -> Dict[str, Any]:
    """
    Compares student's current skills against target career role requirements.
    """
    role_info = ROLE_REQUIREMENTS.get(target_role)
    if not role_info:
        # Default fallback role info if role not explicitly in benchmark dictionary
        role_info = ROLE_REQUIREMENTS.get("Full Stack Developer")
        target_role = "Full Stack Developer"

    required_skills = role_info["required"]
    preferred_skills = role_info["preferred"]

    # Normalize user skills for flexible comparison
    user_skills_lower = {s.lower() for s in user_skills}

    strong_skills = []
    missing_required = []
    missing_preferred = []

    for req in required_skills:
        if req.lower() in user_skills_lower or any(u in req.lower() for u in user_skills_lower):
            strong_skills.append(req)
        else:
            missing_required.append(req)

    for pref in preferred_skills:
        if pref.lower() in user_skills_lower or any(u in pref.lower() for u in user_skills_lower):
            if pref not in strong_skills:
                strong_skills.append(pref)
        else:
            missing_preferred.append(pref)

    # Readiness Score Calculation
    req_match_pct = (len(strong_skills) / len(required_skills)) * 100 if required_skills else 100
    readiness_score = min(100, max(10, round(req_match_pct)))

    # Advice Generation
    if readiness_score >= 80:
        advice = f"You have an excellent foundation for a {target_role} role! Focus on perfecting project depth and system architecture."
    elif readiness_score >= 60:
        advice = f"You possess strong core skills for {target_role}. Target the missing core requirements: {', '.join(missing_required[:3])} to boost your profile."
    else:
        advice = f"To become job-ready for {target_role}, prioritize learning {', '.join(missing_required[:3])} and build hands-on projects."

    return {
        "targetRole": target_role,
        "readinessScore": readiness_score,
        "strongSkills": strong_skills,
        "missingRequiredSkills": missing_required,
        "missingPreferredSkills": missing_preferred,
        "recommendedSkillsToLearn": missing_required + missing_preferred[:3],
        "guidanceAdvice": advice
    }
