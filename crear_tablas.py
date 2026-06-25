from database import conectar

conn = conectar()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE,
    nombre VARCHAR(100),
    direccion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id),
    total NUMERIC(10,2),
    estado VARCHAR(30),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS detalle_pedido(
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id),
    producto VARCHAR(100),
    cantidad INTEGER,
    precio NUMERIC(10,2)
);
""")

conn.commit()
cur.close()
conn.close()

print("Base creada correctamente")