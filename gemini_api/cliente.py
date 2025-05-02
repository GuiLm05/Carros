import google.generativeai as genai

# Configure a API Key
genai.configure(api_key="AIzaSyBBpOqaIdEgCbuGYc8OnKAJTSif2AJS8pw")

def car_gemini_ai(model_name, brand, year):
    # Monta o prompt
    prompt = f"Elaborar um resumo sobre o carro {model_name} da marca {brand} do ano {year} com 200 caracteres."

    # Cria o modelo Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Gera o conteúdo com configuração de geração
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            max_output_tokens=300
        )
    )

    return response.text
