'''
TABELA: petshop
id          - int - autoincrement
tipo_pet    - varchar2(30)
nome_pet    - varchar2(30)
idade       - int
'''

import os
import oracledb # python -m pip install oracledb
import pandas as pd # python -m pip install pandas

os.system("cls")
usuario = "???????" # Coloque a sua credencial do Oracle
senha = "?????????" # Coloque a sua credencial do Oracle
try:
    conn = oracledb.connect(user = usuario, password = senha, dsn='oracle.fiap.com.br:1521/ORCL')
    inst_cadastro = conn.cursor() # Cria um cursor para cadastro - Entende Comandos SQL
    inst_consulta = conn.cursor() # Cria um cursor para cadastro - Entende Comandos SQL
    inst_alteracao = conn.cursor() # Cria um cursor para cadastro - Entende Comandos SQL
    inst_exclusao = conn.cursor() # Cria um cursor para cadastro - Entende Comandos SQL

except Exception as e:
    print("ERRO: ", e)
    conexao = False
else:
    conexao = True

while conexao:
    print("""
    --------- CRUD - PETSHOP ---------
    0 - SAIR
    1 - Cadastrar Pets
    2 - Listar Pets
    3 - Alterar Pets
    4 - Excluir Pets
    5 - Apagar Todos
    """)
    escolha = input("Escolha: ")
    os.system("cls")
    match escolha:
        case "0":
            break 
        case "1":
            try:
                # Capturar os dados do usuário
                print("CADASTRAR PET")
                tipo = input("Tipo......: ")
                nome = input("Nome......: ")
                idade = int(input("Idade....: "))

                # Montagem de instrução CQL de cadastro
                cadastro = f"""
                INSERT INTO petshop
                (tipo_pet, nome_pet, idade)
                VALUES('{tipo}', '{nome}', {idade})
                """

                # Executa a instrução SQL
                inst_cadastro.execute(cadastro)
                conn.commit() # Efetua a gravação magneticamente
            except ValueError:
                print("Digite um número na idade!")
            except Exception as e:
                print("ERRO: ", e)
            else:
                print("\nDADOS GRAVADOS!")
                conn.close()

        case "2":
            print("LISTAR PETS")
            lista_dados = []

            # montar = instrução SQL de listagem dos registros
            inst_consulta.execute('SELECT * FROM petshop')

            data = inst_consulta.fetchall() #  captura todos os registros e joga no objeto data

            if data:
                for dt in data:
                    lista_dados.append(dt)
            else:
                input("Nenhum registro encontrado!")
                continue

            lista_dados.sort()

            dados_df = pd.DataFrame(
                lista_dados,
                columns=['id', 'Tipo', 'Nome', 'Idade'],
            )

            print(dados_df.to_string(
                index=False,
                col_space= {
                    "Id": 5,
                    "Tipo": 15,
                    "Nome": 20,
                    "Idade": 8
                },
                justify="left"
                ))

        case "3":
            try:
                print("EDITANDO OS DADOS")
                consulta = """
                SELECT id, nome_pet
                FROM petshop
                ORDER BY id
                """

                inst_consulta.execute(consulta)

                data = inst_consulta.fetchall()

                if not data:
                    input("A tabela está vazia!")
                    continue

                dados_df = pd.DataFrame(
                    data,
                    columns=["Id", "Nome"]
                )

                print(dados_df.to_string(index=False, col_space=15))

                lista_dados = []

                pet_id = int(input("Id.......: "))

                consulta = f"""
                SELECT *
                FROM petshop
                WHERE id = {pet_id}
                """

                inst_consulta.execute(consulta)
                data = inst_cadastro.fetchall()

                if not data:
                    print("Registro não encontrado")
                    continue

                for dt in data:
                    lista_dados.append(dt)

                    print("EDITAR PET")
                    novo_tipo = input("Tipo......: ")
                    novo_nome = input("Nome......: ")
                    nova_idade = int(input("Idade....: "))

                    # construir a instrução de edição de registro
                    alteracao = f"""
                    UPDATE petshop
                    SET tipo_pet = '{novo_tipo}', nome_pet='{novo_nome}', idade={nova_idade}
                    WHERE id = {pet_id}
                    """

                    inst_alteracao.execute(alteracao)
                    conn.commit()
            except Exception as e:
                print("Erro: ", e)
            else:
                print("Dados atualizados")

        case "4":
            try:
                print("EXCLUIR PET")
                lista_dados = []
                pet_id = int(input("Id.......: "))

                consulta = f"SELECT * FROM petshop WHERE id = {pet_id}"

                inst_consulta.execute(consulta)

                data = inst_consulta.fetchall()

                for dt in data:
                    lista_dados.append(dt)

                if len(lista_dados) == 0:
                    print("Pet não cadastrado com este ID")
                else: # Está cadastrado
                    exclusao = f"DELETE FROM petshop WHERE id = {pet_id}"
                    inst_exclusao.execute(exclusao)
                    conn.commit()
                    print("Pet apagado!")

                
            except Exception as e:
                print("Erro: ", e)
            else:
                conn.close()

        case "5":
            print("!!!!! EXCLUIR TODOS OS REGISTROS DA TABELA !!!!!")
            try:
                exclusao = "DELETE FROM petshop"
                inst_exclusao.execute(exclusao)
                conn.commit()

                # zerando os ids
                data_reset_ids = """ ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                inst_exclusao.execute(data_reset_ids)
                conn.commit()
                print("Todos os registros foram excluídos")


            except Exception as e:
                print("Erro: ", e)
            else:
                conn.close()
    
input("Pressione algo para continuar.........")