# -*- coding: utf-8 -*-
from Admin import Admin
from User import User
from DatabaseCon import connection, close, login

class Start:
    
    def __init__(self):
        print('Witaj w programie \"Parking\"!')
        connection(self)
        print('Za chwilę będziesz mógł się zalogować')
        login(self)
        Start.startSelector(self, self.loggedUser, self.cursor, self.conn)
    
    def startSelector(self, loggedUser, cursor, conn):
        while(True):
            if self.loggedUser == 0:
                login(self)  
            elif (self.loggedUser == 'admin'):
                Admin(cursor, conn)
                self.loggedUser = 0
            elif (self.loggedUser == 'user'):
                User(login, cursor)
                self.loggedUser = 0
            elif self.loggedUser == 'q':
                close(self)
                print('Wyszedłeś z programu')
                break
            else:
                print('Nie powinieneś nigdy zobaczyć tego komunikatu...')
                break
   
run = Start()