import base64
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()


def run_groq(question, img_bytes):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    img_data_url = f"data:image/jpeg;base64,{img_b64}"
    messages = [
        HumanMessage(
            content=[
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": {"url": img_data_url}},
            ]
        )
    ]
    response = llm.invoke(messages)
    return response.content
