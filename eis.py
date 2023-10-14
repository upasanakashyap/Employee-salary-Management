import mysql.connector

# program code for main menu
def menu1():
    ch=0
    while ch != 5:
        print("**********EMPLOYEE INFORMATION SYSTEM **********")
        print("------------------------------------------------")
        print("1.EMPLOYEE           ")
        print("2.SALARY             ")
        print("3.SEARCH             ")
        print("4.STATISTICAL VALUE  ")
        print("5.GRAPH              ")
        print("6.EXIT               ")
        
        ch=int(input("Enter your choice[1-6] :"))
        if ch==1 :
            menu2()
        elif ch==2:
            menu3()
        elif ch==3:
            menu4()
        elif ch==4:
            menu5()
        elif ch==5:
            menu6()    
        elif ch==6:
            break

# program code for employee menu
def menu2():
    ch=0
    while ch != 5:
        print("**********EMPLOYEE MENU **********")
        print("------------------------------------------------")
        print("1.CREATE NEW EMPLOYEE ")
        print("2.MODIFY EMPLOYEE     ")
        print("3.DELETE EMPLOYEE     ")
        print("4.DISPLAY EMPLOYEE    ")
        print("5.RETURN ")
        
       
        ch=int(input("Enter your choice[1-5] :"))
        if ch==1 :
            newemp()
        elif ch== 2:
            modemp()
        elif ch==3:
            delemp()
        elif ch==4:
            dispemp()
        elif ch==5:    
            break


#New employee

def newemp():
    ch="y"
    while ch !="n" or ch !="N" :
           print("***************** NEW EMPLOYEE***********************")
           print("------------------------------------------------")
           e1=int(input("enter a empno:"))
           print("Empno:",e1)
           e2=input("enter a empname:")
           print("Empname:",e2)
           e3=input("enter a job:")
           print("job:",e3)
           e4=input("enter a address:")
           print("address:",e4)
           e5=input("enter a email:")
           print("Email:",e5)
           e6=int(input("enter a dcode:"))
           print("dcode:",e6)
           mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                         )

           mycursor = mydb.cursor()
           sql = "INSERT INTO emp_master(empno,ename,job,addr,email,dcode) VALUES (%s, %s,%s,%s,%s,%s)"
           val = (e1,e2,e3,e4,e5,e6)
           mycursor.execute(sql, val)

           mydb.commit()
           ch=input("Enter your choice[y-n]:")
           if ch=="n" or ch=="N":
                break


def modemp():
     import mysql.connector

     mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
     print("*****************EMPLOYEE MODIFICATION***********************")
     print("--------------------------------------------------------------")
     e1=int(input("Enter a Empno:"))
     print("Empno:",e1)
     
     mycursor = mydb.cursor()
     

     mycursor.execute("SELECT * FROM emp_master where empno='%d'" % (e1))
     myresult = mycursor.fetchone()
     print(myresult)

     
     print("Do  you want to modify:")
     ch=input("Enter your choice [y-n]")
     if ch=="y":
           
           e2=input("enter new empname:")
           print("Empname:",e2)
           e3=input("enter new job:")
           print("job:",e3)
           e4=input("enter new address:")
           print("address:",e4)
           e5=input("enter new email:")
           print("Email:",e5)
           e6=int(input("enter new dcode:"))
           print("dcode:",e6)

           

           
           myc = mydb.cursor()
           data=(e2,e1)
           sql="update emp_master set ename='"+e2+"',job='"+e3+"',addr='"+e4+"',email='"+e5+"',dcode="+str(e6)+" where empno="+str(e1)
           myc.execute(sql)
           mydb.commit() 
           print ("Number of rows updated:",  myc.rowcount)
      

#delete employee
def delemp():
     import mysql.connector

     mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
     print("*****************EMPLOYEE DELETE***********************")
     print("--------------------------------------------------------------")
     e1=int(input("Enter a Empno:"))
     print("Empno:",e1)
     
     mycursor = mydb.cursor()
     #("SELECT * from user_data WHERE Name = '%s'",('name'))
     #self.cursor.execute("SELECT * from user_data WHERE Name = '%s'" % (name))
     #rows = self.cursor.fetchone()
     #print(rows)


     mycursor.execute("DELETE FROM emp_master where empno='%d'" % (e1))
     mydb.commit()
     print("Employee Deleted ...")      

#display employee
def dispemp():
     import mysql.connector

     mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
     print("***********************DISPLAY EMPLOYEE***********************")
     print("--------------------------------------------------------------")
     e1=int(input("Enter a Empno:"))
     print("Empno:",e1)
     
     mycursor = mydb.cursor()


     mycursor.execute("SELECT * FROM emp_master where empno='%d'" % (e1))
     myresult = mycursor.fetchone()
     print("Employee Search Data ")
     print(myresult)


#salary
def menu3():
    ch=0
    while ch != 3:
        print("**********SALARY MENU **********")
        print("--------------------------------")
        print("1.GENERATE SALARY     ")
        print("2.VIEW SALARY         ")
        print("3.RETURN              ")
        
       
        ch=int(input("Enter your choice[1-3] :"))
        if ch==1 :
            gensal()
        elif ch== 2:
            visal()
        elif ch==3:    
            break


def gensal():
    ch="y"
    while ch !="n" or ch !="N" :
           print("***************** SALARY DETAILS***********************")
           print("-------------------------------------------------------")
           e1=int(input("enter a empno:"))
           print("Empno:",e1)
           month=int(input("enter a month"))
           print("month:",month)
           year=int(input("enter a year"))
           print("year:",year)
           sal=int(input("enter a basic:"))
           print("basic:",sal)
           mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                         )

           mycursor = mydb.cursor()
           sql = "INSERT INTO salary_master(empno,month,year,basic) VALUES (%s, %s,%s,%s)"
           val = (e1,month,year,sal)
           mycursor.execute(sql, val)

           mydb.commit()
           print("Do  you want to generate:")
           ch=input("Enter your choice[y-n]:")
           if ch=="n" or ch=="N":
                break


def visal():
    ch="y"
    while ch !="n" or ch !="N" :
           print("***************** VIEW SALARY *************************")
           print("-------------------------------------------------------")
           e1=int(input("enter a empno:"))
           print("Empno:",e1)
           mon=int(input("enter a month"))
           print("month:",mon)
           yr=int(input("enter a year"))
           print("year:",yr)
           mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                         )

           mycursor = mydb.cursor()
               

           mycursor.execute("SELECT * FROM salary_master where empno='%d' and month='%d' and year='%d'" % (e1,mon,yr))
           myresult = mycursor.fetchone()
           print("Employee Search Data ")
           print("Empno :" ,myresult[0])
           print("Month :" ,myresult[1])
           print("Year :" ,myresult[2])
           sal=myresult[3]
           print("Basic :" ,sal)
           hra=sal*.40
           conv=sal*.20
           bon=sal*.30

           tax=(sal+hra+conv+bon)* .05
           print("Hra :" ,hra)
           print("Conv: ",conv)
           print("Bonus :",bon)
           print("Tax :",tax)
           print("Net salary :",(sal+hra+conv+bon)-tax)
           print("Do  you want to generate:")
           ch=input("Enter your choice[y-n]:")
           if ch=="n" or ch=="N":
                break
#search
def menu4():
     ch=0
     while ch != 5:
        print("********** SEARCH EMPLOYEE *************")
        print("------------------------------------------------")
        print("1.SEARCH BY  EMPLOYEE NO ")
        print("2.SEARCH BY EMPLOYEE NAME")
        print("3.SEARCH BY EMPLOYEE JOB ")
        print("4.RETURN                 ")
        
        
       
        ch=int(input("Enter your choice[1-5] :"))
        if ch==1 :
            sbempno()
        elif ch== 2:
            sbempn()
        elif ch==3:
            sbempj()
        elif ch==4:    
            break
def sbempno():
     import mysql.connector

     mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
     print("***********************SEARCH BY  EMPLOYEE NO***********************")
     print("--------------------------------------------------------------")
     e1=int(input("Enter a Empno:"))
     print("Empno:",e1)
     
     mycursor = mydb.cursor()


     mycursor.execute("SELECT * FROM emp_master where empno='%d'" % (e1))
     myresult = mycursor.fetchone()
     
     print("Employee Search Data ")
     print("Empno=      ",myresult[0])
     print("Empname=    ",myresult[1])
     print("job=        ",myresult[2])
     print("Add=:       ",myresult[3])
     print("Email=      ",myresult[4])
     print("Dcode=      ",myresult[5])
     #print(myresult)
     
def sbempn():
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    print("***********************SEARCH BY  EMPLOYEE NAME***********************")
    print("--------------------------------------------------------------")
    e2=(input("Enter a EmpName:"))
    print("EmpName:",e2)
     
    mycursor = mydb.cursor()


    mycursor.execute("SELECT * FROM emp_master where ename='%s'" % (e2))
    myresult = mycursor.fetchone()
    print("Employee Search Data ")
    for x in myresult:
        print("Empno=      ",x[0])
        print("Empname=    ",x[1])
        print("job=        ",x[2])
        print("Add=:       ",x[3])
        print("Email=      ",x[4])
        print("Dcode=      ",x[5])
    #print(myresult)
def sbempj():
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    print("***********************SEARCH BY  EMPLOYEE JOB***********************")
    print("--------------------------------------------------------------")
    e3=(input("Enter a EmpJob:"))
    print("EmpJob:",e3)
     
    mycursor = mydb.cursor()


    mycursor.execute("SELECT * FROM emp_master where job='%s'" % (e3))
    myresult = mycursor.fetchall()
    print("Employee Search Data ")
    
    for x in myresult:
      print("Empno=      ",x[0])
      print("Empname=    ",x[1])
      print("job=        ",x[2])
      print("Add=:       ",x[3])
      print("Email=      ",x[4])
      print("Dcode=      ",x[5])
    #print(myresult)

#STATISTICAL value
def menu5():
    ch=0
    while ch != 4:
        print("**********STATISTICAL MENU **********")
        print("------------------------------------------------")
        print("1.MAX SAL EMPLOYEE               ")
        print("2.MIN SAL EMPLOYEE               ")
        print("3.LESS THAN AVG SAL EMPLOYEE     ")
        print("4.RETURN                         ")
        
       
        ch=int(input("Enter your choice[1-4] :"))
        if ch==1 :
            mxsemp()
        elif ch== 2:
            misemp()
        elif ch==3:
            lavgsemp()
        elif ch==4:
             break

def mxsemp():

    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    print("***********************SEARCH BY  MAX SAL EMPLOYEE **********************")
    print("--------------------------------------------------------------")
    mycursor = mydb.cursor()
    mycursor.execute("select ename,job,basic from emp_master,salary_master where emp_master.empno=salary_master.empno and basic=(select max(basic) from salary_master)")
    myresult = mycursor.fetchone()
    print("Data                    ")
    print("Empname=    ",myresult[0])
    print("job=        ",myresult[1])
    print("Basic Sal=: ",myresult[2])
    
    
def misemp():
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    print("***********************SEARCH BY  MIN SAL EMPLOYEE **********************")
    print("--------------------------------------------------------------")
    mycursor = mydb.cursor()
    mycursor.execute("select ename,job,basic from emp_master,salary_master where emp_master.empno=salary_master.empno and basic=(select min(basic) from salary_master)")
    myresult = mycursor.fetchone()
    print("Data ")
    print("Empname=    ",myresult[0])
    print("job=        ",myresult[1])
    print("Basic Sal=: ",myresult[2])
    
def lavgsemp():
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    print("***********************SEARCH BY  LESS THAN AVG SAL EMPLOYEE **********************")
    print("-------------------------------------------------------------------------")
    mycursor = mydb.cursor()
    mycursor.execute("select ename,job,basic from emp_master,salary_master where emp_master.empno=salary_master.empno and basic<=(select avg(basic) from salary_master)")
    myresult = mycursor.fetchall()
    print("Data ")
    
    for x in myresult:
       #print(x) 
       print("Empname=    ",x[0])
       print("job=        ",x[1])
       print("Basic Sal=: ",x[2])
    

# graph min max avg sal graph
def grp1():
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    
    mycursor = mydb.cursor()
    mycursor.execute("select min(basic),max(basic),avg(basic) from salary_master")
    myresult = mycursor.fetchone()

    x = np.array(["MIN", "MAX", "AVG"])
    y = np.array(myresult)

    plt.bar(x,y)
    plt.show()


# yearly  salary payment graph 
def grp2():
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector

    mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="upasana",
                  database="employee"
                                    )
    
    mycursor = mydb.cursor()
    mycursor.execute("select year,sum(basic) from salary_master group by year order by year")
    myresult = mycursor.fetchall()
    lst=[]
    for x in myresult:
        lst.append(x[1])
    
    mycursor1 = mydb.cursor()
    mycursor1.execute("select distinct year from salary_master order by year")
    myresult1 = mycursor1.fetchall()
    x=(["2021","2022"])
    y = np.array(lst)

    plt.bar(x,y)
    plt.show()




#salary
def menu6():
    ch=0
    while ch != 3:
        print("**********GRAPH MENU **********")
        print("--------------------------------")
        print("1.MIN MAX AVG SALARY GRAPH     ")
        print("2.YEARLY SALARY PAYMENT GRAPH  ")
        print("3.RETURN                       ")
        
       
        ch=int(input("Enter your choice[1-3] :"))
        if ch==1 :
             grp1()
        elif ch==2:
             grp2()
        elif ch==3:    
             break


menu1()        
