import mysql.connector as mysql
connection = mysql.connect(host="127.0.0.1",database='Terminal_Rodoviario',user = "root",passwd= "labinfo26")
cursor = connection.cursor()
def menu1():
    return('Menu de admnistração\n1-Admnistrar Empresas\n2-Admnistrar Ônibus\n3-Admnistrar Viagens')
print(menu1())
adm=int(input())

if adm==1:
    try:
            
        print('Carregando...')
        import time
        time.sleep(3)
        reg1=input('Sistema admnistrativo de empresas\n1-Registro de empresa\n2-Alterar registro\n3-Sair\n')
                # registrar empresa
        if reg1=='1':
                        print('Sequencia de Registro:CNPJ,nome,telefone,veiculos,rua,bairro,cidade,estado')
                        cnpj=input()
                        nomeempr=input()
                        telefoneempr=input()
                        veiculosempr=input()
                        ruaempr=input()
                        bairroempr=input()
                        cidadeempr=input()
                        estadoempr=input()
                        mySql_insert_query = "INSERT INTO Empresa (CNPJ,nome,telefone,veiculos,rua,bairro,cidade,estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(mySql_insert_query, (cnpj,nomeempr,telefoneempr,veiculosempr,ruaempr,bairroempr,cidadeempr,estadoempr))
                        connection.commit()
                        print("Registro de empresa completo")
                    # opção 2 menu empresa/alteração de registro de empresa
        elif reg1=='2':
                    print('Carregando...')
                    import time
                    time.sleep(1)
                    print('Alteração de registro de empresa')
                    update1=input('O que alterar?\n')
                    update2=input('Valor ao ser alterado\n')
                    
                    update3=input('CNPJ da empresa\n')
                    mySql_insert_query = f"UPDATE Empresa SET {update1} = '{update2}' WHERE CNPJ={update3}"
                    cursor.execute(mySql_insert_query)
                    connection.commit()

                    # opção 3/returnar ao menu principal)
        elif reg1=='3':
            print(menu1())
            adm=int(input())
        else:
                    print("Opção Invalida")
    except mysql.connection.Error as error:
                    print("Falha ao registrar empresa{}".format(error))

    finally:
                        ##Fechamento
                        if connection.is_connected():
                            cursor.close()
                            connection.close()
                            print("MySQL finalizado")
elif adm==2:
    try:
        Placa=input()
        chassi=input()
        assentos_comerciais=input()
        assentos_executivos=input()

        cursor = connection.cursor()
        insert = "INSERT INTO Empresa (Placa,chassi,assentos_comerciais,assentos_executivos) VALUES (%s, %s, %s, %s)"
        gravar = (Placa,chassi,assentos_comerciais,assentos_executivos)
        cursor.execute(insert,gravar)
        connection.commit()
        print("Inserção bem executada")

    except mysql.connection.Error as error:
                        print("Falha ao registrar empresa{}".format(error))

    finally:
                            ##Fechamento
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                                print("MySQL finalizado")
