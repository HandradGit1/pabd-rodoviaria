import mysql.connector as mysql
import sys
import datetime
connection = mysql.connect(host="127.0.0.1",database='Terminal_Rodoviario',user = "root",passwd= "labinfo26")
cursor = connection.cursor()

def menu1():
    return('Bem-Vindo\n1-Usário\n2-Bilhetes\n3-Listar Viagens\n4-Pesquisar Viagem\n5-log out')

while True:
    print(menu1())
    user = int(input())
    if user == 1:
        try:
            while True:
                reg1 = input('Menu de Usuário\n1-Registrar Usuário\n2-Alterar dados\n3-Voltar\n')
                # registrar usuario
                if reg1 == '1':
                    print('Sequencia de Registro:CPF,Nome,data de nascimento(ano-mês-dia),telefone')
                    cpf = input()
                    nomeuser = input()
                    nascuser = input()
                    telefoneuser = input()
                    insert_user ="INSERT INTO Passageiro (CPF, nome, data_nascimento) VALUES (%s, %s, %s )"
                    insert_user2 = "INSERT INTO Passageiro_Contato (Passageiro_CPF,contato) VALUES (%s, %s)"
                    cursor.execute(insert_user, (cpf,nomeuser, nascuser))
                    cursor.execute(insert_user2, (cpf,telefoneuser,))
                    connection.commit()
                    print("Registro de usuário completo")
                #update dados de usuario
                elif reg1 == '2':
                    print('Carregando...')
                    import time
                    time.sleep(1)
                    print('Alteração de registro de usuário')
                    update1 = input('O que alterar?\n')
                    update2 = input('Valor ao ser alterado\n')
                    update3 = input('CPF do Usuário\n')
                    if update1=='telefone':
                        userupdatetel= f"UPDATE Passageiro_Contato set contato = '{update2}' where Passageiro_CPF={update3}"
                        cursor.execute(userupdatetel)
                        connection.commit()
                        print("Alteração de telefone feita com sucesso")
                        print("Alteração feita com sucesso")
                    elif update1=='data de nascimento':
                        userupdate= f"UPDATE Passageiro set data_nascimento = '{update2}' where CPF={update3}"
                        cursor.execute(userupdate)
                        connection.commit()
                        print("Alteração de telefone feita com sucesso")
                        print("Alteração feita com sucesso")
                    else:
                        mySql_insert_query = f"UPDATE Passageiro SET {update1} = '{update2}' WHERE CPF={update3}"
                        cursor.execute(mySql_insert_query)
                        connection.commit()
                elif reg1 == '3':
                    break
            
        except mysql.connection.Error as error:
            print("Falha ao registrar usuário{}".format(error))
    if user==2:
            bilh = int(input("1-Gerar bilhete\n2-Alterar data do bilhete\n3-Voltar\n"))
            if bilh == 1:
                print('Data da viagem')
                dataviag = input()
                insert_bilh ="INSERT INTO Bilhete (preço,data_viagem) VALUES (80.00, %s )"
                cursor.execute(insert_bilh, (dataviag,))
                connection.commit()
                print("Registro de Bilhete completo")
            if bilh == 2:
                print("Alterar data")
                databilh = input()
                print("Qual o ID do bilhete?")
                update_bilh2 = input()
                update_bilh = f"UPDATE bilhete SET data_viagem = '{databilh}' WHERE ID = {update_bilh2}"
                cursor.execute(update_bilh)
                connection.commit()

    if user==3:
        listar_viagens = "SELECT * FROM Viagem"
        cursor.execute(listar_viagens)
        lista = cursor.fetchall()
        for x in lista:
            id_viagem = x[0]
            saida = x[1]
            chegada = x[2]
            time_column1 = x[3]
            time_column2 = x[4]
            time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
            time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
            print("ID da viagem:", id_viagem, "saindo de:", saida,"as", time_string2[:8],"e parando em:", chegada,"as:", time_string1[:8])


    if user==4:
        pesquisa= int(input ("Pesquisar viagem por:\n1-ID\n2-Cidade de origem\n3-Cidade de destino\n"))
        def pesquisar_viagem():
                        id_viagem = input("Informe o ID da viagem: ")
                        mycursor = connection.cursor()
                        sql = "SELECT * FROM viagem WHERE ID_viagem = %s"
                        val = (id_viagem,)
                        mycursor.execute(sql, val)
                        result = mycursor.fetchall()
                        
                        try:
                            for x in result:
                                id_viagem = x[0]
                                saida = x[1]
                                chegada = x[2]
                                time_column1 = x[3]
                                time_column2 = x[4]
                                time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
                                time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
                                print("Viagem encontrada: ID:",id_viagem, "saindo de:", saida,"as", time_string2[:8],"e parando em:", chegada,"as:", time_string1[:8])
                        except:
                            print("Viagem não encontrada.")
        def pesquisar_viagens_por_cidade_origem():
                cidade_origem = input("Informe a cidade de origem: ")
                mycursor = connection.cursor()
                sql = "SELECT * FROM viagem WHERE origem = %s"
                val = (cidade_origem,)
                mycursor.execute(sql, val)
                result = mycursor.fetchall()
                try :
                    for x in result:
                                    id_viagem = x[0]
                                    saida = x[1]
                                    chegada = x[2]
                                    time_column1 = x[3]
                                    time_column2 = x[4]
                                    time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
                                    time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
                                    print("Viagem encontrada: ID:",id_viagem, "saindo de:", saida,"as", time_string2[:8],"e parando em:", chegada,"as:", time_string1[:8])
                except:
                    print("Nenhuma viagem encontrada para a esta cidade")


        def pesquisar_viagens_por_cidade_destino():
                cidade_destino = input("Informe a cidade de destino: ")
                mycursor = connection.cursor()
                sql = "SELECT * FROM viagem WHERE destino = %s"
                val = (cidade_destino,)
                mycursor.execute(sql, val)
                result = mycursor.fetchall()
                try :
                    for x in result:
                                    id_viagem = x[0]
                                    saida = x[1]
                                    chegada = x[2]
                                    time_column1 = x[3]
                                    time_column2 = x[4]
                                    time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
                                    time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
                                    print("Viagem encontrada: ID:",id_viagem, "saindo de:", saida,"as", time_string2[:8],"e parando em:", chegada,"as:", time_string1[:8])
                except:
                    print("Nenhuma viagem encontrada para a esta cidade")
        if pesquisa==1:
            pesquisar_viagem()
        if pesquisa== 2:
            pesquisar_viagens_por_cidade_origem()
        if pesquisa==3:
            pesquisar_viagens_por_cidade_destino()
        elif pesquisa==4:
                False
                
                
    elif user==5:
        if connection.is_connected():
                cursor.close()
                connection.close()
                print("Finalizando conexão")
                sys.exit()
