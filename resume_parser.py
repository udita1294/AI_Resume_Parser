import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not found.")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

job_description = """
    Fullstack Developer :

We are seeking an experienced and highly motivated
Fullstack Developer to join our product development team. The ideal candidate
will have a strong background in both front-end and back-end development, with
a focus on building and maintaining scalable, high-performance applications.
This role requires a proven track record in product development, from concept
to deployment.

Roles and Responsibilities :
1) Responsibilities Design, develop, and maintain robust and
scalable full-stack applications
2) Develop user-facing features using ReactJS.
Build efficient and relible server-side components using either Java
Springboot or NodeJS.
3) Manage and optimize database interactions, utilizing
both Relational and Non-Relational databases.
4) Collaborate with Product Managers, designers, and other engineers to define,
design, and ship new features.
5) Participate in code reviews to ensure code quality and adherence to
best practices.
6) Troubleshoot, debug, and upgrade existing systems. Contribute
to the entire application lifecycle, from conception to deployment. Required

Qualifications:
0-1 years of professional experience in Fullstack Development.
Strong proficiency in front-end development using ReactJS and its ecosystem
(Redux, Hooks, etc.). Demonstrated experience in back-end development with
either Java Springboot or NodeJS. Solid understanding and practical
experience with database technologies, including both Relational Databases
(e.g., PostgreSQL, MySQL) and Non-Relational Databases (e.g., MongoDB,
DynamoDB).
Mandatory experience in the full lifecycle of Product Development, from
initial requirement gathering to deployment and maintenance. Experience with
RESTful APIs and asynchronous request handling. Familiarity with version
control systems (e.g., Git). Preferred Qualifications Experience with cloud
platforms (AWS, Azure, GCP). Familiarity with containerization and
orchestration tools (Docker, Kubernetes). Knowledge of modern authorization
mechanisms, such as JSON Web Tokens (JWT). Experience working in an Agile/Scrum development environment.
"""

class JobDescription(BaseModel):
    role:str
    required_skills:list[str]
    preferred_skills:list[str]
    minimum_experience:float|None
    education_requirements:list[str]
    responsibilities:list[str]

jobD_schema = JobDescription.model_json_schema()

system_prompt = f"""
    You are an expert HR Assistant.
    Your job is to analyse the job descriptions and extract structured informations from them.

    Return ONLY valid JSON matching this schema:
    {jobD_schema}

    IMPORTANT:
    - Do not return the schema itself.
    - Do NOT return fields like "properties","title" or "type".
    - Fill the schema with the actual information extracted by the job description.

    If minimum experience is not mentioned in the job description, return null for that field.
    If information for a list is missing return an empty list for that field.
    Do NOT invent any information that is not present in the job description.
"""

user_prompt = f"""
    Analyze the following job description.
    {job_description}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

message_user = {
    "role": "user",
    "content": user_prompt
}
