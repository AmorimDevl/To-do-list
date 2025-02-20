# Adicionar, editar, remover, listar e sair
# Nome do item, descrição, data, pendente ou concluída
# Itens pendentes e/ou concluídos

import datetime
from time import sleep
import sqlite3

try:
   while True:

# Lista de comandos de comandos
    print(''' 
          [1] Adicionar Item 
          [2] Editar item
          [3] Remover item
          [4] Listar
          [5] Sair da lista ''')

# Comando
    comando = int(input('Selecione uma das opções listadas acima: '))

# Criando a função para adicionar o item ao banco de dados

    def adicionar():
        adicionar_nome = str(input('Qual item deseja adicionar? '))
        adicionar_data = input('Data: ')
        adicionar_status = str(input('Pendente ou Concluído: '))
        conn = sqlite3.connect ('banco_dados.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO banco (item, data, status) VALUES (?,?,?)', (adicionar_nome, adicionar_data, adicionar_status))
        conn.commit()
        conn.close()
        
    if comando == 1:
        adicionar()

# Criando a função para editar o item ao banco de dados

    def editar():
        editar_item = input('Insira o ID: ')
        print('''
              [1] Concluído
              [2] Pendente''')
        conn = sqlite3.connect('banco_dados.db')
        cursor = conn.cursor()
        escolha = int(input('Escolha a opção: '))
        if escolha == 1:
          concluido = 'Concluído'
          cursor.execute('UPDATE banco SET status = ? WHERE id = ?', (concluido, editar_item))
        elif escolha == 2:
          pendente = 'Pendente'
          cursor.execute('UPDATE banco SET status = ? WHERE id = ?', (pendente, editar_item))
        conn.commit()
        conn.close()
    if comando == 2:
        editar()

# Criando a função para remover o item ao banco de dados

    def remover():
        remover_item = input('Insira o ID do item que deseja remover: ')
        conn = sqlite3.connect('banco_dados.db')
        cursor = conn.cursor()
        cursor.execute ('DELETE FROM banco WHERE id = ?', (remover_item))
        conn.commit()
        conn.close()
    if comando == 3:
        remover()

# Criando a função para listar o item ao banco de dados

    def listar():
        print('Listando...')
        sleep(2)
        conn = sqlite3.connect('banco_dados.db')
        cursor = conn.cursor()
        cursor.execute ('SELECT * FROM banco;')
        for linha in cursor.fetchall():
          print(linha)
        conn.close()
    if comando == 4:
        listar()

# Criando a função para remover o item ao banco de dados

    if comando == 5:
      break
except:
   print('Se Fodeu')