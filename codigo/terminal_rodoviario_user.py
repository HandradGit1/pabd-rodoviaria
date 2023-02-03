import mysql.connector as mysql
import sys
import datetime
connection = mysql.connect(host="127.0.0.1",database='Terminal_Rodoviario',user = "root",passwd= "labinfo26")
cursor = connection.cursor()

def menu1():
    return('Bem-Vindo\n1-Usário\n2-Bilhetes\n3-Listar Viagens\n4-Pesquisar Viagem')

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
                    False
                    break
            
        except mysql.connection.Error as error:
            print("Falha ao registrar usuário{}".format(error))
    if user==2:
            print('Sessão ainda em construção, tente novamente mais tarde')
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
            print("ID da viagem:", id_viagem, "saindo de:", saida,"as", time_string1[:5],"e parando em:", chegada,"as:", time_string2[:5])


    if user==4:
        print("Pesquisar viagem por:\n1-Data\n2-empresa de ônibus\n3-Cidade de origem\n4-Cidade de destino")
        pesquisa = int(input())
        if pesquisa==1:
            data=input("Insira a data")
            pesquisadata = f"SELECT Viagem.ID_viagem, Viagem.origem, Viagem.destino, Viagem.hora_chegada, Viagem.hora_saida, bilhete.data_viagem FROM Viagem JOIN bilhete ON Viagem.ID_viagem = bilhete.ID_viagem WHERE bilhete.data_viagem='{data}';'"
            cursor.execute(pesquisadata)
            lista = cursor.fetchall()
        for x in lista:
            id_viagem = x[0]
            saida = x[1]
            chegada = x[2]
            time_column1 = x[3]
            time_column2 = x[4]
            time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
            time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
            print("ID da viagem:", id_viagem, "saindo de:", saida,"as", time_string1[:5],"e parando em:", chegada,"as:", time_string2[:5])
            
        if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL finalizado")
