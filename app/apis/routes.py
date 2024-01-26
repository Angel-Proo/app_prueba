from flask import Blueprint
from app.funciones import enviar_correo

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/api/ruta1')
def api_ruta1():
    # Lógica de la API
    enviar_correo('destinatario@example.com', 'Asunto', 'Cuerpo del correo')
    return 'API Ruta 1'