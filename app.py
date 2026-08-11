from flask import Flask, request, jsonify # outil qu'on a besoin
from openai import OpenAI
import base64 #sert avec io a convertir l'image en texte Base 64
import io

app = Flask(__name__)
client = OpenAI()

@app.route('/analyser', methods=['POST'])
def recevoir_photo():
    photo = request.files['photo']
    consigne_ia = """regarde cette photo de table de fin de repas, identifie ce qu'il reste à débarrasser (assiettes,couverts verres, poêles sales, reste, récipient...),répartis obligatoirement les corvées entre ces prénom : Mael, Aédan, Noa et dis précisement qui met au lave vaisselle, qui nettoie la poêle a la main, qui passe un coup d'éponge sur la table, qui met les reste dans des recipient (si il y a des restes)....""" 
    
    photo_bytes = photo.read()
    photo_base64 = base64.b64encode(photo_bytes).decode('utf-8')
    
    reponse = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": consigne_ia},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{photo_base64}"}}
                ]
            }
        ]
    )
    
    return jsonify(corvees=reponse.choices[0].message.content)
