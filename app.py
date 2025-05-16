from flask import Flask, render_template, request, redirect
from models import (
    list_usuarios,
    find_usuario,
    insert_usuario,
    update_usuario,
    delete_usuario,
)

app = Flask(__name__)

@app.route("/")
def index():
    usuarios = list_usuarios()
    return render_template("index.html", usuarios=usuarios)

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        insert_usuario(
            request.form["nome"], request.form["email"], request.form["senha"]
        )
        return redirect("/")
    return render_template("form.html", usuario={})

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        update_usuario(
            id, request.form["nome"], request.form["email"], request.form["senha"]
        )
        return redirect("/")
    usuario = find_usuario(id)
    return render_template("form.html", usuario=usuario)

@app.route("/delete/<int:id>")
def delete(id):
    delete_usuario(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
