# 🛡️ CyberGuard Bot - Telegram

Um bot focado em utilitários de segurança da informação, desenvolvido em Python. Este projeto faz parte do meu portfólio de transição para a área de Tecnologia e Cybersecurity.

## 🚀 Funcionalidades Atuais
- **Gerador de Senhas Fortes**: Utiliza a biblioteca `secrets` do Python para gerar strings criptograficamente seguras, garantindo alta entropia.
- **Interface Intuitiva**: Respostas formatadas em HTML para facilitar a cópia de dados sensíveis no mobile.
- **Arquitetura Assíncrona**: Construído com `python-telegram-bot` (v20+), garantindo alta performance e escalabilidade.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **API**: Telegram Bot API
- **Segurança**: `python-dotenv` (Gestão de variáveis de ambiente) e `secrets` (Criptografia).

## 🔧 Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone[https://github.com/rodrigopereiradevelopment/bot-telegram-infosec.git]
```


2. **Crie um ambiente virtual e instale as dependências:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Configure o arquivo .env:**

Crie um arquivo chamado .env na raiz do projeto e adicione seu token:

```Plaintext
TELEGRAM_TOKEN=seu_token_aqui
```

4. **Execute o bot:**

```bash
python bot.py
```

📄 **Licença**

Este projeto está sob a licença MIT.
