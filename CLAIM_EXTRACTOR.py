import requests

def extract_claims(text):

    prompt = f"""
 Break the following text into atomic factual claims.

Rules:
1. Each claim must contain only one independently verifiable fact.
2. Preserve the original meaning.
3. Do not add facts.
4. Do not remove facts.
5. Return only the claims.
6. Put each claim on a separate line.
7. Do not number the claims.

Text:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    claims = result["response"].strip().split("\n")

    return [
        claim.strip()
        for claim in claims
        if claim.strip()
    ]


# Test
text = """
The Eiffel Tower is located in Paris.
It was completed in 1889 and is 330 meters tall.
It attracts millions of visitors every year.
"""

claims = extract_claims(text)

print("\nAtomic Claims:\n")

for i, claim in enumerate(claims, 1):
    print(f"Claim {i}: {claim}")