# ai_connect_workshop
## Langchain Prompt
Write a Python script called run_groq that takes a question and the path to a local image, then:

Loads GROQ_API_KEY from the environment using python‑dotenv.

Creates a ChatGroq from langchain pointed at the meta‑llama/llama‑4‑scout‑17b‑16e‑instruct model.

Opens the image file, reads its bytes, and base64‑encodes them into a data:image/jpeg;base64,… URL.

Packages the question text and that image URL together in a single HumanMessage (one text dict and one image_url dict).

Calls llm.invoke(...) with that message list and returns the text of the reply.

## Langgraph Prompt
Write a Python script called `langgraph_tut.py` that does the following:

1. Loads environment variables from a `.env` file.
2. Imports `base64`, `os`, `load_dotenv` from `dotenv`, `ChatGroq` from `langchain_groq`, `HumanMessage` from `langchain_core.messages`, and `StateGraph`, `START`, `END` from `langgraph.graph`. Also import `TypedDict` from `typing_extensions`.
3. Defines a function `run_groq(question: str, img_bytes: bytes) -> str` which:
   - Reads `GROQ_API_KEY` from the environment.
   - Instantiates `ChatGroq` with that key and model `"meta-llama/llama-4-scout-17b-16e-instruct"`.
   - Encodes `img_bytes` to a base64 data‑URL.
   - Sends a `HumanMessage` containing the question and the image URL.
   - Returns the LLM’s `.content`.
4. Defines three TypedDicts:
   - `InputState` with `question: str` and `img_bytes: bytes`.
   - `OutputState` with `answer: str`.
   - `OverallState` inheriting both.
5. Defines two pure‑Python graph nodes:
   - `groq_vqa_node(state: InputState) -> OutputState` that calls `run_groq`.
   - `response_node(state: OverallState) -> OutputState` that prefixes the raw answer with `"🖼️ Model says: "`.
6. Builds a `StateGraph` with `state_schema=OverallState`, `input_schema=InputState`, `output_schema=OutputState`; adds the two nodes under names `"Groq VQA"` and `"Responder"`; wires `START → "Groq VQA" → "Responder" → END`.
7. Compiles the graph, renders it to `"agent_flow.png"` via `draw_mermaid_png(output_file_path=...)`, and prints a success message.
8. Defines a `LangGraphAgent` class that wraps the compiled graph and exposes a `.run(question: str, img_path: str) -> str` method (loading the image file, invoking the graph, and returning the answer).
9. Includes a `if __name__ == "__main__":` block that instantiates `LangGraphAgent`, runs it on `"my_painting.jpg"` with the question `"How does the brushwork reflect Baroque drama?"`, and prints both the question and the model’s response.

Use exactly those library imports and function/class names so the result matches the final code.```
::contentReference[oaicite:0]{index=0}



