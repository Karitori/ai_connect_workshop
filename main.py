from langchain_tut import run_gemini
from langchain_tut_groq import run_groq


question = "What makes the lighting dramatic here? also explain the architecture and the history of the building"
img_path = "./Images/gothic-architecture-barcelona.jpg"
img_bytes = open(img_path, "rb").read()
result = run_gemini(question, img_bytes)
print(result)







