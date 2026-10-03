# Claim-Level LLM Hallucination Detection

An AI-based system for detecting factual hallucinations in Large Language Model (LLM) responses using claim-level analysis and external evidence.

## Current Pipeline

```text
LLM Response
     ↓
Claim Extraction
     ↓
Atomic Claims
     ↓
Evidence Retrieval
     ↓
Retrieved Evidence
```

## Current Modules

### 1. Claim Extraction

Uses **Llama 3.2 with Ollama** to break an LLM response into independent factual claims.

### 2. Evidence Retrieval

Uses the **Wikipedia API** to retrieve relevant evidence for each extracted claim.

## Tech Stack

* Python
* Ollama
* Llama 3.2
* Wikipedia API
* Requests
* BeautifulSoup

## Project Structure

```text
├── CLAIM_EXTRACTION.py
├── EVIDENCE_RETRIEVAL.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Install the Ollama model:

```bash
ollama pull llama3.2
```

Run:

```bash
python CLAIM_EXTRACTION.py
python EVIDENCE_RETRIEVAL.py
```

## Status

🟢 Claim Extraction — Completed
🟢 Evidence Retrieval — Completed
⚪ Claim Verification — Upcoming
⚪ Hallucination Scoring — Upcoming


