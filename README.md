# 🍔 Sabor Express - Bot de Telegram para Pedidos de Comida
## Descripción
Sabor Express es un bot desarrollado en Python utilizando la librería python-telegram-bot 22.8 y PostgreSQL 

## Tecnologías utilizadas
Python 3.11
python-telegram-bot 22.8
PostgreSQL
pgAdmin 4
psycopg2
python-dotenv
Visual Studio Code

## Funcionalidades
Inicio mediante `/start`
Menú interactivo
Agregar productos al carrito
Carrito persistente en PostgreSQL
Cálculo automático del total
Vaciar carrito
Confirmar pedido
Solicitar dirección del cliente
Notificación automática al administrador
Consulta de horarios
Respuesta indicando que no se toman reservas
Manejo básico de errores

## Estructura del proyecto
```
bot-comida/
│
├── bot.py
├── database.py
├── config.py
├── products.py
├── .env.example
├── requirements.txt
├── README.md
└── crear_bd.sql
```
## Instalación
### 1. Clonar el repositorio
git clone https://github.com/USUARIO/bot-comida.git

### 2. Entrar al proyecto
cd bot-comida

### 3. Crear un entorno virtual
python -m venv venv

### 4. Activarlo
Windows
venv\Scripts\activate

### 5. Instalar dependencias
pip install -r requirements.txt

### 6. Crear la base de datos
Ejecutar el archivo:

crear_bd.sql

desde pgAdmin o PostgreSQL.

### 7. Configurar el archivo .env
BOT_TOKEN=TU_TOKEN

ADMIN_ID=TU_ADMIN_ID

DB_HOST=localhost
DB_PORT=5432
DB_NAME=bot_comida
DB_USER=postgres
DB_PASSWORD=TU_PASSWORD


### 8. Ejecutar el bot
python bot.py

## Flujo del sistema
/start
      │
      ▼
Menú
      │
      ▼
Agregar productos
      │
      ▼
Ver carrito
      │
      ▼
Confirmar pedido
      │
      ▼
Ingresar dirección
      │
      ▼
Pedido enviado al administrador



