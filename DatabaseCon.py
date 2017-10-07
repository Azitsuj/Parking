# -*- coding: utf-8 -*-
import pymysql
import hashlib, binascii

   
def connection(self):
    while(True):
        try:
            self.conn = pymysql.connect('localhost', 'x', 'strongPasswordWouldBeNice', 'parking', charset='utf8')
            print('Połączenie z bazą zostało utworzone')
            break
        except:
            print('Nie udało się połączyć z bazą, zmień konfigurację połączenia')
            break
    # ustawienie kursora na począteku
    self.cursor = self.conn.cursor()
    return self.cursor

def close(self):
    self.conn.close()
    print('Połączenie z bazą zostało zamknięte')
    

def login(self):
    i = 0
    while(i < 3):
        # temp user selecting
        while(True):
            logtemp = input('Podaj login: 1 - admin, 2 - user, q - wyjście: ')
            if (logtemp == '1'):
                self.loggedUser = 'admin'
                p1 = 'admin'
                break
            elif (logtemp == '2'):
                self.loggedUser = 'user'
                p1 = 'user'
                break
            elif (logtemp == 'q'):
                break
            else:
                print('Coś poszło nie tak, spróbuj ponownie')
        if logtemp == 'q':
            self.loggedUser = 'q'
            break
        # Koniec tymczasowego logowania
        # self.loggedUser = input('Podaj login: ')
        # p1 = input('Podaj hasło: ')
        '''if self.loggedUser == 'Q':
            print('Wyszedłeś z programu.')
            break'''
        p2 = encrypt(self, p1)
        p3 = str(p2)
        p4 = len(p3) - 1
        passwd = p3[:1] + '\'' + p3[2:p4] + '\''
        self.cursor.execute('SELECT login, passwd FROM login WHERE login = %s and passwd = %s', (self.loggedUser, passwd))
        RS = self.cursor.fetchall()
        if (len(RS) != 0):
            print('Logowanie pomyślne!')
            break
        else:
            print('Błąd logowania')
            i += 1
            if (i == 3):
                print('Przekroczyłeś liczbę prób! Program zostanie zamknięty')
                break       
    return self.loggedUser

def encrypt(self, haslo):
    haslob = bytes(haslo, 'utf-8')
    haslo_enc = hashlib.pbkdf2_hmac('sha256', haslob, b'salt', 100000, dklen = 64)
    haslo_enc = binascii.hexlify(haslo_enc)
    return haslo_enc