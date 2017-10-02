# -*- coding: utf-8 -*-

import pymysql
import Headers
import datetime

class User:
    
    def __init__(self):
        print('Jestem w userze')
    
    def panel_usera(self, conn):
       
        while(True):
            print('Wybierz spośród poniższych: ')
            choice = input('1 - lista uprawnionych pojazdów\n2 - lista wszystkich miejsc i pojazdów\nwybierasz: ')
            if (choice == '1'):
                User.lista_aktywnych_pojazdow(self)
                input('Kontynuować?\n')
                
            elif (choice == '2'):
                User.lista_miejsc(self)
                input('Kontynuować?\n')
                
            else:
                conn.close()
                print('Bye')
                break
            
        
    def lista_aktywnych_pojazdow(self):
        self.cursor.execute('SELECT * FROM lista_aktywnych_pojazdow')
        result = self.cursor.fetchall()
        header = Headers.Headers.lista_aktywnych_pojazdow_h
        widths = Headers.Headers.lista_aktywnych_pojazdow_w
        align = Headers.Headers.lista_aktywnych_pojazdow_a
        User.printingTable(self, result, header, widths, align)

    def lista_miejsc(self):
        self.cursor.execute('SELECT * FROM lista_miejsc')
        result = self.cursor.fetchall()
        header = Headers.Headers.lista_miejsc_h
        widths = Headers.Headers.lista_miejsc_w
        align = Headers.Headers.lista_miejsc_a
        User.printingTable(self, result, header, widths, align)
        
    
    def printingTable(self, result, header, widths, align):
        widths_s = 0
        widths_l = len(header) + 1
        
        for v in widths:
            widths_s += int(v)
        widths_total = (widths_l * 2) - 1 + widths_s
        # Początek obramowania nagłówka tabeli
        print(widths_total * '-')
        
        # Nagłówek tabeli
        for v in header:
            print('| {:{align}{w}}'.format(v, align = '^', w = widths[header.index(v)]), end = '')
        print('|')
        print(widths_total * '-')
        # Koniec nagłówka ^
        result_len = len(result)
        i = 0
        # Drukowanie zawartości tabeli
        while (i < result_len):
            k = len(result[i])
            j = 0
            while (j < k):
                dateTest = (type(result[i][j] is datetime.date))
                if (dateTest == True):
                    print('| {:{a}{w}}'.format(x, a = align[j], w = widths[j]), end = '')
                else:
                    strConv = str(result[i][j])
                    print('| {:{a}{w}}'.format(strConv, a = align[j], w = widths[j]), end = '')     
                    # print(result[i][j])
                j += 1
            print('|')
            i += 1
        print(widths_total * '-')
        # Koniec tabeli ^
    