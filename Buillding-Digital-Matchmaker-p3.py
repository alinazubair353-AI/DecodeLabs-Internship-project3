from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
#  DATASET - Job Roles with their required skills
JOB_ROLES = {
    "Data Scientist":         "python sql machine_learning statistics data_analysis tensorflow deep_learning numpy pandas",
    "ML Engineer":            "python tensorflow pytorch machine_learning deep_learning algorithms neural_networks model_deployment",
    "Data Analyst":           "sql excel python power_bi tableau data_visualization statistics reporting",
    "Backend Developer":      "python java sql apis rest_api django nodejs databases postgresql",
    "Frontend Developer":     "javascript react html css typescript ui_ux nodejs vue angular",
    "DevOps Engineer":        "aws docker kubernetes linux ci_cd automation cloud infrastructure git",
    "Cloud Architect":        "aws azure cloud kubernetes terraform infrastructure automation devops networking",
    "Cybersecurity Engineer": "networking linux security firewalls penetration_testing ethical_hacking cryptography",
    "Mobile Developer":       "flutter dart kotlin swift android ios react_native mobile_apps",
    "AI Research Scientist":  "python research mathematics deep_learning nlp computer_vision algorithms papers",
    "Database Administrator": "sql postgresql mysql mongodb database_design optimization backup recovery",
    "Full Stack Developer":   "javascript python react nodejs sql django html css apis databases",
}
#  STEP 1: INGESTION - User input lena
def get_user_skills():
    print("\n" + "="*55)
    print("    TECH STACK RECOMMENDER  |  DecodeLabs AI")
    print("="*55)
    print("  Apni skills enter karo (minimum 3 required)")
    print("  Example: Python, Machine Learning, SQL")
    print("-"*55)
    skills = []
    while len(skills) < 3:
        remaining = 3 - len(skills)
        skill = input(f"    Skill {len(skills)+1}: ").strip()
        if skill:
            clean = skill.lower().replace(" ", "_")
            skills.append(clean)
        else:
            print("    Please enter a valid skill!")
    # Optional extra skills
    print(f"\n   {len(skills)} skills added. Add more? (Enter skill or press Enter to skip)")
    while True:
        extra = input(f"  ➤  Skill {len(skills)+1} (optional): ").strip()
        if not extra:
            break
        skills.append(extra.lower().replace(" ", "_"))

    return skills

#  STEP 2: VECTOR MAPPING + TF-IDF
def build_vectors(user_skills):
    user_text = " ".join(user_skills)

    role_names = list(JOB_ROLES.keys())
    role_docs  = list(JOB_ROLES.values())

    all_docs = role_docs + [user_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_docs)

    # Alag karo
    job_vectors  = tfidf_matrix[:-1]   # Job roles
    user_vector  = tfidf_matrix[-1]    # User profile

    return user_vector, job_vectors, role_names, vectorizer

#  STEP 3: SCORING - Cosine Similarity
def calculate_scores(user_vector, job_vectors, role_names):
    # cos(θ) = A·B / (||A|| × ||B||)
    scores = cosine_similarity(user_vector, job_vectors)[0]

    results = list(zip(role_names, scores))
    return results

#  STEP 4: SORTING + FILTERING (Top-N)
def get_top_recommendations(results, top_n=3):
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    return sorted_results[:top_n]
def skill_gap_analysis(user_skills, role_name):
    role_skills = set(JOB_ROLES[role_name].split())
    user_set    = set(user_skills)
    matched  = role_skills & user_set
    missing  = role_skills - user_set
    match_pct = len(matched) / len(role_skills) * 100
    return matched, missing, match_pct

#  OUTPUT - Display
def display_results(user_skills, top_recs):
    print("\n" + "="*55)
    print("     TOP JOB RECOMMENDATIONS FOR YOU")
    print("="*55)
    print(f"  Your Skills: {', '.join(s.replace('_',' ').title() for s in user_skills)}")
    print("-"*55)
    ranks = ["  #1  BEST MATCH", "  #2  SECOND MATCH", "  #3  THIRD MATCH"]
    for i, (role, score) in enumerate(top_recs):
        pct = score * 100
        print(f"\n  {ranks[i]}")
        print(f"  Role         : {role}")
        print(f"  Match Score  : {pct:.1f} / 100")
        matched, missing, _ = skill_gap_analysis(user_skills, role)
        if matched:
            matched_display = ', '.join(s.replace('_',' ').title() for s in list(matched)[:4])
            print(f"       You have : {matched_display}")
        if missing:
            missing_display = ', '.join(s.replace('_',' ').title() for s in list(missing)[:3])
            print(f"       Learn   : {missing_display}")
    print("\n" + "="*55)
    if all(s == 0 for _, s in top_recs):
        print("    No matches found! Your skills don't match")
        print("  our database. Try skills like: Python, SQL, AWS")
        print("="*55)
#  MAIN PIPELINE
def main():
    user_skills = get_user_skills()
    print(f"\n    Processing {len(user_skills)} skills...")
    print("   Building TF-IDF vectors...")
    print("   Calculating Cosine Similarity...")
    user_vector, job_vectors, role_names, _ = build_vectors(user_skills)

    results = calculate_scores(user_vector, job_vectors, role_names)

    top_recs = get_top_recommendations(results, top_n=3)
    display_results(user_skills, top_recs)
    print("\n   Want to try different skills? (y/n): ", end="")
    again = input().strip().lower()
    if again == 'y':
        main()
    else:
        print("\n  Thanks for using Tech Stack Recommender!")
        print("  Built for DecodeLabs AI Project 3\n")
if __name__ == "__main__":
    main()