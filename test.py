import docx
from docx.shared import Inches
import os
import pandas as pd
import Search
from datetime import datetime
import sqlite3 as sql

if __name__ == '__main__':
    DB = sql.connect(
        "Navtime.db"
    )
    cursorObject = DB.cursor()
    cursorObject.execute("CREATE TABLE NavTime(title, simuchin, user, date)")
    DB.close()
