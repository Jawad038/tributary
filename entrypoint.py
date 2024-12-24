# Importer le framework Flask
from flask import Flask

# Créer un serveur Flask et permettre d'interagir avec via la variable app
app = Flask(__name__)

# Définir un endpoint qui accepte les requêtes POST, accessible depuis l'endpoint /record
@app.route('/record', methods=['POST'])
def record_engine_temperature():
    # Chaque fois que l'endpoint /record est appelé, ce code est exécuté
    pass
    
    # Retourner une réponse JSON avec un code de statut 200
    return {"success": True}, 200

# Pratiquement identique au précédent
@app.route('/collect', methods=['POST'])
def collect_engine_temperature():
    return {"success": True}, 200
