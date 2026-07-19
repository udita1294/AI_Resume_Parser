# AI Resume Parser & Candidate Matching System

An AI-powered Resume Parser and Candidate Matching System built with **Python**, **Groq LLM**, and **Pydantic**. The application automatically extracts structured information from job descriptions and resumes, compares candidate profiles against job requirements, calculates a matching score, and ranks candidates based on their suitability.

## Features

- Parse job descriptions into structured JSON.
- Extract candidate information from PDF and DOCX resumes.
- Identify skills, work experience, education, certifications, and projects.
- Compare resumes with job descriptions using an LLM.
- Generate candidate match scores (0–100).
- Highlight matching and missing skills.
- Check experience eligibility.
- Rank candidates from best to worst match.
- Supports batch processing of multiple resumes.

## Tech Stack

- Python 3.11+
- Groq API (Llama 3.3 70B Versatile)
- Pydantic
- PyPDF
- python-docx
- python-dotenv


## How It Works

### Step 1: Job Description Parsing

The application sends the job description to the Groq LLM and extracts:

- Job Role
- Required Skills
- Preferred Skills
- Minimum Experience
- Responsibilities
- Education Requirements

The output is validated using a Pydantic model.

---

### Step 2: Resume Parsing

Each resume is read automatically.

Supported formats:

- PDF
- DOCX

The parser extracts:

- Name
- Email
- Phone Number
- Skills
- Experience
- Projects
- Education
- Certifications
- Total Experience

---

### Step 3: Candidate Matching

Each parsed resume is compared against the structured job description.

The AI generates:

- Match Score (0–100)
- Matching Skills
- Missing Skills
- Experience Requirement Status
- Final Recommendation

---

### Step 4: Candidate Ranking

Candidates are sorted based on their match score.

The application displays:

- Top 2 Candidates
- Lowest 2 Candidates


## Supported Resume Formats

- PDF
- DOCX

## Libraries Used

- `groq`
- `pydantic`
- `python-dotenv`
- `pypdf`
- `python-docx`

## Learning Outcomes

This project demonstrates:

- Prompt Engineering
- Structured Output Generation
- LLM-powered Information Extraction
- Resume Parsing
- Job Description Analysis
- Pydantic Data Validation
- PDF & DOCX Processing
- AI-based Candidate Ranking
