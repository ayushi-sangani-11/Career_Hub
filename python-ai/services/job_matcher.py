from typing import List, Dict, Any

def calculate_job_match(user_skills: List[str], required_skills: List[str], preferred_skills: List[str] = None) -> Dict[str, Any]:
    """
    Calculates transparent skill match percentage between candidate skills and job requirements.
    """
    if preferred_skills is None:
        preferred_skills = []

    user_skills_set = {s.lower().strip() for s in user_skills}
    required_set = [s for s in required_skills]
    preferred_set = [s for s in preferred_skills]

    matched_required = []
    missing_required = []
    for req in required_set:
        req_clean = req.lower().strip()
        if req_clean in user_skills_set or any(u in req_clean or req_clean in u for u in user_skills_set):
            matched_required.append(req)
        else:
            missing_required.append(req)

    matched_preferred = []
    missing_preferred = []
    for pref in preferred_set:
        pref_clean = pref.lower().strip()
        if pref_clean in user_skills_set or any(u in pref_clean or pref_clean in u for u in user_skills_set):
            matched_preferred.append(pref)
        else:
            missing_preferred.append(pref)

    total_req = len(required_set)
    total_pref = len(preferred_set)

    if total_req > 0:
        req_score = (len(matched_required) / total_req) * 80.0
    else:
        req_score = 80.0

    if total_pref > 0:
        pref_score = (len(matched_preferred) / total_pref) * 20.0
    else:
        pref_score = 15.0

    match_percentage = min(99, max(15, round(req_score + pref_score)))

    reason = f"Matches {len(matched_required)} of {total_req} required skills"
    if matched_preferred:
        reason += f" plus {len(matched_preferred)} preferred skills."
    else:
        reason += "."

    return {
        "matchPercentage": match_percentage,
        "matchedRequired": matched_required,
        "missingRequired": missing_required,
        "matchedPreferred": matched_preferred,
        "missingPreferred": missing_preferred,
        "totalRequired": total_req,
        "matchedCount": len(matched_required) + len(matched_preferred),
        "reason": reason
    }

def rank_recommended_jobs(user_skills: List[str], target_role: str, jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Ranks a list of candidate jobs based on skill compatibility and target role match.
    """
    ranked_jobs = []

    for job in jobs:
        req_skills = job.get("requiredSkills", [])
        pref_skills = job.get("preferredSkills", [])
        job_title = job.get("title", "")

        match_data = calculate_job_match(user_skills, req_skills, pref_skills)
        pct = match_data["matchPercentage"]

        # Boost score slightly if job title matches user's target career role
        if target_role and target_role.lower() in job_title.lower():
            pct = min(98, pct + 5)

        ranked_jobs.append({
            "jobId": str(job.get("_id") or job.get("id")),
            "title": job_title,
            "company": job.get("company", ""),
            "location": job.get("location", ""),
            "type": job.get("type", ""),
            "salary": job.get("salary", ""),
            "matchPercentage": pct,
            "matchedSkills": match_data["matchedRequired"] + match_data["matchedPreferred"],
            "missingSkills": match_data["missingRequired"],
            "recommendationReason": match_data["reason"]
        })

    # Sort descending by match percentage
    ranked_jobs.sort(key=lambda x: x["matchPercentage"], reverse=True)
    return ranked_jobs
