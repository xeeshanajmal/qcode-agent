# Qcode Agent

**Qcode Agent** is a lightweight Streamlit-based application that leverages Large Language Models (LLMs) to detect and repair bugs in Qiskit quantum programs. Designed for researchers and developers in the quantum software engineering domain, it provides a prototype for integrating LLM-assisted bug fixing into secure quantum development workflows.

---

## Features

- Accepts Qiskit source code as input.
- Performs static analysis to detect common bugs and code issues.
- Suggests and applies automatic fixes using different LLM backends.
- Supports multiple language model backends:
  - GPT-4 (via OpenAI API)
  - Granite-8B-Qiskit (IBM via Hugging Face)
  - Code Llama (Meta via Hugging Face)
- Displays patched code with inline comments for transparency.
- Future extensions include automated test verification and security validation.

---

## Live Deployment via Hugging Face Spaces

To deploy the app on Hugging Face Spaces:

1. Navigate to [Hugging Face Spaces](https://huggingface.co/spaces).
2. Click “Create New Space”.
3. Choose “Streamlit” as the SDK.
4. Upload `app.py` and `requirements.txt`.
5. The app will launch automatically and be accessible through a public link.

---

## Local Setup Instructions

To run Qcode Agent locally:

# Clone the repository

```bash
git clone https://github.com/your-username/qcode-agent.git
cd qcode-agent
```

# Install required packages
pip install -r requirements.txt

# Launch the application
streamlit run app.py
