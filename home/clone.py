# from django import settings
# from django.conf import settings
# from django.db import models
# from .models import Round1
import sqlite3
import csv
database = 'mopup.csv'
data = open(database, "w")
writer_handler = csv.writer(data)

connection = sqlite3.connect("Cutoffs.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM MOPUP")
colleges = cursor.fetchall()
for college in colleges:
    writer_handler.writerow(college)
    # print(college)
#     # break

cursor.close()
connection.close()
# with open('cutoffs.csv', "r") as f:
#     csv_reader = csv.reader(f)
#     # college = list(map())
#     n=0
#     for college in csv_reader:
#         n += 1
#         # print(college)
#         # break
#         if n > 109:
#             print(college)
#         if n > 113:
#             break
