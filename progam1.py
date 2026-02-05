from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
import sqlite3
from typing import List, Optional
from datetime import datetime

DB_PATH = "clientes.db"
app = FastAPI(title="API Cadastro de Clientes")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def dict_from_row(row):
    return {"id": row[0], "name": row[1], "email": row[2], "phone": row[3], "created_at": row[4]}


class ClienteCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: Optional[str] = None


class Cliente(ClienteCreate):
    id: int
    created_at: str


@app.on_event("startup")
def startup():
    init_db()


@app.post("/clientes", response_model=Cliente, status_code=201)
def criar_cliente(payload: ClienteCreate):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    try:
        cur.execute(
            "INSERT INTO clientes (name, email, phone, created_at) VALUES (?, ?, ?, ?)",
            (payload.name, payload.email, payload.phone, now),
        )
        conn.commit()
        cliente_id = cur.lastrowid
        cur.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
        row = cur.fetchone()
        return dict_from_row(row)
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    finally:
        conn.close()


@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [dict_from_row(r) for r in rows]


@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obter_cliente(cliente_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return dict_from_row(row)


@app.put("/clientes/{cliente_id}", response_model=Cliente)
def atualizar_cliente(cliente_id: int, payload: ClienteCreate):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE clientes SET name = ?, email = ?, phone = ? WHERE id = ?",
            (payload.name, payload.email, payload.phone, cliente_id),
        )
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cliente não encontrado.")
        conn.commit()
        cur.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
        row = cur.fetchone()
        return dict_from_row(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email já cadastrado por outro cliente.")
    finally:
        conn.close()


@app.delete("/clientes/{cliente_id}", status_code=204)
def deletar_cliente(cliente_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    conn.commit()
    conn.close()
    return None