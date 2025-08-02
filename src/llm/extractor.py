import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise EnvironmentError("Missing GOOGLE_API_KEY in environment.")

genai.configure(api_key=api_key)

# Load prompt from template file
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompt_template.txt")

if not os.path.exists(PROMPT_PATH):
    raise FileNotFoundError(f"Prompt template not found at {PROMPT_PATH}")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt_template_str = f.read()

# Define prompt
prompt = PromptTemplate(
    input_variables=["document_text"],
    template=prompt_template_str
)

# Use Gemini 2.0 Flash model
llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# Chain using modern LangChain interface
chain = prompt | llm  # Replaces deprecated LLMChain

def extract_metadata(document_text: str) -> dict:
    try:
        response = chain.invoke({"document_text": document_text}).strip()
        
        # Remove Markdown-style code block if present
        if response.startswith("```"):
            response = response.strip("`")
            # remove possible "json" prefix
            if response.lower().startswith("json"):
                response = response[4:].strip()
        
        return json.loads(response)
    
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM response is not valid JSON. Response was:\n{response}") from e
    except Exception as e:
        raise RuntimeError(f"Metadata extraction failed: {str(e)}") from e