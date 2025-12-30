import streamlit as st
import requests

st.set_page_config(page_title="Qcode Agent: Qiskit Bug Fixer", layout="centered")
st.title("🤖 Qcode Agent: LLM-Powered Quantum Code Repair")
st.markdown("Paste your Qiskit code below and let an LLM find and fix bugs.")

# Code input
code_input = st.text_area("Qiskit Code Input", height=300, placeholder="Paste your Qiskit code here...")

# Backend selection
model_choice = st.selectbox("Choose LLM Backend", ["GPT-4 (OpenAI)", "Granite-8B-Qiskit (HF)", "Code Llama (HF)"])

# API setup (mocked)
def query_llm(model, code):
    if model == "GPT-4 (OpenAI)":
        return "# Fixed by GPT-4\n" + code.replace("cx(q[0], q[0])", "cx(q[0], q[1])")
    elif model == "Granite-8B-Qiskit (HF)":
        return "# Granite-8B fix suggestion:\n" + code.replace("cx(q[0], q[0])", "cx(q[0], q[1])")
    elif model == "Code Llama (HF)":
        return "# Code Llama fix suggestion:\n" + code.replace("cx(q[0], q[0])", "cx(q[0], q[1])")
    return "No fix found."

# Button to trigger repair
if st.button("Fix My Code"):
    if not code_input.strip():
        st.warning("Please paste some Qiskit code to analyze.")
    else:
        with st.spinner("Querying the selected LLM..."):
            fixed_code = query_llm(model_choice, code_input)
            st.success("Patch generated successfully!")
            st.code(fixed_code, language="python")

st.markdown("---")
st.caption("Built by your Quantum AI copilot 🧠⚛️")
