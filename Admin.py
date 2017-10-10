# -*- coding: utf-8 -*-

import pymysql
from Tools import ToolsAdmin, PrintingTable, UserMenu, SQLQueries
from User import User
from DatabaseCon import connection, close, login

class Admin:
    
    columns = ()
    result = 0
    pytanie = True
    
    def __init__(self, cursor, conn):
        print('Jesteś w adminie')
        Admin.panel_admina(self, cursor, conn)
    
    def panel_admina(self, cursor, conn):
        
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
                                                    \nwybierasz: ').upper()                    
                    if (choice == '1'):
                        query = SQLQueries.tabela_miejsc
                        Admin.tabela_miejsc(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if (self.collist != []):
                                Admin.tabela_miejsc_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)                          
                            else:
                                break
                        
                    if (choice == '2'):
                        query = SQLQueries.tabela_klientow
                        Admin.tabela_klientow(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            Admin.tabela_klientow_sorted(self, self.result, self.columns)
                            sort = UserMenu.sortQuestion(self)                          
                        
                    elif (choice == 'B'):
                        print('Powrót do głównego menu')
                        break
                       
                       
            elif (choice == '3'):
                while(True):
                    choice = input('Jesteś w menu \'3 - Zarządzanie - edycja tabel\', wybierz następny krok:\
                                                                    \n1 - *edycja tabeli miejsc*\
                                                                    \n2 - *edycja tabeli klientów*\
                                                                    \n3 - *edycja tabeli samochodów*\
                                                                    \n4 - *edycja tabeli pilotów*\
                                                                    \n5 - *edycja tabeli statusów* \
                                                                    \nb - powrót do poprzedniego menu\
                                                                    \nwybierasz: ').upper()                    
                    if (choice == '1'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli miejsc, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu - zablokowane\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu - zablokowane\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            if (choice == '2'):
                                print('W tabeli miejsc możesz edytować jedynie opis')
                                id_m = input('Podaj numer miejsca, które chcesz edytować: ')
                                opis_m = input('Podaj nowy opis wybranego miejsca: ')
                                query_update = SQLQueries.tabela_miejsc_update
                                query_updated = SQLQueries.tabela_miejsc_after_update
                                self.query_param = (opis_m, id_m)
                                self.execute = True
                                Admin.tabela_miejsc(self, conn, cursor, 0, query_update, query_updated)
                            
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                            
                    if (choice == '2'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli klientów, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            if (choice == '1'):
                                imie = input('Podaj imię nowego klienta: ')
                                nazwisko = input('Podaj nazwisko nowego klienta: ')
                                ulica = input('Podaj ulicę nowego klienta: ')
                                nr_budynku = input('Podaj nr budynku nowego klienta: ')
                                nr_mieszkania = int(input('Podaj nr mieszkania nowego klienta: '))
                                kod = input('Podaj kod pocztowy nowego klienta: ')
                                miasto = input('Podaj miasto nowego klienta: ')
                                query_update = SQLQueries.tabela_klientow_insert
                                query_updated = SQLQueries.tabela_klientow_after_insert
                                self.query_param = (imie, nazwisko, ulica, nr_budynku, nr_mieszkania, kod, miasto)
                                self.execute = True
                                Admin.tabela_klientow(self, conn, cursor, 0, query_update, query_updated)
                            
                            if (choice == '2'):
                                while(True):
                                    id_k = int(input('Podaj id klienta, którego dane chcesz zmieniać: '))
                                    if (id_k):
                                        query = SQLQueries.tabela_klientow_for_update
                                        self.query_param = (id_k)
                                        Admin.tabela_klientow_for_update(self, conn, cursor, query)
                                        break
                                    else:
                                        print('Podałeś złe id klienta, spróbuj ponownie')
                                choice = input('Czy chcesz zmienić imię? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Imię przed zmianą: ' + str(self.result_for_update[1][0][1]))
                                    imie = input('Podaj nowe imię (aby pominąć, wciśnij Enter): ')
                                    if (imie == ''):
                                        imie = self.result_for_update[1][0][1]
                                else:
                                    imie = self.result_for_update[1][0][1]
                                choice = input('Czy chcesz zmienić nazwisko? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Nazwisko przed zmianą: ' + str(self.result_for_update[1][0][2]))
                                    nazwisko = input('Podaj nowe nazwisko (aby pominąć, wciśnij Enter): ')
                                    if (nazwisko == ''):
                                        nazwisko = self.result_for_update[1][0][2]
                                else:
                                    nazwisko = self.result_for_update[1][0][2]
                                choice = input('Czy chcesz zmienić ulicę? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Ulica przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][3]))
                                    ulica = input('Podaj nową ulicę: ')
                                    if (ulica == ''):
                                        ulica = self.result_for_update[1][0][3]
                                else:
                                    ulica = self.result_for_update[1][0][3]
                                choice = input('Czy chcesz zmienić nr budynku? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Nr budynku przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][4]))
                                    nr_budynku = input('Podaj nowy nr budynku: ')
                                    if (nr_budynku == ''):
                                        nr_budynku = self.result_for_update[1][0][4]
                                else:
                                    nr_budynku = self.result_for_update[1][0][4]
                                choice = input('Czy chcesz zmienić nr mieszkania? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Nr mieszkania przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][5]))
                                    nr_mieszkania = int(input('Podaj nowy nr mieszkania: '))
                                    if (nr_mieszkania == ''):
                                        nr_mieszkania = self.result_for_update[1][0][5]
                                else:
                                    nr_mieszkania = self.result_for_update[1][0][5]
                                choice = input('Czy chcesz zmienić kod pocztowy? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Kod pocztowy przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][6]))
                                    kod = input('Podaj nowy kod pocztowy: ')
                                    if (kod == ''):
                                        kod = self.result_for_update[1][0][6]
                                else:
                                    kod = self.result_for_update[1][0][6]
                                choice = input('Czy chcesz zmienić miasto? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Miasto przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][7]))
                                    miasto = input('Podaj nowe miasto: ')
                                    if (miasto == ''):
                                        miasto = self.result_for_update[1][0][7]
                                else:
                                    miasto = self.result_for_update[1][0][7]
                                query_update = SQLQueries.tabela_klientow_update
                                query_updated = SQLQueries.tabela_klientow_after_update
                                self.query_param = (imie, nazwisko, ulica, nr_budynku, nr_mieszkania, kod, miasto, id_k)
                                self.query_param_after = (id_k)
                                self.execute = True
                                Admin.tabela_klientow(self, conn, cursor, 0, query_update, query_updated)
                            
                            if (choice == '3'):
                                delete_tekst = 0
                                while(True):
                                    if (delete_tekst):
                                        pytanie = input('Czy chcesz usunąć kolejnego klienta?\
                                                        \n1 - tak\
                                                        \nb - powrót do poprzedniego menu\
                                                        \nwybierasz: ').upper()
                                        if (pytanie == 'B'):
                                            break
                                    pytanie = input('Czy chcesz sprawdzić tabelę klientów przed usunięciem klienta?\
                                                    \n1 - tak\
                                                    \n2 - nie\
                                                    \nb - powrót do poprzedniego menu\
                                                    \nwybierasz: ').upper()
                                    if (pytanie == '1'):
                                        query = SQLQueries.tabela_klientow
                                        Admin.tabela_klientow(self, conn, cursor, query, 0, 0)
                                        sort = True
                                        while(sort):
                                            UserMenu.sorting(self, self.columns, self.result)
                                            Admin.tabela_klientow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)                                        
                                    if (pytanie == 'B'):
                                        break
                                    else:
                                        id_klient = input('Podaj id klienta, którego chcesz usunąć, aby powrócić do poprzedniego menu, naciśnij \'b\': ').upper()
                                        if (id_klient == 'B'):
                                            break
                                        else:
                                            query_delete = SQLQueries.tabela_klientow_delete
                                            query_after_delete = SQLQueries.tabela_klientow
                                            self.query_param_after = (id_klient)
                                            self.delete_temp = False
                                            Admin.tabela_klientow(self, conn, cursor, 0, query_delete, query_after_delete)
                                            delete_tekst = True
                                            
                                    
                            
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                            
                    elif (choice == 'B'):
                        print('Powrót do poprzedniego menu')
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
        
    def tabela_miejsc(self, conn, cursor, query, query_update, query_updated):
        if (query != 0):
            cursor.execute(query)
            self.result = cursor.fetchall()
            self.columns = ('id_m', 'opis_m', 'slup_lewy', 'slup_prawy', 'sciana_lewa', 'sciana_prawa', 'sciana_przod', 'klatka_m')            
        else:
            cursor.execute(query_update, self.query_param)
            if (self.execute):
                conn.commit()
                cursor.execute(query_updated, self.query_update)
                self.result = cursor.fetchall()
                self.columns = ('id_m', 'opis_m', 'slup_lewy', 'slup_prawy', 'sciana_lewa', 'sciana_prawa', 'sciana_przod', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        return self.columns    
    
    def tabela_miejsc_sorted(self, result, columns):
        self.columns = ('id_m', 'opis_m', 'slup_lewy', 'slup_prawy', 'sciana_lewa', 'sciana_prawa', 'sciana_przod', 'klatka_m')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_klientow(self, conn, cursor, query, query_update, query_updated):
        temp = True
        if (query != 0):
            cursor.execute(query)
            self.result = cursor.fetchall()
            self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')            
        else:
            try:
                cursor.execute(query_update, self.query_param_after)
                if (self.delete_temp == False):
                    conn.commit()
                    print('Usunąłeś klienta o numerze: ' + str(self.query_param_after))
                    print('Tabela klientów po usunięciu wygląda następująco:')
                    cursor.execute(query_updated)
                    self.result = cursor.fetchall()
                    self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')                
                elif (self.execute):
                    conn.commit()
                    print('Dodałeś/zmieniłeś następującego klienta:')
                    cursor.execute(query_updated, self.query_param_after)
                    self.result = cursor.fetchall()
                    self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
            except:
                print('Nie możesz usunąć tego rekordu, spróbuj ponownie z innym lub najpierw usuń odwołania do niego w innych tabelach')
                temp = False
        if (temp != False):
            table = PrintingTable.tableParameters(self, self.columns)
            PrintingTable.printingTable(self, self.result, table)        
        return self.columns    
    
    def tabela_klientow_sorted(self, result, columns):
        self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_klientow_for_update(self, conn, cursor, query):
        cursor.execute(query, self.query_param)
        self.result = cursor.fetchall()
        self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
        self.result_for_update = []
        self.result_for_update.append(self.columns)
        self.result_for_update.append(self.result)