import base64
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

load_dotenv()


# ── Step 1: Your existing run_groq helper ────────────────────────────────────
def run_groq(question: str, img_bytes: bytes) -> str:
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
                {"type": "text",  "text": question},
                {"type": "image_url", "image_url": {"url": img_data_url}},
            ]
        )
    ]
    return llm.invoke(messages).content


# ── Step 2: Define schemas & graph nodes ─────────────────────────────────────
class InputState(TypedDict):
    question: str
    img_bytes: bytes

class OutputState(TypedDict):
    answer: str

class OverallState(InputState, OutputState):
    pass

def groq_vqa_node(state: InputState) -> OutputState:
    return {"answer": run_groq(state["question"], state["img_bytes"])}

def response_node(state: OverallState) -> OutputState:
    formatted = f"🖼️ Model says: {state['answer']}"
    return {"answer": formatted}


# ── Step 3: Build & compile the StateGraph ───────────────────────────────────
builder = StateGraph(
    state_schema=OverallState,
    input_schema=InputState,
    output_schema=OutputState
)
builder.add_node("Groq VQA", groq_vqa_node)
builder.add_node("Responder", response_node)
builder.add_edge(START,      "Groq VQA")
builder.add_edge("Groq VQA", "Responder")
builder.add_edge("Responder", END)

agent_graph = builder.compile()
agent_graph.get_graph().draw_mermaid_png(output_file_path="agent_flow.png")
print("✅ Diagram saved to agent_flow.png")


# ── Step 4: Wrap it as an “agent” ────────────────────────────────────────────
class LangGraphAgent:
    def __init__(self, graph_app):
        self._graph = graph_app

    def run(self, question: str, img_path: str) -> str:
        with open(img_path, "rb") as f:
            img_data = f.read()
        result = self._graph.invoke({
            "question": question,
            "img_bytes": img_data
        })
        return result["answer"]


# ── Usage Example ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    agent = LangGraphAgent(agent_graph)
    q = "describe the image"
    answer = agent.run(q, "./Images/gothic-architecture-barcelona.jpg")
    print("❓", q)
    print("💬", answer)
