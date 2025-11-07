import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load .env file locally
load_dotenv()

st.set_page_config(page_title="Viraj Gen AI App")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY is not set. Check .env or Azure App Service → Configuration.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.title("🤖 Simple Gen AI App")
st.write("Powered by OpenAI — Designed by **Viraj**")

prompt = st.text_area("Enter your prompt", placeholder="Ask me anything...")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",  # ✅ stable model
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt},
                ]
            )

            # ✅ Correct return value access
            answer = response.choices[0].message.content

        st.success(answer)

# ----------------- Footer ------------------
st.markdown(
    """
    <br><p style="text-align:center; color:gray;">
        ✨ Design by <b>Viraj</b> ✨
    </p>
    """,
    unsafe_allow_html=True
)
