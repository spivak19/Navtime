import docx
from docx.shared import Inches
import os
import pandas as pd
import Search
from datetime import datetime
import time
import sqlite3 as sql

class TempEditor:

    def __init__(self,doctitle):
        users = pd.read_csv('users/users.csv')
        userLogin = os.getlogin()
        self.doctitle = doctitle
        self.user = Search.search(users, userLogin)
        self.simuchin = ""

        self.name = self.MakeName()  # The path to the file

        today = datetime.now()
        self.date = f'{today.day}/{today.month}/{today.year}'

        self.hebrewname = f'{self.user["Hebrew First Name"][0]} {self.user["Hebrew Last Name"][0]}'

        self.data = {
            '[date]': self.date,
            '[simuchin]': f"{self.simuchin} סימוכין ",
            '[Hebrew name]': self.hebrewname,
            '[rank]' : f'{self.user["rank"][0]}',
            '[title]': self.user["title"][0],
            '[doctitle]': self.doctitle
        }

    # Makes the path to the file
    def MakeName(self):

        today = datetime.now()
        date = f'{today.day}{today.month}{today.year % 100}'


        dir = f'Documents/{today.month}{today.year % 100}'

        if not (os.path.exists(dir)):
            os.mkdir(dir)

        i = 1

        self.simuchin = f'{self.user["Initials"][0]}-{date}-{i}'
        name = f'{dir}/{self.user["Initials"][0]}-{date}-{i}.docx'

        while os.path.exists(f'{name}'):
            i += 1
            self.simuchin = f'{self.user["Initials"][0]}-{date}-{i}'
            name = f'{dir}/{self.user["Initials"][0]}-{date}-{i}.docx'
        return name

    def Add2DB(self):
        con = sql.connect("NavTime.db")
        cur = con.cursor()

        cur.execute(f"""
            INSERT INTO NavTime VALUES
                ('{self.doctitle}', '{self.simuchin}', '{self.hebrewname}', '{self.date}')
        """)

        con.commit()
        con.close()
    def NewDoc(self):

        doc = docx.Document("Templates/basic.docx")

        paragraphs = doc.paragraphs
        for paragraph in paragraphs:
            for key,value in self.data.items():
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key,value)
        doc.save(f"{self.name}")

        self.Add2DB()

if __name__ == '__main__':
    doctitle = "בדיקה"

    New = TempEditor(doctitle)
    _ = New.NewDoc()
    os.startfile(f"D:/python projects/navtime/{New.name}")
