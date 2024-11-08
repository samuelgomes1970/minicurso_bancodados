import DAO
DAO.inserir_usuario('Amanda', 'amanda@teste.com', )
DAO.inserir_usuario('Natan', 'natan@teste.com', )
DAO.inserir_usuario('José', 'jose@teste.com', )
# Teste de consulta
saida = DAO.buscar_usuario('Natan')
print(saida)
# Teste de listar todos
saida = DAO.listar_usuarios()
print(saida)
# Teste de atualização
saida = DAO.atualizar_usuario(2,'amanda2','amanda2@teste.com')
print(saida)
# Teste de remoção
