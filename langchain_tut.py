import base64
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()


def run_gemini(question, img_bytes):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GOOGLE_API_KEY,
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
