# -*- coding: utf-8 -*-
import pymysql
import hashlib, binascii
import getpass, sys
from msvcrt import getch
   
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
    return self.cursor, self.conn

def close(self):
    self.conn.close()
    print('Połączenie z bazą zostało zamknięte')
    

def login(self):
    i = 0
    while(i < 3):
        # temp user selecting
        '''
        while(True):
            logtemp = input('Podaj login: 1 - admin, 2 - user, q - wyjście: ')
            if (logtemp == '1'):
                self.loggedUser = 'owner'
                pwd = 'admin'
                break
            elif (logtemp == '2'):
                self.loggedUser = 'ochroniarz'
                pwd = 'user'
                break
            elif (logtemp == 'q'):
                break
            else:
                print('Coś poszło nie tak, spróbuj ponownie')
        if logtemp == 'q':
            RS = (('q'))
            break
        # Koniec tymczasowego logowania
        '''
        self.loggedUser = input('Podaj login (\'q\' aby wyjść): ')
        if self.loggedUser.upper() == 'Q':
            print('Wychodzisz z programu.')
            RS = 'q'
            break
        pwd = pyssword()
        
        # pwd = input('Podaj hasło: ')
        pwd2 = encrypt(self, pwd)
        pwd3 = str(pwd2)
        pwd4 = len(pwd3) - 1
        passwd = pwd3[:1] + '\'' + pwd3[2:pwd4] + '\''
        self.cursor.execute('SELECT role FROM login WHERE login = %s and passwd = %s', (self.loggedUser, passwd))
        RS = self.cursor.fetchall()
        if (len(RS) != 0):
            RS = str(RS[0][0][:len(RS[0][0])-1])
            print('Logowanie pomyślne!')
            break
        else:
            print('Błąd logowania')
            i += 1
            if i == 1:
                print('Masz jeszcze ' + str(3 - i) + ' próby')
            elif i == 2:
                print('Masz jeszcze ' + str(3 - i) + ' próbę')
            if (i == 3):
                print('Przekroczyłeś liczbę prób! Program zostanie zamknięty')
                RS = 'q'
                break       
    return RS

def encrypt(self, haslo):
    haslob = bytes(haslo, 'utf-8')
    haslo_enc = hashlib.pbkdf2_hmac('sha256', haslob, b'salt', 100000, dklen = 64)
    haslo_enc = binascii.hexlify(haslo_enc)
    return haslo_enc

def pyssword(prompt='Podaj hasło: '):
    '''
        Prompt for a password and masks the input.
        Returns:
            the value entered by the user.
    '''
    
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""        
        sys.stdout.write(prompt)
        sys.stdout.flush()        
        while True:
            key = ord(getch())
            if key == 13: #Return Key
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8: #Backspace key
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')                
                    sys.stdout.flush()
                    pwd = pwd[:-1]                    
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()                
                pwd = pwd + char