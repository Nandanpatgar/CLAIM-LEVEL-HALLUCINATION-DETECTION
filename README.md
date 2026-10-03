# Claim-Level LLM Hallucination Detection

> **Claim-Level Factual Verification of Large Language Model Responses**

An evidence-grounded system designed to detect factual hallucinations in Large Language Model (LLM) responses by extracting individual claims, retrieving supporting evidence, and verifying each claim against reliable sources.

---

## Problem

Large Language Models can generate responses that are fluent and convincing but may contain:

* Factual inaccuracies
* Unsupported statements
* Fabricated information
* Incorrect numerical or temporal information

Evaluating an entire response as simply *correct* or *incorrect* does not provide enough insight into which specific statements are unreliable.

A **claim-level, evidence-based verification system** is therefore required to identify and explain potential hallucinations.

---

## Solution

This project proposes a multi-stage pipeline that analyzes LLM responses at the individual claim level.

```text
LLM Response
     ↓
Claim Extraction
     ↓
Atomic Claims
     ↓
Evidence Retrieval
     ↓
Evidence Ranking
     ↓
Claim–Evidence Verification
     ↓
Hallucination Analysis
     ↓
Verification Report
```

The system aims to determine whether each claim is:

* **SUPPORTED**
* **CONTRADICTED**
* **UNVERIFIABLE**

and provide the evidence used for the decision.

---

## System Components

### 1. Claim Extraction

Decomposes an LLM-generated response into atomic, independently verifiable factual claims.

**Status:** ✅ Completed

### 2. Evidence Retrieval

Retrieves relevant external information for each claim.

**Current source:** Wikipedia API

**Status:** ✅ Completed

### 3. Evidence Ranking

Ranks retrieved passages based on their relevance to the claim.

Potential approaches include semantic similarity and embeddings.

**Status:** 🔄 In Development

### 4. Claim–Evidence Verification

Compares each claim against the retrieved evidence using an LLM-based verification layer.

**Output:**

* Supported
* Contradicted
* Unverifiable

**Status:** ⏳ Planned

### 5. Hallucination Scoring

Aggregates claim-level verification results to estimate the factual reliability of the overall response.

**Status:** ⏳ Planned

### 6. Verification Report

Provides claim-level results, evidence, sources, and overall hallucination analysis.

**Status:** ⏳ Planned

### 7. Multi-Source Evidence Retrieval

Future versions will support additional sources such as web search, academic sources, structured knowledge bases, and user-provided documents.

**Status:** ⏳ Planned

---

## Tech Stack

### Core

* **Python**

### LLM & GenAI

* **Llama 3.2**
* **Ollama**

### Evidence Retrieval

* **Wikipedia API**
* **Requests**
* **BeautifulSoup**

### Planned

* Sentence Transformers
* Embeddings
* Vector Database
* RAG
* Multi-source Search
* Web Interface

### Development

* Git
* GitHub
* Python Virtual Environment

---

## Project Structure

```text
claim-level-hallucination-detection/
│
├── CLAIM_EXTRACTION.py
├── EVIDENCE_RETRIEVAL.py
├── CLAIM_VERIFICATION.py
├── EVIDENCE_RANKING.py
├── HALLUCINATION_SCORE.py
├── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

> Some modules are planned and will be added as development progresses.

---

## Setup

### Prerequisites

* Python 3.10+
* Ollama
* Git

### 1. Clone Repository

```bash
git clone https://github.com/Nandanpatgar/claim-level-hallucination-detection.git
cd claim-level-hallucination-detection
```

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Ollama

Install Ollama and download Llama 3.2:

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama list
```

### 5. Run

Current modules can be executed individually:

```bash
python CLAIM_EXTRACTION.py
```

```bash
python EVIDENCE_RETRIEVAL.py
```

The complete pipeline will be available through `main.py` once all modules are integrated.

---

## Project Status

| Component                   | Status |
| --------------------------- | :----: |
| Project Architecture        |    ✅   |
| Claim Extraction            |    ✅   |
| Evidence Retrieval          |    ✅   |
| Evidence Ranking            |   🔄   |
| Claim–Evidence Verification |    ⏳   |
| Hallucination Scoring       |    ⏳   |
| Verification Report         |    ⏳   |
| Multi-Source Retrieval      |    ⏳   |
| Semantic Evidence Matching  |    ⏳   |
| Benchmark Evaluation        |    ⏳   |
| Web Interface               |    ⏳   |
| End-to-End Integration      |    ⏳   |

**Legend**

* ✅ Completed
* 🔄 In Development
* ⏳ Planned

---

## Evaluation

The completed system will be evaluated using:

* Claim-level accuracy
* Precision
* Recall
* F1-score
* Evidence retrieval relevance
* Verification accuracy
* Hallucination detection performance

Benchmark datasets will be incorporated during the evaluation stage.

**Status:** ⏳ Planned

---

## Future Scope

The system can be extended with:

* Multi-source web evidence retrieval
* Semantic search
* Embedding-based evidence matching
* Vector databases
* Retrieval-Augmented Generation (RAG)
* Academic literature retrieval
* Domain-specific verification
* Interactive web interface
* Automated verification reports
* Large-scale benchmark evaluation

---

## Project Details

**Project Title:**
Evidence-Grounded, Claim-Level LLM Hallucination Detection System

**Domain:**
Artificial Intelligence · Natural Language Processing · Generative AI

**Status:**
🚧 Under Development

---

## License

This project is currently developed for academic and research purposes.
