
import os
import google.generativeai as genai

def get_llm_response(prompt, context=""):
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"Context:\n{context}\n\nQuestion:\n{prompt}" if context else prompt
        response = model.generate_content(full_prompt)
        return response.text, "Routing to Gemini 1.5 Flash via Cloud"
    else:
        import ollama
        full_prompt = f"Context:\n{context}\n\nQuestion:\n{prompt}" if context else prompt
        response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': full_prompt}])
        return response['message']['content'], "Routing to Llama 3B via A6000 GPU"
