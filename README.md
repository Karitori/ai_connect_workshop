# ai_connect_workshop
## Langchain Prompt
Write a Python script called run_groq that takes a question and the path to a local image, then:

Loads GROQ_API_KEY from the environment using python‑dotenv.

Creates a ChatGroq from langchain pointed at the meta‑llama/llama‑4‑scout‑17b‑16e‑instruct model.

Opens the image file, reads its bytes, and base64‑encodes them into a data:image/jpeg;base64,… URL.

Packages the question text and that image URL together in a single HumanMessage (one text dict and one image_url dict).

Calls llm.invoke(...) with that message list and returns the text of the reply.




