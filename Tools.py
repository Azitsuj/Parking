# -*- coding: utf-8 -*-

import datetime
from operator import itemgetter, attrgetter, methodcaller

'''
class ToolsUser:
    
    # User view lista_aktywnych_pojazdow
    lista_aktywnych_pojazdow_h = ('Nr', 'Rejestracja', 'Data od', 'Data do')
    lista_aktywnych_pojazdow_w = ('4', '11', '12', '12')
    lista_aktywnych_pojazdow_a = ('>', '^', '<', '<')
    
    # User view lista_miejsc
    lista_miejsc_h = ('Nr', 'Opis', 'Rejestracja', 'Imię', 'Nazwisko')
    lista_miejsc_w = ('4', '15', '11', '15', '20')
    lista_miejsc_a = ('>', '<', '^', '<', '<')
'''    
class ToolsAdmin:
    lista = 0
    # ToDo--->>>


class TableHeaders:
    
    header_length = {
        # miejsce:
        'id_m':'10',
        'opis_m':'15',
        'slup_lewy':'6',
        'slup_prawy':'6',
        'sciana_lewa':'8',
        'sciana_prawa':'8',
        'sciana_przod':'8',
        'klatka_m':'6',
        # klient:
        'id_k':'5',
        'imie':'15',
        'nazwisko':'20',
        'ulica':'20',
        'nr_budynku':'6',
        'nr_mieszkania':'7',
        'kod':'6',
        'miasto':'20',
        # samochód:
        'id_s':'7',
        'rejestracja':'11',
        'marka':'15',
        'model':'15',
        # pilot:
        'id_p':'9',
        'nr_p':'15',
        # status:
        'id_st':'8',
        'data_start':'12',
        'data_koniec':'12',
        'utworzono':'19',
        # lista/najwięcej pojazdów:
        'wlasciciel':'45',
        'liczba_pojazdow':'15'
    }
    
    header_name = {
        # miejsce
        'id_m':'Nr miejsca',
        'opis_m':'Opis',
        'slup_lewy':'Słup_l',
        'slup_prawy':'Słup_p',
        'sciana_lewa':'Ściana_l',
        'sciana_prawa':'Ściana_p',
        'sciana_przod':'Ściana_f',
        'klatka_m':'Klatka',
        # klient:
        'id_k':'Nr_kl',
        'imie':'Imię',
        'nazwisko':'Nazwisko',
        'ulica':'Ulica',
        'nr_budynku':'Nr ul.',
        'nr_mieszkania':'Mieszk.',
        'kod':'Kod',
        'miasto':'Miasto',
        # samochód:
        'id_s':'Nr sam.',
        'rejestracja':'Rejestracja',
        'marka':'Marka',
        'model':'Model',
        # pilot:
        'id_p':'Nr pilota',
        'nr_p':'Nr seryjny',
        # status:
        'id_st':'Nr wpisu',
        'data_start':'Data od',
        'data_koniec':'Data do',
        'utworzono':'Data wpisu',
        # lista/najwięcej pojazdów:
        'wlasciciel':'Imię i nazwisko',
        'liczba_pojazdow':'Liczba pojazdów'        
    }
    
    content_position = {
        # miejsce
        'id_m':'>',
        'opis_m':'<',
        'slup_lewy':'^',
        'slup_prawy':'^',
        'sciana_lewa':'^',
        'sciana_prawa':'^',
        'sciana_przod':'^',
        'klatka_m':'^',
        # klient:
        'id_k':'>',
        'imie':'<',
        'nazwisko':'<',
        'ulica':'<',
        'nr_budynku':'>',
        'nr_mieszkania':'>',
        'kod':'^',
        'miasto':'<',
        # samochód:
        'id_s':'>',
        'rejestracja':'^',
        'marka':'<',
        'model':'<',
        # pilot:
        'id_p':'>',
        'nr_p':'^',
        # status:
        'id_st':'>',
        'data_start':'^',
        'data_koniec':'^',
        'utworzono':'^',
        # lista/najwięcej pojazdów:
        'wlasciciel':'<',
        'liczba_pojazdow':'^'       
    }

class SQLQueries:
    
    # zapytania usera:
    lista_aktywnych_pojazdow = 'SELECT * FROM lista_aktywnych_pojazdow'
    lista_miejsc = 'SELECT * FROM lista_miejsc'
    
    # zapytania admina:
    lista_aktywnych_klientow = 'select * from lista_aktywnych_klientow'
    lista_posiadaczy_pilotow = 'select * from lista_posiadaczy_pilotow'
    lista_klientow_z_abonamentem = 'select * from lista_klientow_premium'
    lista_miejsc_niewynajetych = 'select * from lista_miejsc_niewynajetych_bez_przeszkod'
    lista_wszystkich_klientow = 'select imie, nazwisko, rejestracja, marka, model from klient join status using (id_k) join samochod using (id_s) order by nazwisko'
    lista_klientow_z_nadchodzacym = 'select id_m as numer_miejsca, klient.imie, klient.nazwisko, samochod.rejestracja, data_start, data_koniec from miejsce join status using(id_m) join klient using (id_k) join samochod using (id_s) where curdate() < date(data_start) order by id_m'
    lista_klientow_duzo_samochodow = 'select concat_ws(\' \',imie, nazwisko) as wlasciciel, count(rejestracja) as liczba_pojazdow from status join klient using (id_k) join samochod using (id_s) group by wlasciciel order by liczba_pojazdow desc, nazwisko'
    tabela_miejsc = 'select * from miejsce'
    tabela_klientow = 'SELECT * FROM klient'
    tabela_samochodow = 'SELECT * FROM samochod'
    tabela_pilotow = 'SELECT * FROM pilot'
    tabela_statusow = 'SELECT * FROM status'
    tabela_statusow_friendly = 'SELECT id_st, data_start, data_koniec, klient.imie, klient.nazwisko, samochod.rejestracja, samochod.marka, samochod.model, pilot.id_p, miejsce.id_m, miejsce.opis_m FROM status JOIN klient using(id_k) JOIN samochod using(id_s) JOIN pilot using(id_p) JOIN miejsce using(id_m) ORDER BY id_st'
    
    # insert
    tabela_klientow_insert = 'INSERT INTO klient (imie, nazwisko, ulica, nr_budynku, nr_mieszkania, kod, miasto) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    tabela_klientow_after_insert = 'SELECT * FROM klient WHERE imie = %s AND nazwisko = %s AND ulica = %s AND nr_budynku = %s AND nr_mieszkania = %s AND kod = %s AND miasto = %s'
    tabela_samochodow_insert = 'INSERT INTO samochod (id_k, rejestracja, marka, model) VALUES (%s, %s, %s, %s)'
    tabela_samochodow_after_insert = 'SELECT * FROM samochod WHERE id_k = %s AND rejestracja = %s AND marka = %s AND model = %s'
    tabela_pilotow_insert = 'INSERT INTO pilot (nr_p) VALUES (%s)'
    tabela_pilotow_after_insert = 'SELECT * FROM pilot WHERE nr_p = %s'
    tabela_statusow_insert = 'INSERT INTO status (id_k, id_s, id_p, id_m, data_start, data_koniec) VALUES (%s, %s, %s, %s, %s, %s)'
    tabela_statusow_after_insert = 'SELECT * FROM status WHERE id_k = %s AND id_s = %s AND id_p = %s AND id_m = %s AND data_start = %s AND data_koniec = %s'
    
    # update
    tabela_miejsc_update = "UPDATE miejsce SET opis_m = %s WHERE id_m = %s"
    tabela_miejsc_after_update = "SELECT * FROM miejsce WHERE opis_m = %s AND id_m = %s"
    tabela_klientow_for_update = 'SELECT * FROM klient WHERE id_k = %s'
    tabela_klientow_update = 'UPDATE klient SET imie = %s, nazwisko = %s, ulica = %s, nr_budynku = %s, nr_mieszkania = %s, kod = %s, miasto = %s WHERE id_k = %s'
    tabela_klientow_after_update = 'SELECT * from klient WHERE id_k = %s'
    tabela_samochodow_update = 'UPDATE samochod SET id_k = %s, rejestracja = %s, marka = %s, model = %s WHERE id_s = %s'
    tabela_samochodow_after_update = 'SELECT * FROM samochod WHERE id_s = %s'
    tabela_samochodow_for_update = 'SELECT * FROM samochod WHERE id_s = %s'
    tabela_pilotow_for_update = 'SELECT * FROM pilot WHERE id_p = %s'
    tabela_pilotow_update = 'UPDATE pilot SET nr_p = %s WHERE id_p = %s'
    tabela_statusow_update = 'UPDATE status SET id_k = %s, id_s = %s, id_p = %s, id_m = %s, data_start = %s, data_koniec = %s WHERE id_st = %s'
    tabela_statusow_for_update = 'SELECT * FROM status WHERE id_st = %s'
    
    # delete
    tabela_klientow_delete = 'DELETE FROM klient WHERE id_k = %s'
    tabela_samochodow_delete = 'DELETE FROM samochod WHERE id_s = %s'
    tabela_pilotow_delete = 'DELETE FROM pilot WHERE id_p = %s'
    tabela_statusow_delete = 'DELETE FROM status WHERE id_st = %s'

class PrintingTable:
    
    def tableParameters(self, columns):
        header = []
        widths = []
        align = []        
        for i in columns:
            header.append(TableHeaders.header_name[i])
            widths.append(TableHeaders.header_length[i])
            align.append(TableHeaders.content_position[i])
        return header, widths, align
    
    def printingTable(self, result, table):
        widths_s = 0
        widths_l = len(table[0]) + 1
        
        for v in table[1]:
            widths_s += int(v)
        widths_total = (widths_l * 2) - 1 + widths_s
        
        # Początek obramowania nagłówka tabeli:
        print(widths_total * '-')
        
        # Nagłówek tabeli
        for v in table[0]:
            print('| {:{align}{w}}'.format(v, align = '^', w = table[1][table[0].index(v)]), end = '')
            # widths[header.index(v)]
        print('|')
        print(widths_total * '-')
        # Koniec nagłówka ^
        result_len = len(result)
        i = 0
        # Drukowanie zawartości tabeli (tuple'a):
        # do testów while:
        # while (i < 1):
        while (i < result_len):
            k = len(result[i])
            j = 0
            while (j < k):
                dateTest = (type(result[i][j] is datetime.date))
                if (dateTest == True):
                    print('| {:{a}{w}}'.format(x, a = table[2][j], w = table[1][j]), end = '')
                else:
                    strConv = str(result[i][j]).replace('\r','')
                    # print(strConv)
                    print('| {:{a}{w}}'.format(strConv, a = table[2][j], w = table[1][j]), end = '')     
                    # print(result[i][j])
                j += 1
            print('|')
            i += 1
        print(widths_total * '-')
        # Koniec tabeli ^
        
class UserMenu(TableHeaders):
    
    def sorting(self, columns, result):
        self.sortFalse = True
        self.collist = []
        ascdesc = []
        collisttemp = list(columns)
        pytanie = False
        counter = 0
        while(True):
            if counter == len(collisttemp):
                break            
            if pytanie == False:
                sortInput = input('Czy chcesz zmienić sortowanie? Jeśli tak, wybierz \'1\', aby pominąć wciśnij dowolny klawisz: ')
            else:
                sortInput = input('Czy chcesz dodać kolejną kolumnę sortowania? Jeśli tak, wybierz \'1\', aby pominąć wciśnij dowolny klawisz: ')
            if sortInput == '1':
                print('Wybierz kolumnę(y) sortowania:')
                for i, v in enumerate(collisttemp):
                    if v != 0:
                        print(str(i + 1) + ':\t' + TableHeaders.header_name[v])
                try:
                    idkol = int(input('Podaj nr kolumny: ')) - 1
                    collisttemp[idkol] = 0
                    self.collist.append(str(idkol))
                    sort = True
                except:
                    print('Podałeś zły numer kolumny, spróbuj jeszcze raz')
                    sort = False
                while(sort):
                    sorttype = input('Aby sortować rosnąco - wybierz \'1\', malejąco - wybierz \'2\': ')
                    if sorttype == '1':
                        sorttype = False
                        break
                    elif sorttype == '2':
                        sorttype = True
                        break
                    else:
                        print('Podałeś zły parametr sortowania, spróbuj ponownie')
                if (sort == True):
                    ascdesc.append(sorttype)
                    counter += 1
                    pytanie = True
            else:
                # return collist
                break
        for i, v in enumerate(self.collist):
            self.result = sorted(self.result, key = itemgetter(int(v)), reverse = ascdesc[i])
            # print(self.result)
        return self.result, self.collist
    
    def sortOption(self, columns):
        sortInput = input('Czy chcesz zmienić domyślne sortowanie? Jeśli tak, wybierz \'1\', aby pominąć wciśnij dowolny klawisz: ')
        if sortInput == '1':
            sortType = input('Czy chcesz zmienić domyślne sortowanie na malejące? Jeśli tak, wybierz \'1\' ')
            print('Po której kolumnie chcesz sortować:')
            k = 1
            for i in columns:
                print(str(k) + ' - ' + TableHeaders.header_name[i])
                k += 1
            sortInput = input('Podaj numer kolumny: ')
            if sortType != '1':
                return str(sortInput)
            else:
                return str(sortInput + 'desc')
        else:
            print('Powrót do poprzedniego menu')
            return False
        
    def sortMany(self, sortInput, query, columns, sortType):
        print('sortInput: ' + str(sortInput))
        i = len(sortInput)
        if (i > 1):
            sortInput = list(sortInput)
            sortFinal = []
            for i in sortInput:
                sortFinal += i
        else:
            sortFinal = sortInput
        queryFinal = query
        print('sortFinal: ' + str(sortFinal))
        for k in sortFinal:
            print(k)
            print(queryFinal)
            queryFinal = queryFinal + self.columns[int(k) - 1] + ', '
        queryFinal = queryFinal[:-2] + sortType
        print(queryFinal)
        return queryFinal
    
    def sortQuestion(self):
        sortq = input('Aby powrócić do menu sortowania, wybierz \'1\', aby powrócić do poprzedniego menu, wybierz dowolny klawisz: ')
        if sortq != '1':
            sortq = False
        return sortq
            
