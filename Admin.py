# -*- coding: utf-8 -*-

import pymysql
from Tools import ToolsAdmin, PrintingTable, UserMenu, SQLQueries
from User import User
from DatabaseCon import connection, close, login

class Admin:
    
    columns = ()
    result = 0
    pytanie = True
    
    def __init__(self, conn, cursor):
        print('Jesteś w adminie')
        Admin.panel_admina(self, conn, cursor)
    
    def panel_admina(self, conn, cursor):
        
        while(True):
            print('Wybierz spośród poniższych: ')
            choice = input(  '1 - Podgląd - lista widoków\
                            \n2 - Podgląd - lista tabel\
                            \n3 - Zarządzanie - edycja tabel\
                            \nq - wyloguj\
                            \nwybierasz: ').upper()
            if (choice == '1'):
                while(True):
                    choice = input('Jesteś w menu \'Podgląd - lista widoków\', wybierz następny krok:\
                                    \n1 - lista uprawnionych pojazdów\
                                    \n2 - lista wszystkich miejsc i pojazdów\
                                    \n3 - *lista aktywnych klientów*\
                                    \n4 - *lista posiadaczy pilotów*\
                                    \n5 - *lista klientów z abonamentem > 1 miesiąc* \
                                    \n6 - *lista miejsc niewynajętych i bez przeszkód*\
                                    \n10 - *lista wszystkich klientów*\
                                    \n11 - *lista klientów z nadchodzącym abonamentem*\
                                    \n12 - *lista klientów mających najwięcej pojazdów*\
                                    \nb - powrót do poprzedniego menu\
                                    \n\twybierasz: ').upper()
                    
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

                    elif (choice == '3'):
                        query = SQLQueries.lista_aktywnych_klientow
                        Admin.lista_aktywnych_klientow(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_aktywnych_klientow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                        
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == '4'):
                        query = SQLQueries.lista_posiadaczy_pilotow
                        Admin.lista_posiadaczy_pilotow(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_posiadaczy_pilotow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                           
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == '5'):
                        query = SQLQueries.lista_klientow_z_abonamentem
                        Admin.lista_klientow_z_abonamentem(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_klientow_z_abonamentem_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                           
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == '6'):
                        query = SQLQueries.lista_miejsc_niewynajetych
                        Admin.lista_miejsc_niewynajetych(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_miejsc_niewynajetych_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                             
                            else:
                                print('Wracasz do głównego menu')
                                break                            

                    elif (choice == '10'):
                        query = SQLQueries.lista_wszystkich_klientow
                        Admin.lista_wszystkich_klientow(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_wszystkich_klientow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                        
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == '11'):
                        query = SQLQueries.lista_klientow_z_nadchodzacym
                        Admin.lista_klientow_z_nadchodzacym(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_klientow_z_nadchodzacym_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == '12'):
                        query = SQLQueries.lista_klientow_duzo_samochodow
                        Admin.lista_klientow_duzo_samochodow(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            print(self.result)
                            UserMenu.sorting(self, self.columns, self.result)
                            if len(self.collist) > 0:
                                Admin.lista_klientow_duzo_samochodow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                        
                            else:
                                print('Wracasz do głównego menu')
                                break

                    elif (choice == 'B'):
                        print('Powrót do głównego menu')
                        break
                    
                    else:
                        print('Nie ma takiej opcji, spróbuj jeszcze raz...')
                    
            
            elif (choice == '2'):
                while(True):
                    choice = input('Jesteś w menu \'Podgląd - lista tabel\', wybierz następny krok:\
                                                    \n1 - *tabela miejsc*\
                                                    \n2 - *tabela klientów*\
                                                    \n3 - *tabela samochodów*\
                                                    \n4 - *tabela pilotów*\
                                                    \n5 - *tabela statusów* \
                                                    \nb - powrót do poprzedniego menu\
                                                    \n\twybierasz: ').upper()                    
                    if (choice == '1'):
                        query = SQLQueries.tabela_miejsc
                        Admin.tabela_miejsc(self, conn, cursor, query)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            Admin.tabela_miejsc_sorted(self, self.result, self.columns)
                            sort = UserMenu.sortQuestion(self)                          
                        
                    elif (choice == 'B'):
                        print('Powrót do głównego menu')
                        break
                       
                       
            elif (choice == 'Q'):
                print('Zostałeś wylogowany')
                # login(self)
                break
            
            else:
                print('Zostałeś wylogowany')
                # login(self)
                break
    
    # metody tabel i list:
    def lista_aktywnych_klientow(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns
    
    def lista_aktywnych_klientow_sorted(self, result, columns):
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def lista_posiadaczy_pilotow(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('imie', 'nazwisko', 'nr_p')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    
    
    def lista_posiadaczy_pilotow_sorted(self, result, columns):
        self.columns = ('imie', 'nazwisko', 'nr_p')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
    
    def lista_klientow_z_abonamentem(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    

    def lista_klientow_z_abonamentem_sorted(self, result, columns):
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def lista_miejsc_niewynajetych(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'opis_m', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    

    def lista_miejsc_niewynajetych_sorted(self, result, columns):
        self.columns = ('id_m', 'opis_m', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
             
    def lista_wszystkich_klientow(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('imie', 'nazwisko', 'rejestracja', 'marka', 'model')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    

    def lista_wszystkich_klientow_sorted(self, result, columns):
        self.columns = ('imie', 'nazwisko', 'rejestracja', 'marka', 'model')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def lista_klientow_z_nadchodzacym(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    

    def lista_klientow_z_nadchodzacym_sorted(self, result, columns):
        self.columns = ('id_m', 'imie', 'nazwisko', 'rejestracja', 'data_start', 'data_koniec')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def lista_klientow_duzo_samochodow(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('wlasciciel', 'liczba_pojazdow')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns

    def lista_klientow_duzo_samochodow_sorted(self, result, columns):
        self.columns = ('wlasciciel', 'liczba_pojazdow')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_miejsc(self, conn, cursor, query):
        cursor.execute(query)
        self.result = cursor.fetchall()
        self.columns = ('id_m', 'opis_m', 'slup_lewy', 'slup_prawy', 'sciana_lewa', 'sciana_prawa', 'sciana_przod', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    
    
    def tabela_miejsc_sorted(self, result, columns):
        self.columns = ('id_m', 'opis_m', 'slup_lewy', 'slup_prawy', 'sciana_lewa', 'sciana_prawa', 'sciana_przod', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)