# -*- coding: utf-8 -*-

import datetime

class ToolsUser:
    
    # User view lista_aktywnych_pojazdow
    lista_aktywnych_pojazdow_h = ('Nr', 'Rejestracja', 'Data od', 'Data do')
    lista_aktywnych_pojazdow_w = ('4', '11', '12', '12')
    lista_aktywnych_pojazdow_a = ('>', '^', '<', '<')
    
    # User view lista_miejsc
    lista_miejsc_h = ('Nr', 'Opis', 'Rejestracja', 'Imię', 'Nazwisko')
    lista_miejsc_w = ('4', '15', '11', '15', '20')
    lista_miejsc_a = ('>', '<', '^', '<', '<')
    
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
        'data_stop':'12',
        'utworzono':'12'
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
        'data_stop':'Data do',
        'utworzono':'Data wpisu'
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
        'data_stop':'^',
        'utworzono':'^'
    }
    
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
        while (i < result_len):
            k = len(result[i])
            j = 0
            while (j < k):
                dateTest = (type(result[i][j] is datetime.date))
                if (dateTest == True):
                    print('| {:{a}{w}}'.format(x, a = table[2][j], w = table[1][j]), end = '')
                else:
                    strConv = str(result[i][j])
                    print('| {:{a}{w}}'.format(strConv, a = table[2][j], w = table[1][j]), end = '')     
                    # print(result[i][j])
                j += 1
            print('|')
            i += 1
        print(widths_total * '-')
        # Koniec     tabeli ^