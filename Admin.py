# -*- coding: utf-8 -*-

import pymysql, re
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
                            \n' + 5*'-' + '\
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
                                    \n' + 5*'-' + '\
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
                                                    \n5 - *tabela statusów*\
                                                    \n' + 5*'-' + '\
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
                                print('Wracasz do głównego menu')
                                break
                        
                    elif (choice == '2'):
                        query = SQLQueries.tabela_klientow
                        Admin.tabela_klientow(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if (self.collist != []):
                                Admin.tabela_klientow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)
                            else:
                                print('Wracasz do głównego menu')
                                break
                    
                    elif (choice == '3'):
                        query = SQLQueries.tabela_samochodow
                        Admin.tabela_samochodow(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if (self.collist != []):
                                Admin.tabela_samochodow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)
                            else:
                                print('Wracasz do głównego menu')
                                break
                    
                    elif (choice == '4'):
                        query = SQLQueries.tabela_pilotow
                        Admin.tabela_pilotow(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if (self.collist != []):
                                Admin.tabela_pilotow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)
                            else:
                                print('Wracasz do głównego menu')
                                break
                      
                    elif (choice == '5'):
                        query = SQLQueries.tabela_statusow
                        Admin.tabela_statusow(self, conn, cursor, query, 0, 0)
                        sort = True
                        while(sort):
                            UserMenu.sorting(self, self.columns, self.result)
                            if (self.collist != []):
                                Admin.tabela_statusow_sorted(self, self.result, self.columns)
                                sort = UserMenu.sortQuestion(self)
                            else:
                                print('Wracasz do głównego menu')
                                break
                      
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
                                                                    \n' + 5*'-' + '\
                                                                    \nb - powrót do poprzedniego menu\
                                                                    \nwybierasz: ').upper()                    
                    # Tabela miejsc
                    if (choice == '1'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli miejsc, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu - zablokowane\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu - zablokowane\
                                            \n' + 5*'-' + '\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            
                            # Tabela miejsc - dodawanie
                            if (choice == '1'):
                                print('Nie można dodawać nowych miejsc! Nastąpi powrót do poprzedniego menu')
                            
                            # Tabela miejsc - edycja
                            if (choice == '2'):
                                print('W tabeli miejsc możesz edytować jedynie opis')
                                id_m = input('Podaj numer miejsca, które chcesz edytować: ')
                                opis_m = input('Podaj nowy opis wybranego miejsca: ')
                                query_update = SQLQueries.tabela_miejsc_update
                                query_updated = SQLQueries.tabela_miejsc_after_update
                                self.query_param = (opis_m, id_m)
                                self.execute = True
                                Admin.tabela_miejsc(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela miejsc - usuwanie
                            if (choice == '3'):
                                print('Nie można usuwać istniejących miejsc! Nastąpi powrót do poprzedniego menu')
                            
                            # Tabela miejsc - powrót
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                            
                    # Tabela klientów
                    if (choice == '2'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli klientów, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu\
                                            \n' + 5*'-' + '\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            
                            # Tabela klientów - dodawanie
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
                                self.addnew = True
                                self.execute = False
                                self.delete_temp = True
                                Admin.tabela_klientow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela klientów - edycja
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
                                self.delete_temp = True
                                self.execute = True
                                self.addnew = False
                                Admin.tabela_klientow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela klientów - usuwanie
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
                                            if self.collist != []:
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
                                            self.execute = False
                                            self.addnew = False
                                            Admin.tabela_klientow(self, conn, cursor, 0, query_delete, query_after_delete)
                                            delete_tekst = True
                                            
                                    
                            # Tabela klientów - powrót
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                    
                    # Tabela pojazdów
                    if (choice == '3'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli samochodów, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu\
                                            \n' + 5*'-' + '\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            # Tabela pojazdów - dodanie
                            if (choice == '1'):
                                rejestracja = input('Podaj numer rejestracji nowego pojazdu: ')
                                marka = input('Podaj markę nowego pojazdu: ')
                                model = input('Podaj model nowego pojazdu: ')
                                self.pojazd = input('Czy chcesz sprawdzić tabelę klientów przed podaniem nr klienta dla wprowadzanego pojazdu? \'t/n\': ').upper()
                                if (self.pojazd == 'T'):
                                    query = SQLQueries.tabela_klientow
                                    Admin.tabela_klientow(self, conn, cursor, query, 0, 0)
                                    sort = True
                                    while(sort):
                                        UserMenu.sorting(self, self.columns, self.result)
                                        if (self.collist != []):
                                            Admin.tabela_klientow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)
                                        else:
                                            print('Kontynuujesz wprowadzanie nowego pojazdu')
                                            break
                                id_k = input('Podaj nr klienta, do którego należy pojazd: ')
                                query_update = SQLQueries.tabela_samochodow_insert
                                query_updated = SQLQueries.tabela_samochodow_after_insert
                                self.query_param = (id_k, rejestracja, marka, model)
                                self.delete_temp = True
                                self.execute = False
                                self.addnew = True
                                Admin.tabela_samochodow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pojazdów - edycja
                            if (choice == '2'):
                                while(True):
                                    id_s = int(input('Podaj nr pojazdu, którego dane chcesz zmieniać: '))
                                    if (id_s):
                                        query = SQLQueries.tabela_samochodow_for_update
                                        self.query_param = (id_s)
                                        Admin.tabela_samochodow_for_update(self, conn, cursor, query)
                                        break
                                    else:
                                        print('Podałeś zły nr pojazdu, spróbuj ponownie')
                                choice = input('Czy chcesz zmienić rejestrację? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Rejestracja przed zmianą: ' + str(self.result_for_update[1][0][2]))
                                    rejestracja = input('Podaj nową rejestrację (aby pominąć, wciśnij Enter): ')
                                    if (rejestracja == ''):
                                        rejestracja = self.result_for_update[1][0][2]
                                else:
                                    rejestracja = self.result_for_update[1][0][2]
                                choice = input('Czy chcesz markę pojazdu? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Marka pojazdu przed zmianą: ' + str(self.result_for_update[1][0][3]))
                                    marka = input('Podaj nową markę pojazdu (aby pominąć, wciśnij Enter): ')
                                    if (marka == ''):
                                        marka = self.result_for_update[1][0][3]
                                else:
                                    marka = self.result_for_update[1][0][3]
                                choice = input('Czy chcesz zmienić model pojazdu? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Model przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][4]))
                                    model = input('Podaj nowy model pojazdu: ')
                                    if (model == ''):
                                        model = self.result_for_update[1][0][4]
                                else:
                                    model = self.result_for_update[1][0][4]
                                choice = input('Czy chcesz zmienić przynależność pojazdu (nr klienta)? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Nr klienta przed zmianą (aby pominąć, wciśnij Enter): ' + str(self.result_for_update[1][0][1]))
                                    id_k = input('Podaj nowy nr klienta: ')
                                    if (id_k == ''):
                                        id_k = self.result_for_update[1][0][1]
                                else:
                                    id_k = self.result_for_update[1][0][1]
                                query_update = SQLQueries.tabela_samochodow_update
                                query_updated = SQLQueries.tabela_samochodow_after_update
                                self.query_param = (id_k, rejestracja, marka, model, id_s)
                                self.query_param_after = (id_s)
                                self.execute = True
                                self.delete_temp = True
                                self.addnew = False
                                Admin.tabela_samochodow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pojazdów - usuwanie
                            if (choice == '3'):
                                delete_tekst = 0
                                while(True):
                                    if (delete_tekst):
                                        pytanie = input('Czy chcesz usunąć kolejny pojazd?\
                                                        \n1 - tak\
                                                        \nb - powrót do poprzedniego menu\
                                                        \n' + 5*'-' + '\
                                                        \nwybierasz: ').upper()
                                        if (pytanie == 'B'):
                                            break
                                    pytanie = input('Czy chcesz sprawdzić tabelę pojazdów przed usunięciem pojazdu?\
                                                    \n1 - tak\
                                                    \n2 - nie\
                                                    \n' + 5*'-' + '\
                                                    \nb - powrót do poprzedniego menu\
                                                    \nwybierasz: ').upper()
                                    if (pytanie == '1'):
                                        query = SQLQueries.tabela_samochodow
                                        Admin.tabela_samochodow(self, conn, cursor, query, 0, 0)
                                        sort = True
                                        while(sort):
                                            UserMenu.sorting(self, self.columns, self.result)
                                            if self.collist != []:
                                                Admin.tabela_samochodow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)                                        
                                    if (pytanie == 'B'):
                                        break
                                    else:
                                        id_pojazd = input('Podaj nr pojazdu, który chcesz usunąć, aby powrócić do poprzedniego menu, naciśnij \'b\': ').upper()
                                        if (id_pojazd == 'B'):
                                            break
                                        else:
                                            query_delete = SQLQueries.tabela_samochodow_delete
                                            query_after_delete = SQLQueries.tabela_samochodow
                                            self.query_param_after = (id_pojazd)
                                            self.delete_temp = False
                                            Admin.tabela_klientow(self, conn, cursor, 0, query_delete, query_after_delete)
                                            delete_tekst = True
                                            
                                    
                            # Tabela pojazdów - powrót
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                    
                    # Tabela pilotów
                    if (choice == '4'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli pilotów, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu\
                                            \n' + 5*'-' + '\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            
                            # Tabela pilotow - dodanie
                            if (choice == '1'):
                                nr_p = input('Podaj numer nowego pilota: ')
                                query_update = SQLQueries.tabela_pilotow_insert
                                query_updated = SQLQueries.tabela_pilotow_after_insert
                                self.query_param = (nr_p)
                                self.delete_temp = True
                                self.execute = False
                                self.addnew = True
                                Admin.tabela_pilotow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pilotów - edycja
                            if (choice == '2'):
                                wyjscie = ''
                                while(True):
                                    try:
                                        id_p = int(input('Podaj nr pilota, którego numer chcesz zmienić: '))
                                        if (id_p):
                                            query = SQLQueries.tabela_pilotow_for_update
                                            self.query_param = (id_p)
                                            Admin.tabela_pilotow_for_update(self, conn, cursor, query)
                                            break
                                    except:
                                        print('Podałeś zły nr pilota, spróbuj ponownie')
                                        wyjscie = input('Aby wyjść, naciśnij \'q\'').upper()
                                        if wyjscie == 'Q':
                                            break
                                if wyjscie == 'Q':
                                    break
                                choice = input('Czy chcesz zmienić numer? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Numer przed zmianą: ' + str(self.result_for_update[1][0][1]))
                                    nr_p = input('Podaj nowy numer (aby pominąć, wciśnij Enter): ')
                                    if (nr_p == ''):
                                        nr_p = self.result_for_update[1][0][1]
                                else:
                                    nr_p = self.result_for_update[1][0][1]
                                query_update = SQLQueries.tabela_pilotow_update
                                query_updated = SQLQueries.tabela_pilotow_for_update
                                self.query_param = (nr_p, id_p)
                                self.query_param_after = (id_p)
                                self.execute = True
                                self.delete_temp = True
                                self.addnew = False
                                Admin.tabela_pilotow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pilotów - usuwanie
                            if (choice == '3'):
                                delete_tekst = 0
                                while(True):
                                    if (delete_tekst):
                                        pytanie = input('Czy chcesz usunąć kolejny pilot?\
                                                        \n1 - tak\
                                                        \nb - powrót do poprzedniego menu\
                                                        \n' + 5*'-' + '\
                                                        \nwybierasz: ').upper()
                                        if (pytanie == 'B'):
                                            break
                                    pytanie = input('Czy chcesz sprawdzić tabelę pilotów przed usunięciem pojazdu?\
                                                    \n1 - tak\
                                                    \n2 - nie\
                                                    \n' + 5*'-' + '\
                                                    \nb - powrót do poprzedniego menu\
                                                    \nwybierasz: ').upper()
                                    if (pytanie == '1'):
                                        query = SQLQueries.tabela_pilotow
                                        Admin.tabela_pilotow(self, conn, cursor, query, 0, 0)
                                        sort = True
                                        while(sort):
                                            UserMenu.sorting(self, self.columns, self.result)
                                            if self.collist != []:
                                                Admin.tabela_pilotow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)                                        
                                    if (pytanie == 'B'):
                                        break
                                    else:
                                        id_p = input('Podaj nr pilota, który chcesz usunąć, aby powrócić do poprzedniego menu, naciśnij \'b\': ').upper()
                                        if (id_p == 'B'):
                                            break
                                        else:
                                            query_delete = SQLQueries.tabela_pilotow_delete
                                            query_after_delete = SQLQueries.tabela_pilotow
                                            self.query_param_after = (id_p)
                                            self.delete_temp = False
                                            Admin.tabela_pilotow(self, conn, cursor, 0, query_delete, query_after_delete)
                                            delete_tekst = True
                                            
                            # Tabela pilotów - powrót
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                    
                    # Tabela statusów
                    if (choice == '5'):
                        while(True):
                            self.execute = False
                            choice = input('Wszedłeś do edycji tabeli pilotów, wybierz rodzaj działania:\
                                            \n1 - dodanie rekordu\
                                            \n2 - edycja rekordu\
                                            \n3 - usunięcie rekordu\
                                            \n' + 5*'-' + '\
                                            \nb - powrót do poprzedniego menu\
                                            \nwybierasz: ').upper()
                            
                            # Tabela statusów - dodanie
                            if (choice == '1'):
                                error = False
                                query = SQLQueries.tabela_klientow
                                id_k_temp = Admin.status_tabele(self, conn, cursor, query)
                                query = SQLQueries.tabela_samochodow
                                id_s_temp = Admin.status_tabele(self, conn, cursor, query)
                                query = SQLQueries.tabela_pilotow
                                id_p_temp = Admin.status_tabele(self, conn, cursor, query)
                                query = SQLQueries.tabela_miejsc
                                id_m_temp = Admin.status_tabele(self, conn, cursor, query)                                
                                pytanie = input('Aby dodać status, musisz podać istniejący numer klienta, dla którego status chcesz wprowadzić. Czy chcesz sprawdzić tabelę klientów przed dodaniem statusu?\
                                                                                \n1 - tak\
                                                                                \n2 - nie\
                                                                                \n' + 5*'-' + '\
                                                                                \nb - powrót do poprzedniego menu\
                                                                                \nwybierasz: ').upper()
                                if (pytanie == '1'):
                                    query = SQLQueries.tabela_klientow
                                    Admin.tabela_klientow(self, conn, cursor, query, 0, 0)
                                    sort = True
                                    while(sort):
                                        UserMenu.sorting(self, self.columns, self.result)
                                        if self.collist != []:
                                            Admin.tabela_klientow_sorted(self, self.result, self.columns)
                                        sort = UserMenu.sortQuestion(self)                                        
                                if (pytanie == 'B'):
                                    break
                                else:                                
                                    flag = False
                                    while(True):
                                        error = False
                                        if (flag):
                                            break
                                        id_k = input('Podaj numer klienta, dla którego ma być utworzony status: ')
                                        try:
                                            int(id_k)
                                        except:
                                            print('Podałeś zły numer, spróbuj jeszcze raz')
                                            error = True
                                        i = 0
                                        while (i < len(id_k_temp) and error == False):
                                            if int(id_k) == id_k_temp[i][0]:
                                                flag = True
                                                print('Numer prawidłowy')
                                                break
                                            else:
                                                i += 1
                                            if (i == len(id_k_temp)):
                                                print('Podałeś numer spoza tabeli klientów, spróbuj jeszcze raz')
                                                break
                                    pytanie = input('Aby dodać status, musisz podać istniejący numer samochodu, dla którego status chcesz wprowadzić. Czy chcesz sprawdzić tabelę samochodów przed dodaniem statusu?\
                                                      \n1 - tak\
                                                      \n2 - nie\
                                                      \n' + 5*'-' + '\
                                                      \nb - powrót do poprzedniego menu\
                                                      \nwybierasz: ').upper()
                                    if (pytanie == '1'):
                                        query = SQLQueries.tabela_samochodow
                                        Admin.tabela_samochodow(self, conn, cursor, query, 0, 0)
                                        sort = True
                                        while(sort):
                                            UserMenu.sorting(self, self.columns, self.result)
                                            if self.collist != []:
                                                Admin.tabela_samochodow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)                                        
                                    if (pytanie == 'B'):
                                        break
                                    else:                                
                                        flag = False
                                        while(True):
                                            error = False
                                            if (flag):
                                                break                                            
                                            id_s = input('Podaj numer samochodu, dla którego ma być utworzony status: ')
                                            try:
                                                int(id_s)
                                            except:
                                                print('Podałeś zły numer, spróbuj jeszcze raz')
                                                error = True
                                            i = 0
                                            while (i < len(id_s_temp) and error == False):
                                                if int(id_s) == id_s_temp[i][0]:
                                                    flag = True
                                                    print('Numer prawidłowy')
                                                    break
                                                else:
                                                    i += 1
                                                if (i == len(id_s_temp)):
                                                    print('Podałeś numer spoza tabeli samochodów, spróbuj jeszcze raz')
                                                    break

                                        pytanie = input('Aby dodać status, musisz podać istniejący numer pilota, dla którego status chcesz wprowadzić. Czy chcesz sprawdzić tabelę pilotów przed dodaniem statusu?\
                                                                                          \n1 - tak\
                                                                                          \n2 - nie\
                                                                                          \n' + 5*'-' + '\
                                                                                          \nb - powrót do poprzedniego menu\
                                                                                          \nwybierasz: ').upper()
                                        if (pytanie == '1'):
                                            query = SQLQueries.tabela_pilotow
                                            Admin.tabela_pilotow(self, conn, cursor, query, 0, 0)
                                            sort = True
                                            while(sort):
                                                UserMenu.sorting(self, self.columns, self.result)
                                                if self.collist != []:
                                                    Admin.tabela_pilotow_sorted(self, self.result, self.columns)
                                                sort = UserMenu.sortQuestion(self)                                        
                                        if (pytanie == 'B'):
                                            break
                                        else:                                
                                            flag = False
                                            while(True):
                                                error = False
                                                if (flag):
                                                    break                                                
                                                id_p = input('Podaj numer pilota, dla którego ma być utworzony status: ')
                                                try:
                                                    int(id_p)
                                                except:
                                                    print('Podałeś zły numer, spróbuj jeszcze raz')
                                                    error = True
                                                i = 0
                                                while (i < len(id_p_temp) and error == False):
                                                    if int(id_p) == id_p_temp[i][0]:
                                                        flag = True
                                                        print('Numer prawidłowy')
                                                        break
                                                    else:
                                                        i += 1
                                                    if (i == len(id_p_temp)):
                                                        print('Podałeś numer spoza tabeli pilotów, spróbuj jeszcze raz')
                                                        break
                                                        
                                            pytanie = input('Aby dodać status, musisz podać istniejący numer miejsca, dla którego status chcesz wprowadzić. Czy chcesz sprawdzić tabelę miejsc przed dodaniem statusu?\
                                                            \n1 - tak\
                                                            \n2 - nie\
                                                            \n' + 5*'-' + '\
                                                            \nb - powrót do poprzedniego menu\
                                                            \nwybierasz: ').upper()
                                            if (pytanie == '1'):
                                                query = SQLQueries.tabela_miejsc
                                                Admin.tabela_miejsc(self, conn, cursor, query, 0, 0)
                                                sort = True
                                                while(sort):
                                                    UserMenu.sorting(self, self.columns, self.result)
                                                    if self.collist != []:
                                                        Admin.tabela_miejsc_sorted(self, self.result, self.columns)
                                                    sort = UserMenu.sortQuestion(self)                                        
                                            if (pytanie == 'B'):
                                                break
                                            else:                                
                                                flag = False
                                                while(True):
                                                    error = False
                                                    if (flag):
                                                        break
                                                    id_m = input('Podaj numer miejsca, dla którego ma być utworzony status: ')
                                                    try:
                                                        int(id_m)
                                                    except:
                                                        print('Podałeś zły numer, spróbuj jeszcze raz')
                                                        error = True
                                                    i = 0
                                                    while (i < len(id_m_temp) and error == False):
                                                        if int(id_m) == id_m_temp[i][0]:
                                                            flag = True
                                                            print('Numer prawidłowy')
                                                            break
                                                        else:
                                                            i += 1
                                                        if (i == len(id_m_temp)):
                                                            print('Podałeś numer spoza tabeli miejsc, spróbuj jeszcze raz')
                                                            break
                                                while(True):                                            
                                                    data_start = input('Podaj datę rozpoczęcia wynajmu miejsca (rrrr-mm-dd): ')
                                                    isDate = re.match('[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]', data_start)
                                                    if(isDate):
                                                        break
                                                    else:
                                                        print('Podałeś złą datę, spróbuj jeszcze raz')
                                                while(True):
                                                    data_koniec = input('Podaj datę zakończenia wynajmu miejsca (rrrr-mm-dd): ')
                                                    isDate = re.match('[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]', data_koniec)
                                                    if(isDate):
                                                        break
                                                    else:
                                                        print('Podałeś złą datę, spróbuj jeszcze raz')
                                                query_update = SQLQueries.tabela_statusow_insert
                                                query_updated = SQLQueries.tabela_statusow_after_insert
                                                self.query_param = (id_k, id_s, id_p, id_m, data_start, data_koniec)
                                                self.delete_temp = True
                                                self.execute = False
                                                self.addnew = True
                                                Admin.tabela_statusow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pilotów - edycja TO DO
                            if (choice == '2'):
                                wyjscie = ''
                                while(True):
                                    try:
                                        id_p = int(input('Podaj nr pilota, którego numer chcesz zmienić: '))
                                        if (id_p):
                                            query = SQLQueries.tabela_pilotow_for_update
                                            self.query_param = (id_p)
                                            Admin.tabela_pilotow_for_update(self, conn, cursor, query)
                                            break
                                    except:
                                        print('Podałeś zły nr pilota, spróbuj ponownie')
                                        wyjscie = input('Aby wyjść, naciśnij \'q\'').upper()
                                        if wyjscie == 'Q':
                                            break
                                if wyjscie == 'Q':
                                    break
                                choice = input('Czy chcesz zmienić numer? \'t/n\'').upper()
                                if(choice == 'T'):
                                    print('Numer przed zmianą: ' + str(self.result_for_update[1][0][1]))
                                    nr_p = input('Podaj nowy numer (aby pominąć, wciśnij Enter): ')
                                    if (nr_p == ''):
                                        nr_p = self.result_for_update[1][0][1]
                                else:
                                    nr_p = self.result_for_update[1][0][1]
                                query_update = SQLQueries.tabela_pilotow_update
                                query_updated = SQLQueries.tabela_pilotow_for_update
                                self.query_param = (nr_p, id_p)
                                self.query_param_after = (id_p)
                                self.execute = True
                                self.delete_temp = True
                                self.addnew = False
                                Admin.tabela_pilotow(self, conn, cursor, 0, query_update, query_updated)
                            
                            # Tabela pilotów - usuwanie
                            if (choice == '3'):
                                delete_tekst = 0
                                while(True):
                                    if (delete_tekst):
                                        pytanie = input('Czy chcesz usunąć kolejny pilot?\
                                                        \n1 - tak\
                                                        \nb - powrót do poprzedniego menu\
                                                        \n' + 5*'-' + '\
                                                        \nwybierasz: ').upper()
                                        if (pytanie == 'B'):
                                            break
                                    pytanie = input('Czy chcesz sprawdzić tabelę pilotów przed usunięciem pojazdu?\
                                                    \n1 - tak\
                                                    \n2 - nie\
                                                    \n' + 5*'-' + '\
                                                    \nb - powrót do poprzedniego menu\
                                                    \nwybierasz: ').upper()
                                    if (pytanie == '1'):
                                        query = SQLQueries.tabela_pilotow
                                        Admin.tabela_pilotow(self, conn, cursor, query, 0, 0)
                                        sort = True
                                        while(sort):
                                            UserMenu.sorting(self, self.columns, self.result)
                                            if self.collist != []:
                                                Admin.tabela_pilotow_sorted(self, self.result, self.columns)
                                            sort = UserMenu.sortQuestion(self)                                        
                                    if (pytanie == 'B'):
                                        break
                                    else:
                                        id_p = input('Podaj nr pilota, który chcesz usunąć, aby powrócić do poprzedniego menu, naciśnij \'b\': ').upper()
                                        if (id_p == 'B'):
                                            break
                                        else:
                                            query_delete = SQLQueries.tabela_pilotow_delete
                                            query_after_delete = SQLQueries.tabela_pilotow
                                            self.query_param_after = (id_p)
                                            self.delete_temp = False
                                            Admin.tabela_pilotow(self, conn, cursor, 0, query_delete, query_after_delete)
                                            delete_tekst = True
                                            
                            # Tabela pilotów - powrót
                            elif (choice == 'B'):
                                print('Powrót do poprzedniego menu')
                                break
                    
                    # Zarządzanie - edycja tabel - powrót
                    elif (choice == 'B'):
                        print('Powrót do poprzedniego menu')
                        break  
            
            # Wylogowanie
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
                if (self.delete_temp == False):
                    cursor.execute(query_update, self.query_param_after)
                    conn.commit()
                    print('Usunąłeś klienta o numerze: ' + str(self.query_param_after))
                    print('Tabela klientów po usunięciu wygląda następująco:')
                    cursor.execute(query_updated)
                    self.result = cursor.fetchall()
                    self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
            except:
                print('Nie możesz usunąć tego rekordu, spróbuj ponownie z innym lub najpierw usuń odwołania do niego w innych tabelach')
                temp = False
            try:
                if (self.execute):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Zmieniłeś następującego klienta:')
                    cursor.execute(query_updated, self.query_param_after)
                    self.result = cursor.fetchall()
                    self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
                    temp = True
            
                if (self.addnew):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Dodałeś następującego klienta:')
                    cursor.execute(query_updated, self.query_param)
                    self.result = cursor.fetchall()
                    self.columns = ('id_k', 'imie', 'nazwisko', 'ulica', 'nr_budynku', 'nr_mieszkania', 'kod', 'miasto')
                    temp = True
            except:
                print('Nieoczekiwany błąd')
                
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
        
    def tabela_samochodow(self, conn, cursor, query, query_update, query_updated):
        temp = True
        self.columns = ('id_s', 'id_k', 'rejestracja', 'marka', 'model')
        if (query != 0):
            cursor.execute(query)
            self.result = cursor.fetchall()
            self.columns = ('id_s', 'id_k', 'rejestracja', 'marka', 'model')
        else:
            try:
                if (self.delete_temp == False):
                    cursor.execute(query_update, self.query_param_after)
                    conn.commit()
                    print('Usunąłeś samochód o numerze: ' + str(self.query_param_after))
                    print('Tabela samochodów po usunięciu wygląda następująco:')
                    cursor.execute(query_updated)
                    self.result = cursor.fetchall()
            except:
                print('Nie możesz usunąć tego rekordu, spróbuj ponownie z innym lub najpierw usuń odwołania do niego w innych tabelach')
                temp = False
            try:    
                if (self.execute):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Zmieniłeś następujący pojazd:')
                    cursor.execute(query_updated, self.query_param_after)
                    self.result = cursor.fetchall()
                    
                if (self.addnew):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Dodałeś następujący pojazd:')
                    cursor.execute(query_updated, self.query_param)
                    self.result = cursor.fetchall()
                    temp = True
            except:
                print('Nieoczekiwany błąd')
            
        if (temp != False):
            table = PrintingTable.tableParameters(self, self.columns)
            PrintingTable.printingTable(self, self.result, table)        
        return self.columns    
    
    def tabela_samochodow_sorted(self, result, columns):
        self.columns = ('id_s', 'id_k', 'rejestracja', 'marka', 'model')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_samochodow_for_update(self, conn, cursor, query):
        cursor.execute(query, self.query_param)
        self.result = cursor.fetchall()
        self.columns = ('id_s', 'id_k', 'rejestracja', 'marka', 'model')
        self.result_for_update = []
        self.result_for_update.append(self.columns)
        self.result_for_update.append(self.result)
        
    def tabela_pilotow(self, conn, cursor, query, query_update, query_updated):
        temp = True
        self.columns = ('id_p', 'nr_p')
        if (query != 0):
            cursor.execute(query)
            self.result = cursor.fetchall()
            
        else:
            try:
                if (self.delete_temp == False):
                    cursor.execute(query_update, self.query_param_after)
                    conn.commit()
                    print('Usunąłeś pilot o numerze: ' + str(self.query_param_after))
                    print('Tabela pilotów po usunięciu wygląda następująco:')
                    cursor.execute(query_updated)
                    self.result = cursor.fetchall()
            except:
                print('Nie możesz usunąć tego rekordu, spróbuj ponownie z innym lub najpierw usuń odwołania do niego w innych tabelach')
                temp = False
            
            try:
                if (self.execute):
                    cursor.execute(query_update, self.query_param)                    
                    conn.commit()
                    print('Zmieniłeś następujący pilot:')
                    cursor.execute(query_updated, self.query_param_after)
                    self.result = cursor.fetchall()
                    
                if (self.addnew):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Dodałeś następujący pilot:')
                    cursor.execute(query_updated, self.query_param)
                    self.result = cursor.fetchall()
                    temp = True    
            except:
                print('Nieoczekiwany błąd')
                
        if (temp != False):
            table = PrintingTable.tableParameters(self, self.columns)
            PrintingTable.printingTable(self, self.result, table)        
        return self.columns    
    
    def tabela_pilotow_sorted(self, result, columns):
        self.columns = ('id_p', 'nr_p')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_pilotow_for_update(self, conn, cursor, query):
        cursor.execute(query, self.query_param)
        self.result = cursor.fetchall()
        self.columns = ('id_p', 'nr_p')
        self.result_for_update = []
        self.result_for_update.append(self.columns)
        self.result_for_update.append(self.result)
        
    def tabela_statusow(self, conn, cursor, query, query_update, query_updated):
        temp = True
        self.columns = ('id_st', 'id_k', 'id_s', 'id_p', 'id_m', 'data_start', 'data_koniec', 'utworzono')
        if (query != 0):
            cursor.execute(query)
            self.result = cursor.fetchall()
        else:
            try:
                if (self.delete_temp == False):
                    cursor.execute(query_update, self.query_param_after)
                    conn.commit()
                    print('Usunąłeś status o numerze: ' + str(self.query_param_after))
                    print('Tabela statusów po usunięciu wygląda następująco:')
                    cursor.execute(query_updated)
                    self.result = cursor.fetchall()
            except:
                print('Nie możesz usunąć tego rekordu, spróbuj ponownie z innym lub najpierw usuń odwołania do niego w innych tabelach')
                temp = False
                
            try:
                if (self.execute):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Zmieniłeś następujący status:')
                    cursor.execute(query_updated, self.query_param_after)
                    self.result = cursor.fetchall()
                
                if (self.addnew):
                    cursor.execute(query_update, self.query_param)
                    conn.commit()
                    print('Dodałeś następujący status:')
                    cursor.execute(query_updated, self.query_param)
                    self.result = cursor.fetchall()
                    temp = True    
            except:
                print('Nieoczekiwany błąd')    
            
        if (temp != False):
            table = PrintingTable.tableParameters(self, self.columns)
            PrintingTable.printingTable(self, self.result, table)
            pytanie = input('Czy chcesz zobaczyć wersję zagregowaną z danymi z innych tabel? \'t/n\': ').upper()
            if pytanie == 'T':
                query_friendly = SQLQueries.tabela_statusow_friendly
                cursor.execute(query_friendly)
                self.result = cursor.fetchall()
                self.columns = ('id_st', 'data_start', 'data_koniec', 'imie', 'nazwisko', 'rejestracja', 'marka', 'model', 'id_p', 'id_m', 'opis_m')
                table = PrintingTable.tableParameters(self, self.columns)
                PrintingTable.printingTable(self, self.result, table)                
        return self.columns
    
    def tabela_statusow_sorted(self, result, columns):
        # self.columns = ('id_st', 'id_k', 'id_s', 'id_p', 'id_m', 'data_start', 'data_koniec', 'utworzono')
        table = PrintingTable.tableParameters(self, self.columns)
        PrintingTable.printingTable(self, self.result, table)
        
    def tabela_statusow_for_update(self, conn, cursor, query):
        cursor.execute(query, self.query_param)
        self.result = cursor.fetchall()
        self.columns = ('id_st', 'id_k', 'id_s', 'id_p', 'id_m', 'data_start', 'data_koniec', 'utworzono')
        self.result_for_update = []
        self.result_for_update.append(self.columns)
        self.result_for_update.append(self.result)
        
    def status_tabele(self, conn, cursor, query):
        cursor.execute(query)
        tempResult = cursor.fetchall()
        return tempResult