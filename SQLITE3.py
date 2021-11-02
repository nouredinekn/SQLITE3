###>>>>>>>>>>>>>>>>>>>>>>>>###SQL LANGUE WITH PYTHON __ DATABASE ###>>>>>>>>>>>>>>>>>>>>>>>>###
import sqlite3
FOR MAKE DATA BASE ( CREATE DATABASE NAME O  YOUR DATA.)

nouredine= sqlite3.connect('SUDENTS.db')


###-----------------------### FOR MAKE TABLE ###-----------------------###

nouredine.execute("CREATE TABLE STUDENT ( ID INT(16)  PRIMARY KEY , NAME TEXT(17) NOT NULL ,  LAST_NAME TEXT(17) NOT NULL , NUM_PHONE VARSHARE(16)  NOT NULL);")

###-----------------------### FOR MAKE ADD COLUMN IN TABLE ###-----------------------###

nouredine.execute("INSERT INTO STUDENT(ID,NAME,LAST_NAME , NUM_PHONE) VALUES (17,'NOUREDINE' , 'KAOINE' , +212769999999) ");

nouredine.execute("INSERT INTO STUDENT(ID,NAME,LAST_NAME , NUM_PHONE) VALUES (7,'HADINE' , 'OINE' , +212679111599) ");
nouredine.commit()
nouredine.close()

###-----------------------### TO SELECT ANY DATA ###-----------------------###
y= nouredine.execute("SELECT * FROM STUDENT ")
for x in y :
	print(x)

b= nouredine.execute("SELECT * FROM STUDENT WHERE ID=7")
for x in b:
	print("\n NAME=",x[1],"\n","LAST NAME=",x[2],"\n","NUM PHONE",x[3])

###-----------------------### TO CHANGE OR UPDATE  ANY DATA###-----------------------###

nouredine.execute("UPDATE STUDENT SET NAME='DELONE' WHERE ID=7 ")
print("SAVE")
nouredine.commit()

###-----------------------### TO DELETE ANY COLUMN ###------------------------###

nouredine.execute("DELETE FROM STUDENT WHERE ID=7")
nouredine.commit()
print("your column has been deleted")
