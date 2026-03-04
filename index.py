from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    """Controla la lógica principal de la aplicación."""
    resultado = None

    if request.method == "POST":
        opcion = request.form.get("opcion")

        if opcion == "calculadora":
            numero1 = float(request.form.get("numero1"))
            numero2 = float(request.form.get("numero2"))
            operacion = request.form.get("operacion")

            if operacion == "sumar":
                resultado = numero1 + numero2
            elif operacion == "restar":
                resultado = numero1 - numero2
            elif operacion == "multiplicar":
                resultado = numero1 * numero2
            elif operacion == "dividir":
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    resultado = "No se puede dividir entre cero."

        elif opcion == "moneda":
            dolares = float(request.form.get("dolares"))
            tasa_cambio = 4000
            resultado = dolares * tasa_cambio

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)