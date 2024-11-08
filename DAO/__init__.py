import psycopg2
# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="db_aula_minicurso",
                               host="localhost",
                               user="postgres",
                               password="Samuelgomes1970.",
                               port="5432")
    return conexao
# Chame a função para testar a conexão
conexao = conectardb()

def inserir_usuario(nome, email):
    conexao = conectardb()                  # Estabelece conexão com o banco de dados.
    cursor = conexao.cursor()             # Cria um cursor para executar comandos SQL.
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
                                         # Executa o comando INSERT para adicionar um novo usuário.
    conexao.commit()                      # Salva (confirma) a transação no banco de dados.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco de dados.