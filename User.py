# -*- coding: utf-8 -*-

import pymysql

from Tools import TableHeaders, PrintingTable, UserMenu, SQLQueries
from DatabaseCon import close, login


class User:
    
    columns = ()
    
    def __init__(self, conn, cursor):
        print('Jesteś w userze')
        User.panel_usera(self, conn, cursor)
    
    def panel_usera(self, conn, cursor):
                    
        while(True):
            print('Wybierz spośród poniższych: ')
            choice = input('1 - lista uprawnionych pojazdów\n2 - lista wszystkich miejsc i pojazdów\nq - wyloguj\nwybierasz: ').upper()
            if (choice == '1'):
                query = SQLQueries.lista_aktywnych_pojazdow
                User.lista_aktywnych_pojazdow(self, conn, cursor, query)
                sort = True
                while(sort):
                    UserMenu.sorting(self, self.columns, self.result)
                    if len(self.collist) > 0:
                        User.lista_aktywnych_pojazdow_sorted(self, self.result, self.columns)
                        sort = UserMenu.sortQuestion(self)
                    else:
                        print('Wracasz do głównego menu')
                        break
                
            elif (choice == '2'):
                query = SQLQueries.lista_miejsc
                User.lista_miejsc(self, conn, cursor, query)
                sort = True
                while(sort):
                    UserMenu.sorting(self, self.columns, self.result)
                    if len(self.collist) > 0:
                        User.lista_miejsc_sorted(self, self.result, self.columns)
                        sort = UserMenu.sortQuestion(self)
                    else:
                        print('Wracasz do głównego menu')
                        break
            
            elif (choice == 'Q'):
                print('Zostałeś wylogowany')
                # login(self)
                break

            else:
                print('Wychodzisz z programu...')
                close(self)
                print('Wyszedłeś z programu')
                break
            
        
    def lista_aktywnych_pojazdow(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns
    
    def lista_aktywnych_pojazdow_sorted(self, result, columns):
        self.columns = ('id_m', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)   

    def lista_miejsc(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'opis_m', 'rejestracja', 'imie', 'nazwisko')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns

    def lista_miejsc_sorted(self, result, columns):
        self.columns = ('id_m', 'opis_m', 'rejestracja', 'imie', 'nazwisko')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table) 