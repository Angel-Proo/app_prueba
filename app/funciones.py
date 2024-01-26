from flask_mail import Message
from app import mail

import os
from flask_mail import Message
from app import app, mail

def enviar_correo(destinatario, asunto, cuerpo, archivos_adjuntos=None):
    msg = Message(asunto, recipients=[destinatario])
    msg.body = cuerpo

    if archivos_adjuntos:
        for archivo, tipo in archivos_adjuntos:
            with app.open_resource(archivo) as adjunto:
                msg.attach(archivo, tipo, adjunto.read())

            # Eliminar el archivo después de adjuntarlo
            eliminar_archivo(archivo)

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f'Error al enviar el correo: {e}')
        return False

def eliminar_archivo(archivo):
    ruta_archivo = os.path.join(app.root_path, archivo)

    try:
        os.remove(ruta_archivo)
        print(f'Archivo {archivo} eliminado correctamente.')
    except Exception as e:
        print(f'Error al eliminar el archivo {archivo}: {e}')