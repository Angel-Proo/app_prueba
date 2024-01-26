from flask import Blueprint, render_template, url_for
from app.funciones import enviar_correo

forms_bp = Blueprint('forms_bp', __name__,template_folder='templates')

@forms_bp.route('/formulario')
def mostrar_formulario():
    # Lógica para renderizar el formulario
    print(url_for('forms_bp.mostrar_formulario'))
    enviar_correo('destinatario@example.com', 'Asunto', 'Cuerpo del correo')
    return render_template('formulario.html')