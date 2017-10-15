# -*- coding: utf-8 -*-
from Admin import Admin
from User import User
from DatabaseCon import connection, close, login

class Start:
    
    RS = 0
    
    def __init__(self):
        print('Witaj w programie \"Parking\"!')
        connection(self)
        print('Za chwilę będziesz mógł się zalogować')
        RS = login(self)
        Start.startSelector(self, RS, self.cursor, self.conn)
    
    def startSelector(self, RS, cursor, conn):
        while(True):
            if RS == 0:
                RS = login(self)  
            elif (RS == 'admin'):
                Admin(cursor, conn)
                RS = 0
            elif (RS == 'user'):
                User(cursor, conn)
                RS = 0
            elif RS == 'q':
                close(self)
                print('Wyszedłeś z programu')
                break
            else:
                close(self)
                print('Wyszedłeś z programu')
                break
   
run = Start()