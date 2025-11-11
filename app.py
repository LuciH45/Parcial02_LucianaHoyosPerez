from flask import Flask, jsonify

app = Flask(__name__)

# Ruta que recibe un número por la URL
@app.route('/numero/<int:n>', methods=['GET'])
def calcular(n):
    # Calcular factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Determinar si es par o impar
    tipo = "par" if n % 2 == 0 else "impar"

    # Crear respuesta JSON
    respuesta = {
        "numero": n,
        "factorial": factorial,
        "tipo": tipo
    }

    return jsonify(respuesta)


if __name__ == '__main__':
    app.run(debug=True)
