import mysql.connector

class MySqlQuery:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
    )

    mycursor = mydb.cursor()

    def showDatabases(self):
        print("================================================")
        print("         +=+=+ | Database List | +=+=+        \n")
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print(x)
        msq.backMenu()

    def createDatabase(self):
        print("================================================")
        print("         +=+=+ | Create Database | +=+=+      \n")
        dbName = input("Enter Database Name : ")
        self.mycursor.execute("CREATE DATABASE %s"%dbName)
        msq.backMenu()

    def removeDatabase(self):
        print("================================================")
        print("         +=+=+ | Delete Database | +=+=+      \n")
        dbName = input("Enter Database Name : ")
        self.mycursor.execute("DROP DATABASE %s"%dbName)
        msq.backMenu()

    def createTable(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        
        TableName = input("Enter Table Name : ")
        self.mycursor.execute("CREATE TABLE %s (abc int)"%TableName)
        
        col = int(input("Select Number Column : "))

        for i in range(col):
            colName = input("Enter Column Name : ")
            datatype = input("Enter Data Type with Constrant : ")
            self.mycursor.execute("ALTER TABLE "+TableName+" ADD "+colName+" "+datatype+"") 
            #self.colNo[colName] = ("%s"%datatype)
        self.mycursor.execute("ALTER TABLE "+TableName+" DROP abc")
        #print(self.colNo)
        msq.menu()

    def showTable(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        self.mycursor.execute("show Tables")
        print("\n")
        i = 0
        for table_name in self.mycursor:
            print(table_name[i])
            i+1
        msq.menu()

    def selectTable(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        TableName = input("Enter Table Name : ")
        self.mycursor.execute("SELECT * FROM %s"%TableName)
        
        for record in self.mycursor:
            print(record)
        msq.menu()

    def insertIntoTable(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        TableName = input("Enter Table Name : ")
        self.mycursor.execute("SELECT COUNT(*) AS COLUMN_NO FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'"%TableName)
        results = self.mycursor.fetchall()
        TableCol = results[0]
        print("Table Col : ",TableCol[0])
        
        for i in range(1,TableCol[0]+1):
            self.mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '%s' AND TABLE_NAME = '%s' AND ORDINAL_POSITION = '%d'"%(useDB,TableName,i)) 
            lName = self.mycursor.fetchall()
            colName = lName[0]
            print(colName[0])
            
            val = input("Enter ("+colName[0]+") Value : ")
            print(TableName)
            print(val)
           # self.mycursor.execute("INSERT INTO "+TableName+"("+colName[0]+") VALUES ('"+val+"')") 
            
        msq.menu()

    def deleteTable(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        TableName = input("Enter Table Name : ")
        self.mycursor.execute("DROP TABLE %s",TableName)
        msq.menu()

    def tableStructure(self):
        useDB = input("Use Database : ")
        self.mycursor.execute("USE %s"%useDB)
        TableName = input("Enter Table Name : ")
        self.mycursor.execute("DROP TABLE %s",TableName)
        
        self.schema = self.mycursor.fetchall()
        print(self.schema)
        #for s in self.schema:
        #    print(s)
        msq.menu()

    def menu(self):
        print("================================================")
        print("        +=+=+ | Database Query | +=+=+        \n")
        print("1. Check Databases")
        print("2. Create Databases")
        print("3. Delete Databases")
        print("4. Create Table")
        print("5. Show Tables")
        print("6. Select Table")
        print("7. Insert Data")
        print("8. Delete Table")
        print("9. Table Structure")

        op = int(input("\nSelect Option : "))

        if op == 1:
            msq.showDatabases()
        elif op == 2:
            msq.createDatabase()
        elif op == 3:
            msq.removeDatabase()
        elif op == 4:
            msq.createTable()
        elif op == 5:
            msq.showTable()
        elif op == 6:
            msq.selectTable()
        elif op == 7:
            msq.insertIntoTable()
        elif op == 8:
            msq.deleteTable()
        elif op == 9:
            msq.tableStructure()
        else:
            print("Wrong Input...!")
            msq.menu()

    def backMenu(self):
        print("================================================")
        btn = input("Back 'B' & Exit 'E' : ")

        if btn == 'B' or btn == 'b':
            msq.menu()
        elif btn == 'E' or btn == 'e':
            exit(0)
        else:
            print("Wrong Input...!")
            msq.menu()

msq = MySqlQuery()
msq.menu()