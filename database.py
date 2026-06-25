import psycopg2
from config import *

def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
def agregar_al_carrito(telegram_id, producto):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO carrito(telegram_id, producto, cantidad)
        VALUES(%s,%s,1)
    """, (telegram_id, producto))

    conn.commit()

    cur.close()
    conn.close()

def obtener_carrito(telegram_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT producto,
               COUNT(*) as cantidad
        FROM carrito
        WHERE telegram_id = %s
        GROUP BY producto
    """, (telegram_id,))

    datos = cur.fetchall()

    cur.close()
    conn.close()

    return datos

def vaciar_carrito(telegram_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM carrito WHERE telegram_id=%s",
        (telegram_id,)
    )

    conn.commit()

    cur.close()
    conn.close()