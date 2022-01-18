import ftplib
session = ftplib.FTP('192.168.189.77','ftp-user','12345')

'''with open("rajkot.txt") as file:
    session.retrbinary(f'RETR rajkot.txt',file.write)
file = open("rajkot.txt","r")
print("file content: ",file.read())

with open("ahmedabad.txt") as file:
    session.retrbinary(f"RETR ahmedabad.txt",file.write)
file = open("ahmedabad.txt","r")
print("file content : ", "r")'''
with open("rajkot.txt", "wb") as file:
    session.retrbinary(f"RETR rajkot.txt", file.write)
file = open("rajkot.txt", "r")
print('File Content:', file.read())

with open("ahmedabad.txt", "wb") as file:
    session.retrbinary(f"RETR ahmedabad.txt", file.write)
file = open("ahmedabad.txt", "r")
print('File Content:', file.read())

with open("pune.txt", "wb") as file:
    session.retrbinary(f"RETR pune.txt", file.write)
file = open("pune.txt", "r")
print('File Content:', file.read())

with open("mumbai.txt", "wb") as file:
    session.retrbinary(f"RETR mumbai.txt", file.write)
file = open("mumbai.txt", "r")
print('File Content:', file.read())

session.quit()