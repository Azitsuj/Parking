# -*- coding: utf-8 -*-

import pymysql
from Tools import ToolsAdmin
from User import User
from DatabaseCon import connection, close, login

class Admin:
    
    def __init__(self, conn, cursor):
        print('Jesteś w adminie')
        Admin.panel_admina(self, conn, cursor)
    
    def panel_admina(self, conn, cursor):
        
        while(True):
            print('Wybierz spośród poniższych: ')
            choice = input(  '1 - lista uprawnionych pojazdów\
                            \n2 - lista wszystkich miejsc i pojazdów\
                            \nq - wyloguj\
                            \nwybierasz: ').upper()
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
                print('Zostałeś wylogowany')
                # login(self)
                break
            

    
    '''
    def connection(self):
        while(True):
            try:
                self.conn = pymysql.connect('localhost', 'x', 'strongPasswordWouldBeNice', 'parking', charset='utf8')
                break
            except:
                print('Nie udało się połączyć z bazą, zmień konfigurację połączenia')
                break
        # ustawienie kursora na począteku
        self.cursor = self.conn.cursor()
    
    def DBclose(self):
        print('Koniec')
        self.conn.close()    
    
    def login(self):
        i = 0
        while(i < 3):
            self.login = 'user'
            # self.login = input('Podaj login: ')
            # p1 = input('Podaj hasło: ')
            p1 = 'user'
            p2 = self.encrypt(p1)
            p3 = str(p2)
            p4 = len(p3) - 1
            passwd = p3[:1] + '\'' + p3[2:p4] + '\''
            self.cursor.execute('SELECT login, passwd FROM login WHERE login = %s and passwd = %s', (self.login, passwd))
            RS = self.cursor.fetchall()
            if (len(RS) != 0):
                print('ok')
                break
            else:
                print('Błąd logowania')
                i += 1
                if (i == 3):
                    print('Przekroczyłeś liczbę prób! Program zostanie zamknięty')
                    break
                    
        return self.login
    
    def encrypt(self, haslo):
        haslob = bytes(haslo, 'utf-8')
        haslo_enc = hashlib.pbkdf2_hmac('sha256', haslob, b'salt', 100000, dklen = 64)
        haslo_enc = binascii.hexlify(haslo_enc)
        return haslo_enc
    '''
    
# test = Admin()