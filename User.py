# -*- coding: utf-8 -*-

import pymysql

from Tools import ToolsUser, TableHeaders, PrintingTable
from DatabaseCon import close, login


class User:
    
    def __init__(self, conn, cursor):
        print('Jesteś w userze')
        User.panel_usera(self, conn, cursor)
    
    def panel_usera(self, conn, cursor):
                    
        while(True):
            print('Wybierz spośród poniższych: ')
            choice = input('1 - lista uprawnionych pojazdów\n2 - lista wszystkich miejsc i pojazdów\nq - wyloguj\nwybierasz: ').upper()
            if (choice == '1'):
                User.lista_aktywnych_pojazdow(self, conn, cursor)
                input('Kontynuuj\n')
                
            elif (choice == '2'):
                User.lista_miejsc(self, conn, cursor)
                input('Kontynuuj\n')
                
            elif (choice == 'Q'):
                print('Zostałeś wylogowany')
                # login(self)
                break

            else:
                print('Wychodzisz z programu...')
                close(self)
                print('Wyszedłeś z programu')
                break
            
        
    def lista_aktywnych_pojazdow(self, conn, cursor):
        cursor.execute('SELECT * FROM lista_aktywnych_pojazdow')
        result = cursor.fetchall()
        columns = ('id_m', 'rejestracja', 'data_start', 'data_stop')
        table = PrintingTable.tableParameters(self, columns)
        PrintingTable.printingTable(self, result, table)

    def lista_miejsc(self, conn, cursor):
        cursor.execute('SELECT * FROM lista_miejsc')
        result = cursor.fetchall()
        columns = ('id_m', 'opis_m', 'rejestracja', 'imie', 'nazwisko')
        table = PrintingTable.tableParameters(self, columns)
        PrintingTable.printingTable(self, result, table)
        
    
