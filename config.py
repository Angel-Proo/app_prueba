class Config:
    SECRET_KEY = 'tu_clave_secreta'
    # Otras configuraciones de la aplicación Flask

class MailConfig:
    MAIL_SERVER = 'tu_servidor_smtp'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'tu_correo@gmail.com'
    MAIL_PASSWORD = 'tu_contraseña'