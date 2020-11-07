import os
from dotenv import load_dotenv

load_dotenv()

# CONSTS
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
TOKEN_VK = os.getenv('VK')
TOKEN_TEL = os.getenv('TELEGRAM')
ID_VK = os.getenv('ID_VK')
ID_TEL = os.getenv('ID_TEL')