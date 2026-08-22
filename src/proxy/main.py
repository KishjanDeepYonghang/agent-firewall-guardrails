from fastapi import FastAPI
from src.pii_redaction.anonymizer import PIIAnonymizer

app = FastAPI(title="LLM API Firewall", version="1.0.0")
anonymizer = PIIAnonymizer()

@app.post("/v1/chat/completions")
async def proxy_completions(prompt: str):
    # 1. PII Redaction
    clean_prompt = anonymizer.redact(prompt)
    # 2. Guardrails check (jailbreak detection)
    # 3. Forward to OpenAI/Anthropic
    return {"status": "forwarded", "prompt_sent": clean_prompt}
