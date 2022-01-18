import ftplib
session = ftplib.FTP('192.168.189.77', 'ftp-user', '12345')

file = open('pune.txt', 'rb')
session.storbinary('STOR pune.txt', file)
file.close()

file = open('ahmedabad.txt', 'rb')
session.storbinary('STOR ahmedabad.txt', file)
file.close()

file = open('rajkot.txt', 'rb')
session.storbinary('STOR rajkot.txt', file)
file.close()

file = open('mumbai.txt', 'rb')
session.storbinary('STOR mumbai.txt', file)
file.close()

file = open('delhi.txt', 'rb')
session.storbinary('STOR delhi.txt', file)
file.close()
session.dir()
session.quit()