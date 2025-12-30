# Qcode Agent 

**Qcode Agent** is a lightweight Streamlit app that uses Large Language Models (LLMs) to find and fix bugs in Qiskit quantum code.

##  What It Does

- Accepts Qiskit code as input
- Detects and fixes common bugs
- Supports multiple LLM backends:
  - GPT-4 (OpenAI)
  - Granite-8B-Qiskit (IBM)
  - Code Llama (Meta)
- Shows fixed code with comments
- Future: test verification and execution safety checks

## 🚀 Try It Live

You can deploy this app on [Hugging Face Spaces](https://huggingface.co/spaces):

- Select "Streamlit" as the app type
- Upload `app.py` and `requirements.txt`
- You're live in minutes!

## 🛠 Setup (Local)

```bash
git clone https://github.com/your-username/qcode-agent.git
cd qcode-agent
pip install -r requirements.txt
streamlit run app.py
```
## Dependencies
- streamlit
- requests

