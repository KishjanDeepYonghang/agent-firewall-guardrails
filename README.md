# Enterprise Agent Firewall & Guardrails 🛡️

A robust proxy layer that sits between your enterprise applications and external LLM APIs (OpenAI, Anthropic). Ensures SOC2/GDPR compliance by automatically redacting PII and blocking prompt injection attacks.

## 🎯 Business Value
- **Data Security:** Zero-trust architecture ensures no customer PII ever leaves your VPC.
- **Compliance:** Built-in auditing and GDPR-compliant data masking using Microsoft Presidio.
- **Brand Protection:** NeMo Guardrails prevents the AI from discussing competitors, politics, or going off-topic.

## 🏗️ System Architecture

```mermaid
graph LR
    App[Enterprise App] --> Proxy[FastAPI Firewall Proxy]
    Proxy --> PII[PII Redaction (Presidio)]
    Proxy --> Guard[NeMo Guardrails]
    PII --> CleanPrompt[Sanitized Payload]
    Guard --> CleanPrompt
    CleanPrompt --> LLM[External LLM API]
```

## 🛠️ Tech Stack
- **Core:** Python 3.11, FastAPI
- **Security:** Microsoft Presidio (PII), NVIDIA NeMo Guardrails
- **Infrastructure:** Docker

## 🚀 Quick Start
```bash
docker-compose up --build
```
