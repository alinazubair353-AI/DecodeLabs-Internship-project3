
# Project 3: Digital Matchmaker - Job Recommender (DecodeLabs Internship)

## What is this?
This is my third project at DecodeLabs. It recommends job roles based on your technical skills using TF-IDF and Cosine Similarity.

## How It Works
1. You enter your skills (Python, SQL, etc.)
2. System compares your skills with 12 different job roles
3. It shows top 3 jobs that match your skills
4. It also tells what skills you are missing

## Job Roles in Database
- Data Scientist
- ML Engineer
- Data Analyst
- Backend Developer
- Frontend Developer
- DevOps Engineer
- Cloud Architect
- Cybersecurity Engineer
- Mobile Developer
- AI Research Scientist
- Database Administrator
- Full Stack Developer

## How to Run
1. Install required library:
   pip install scikit-learn numpy
2. Run the file: Buillding-Digital-Matchmaker-p3.py
3. Enter your skills (minimum 3)
4. See your top job matches

## Technologies Used
| Library | Purpose |
|---------|---------|
| scikit-learn | TF-IDF and Cosine Similarity |
| numpy | calculations |
#output:

=======================================================
    TECH STACK RECOMMENDER  |  DecodeLabs AI
=======================================================
  Apni skills enter karo (minimum 3 required)
  Example: Python, Machine Learning, SQL
-------------------------------------------------------
    Skill 1: ml
    Skill 2: python
    Skill 3: java

   3 skills added. Add more? (Enter skill or press Enter to skip)
  ➤  Skill 4 (optional): math
  ➤  Skill 5 (optional): c++
  ➤  Skill 6 (optional): 

    Processing 5 skills...
   Building TF-IDF vectors...
   Calculating Cosine Similarity...

=======================================================
     TOP JOB RECOMMENDATIONS FOR YOU
=======================================================
  Your Skills: Ml, Python, Java, Math, C++
-------------------------------------------------------

    #1  BEST MATCH
  Role         : Backend Developer
  Match Score  : 24.1 / 100
       You have : Java, Python
       Learn   : Postgresql, Apis, Databases

    #2  SECOND MATCH
  Role         : ML Engineer
  Match Score  : 6.5 / 100
       You have : Python
       Learn   : Model Deployment, Algorithms, Tensorflow

    #3  THIRD MATCH
  Role         : Data Analyst
  Match Score  : 6.4 / 100
       You have : Python
       Learn   : Power Bi, Excel, Statistics

=======================================================

   Want to try different skills? (y/n): no

  Thanks for using Tech Stack Recommender!
  Built for DecodeLabs AI Project 3

## Author
Alina Zubair - AI Intern at DecodeLabs

## Date
DecodeLabs Internship Program 2026
