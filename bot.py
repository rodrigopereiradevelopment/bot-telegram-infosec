import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import secrets
import string

# Carrega as variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Configuração de Logs (para ver o que acontece no terminal)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(
        f"Olá {user}! Eu sou o CyberGuard Bot. 🛡️\n"
        "Estou pronto para te ajudar com ferramentas de segurança.\n"
        "Use /ajuda para ver o que eu posso fazer."
    )

# Comando /ajuda atualizado
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Meus comandos atuais:\n"
        "/start - Inicia o bot\n"
        "/ajuda - Mostra esta lista\n"
        "/ping - Verifica se estou online\n"
        "/senha - Gera uma senha forte (Infosec)"
    )

# Comando /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("PONG! 🏓 Estou ativo e operacional.")

async def gerar_senha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*()-_=+"
    senha = ''.join(secrets.choice(caracteres) for i in range(16))
    
    # Usando HTML é mais fácil de evitar erros com caracteres especiais da senha
    texto_resposta = (
        f"🛡️ <b>Senha Segura Gerada:</b>\n\n"
        f"<code>{senha}</code>\n\n"
        f"<i>Clique na senha para copiar</i>"
    )
    
    await update.message.reply_text(texto_resposta, parse_mode='HTML')

if __name__ == '__main__':
    # Inicializa o Bot
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Adiciona os "escutadores" de comandos
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('ajuda', ajuda))
    application.add_handler(CommandHandler('ping', ping))
    application.add_handler(CommandHandler('senha', gerar_senha))
    
    print("Bot rodando... Aperte Ctrl+C para parar.")
    application.run_polling()