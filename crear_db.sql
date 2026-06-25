```sql
CREATE DATABASE bot_comida;

-- Conectarse a la base bot_comida antes de ejecutar el resto.

CREATE TABLE clientes (

    id SERIAL PRIMARY KEY,

    telegram_id BIGINT UNIQUE NOT NULL,

    nombre VARCHAR(100),

    usuario VARCHAR(100),

    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE carrito (

    id SERIAL PRIMARY KEY,

    telegram_id BIGINT NOT NULL,

    producto VARCHAR(100) NOT NULL,

    cantidad INTEGER DEFAULT 1,

    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE pedidos (

    id SERIAL PRIMARY KEY,

    telegram_id BIGINT NOT NULL,

    direccion TEXT,

    total NUMERIC(10,2),

    estado VARCHAR(30) DEFAULT 'Pendiente',

    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE detalle_pedido (

    id SERIAL PRIMARY KEY,

    pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,

    producto VARCHAR(100),

    cantidad INTEGER,

    precio NUMERIC(10,2)

);
```
