import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Unitins@2025",
        database="aula11pmw",
    )

def list_usuarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuario")
    colunas = [desc[0] for desc in cursor.description]
    usuarios = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    con.close()
    return usuarios

def find_usuario(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id = %s", (id,))
    colunas = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    usuario = dict(zip(colunas, row)) if row else None
    con.close()
    return usuario

def insert_usuario(nome, email, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)",
        (nome, email, senha),
    )
    con.commit()
    con.close()

def update_usuario(id, nome, email, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE usuario SET nome=%s, email=%s, senha=%s WHERE id=%s",
        (nome, email, senha, id),
    )
    con.commit()
    con.close()

def delete_usuario(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    con.commit()
    con.close()
