from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

modelo = "gpt-4"

def categoriza_artista(nome_artista, lista_categorias_possiveis):
        prompt_sistema = f"""
                Você é um categorizador de artistas.
                Você deve assumir as categorias presentes na lista abaixo.

                # Lista de Categorias Válidas
                {lista_categorias_possiveis.split(",")}

                # Formato da Saída
                Artista: Nome do Artista
                Categoria: apresente a categoria do artista

                # Exemplo de Saída
                Artista: Beatles
                Categoria: Rock
        """

        resposta = cliente.chat.completions.create(
                messages=[
                        {
                                "role" : "system",
                                "content" : prompt_sistema
                        },
                        {
                                "role" : "user",
                                "content" : nome_artista
                        }
                ],
                model = modelo,
                temperature = 0,
                max_tokens = 200
        )

        return resposta.choices[0].message.content


categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
        nome_artista = input("Digite o nome do artista: ")
        texto_resposta = categoriza_artista(nome_artista, categorias_validas)
        print(texto_resposta)
