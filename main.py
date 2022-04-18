from io import open
import csv

f = open("file.txt", mode="r", encoding="utf-8")
csv_file = open('emails.csv', 'a', newline='')

with f as file_in:
    for line in file_in:
       for l in line.split(","):
           if l.find('@gmail.com') != -1 and ' ' not in l:
                 writer = csv.writer(csv_file)
                 try:
                    writer.writerow([l.replace('"', '')])
                    print(l)
                 except:
                    continue



csv_file.close()
f.close()