import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self):
        self.smtp_server = settings.SMTP_SERVER
        self.smtp_port = settings.SMTP_PORT
        self.smtp_user = settings.SMTP_USER
        self.smtp_password = settings.SMTP_PASSWORD

    async def send_password_reset(self, to_email: str, token: str):
        message = MIMEMultipart()
        message["From"] = "no-reply@schoolsystem.com"
        message["To"] = to_email
        message["Subject"] = "Recuperación de contraseña"
        
        text = f"""Para restablecer tu contraseña, usa este enlace:
        {settings.FRONTEND_URL}/reset-password?token={token}
        """
        
        message.attach(MIMEText(text, "plain"))
        
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(
                self.smtp_user,
                to_email,
                message.as_string()
            )