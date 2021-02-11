from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")
@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:    
        if (request.form["n1"] !="" and request.form ["n2"] != ""):
            n1 = int(request.form["n1"])
            n2 = int(request.form ["n2"])

            if (request.form['opc'] == 'soma'):
                soma = str(n1 + n2)
                return soma

            elif (request.form['opc'] == 'subtracao'):
                subtracao = str(n1-n2)
                return subtracao

            elif (request.form['opc'] == 'multiplicacao'):
                multiplicacao = str(n1*n2)
                return multiplicacao

            elif (request.form['opc'] == 'divisao'):
                divisao = str(n1/n2)
                return divisao
        else:
            return "Informe dois valores para o cálculo!"


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=5001, debug=True)