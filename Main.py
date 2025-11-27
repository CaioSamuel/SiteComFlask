from flask import Flask, url_for, render_template, request, redirect

arquivo = 'arquivos.txt'
#Inicialização
app = Flask(__name__)

#Rotas
@app.route('/')
def ola_mundo():
    titulo = "Seja bem-vindo!"
    return render_template('index.html', titulo=titulo)

@app.route('/sobre')
def pagina_sobre():
    return 'Página Sobre'

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']

    try:
        with open(arquivo, 'a') as f:
            f.write(f"Nome: {nome}; Email: {email} \n")
        print(f"Dados salvo em: {arquivo}")
    except Exception as exc:
        print(f"Erro ao salvar os dados em", exc)

    return f"Dados recebidos!"

#Execução
app.run(debug = True)