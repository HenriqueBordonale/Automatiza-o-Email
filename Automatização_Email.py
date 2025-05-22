import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
import os


class Automatizacao:
    def  __init__(self):
        self.usuarioRemetente = input("Digite seu usuário: ")
        self.usuario = input("Digite o usuário criado: ")
        self.senhaEmail = input ("Digite a senha criada: ")
        self.emailDestinatario = input("Digite o E-mail destinatario: ")
        self.enderecoEmail = self.usuarioRemetente + "@unaerp.br"
        self.senha = os.getenv("GMAIL_SENHA")
  
        

    def carregar_template(self, caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
        
    def enviar_email(self):
            html = self.carregar_template("email.html")
            corpo_email = html.replace("{{usuario}}", self.usuario).replace("{{senha}}", self.senhaEmail)
            destinatario = [self.emailDestinatario, f"{self.usuario}@unaerp.br"]

            msg = MIMEMultipart("alternative")
            msg['Subject'] = "Bem vindo a UNAERP!!!"
            msg['From'] = self.enderecoEmail
            msg['To'] = ", ".join(destinatario)

            parte_html = MIMEText(corpo_email, 'html')
            msg.attach(parte_html)
                
            try:
                print("Conectando ao servidor...")
                servidor_email = smtplib.SMTP('smtp.gmail.com', 587)     
                servidor_email.starttls()     
                print("Autenticando...")   
                servidor_email.login(self.enderecoEmail, self.senha)
                servidor_email.sendmail(self.enderecoEmail, destinatario, msg.as_string())
                print("E-mail enviado com sucesso!")
                print(f"E-mail remetente: {self.enderecoEmail}")
                print(f"E-mail destinatario: {self.emailDestinatario}")
                input("Aperte qualquer tecla para sair.")

            except smtplib.SMTPConnectError:
                print("Falha ao conectar ao servidor SMTP.")
            except smtplib.SMTPAuthenticationError:
                print("Falha ao autenticar!")    
                input("Pressione qualquer tecla para prosseguir")
            except smtplib.SMTPException as e:
                print(f"Erro geral de SMTP: {e}")
                input("Pressione qualquer tecla para prosseguir")
            except Exception as e:
                print(f"Outro erro inesperado: {e}")
                input("Pressione qualquer tecla para prosseguir")
            finally:
                try:
                    servidor_email.quit()
                except:
                    pass

if __name__ == "__main__":
    auto = Automatizacao()
    auto.enviar_email()
