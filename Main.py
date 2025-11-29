from flask import Flask, url_for, render_template, request, redirect
import os

arquivo_estoque = "listaEstoque.txt"
arquivo_funcionarios = "listaFuncionarios.txt"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
arquivo_estoque = os.path.join(BASE_DIR, arquivo_estoque)
arquivo_funcionarios = os.path.join(BASE_DIR, arquivo_funcionarios)

#Inicialização
app = Flask(__name__)

#Rotas
@app.route('/')
def index():
    titulo = "Seja bem-vindo ao gerenciador do Mercadinho do seu Zé"
    return render_template('index.html', titulo=titulo)

@app.route('/adicionarEst', methods = ["POST"])
def adicionarEstoque(produto, prUnit, qtd):
    try:
        with open(arquivo_estoque, "w", encoding="utf-8") as e:
            e.write("{}; {}; {}\n".format(produto, prUnit, qtd))
        print(f"Estoque salvo em: {arquivo_estoque}")
    except Exception as exc:
        print("Erro ao salvar estoque:", exc)
    return render_template('gerEstoque.html')

@app.route('/lerEst')
def lerEstoque(arquivo_estoque):
    try:
        with open(arquivo_estoque, "r", encoding="utf-8") as e:
            for linha in e:
                estoque = linha.strip()
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado.")
    return render_template('gerEstoque.html', estoque=estoque)

@app.route('/adicionarFun', methods=["POST"])
def adicionarFuncionarios(nome, idade, funcao):
    try:
        with open(arquivo_funcionarios, "w", encoding="utf-8") as f:
            f.write("{}; {}; {}\n".format(nome, idade, funcao))
            f.flush()  # força escrita no disco
            os.fsync(f.fileno())  # garante que OS salvou no disco
        print(f"Funcionário salvo em: {arquivo_funcionarios}")
        print("Dados salvos com sucesso!")
    except Exception as exc:
        print("Erro ao salvar funcionário:", exc)
    return render_template('gerFunc.html')

@app.route('/verFun', methods=["GET"])
def verFuncionarios(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                funcionario = linha.strip()
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    return render_template('gerFunc.html', funcionario=funcionario)

@app.route('/buscarProd', methods=["GET"])
def buscarProduto(arquivo_estoque):
    nome_busca = input("Digite o nome do produto: ").strip().lower()
    encontrado = False

    try:
        with open(arquivo_estoque, "r", encoding="utf-8") as e:
            for linha in e:
                dados = linha.split(";")
                nome_produto = dados[0].strip().lower()

                if nome_produto == nome_busca:
                    print(f"Nome: {dados[0].strip()}")
                    print(f"Valor: R$ {dados[1].strip()}")
                    print(f"Quantidade: {dados[2].strip()}")
                    encontrado = True
                    break

        if not encontrado:
            print("Produto não encontrado!")

    except FileNotFoundError:
        print("Arquivo não encontrado!")
    return render_template('gerEstoque.html')

@app.route("/buscarFun", methods=["GET"])
def buscarFuncionario(arquivo_funcionarios):
    nome_busca = input("Digite o nome do funcionário: ").strip().lower()
    encontrado = False

    try:
        with open(arquivo_funcionarios, "r", encoding="utf-8") as e:
            for linha in e:
                dados = linha.split(";")
                nome_funcionario = dados[0].strip().lower()

                if nome_funcionario == nome_busca:
                    print(f"Nome: {dados[0].strip()}")
                    print(f"Idade: {dados[1].strip()} anos")
                    print(f"Função: {dados[2].strip()}")
                    encontrado = True
                    break

        if not encontrado:
            print("Funcionário não encontrado!")

    except FileNotFoundError:
        print("Arquivo não encontrado!")
    return render_template('gerFunc.html')


#Execução
app.run(debug = True)