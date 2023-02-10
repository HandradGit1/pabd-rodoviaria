import mysql.connector as mysql
import sys
import time
import datetime
connection = mysql.connect(host="127.0.0.1",database='Terminal_Rodoviario',user = "root",passwd= "labinfo26")
cursor = connection.cursor()

def menu1():
    return('Menu de admnistração\n1-Admnistrar Empresas\n2-Admnistrar Ônibus\n3-Admnistrar Viagens\n4-Relatórios\n5-Finalizar sessão')

while True:
    print(menu1())
    adm = int(input())
    if adm == 1:
        try:
            while True:
                print('Carregando...')
                time.sleep(1)
                reg1 = input('Sistema admnistrativo de empresas\n1-Registrar empresa\n2-Alterar registro\n3-Voltar\n')
                # registrar empresa
                if reg1 == '1':
                    print('Sequencia de Registro:CNPJ,nome,telefone,rua,bairro,cidade,estado')
                    cnpj = input()
                    nomeempr = input()
                    telefoneempr = input()
                    ruaempr = input()
                    bairroempr = input()
                    cidadeempr = input()
                    estadoempr = input()
                    mySql_insert_query = "INSERT INTO Empresa (CNPJ,nome,telefone,rua,bairro,cidade,estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(mySql_insert_query, (cnpj,nomeempr,telefoneempr,ruaempr,bairroempr,cidadeempr,estadoempr))
                    connection.commit()
                    print("Registro de empresa completo")
                elif reg1 == '2':
                    print('Carregando...')
                    import time
                    time.sleep(1)
                    print('Alteração de registro de empresa')
                    update1 = input('O que alterar?\n')
                    update2 = input('Valor ao ser alterado\n')
                    update3 = input('CNPJ da empresa\n')
                    mySql_insert_query = f"UPDATE Empresa SET {update1} = '{update2}' WHERE CNPJ={update3}"
                    cursor.execute(mySql_insert_query)
                    connection.commit()
                elif reg1 == '3':
                    False
                    break

        except mysql.connection.Error as error:
            print("Falha ao alterar banco de dados{}".format(error))

            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL finalizado")

    #menu Onibus
    elif adm==2:
        while True:
            try:
                print('Carregando...')
                time.sleep(1)
                regon1=int(input('Sistema admnistrativo de ônibus\n1-Registrar Veículo\n2-Alterar registro do veículo\n3-Voltar\n'))
                #registro de onibus
                if regon1==1:
                    print("Qual a placa do veículos")
                    placa=input()
                    print('Qual o destino do veículo')
                    destino=input()
                    print('Quantos assentos comerciais ele possuí?')
                    assentos_comerciais=input()
                    print('Quantos assentos executivos ele possuí?')
                    assentos_executivos=input()
                    print('CNPJ da empresa proprietária')
                    cnpj=input()

                    cursor = connection.cursor()
                    insertonib = "INSERT INTO Onibus (Placa,destino,assentos_comerciais,assentos_executivos,Empresa_CNPJ) VALUES (%s, %s, %s, %s,%s)"
                    gravar = (placa,destino,assentos_comerciais,assentos_executivos,cnpj)
                    cursor.execute(insertonib,gravar)
                    connection.commit()
                    print("Inserção bem executada")
                #alterar registro de onibus
                elif regon1==2:
                            print('Carregando...')
                            import time
                            time.sleep(1)
                            print('Alteração de registro de Veiculo')
                            update1=input('O que alterar?\n')
                            update2=input('Valor ao ser alterado\n')
                            
                            update3=input('Placa do Veículo\n')
                            mySql_insert_query = f"UPDATE Onibus SET {update1} = '{update2}' WHERE Placa={update3}"
                            cursor.execute(mySql_insert_query)
                            connection.commit()
                #voltar ao menu principal
                elif regon1==3:
                    False
                    break
                else:
                            print("Opção Invalida")


            except mysql.connection.Error as error:
                print("Falha ao alterar banco de dados{}".format(error))
    #menu viagens
    elif adm == 3:
        try:
            while True:
                print('Carregando...')
                time.sleep(1)
                reg1 = input('Sistema admnistrativo de viagens\n1-Cadastrar Viagem\n2-Alterar Viagem\n3-Voltar\n')
                # registrar viagem
                if reg1 == '1':
                    print('Sequencia de Registro:ID,Cidade de origem,Cidade de destino,hora de saida,hora de chegada')
                    id_viagem= input()
                    cid_orig = input()
                    cid_dest = input()
                    hora_sai = input()
                    hora_cheg = input()
                    viagemreg = "INSERT INTO Viagem (ID_viagem,origem,destino,hora_saida,hora_chegada) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(viagemreg, (id_viagem,cid_orig,cid_dest,hora_sai,hora_cheg))
                    connection.commit()
                    print("Registro de viagem completo")
                elif reg1 == '2':
                    print('Carregando...')
                    time.sleep(1)
                    print('Alteração de registro de viagem')
                    update1 = input('O que alterar?\n')
                    update2 = input('Valor ao ser alterado\n')
                    update3 = input('ID da viagem\n')
                    if update1=="horário de saída":
                        updateviag = f"UPDATE Viagem SET hora_saida = '{update2}' WHERE ID_viagem={update3}"
                        cursor.execute(updateviag)
                        connection.commit()
                    elif update1=="horário de chegada":
                        updateviag = f"UPDATE Viagem SET hora_chegada = '{update2}' WHERE ID_viagem={update3}"
                        cursor.execute(updateviag)
                        connection.commit()
                    else:
                        updateviag = f"UPDATE Viagem SET {update1} = '{update2}' WHERE ID_viagem={update3}"
                        cursor.execute(updateviag)
                        connection.commit()
                    print("Viagem alterada com sucesso")
                elif reg1 == '3':
                    False
                    break
        except mysql.connection.Error as error:
            print("Falha ao alterar banco de dados{}".format(error))
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL finalizado")
    #Menu relatorio
    if adm == 4:
    

    # Função para listar as viagens que irão ocorrer
        def listar_viagens_por_ocorrer():
            mycursor = connection.cursor()
            sql = "SELECT * FROM viagem WHERE hora_saida > NOW()"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print("Lista de viagens a ocorrer:")
            for x in result:
                id_viagem = x[0]
                saida = x[1]
                chegada = x[2]
                time_column1 = x[3]
                time_column2 = x[4]
                time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
                time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
                print("ID da viagem:", id_viagem, "saindo de:", saida,"as", time_string1[:8],"e parando em:", chegada,"as:", time_string2[:8])
    # Função para listar as viagens que já ocorreram
        def listar_viagens_ocorridas():
            mycursor = connection.cursor()
            sql = "SELECT * FROM viagem WHERE hora_saida < NOW()"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print("Lista de viagens que já ocorreram:")
            for x in result:
                id_viagem = x[0]
                saida = x[1]
                chegada = x[2]
                time_column1 = x[3]
                time_column2 = x[4]
                time_string1 = str(datetime.timedelta(seconds=time_column1.total_seconds()))
                time_string2 = str(datetime.timedelta(seconds=time_column2.total_seconds()))
                print("ID da viagem:", id_viagem, "saindo de:", saida,"as", time_string1[:8],"e parando em:", chegada,"as:", time_string2[:8])
    # Loop do menu (levemente problemática, repete em toda saida de menu)
    while True:
        print("Relatório")
        print("1- Lista de viagens a ocorrer")
        print("2- Lista de viagens que já ocorreram")
        print("3- Voltar")
        option = int(input("Escolha uma opção: "))

        if option == 1:
            listar_viagens_por_ocorrer()
        elif option == 2:
            listar_viagens_ocorridas()
        elif option == 3:
            break
        else:
            print("Opção inválida.")
    
    if adm == 5:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Finalizando conexão")
            sys.exit()