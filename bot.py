from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

import os
from dotenv import load_dotenv

from database import (
    agregar_al_carrito,
    obtener_carrito,
    vaciar_carrito
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

usuarios_esperando_direccion = {}

PRECIOS = {
    "Hamburguesa Clásica": 8500,
    "Hamburguesa Doble": 11500,
    "Pizza Muzzarella": 14000,
    "Papas Grandes": 6000
}


# ---------------- START ----------------

async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    teclado = [
        ["📋 Menú"],
        ["🛒 Mi Pedido"],
        ["🗑 Vaciar Carrito"],
        ["✅ Confirmar Pedido"],
        ["📍 Horarios"],
        ["❓ Ayuda"]
    ]

    await update.message.reply_text(
        "🍔 Bienvenido a Sabor Express",
        reply_markup=ReplyKeyboardMarkup(
            teclado,
            resize_keyboard=True
        )
    )


# ---------------- MENU ----------------

async def menu(update: Update,
               context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🍔 MENÚ\n\n"
        "1 - Hamburguesa Clásica ($8500)\n"
        "2 - Hamburguesa Doble ($11500)\n"
        "3 - Pizza Muzzarella ($14000)\n"
        "4 - Papas Grandes ($6000)\n\n"
        "Escribí el número del producto."
    )


# ---------------- MENSAJES ----------------

async def mensajes(update: Update,
                   context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text

    # DIRECCION

    if update.effective_user.id in usuarios_esperando_direccion:

        direccion = texto

        usuarios_esperando_direccion.pop(
            update.effective_user.id
        )

        await update.message.reply_text(
            "✅ Pedido confirmado\n\n"
            f"📍 Dirección:\n{direccion}\n\n"
            "🍔 Lo estamos preparando."
        )

        return

    texto = texto.lower()

    # RESERVAS

    if "reserva" in texto or "mesa" in texto:

        await update.message.reply_text(
            "ℹ️ Actualmente solo trabajamos con pedidos para entrega o retiro.\n\n"
            "No tomamos reservas."
        )

    # HORARIOS

    elif texto == "📍 horarios":

        await update.message.reply_text(
            "⏰ Horario de atención\n\n"
            "Lunes a Domingo\n"
            "18:00 a 00:00"
        )

    # AYUDA

    elif texto == "❓ ayuda":

        await update.message.reply_text(
            "📌 Opciones disponibles:\n\n"
            "📋 Menú\n"
            "🛒 Mi Pedido\n"
            "🗑 Vaciar Carrito\n"
            "✅ Confirmar Pedido\n"
            "📍 Horarios"
        )

    # MENU

    elif texto == "📋 menú":

        await menu(update, context)

    # PRODUCTO 1

    elif texto == "1":

        agregar_al_carrito(
            update.effective_user.id,
            "Hamburguesa Clásica"
        )

        await update.message.reply_text(
            "✅ Hamburguesa Clásica agregada."
        )

    # PRODUCTO 2

    elif texto == "2":

        agregar_al_carrito(
            update.effective_user.id,
            "Hamburguesa Doble"
        )

        await update.message.reply_text(
            "✅ Hamburguesa Doble agregada."
        )

    # PRODUCTO 3

    elif texto == "3":

        agregar_al_carrito(
            update.effective_user.id,
            "Pizza Muzzarella"
        )

        await update.message.reply_text(
            "✅ Pizza Muzzarella agregada."
        )

    # PRODUCTO 4

    elif texto == "4":

        agregar_al_carrito(
            update.effective_user.id,
            "Papas Grandes"
        )

        await update.message.reply_text(
            "✅ Papas Grandes agregadas."
        )

    # VER CARRITO

    elif texto == "🛒 mi pedido":

        carrito = obtener_carrito(
            update.effective_user.id
        )

        if not carrito:

            await update.message.reply_text(
                "🛒 Tu carrito está vacío."
            )
            return

        mensaje = "🛒 TU PEDIDO\n\n"

        total = 0

        for producto, cantidad in carrito:

            subtotal = PRECIOS[producto] * cantidad
            total += subtotal

            mensaje += f"{cantidad}x {producto}\n"

        mensaje += f"\n💰 Total: ${total}"

        await update.message.reply_text(
            mensaje
        )

    # VACIAR

    elif texto == "🗑 vaciar carrito":

        vaciar_carrito(
            update.effective_user.id
        )

        await update.message.reply_text(
            "🗑 Carrito vaciado correctamente."
        )

    # CONFIRMAR

    elif texto == "✅ confirmar pedido":

        carrito = obtener_carrito(
            update.effective_user.id
        )

        if not carrito:

            await update.message.reply_text(
                "🛒 Tu carrito está vacío."
            )
            return

        usuarios_esperando_direccion[
            update.effective_user.id
        ] = True

        await update.message.reply_text(
            "📍 Escribí tu dirección completa."
        )

    # DESCONOCIDO

    else:

        await update.message.reply_text(
            "❌ No entendí tu mensaje.\n\n"
            "Usá los botones del menú."
        )


# ---------------- APP ----------------

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("menu", menu)
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        mensajes
    )
)

print("Bot iniciado correctamente...")

app.run_polling()