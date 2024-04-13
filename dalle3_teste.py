from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="3 pessoas com machucados no rosto que as faça parecerem zumbis, sentadas em um banco branco de uma praça pública, olhando atentamente seus telefones celulares, num dia de sol.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)