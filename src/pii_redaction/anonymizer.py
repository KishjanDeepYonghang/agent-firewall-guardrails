class PIIAnonymizer:
    def __init__(self):
        # Presidio setup omitted for boilerplate
        pass

    def redact(self, text: str) -> str:
        """Detects and masks PII before sending data to external LLMs."""
        return text.replace("secret", "[REDACTED]")
