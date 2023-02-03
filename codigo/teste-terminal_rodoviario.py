import mysql.connector as mysql
import sys
connection = mysql.connect(host="127.0.0.1",database='Terminal_Rodoviario',user = "root",passwd= "labinfo26")
cursor = connection.cursor()

def menu1():
    return('Menu de admnistração\n1-Admnistrar Empresas\n2-Admnistrar Ônibus\n3-Admnistrar Viagens\n5-Finalizar sessão')

while True:
    print(menu1())
    adm = int(input())
    if adm == 1:
        try:
            while True:
                print('Carregando...')
                import time
                time.sleep(1)
                reg1 = input('Sistema admnistrativo de empresas\n1-Registrar empresa\n2-Alterar registro\n3-Voltar\n')
                # registrar empresa
                if reg1 == '1':
                    print('Sequencia de Registro:CNPJ,nome,telefone,veiculos,rua,bairro,cidade,estado')
                    cnpj = input()
                    nomeempr = input()
                    telefoneempr = input()
                    veiculosempr = input()
                    ruaempr = input()
                    bairroempr = input()
                    cidadeempr = input()
                    estadoempr = input()
                    mySql_insert_query = "INSERT INTO Empresa (CNPJ,nome,telefone,veiculos,rua,bairro,cidade,estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(mySql_insert_query, (cnpj,nomeempr,telefoneempr,veiculosempr,ruaempr,bairroempr,cidadeempr,estadoempr))
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
            print("Falha ao registrar empresa{}".format(error))

            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL finalizado")

    #menu Onibus
    elif adm==2:
        while True:
            try:
                print('Carregando...')
                import time
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
                                print("Falha ao registrar empresa{}".format(error))
    
    if adm == 5:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL finalizado")
            sys.exit()