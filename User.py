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
                sort = UserMenu.sortOption(self, self.columns)
                while(sort):
                    print(sort)
                    if sort == 'sort again':
                        sort = UserMenu.sortOption(self, self.columns)
                        if sort == False:
                            break
                    sort_kol = self.columns[int(sort[0]) - 1]
                    try:
                        if sort[1] == 'desc':
                            sortType = ' desc'
                    except:
                        sortType = ''
                    query = SQLQueries.lista_aktywnych_pojazdow_sorted + sort_kol + sortType
                    User.lista_aktywnych_pojazdow(self, conn, cursor, query)
                    sort = UserMenu.sortQuestion(self)
                
            elif (choice == '2'):
                query = SQLQueries.lista_miejsc
                User.lista_miejsc(self, conn, cursor, query)
                sort = UserMenu.sortOption(self, self.columns)
                while(sort):
                    print(sort)
                    if sort == 'sort again':
                        sort = UserMenu.sortOption(self, self.columns)
                        if sort == False:
                            break
                    sort_kol = self.columns[int(sort[0]) - 1]
                    try:
                        if sort[1] == 'desc':
                            sortType = ' desc'
                    except:
                        sortType = ''
                        
                    query = SQLQueries.lista_miejsc_sorted + sort_kol + sortType
                    User.lista_miejsc(self, conn, cursor, query)
                    sort = UserMenu.sortQuestion(self)                
                
                # User.lista_miejsc(self, conn, cursor)
                
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
        result = cursor.fetchall()
        self.columns = ('id_m', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, result, table)
        return self.columns
        

    def lista_miejsc(self, conn, cursor, query):
        cursor.execute(query)
        result = cursor.fetchall()
        self.columns = ('id_m', 'opis_m', 'rejestracja', 'imie', 'nazwisko')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, result, table)
        return self.columns
