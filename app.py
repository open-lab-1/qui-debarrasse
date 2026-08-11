from flask import Flask, request, jsonify # outil qu'on a besoin
app = Flask(__name__)
@app.route('/analyser', methods=['POST'])
def recevoir_photo():
    photo = request.files['photo']
    return jsonify(corvees="Le serveur a bien recu la photo !")
