import mysql.connector
from tkinter import *
import os
from mysql import *
from tkinter import messagebox as msg
import random


def create_account():
    global create_account_screen
    global contact_number
    global name
    global address
    global DOB

    create_account_screen = Toplevel(main_screen)
    create_account_screen.title("Create New Account")
    create_account_screen.geometry("1000x1000")


    Label(create_account_screen, text="Please enter details below", bg="red").pack()
    Label(create_account_screen, text="").pack()

    name_label = Label(create_account_screen, text="Name ")
    name_label.pack()
    name = Entry(create_account_screen)
    name.pack()

    Label(create_account_screen, text="").pack()

    contactnumber_label = Label(create_account_screen, text="Contact number * ")
    contactnumber_label.pack()
    contact_number = Entry(create_account_screen)
    contact_number.pack()

    Label(create_account_screen, text="").pack()

    DOB_label = Label(create_account_screen, text="Date of Birth * (YYYY-MM-DD) format")
    DOB_label.pack()
    DOB = Entry(create_account_screen)
    DOB.pack()

    Label(create_account_screen, text="").pack()

    address_label = Label(create_account_screen, text="Address ")
    address_label.pack()
    address = Entry(create_account_screen)
    address.pack()

    Label(create_account_screen, text="").pack()

    global gender
    global acc_type
    global branch
    gender = IntVar()
    acc_type = IntVar()
    branch = IntVar()

    gender_label = Label(create_account_screen, text="Select Gender")
    gender_label.pack()
    R1 = Radiobutton(create_account_screen, text="Female", variable=gender, value=1,
                     command=sel)
    R1.pack(anchor=W)

    R2 = Radiobutton(create_account_screen, text="Male", variable=gender, value=2,
                     command=sel)
    R2.pack(anchor=W)

    R3 = Radiobutton(create_account_screen, text="Other", variable=gender, value=3,
                     command=sel)
    R3.pack(anchor=W)

    Label(create_account_screen, text="").pack()

    Acc_type_label = Label(create_account_screen, text="Select Account Type")
    Acc_type_label.pack()

    C1 = Radiobutton(create_account_screen, text="Savings", variable=acc_type, value=1,
                     command=sel)
    C1.pack(anchor=W)

    C2 = Radiobutton(create_account_screen, text="Current", variable=acc_type, value=2,
                     command=sel)
    C2.pack(anchor=W)

    branch_label = Label(create_account_screen, text="Select Branch")
    branch_label.pack()

    B1 = Radiobutton(create_account_screen, text="COEP Shivajinagar", variable=branch, value=1,
                     command=sel)
    B1.pack(anchor=W)

    B2 = Radiobutton(create_account_screen, text="Wakad", variable=branch, value=2,
                     command=sel)
    B2.pack(anchor=W)

    B3 = Radiobutton(create_account_screen, text="Hadapsar", variable=branch, value=3,
                     command=sel)
    B3.pack(anchor=W)

    B4 = Radiobutton(create_account_screen, text="FC Road", variable=branch, value=4,
                     command=sel)
    B4.pack(anchor=W)

    B5 = Radiobutton(create_account_screen, text="Baner", variable=branch, value=5,
                     command=sel)
    B5.pack(anchor=W)


    Button(create_account_screen, text="Create", width=10, height=1, bg="red", command=create_account_sql).pack()

def create_account_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    if len(contact_number.get()) == 0:
        msg.showinfo('Contact number field should not be empty')
        return

    if(len(DOB.get()) == 0):
        msg.showinfo('Date of birth field should not be empty')
        return

    if (len(address.get()) == 0):
        msg.showinfo('Address field should not be empty')
        return

    if (len(name.get()) == 0):
        msg.showinfo('NAME field should not be empty')
        return


    contact=contact_number.get()
    if(len(contact) != 10):
        return

    flag = 0
    while (flag == 0):
        acc_no = random.randint(0, 99999999)
        sql = "SELECT Account_Type from account_table WHERE Account_Number = %s"
        cur.execute(sql,(acc_no))
        rows=cur.fetchall()
        if(cur.rowcount != 0)
            continue
        else:
            flag = 1

    g=int(gender.get())

    type=int(acc_type.get())
    br = int(branch.get())
    balance = 0
    if(g == 1):
        gender1='F'
    elif(g ==2):
        gender1='M'
    elif(g ==3):
        gender1="O"
    else:
        msg.showinfo('Select a gender')
        return


    if(type ==1):
        acc_type1='S'
    elif(type ==2):
        acc_type1='C'
    else:
        msg.showinfo('Select an account type')
        return

    if(br == 5):
        branch_id= 1105
    elif(br == 4):
        branch_id = 1104
    elif (br == 3):
        branch_id = 1103
    elif (br == 2):
        branch_id = 1102
    elif (br== 1):
        branch_id = 1101
    else:
        msg.showinfo('Select a Branch')
        return


    sql = "Insert into account_table values(%s,'%s',%s, %f,%s)"
    cur.execute(sql,(acc_no, acc_type1, branch_id,balance,contact_number))
    con.commit()
    sql1 = "SELECT Name WHERE ContactNumber = %s "
    cur.execute(sql1, (contact_number))
    con.commit()

    if(cur.rowcount !=0 ):
        if (i >= 1):
            con.commit()
            msg.showinfo('Information', 'Record Saved')
    else:
        sql = "Insert into customer values(%s,'%s',%s, %s,%s)"
        cur.execute(sql, (contact_number,name,address,DOB, gender1))
        con.commit()
        msg.showinfo('Information', 'Record Saved')


    con.close()

def sel():
    selection = 0
    return selection

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("3000x2500")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()



    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    Button(login_screen, text="GO BACK", width=10, height=1, bg="orange", command=destroy_login).pack()

def destroy_login():
    login_screen.destroy()

def login_verify():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    user = str(username_verify.get())
    passwd = str(password_verify.get())

    cur.execute("SELECT * FROM login")
    con.commit()
    flag=0
    for i in range(cur.rowcount):
        row = cur.fetchone()

        if(row[0] == user):
            if(row[1] == passwd):
                flag = 1
                break
            else:
                flag = 2
                break
        else:
            flag = 3
            user_not_found()

    if(flag==1):
        login_sucess()
    elif(flag ==2 ):
        incorrect_password()
    else:
        user_not_found()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    # Button(login_success_screen, text="OK", command=delete_login_success).pack()
    Button(login_success_screen, text="OK", command=menu).pack()


# Designing popup for login invalid password

def incorrect_password():
    global incorrect_password_screen
    incorrect_password_screen = Toplevel(login_screen)
    incorrect_password_screen.title("Success")
    incorrect_password_screen.geometry("150x100")
    Label(incorrect_password_screen, text="Incorrect Password ").pack()
    Button(incorrect_password_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    incorrect_password_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def create_user():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("CREATE NEW USERNAME")
    register_screen.geometry("1000x250")

    global username
    global password
    global contact_number
    global username_entry
    global password_entry
    global contactnumber_entry
    username = StringVar()
    password = StringVar()
    contact_number = StringVar()

    Label(register_screen, text="Please enter details below", bg="red").pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username * ")

    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)

    username_entry.pack()
    contactnumber_label = Label(register_screen, text="Contact number * ")
    contactnumber_label.pack()

    contactnumber_entry = Entry(register_screen, textvariable=contact_number)
    contactnumber_entry.pack()

    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command=create_user_sql).pack()
    Button(register_screen, text="GO BACK", width=10, height=1, bg="orange", command=destroy_create_user).pack()

def destroy_create_user():
    register_screen.destroy()

def create_user_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    flag = 0
    cur.execute("SELECT * FROM login")
    rows = cur.fetchall()
    user = str(username.get())
    contact=str(contact_number.get())
    passwd=str(password.get())

    for row in rows:

        if(row[3] == contact):
            flag=1
            msg.showinfo('A username is already registered with this contact number')

        if (row[0] != user):
            if (row[1] != passwd):
                continue
            else:
                flag = 1
                msg.showinfo('Enter another password')
                break
        else:
            flag = 1
            msg.showinfo('Enter another username')
            break

    if(flag == 0):
        sql = "INSERT INTO login (Username,password,ContactNumber) VALUES (%s, %s, %s);"
        cur.execute(sql,(user, passwd,contact))
        con.commit()
        msg.showinfo('Information', 'Record Saved')


def deposit():

    global a1
    global am1
    global deposit_screen
    deposit_screen = Toplevel(main_screen)
    deposit_screen.title("deposit")
    deposit_screen.geometry("3000x2500")
    Label(deposit_screen, text="Please enter details below to Deposit").pack()
    Label(deposit_screen, text="").pack()


    account_label = Label(deposit_screen, text="Account number * ")
    account_label.pack()
    a1 = Entry(deposit_screen)
    a1.pack()


    amount_label = Label(deposit_screen, text="Amount * ")
    amount_label.pack()
    am1 = Entry(deposit_screen)
    am1.pack()


    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="Deposit", width=10, height=1, bg="red", command=deposit_sql).pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="GO HOME", height="2", width="10", fg='black', bg='orange', command=main_menu).pack()
    Label(deposit_screen, text="").pack()


def deposit_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    acc_no = a1.get()
    amnt = float(am1.get())

    sql ="SELECT Balance FROM account_table WHERE Account_Number = %s"

    cur.execute(sql, (acc_no))
    records = cur.fetchall()
    con.commit()

    if (cur.rowcount != 0 ):
        con.commit()

        for row in records:
            Bal = row[3]
            Bal += amnt
            a = "UPDATE account_table SET Balance = %f WHERE Account_Number = %s"
            cur.execute((a,(Bal,acc_no)))
            con.commit()
            msg.showinfo('Transaction Successful')

    else:
        msg.showinfo('Account Number does not exists')

    a1.delete(0, 'end')
    am1.delete(0, 'end')
    con.close()
    
def main_menu():
    deposit_screen.destroy()



def withdraw():
    global withdraw_screen
    withdraw_screen = Toplevel(main_screen)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry("3000x2500")
    Label(withdraw_screen, text="Please enter details below to Withdraw").pack()
    Label(withdraw_screen, text="").pack()


    account_label = Label(withdraw_screen, text="Account number * ")
    account_label.pack()
    a1 = Entry(withdraw_screen)
    a1.pack()


    amount_label = Label(withdraw_screen, text="Amount * ")
    amount_label.pack()
    am1 = Entry(withdraw_screen)
    am1.pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="Withdraw", width=10, height=1, bg="red", command=withdraw_sql).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="GO HOME", height="2", width="10", fg='black', bg='orange', command=main_menu1).pack()
    Label(withdraw_screen, text="").pack()

def withdraw_sql():

    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    acc_no = a1.get()
    amnt = float(am1.get())

    sql = "SELECT Balance FROM account_table WHERE Account_Number = %s"

    cur.execute(sql, (acc_no))
    records = cur.fetchall()
    con.commit()

    if (cur.rowcount != 0):
        con.commit()

        for row in records:
            Bal = row[3]
            if(Bal >= amount):
                Bal-=amount
                a = cur.execute("UPDATE account_table SET Balance = %f WHERE Account_Number = %s")
                cur.execute((a, (Bal, acc_no)))
                con.commit()
                msg.showinfo('Transaction Successful')
            else:
                msg.showinfo('Insufficent Balance')
                a1.delete(0, 'end')
                am1.delete(0, 'end')




    else:
        msg.showinfo('Account Number does not exists')

    a1.delete(0, 'end')
    am1.delete(0, 'end')

    con.close()


def main_menu1():
    withdraw_screen.destroy()

def Show_Account():
    global show_account
    global c1

    c1= StringVar()
    show_account = Toplevel(main_screen)
    show_account.title("Show Accounts")
    show_account.geometry("3000x2500")
    Label(show_account, text="Your Accounts ").pack()
    Label(show_account, text="").pack()
    contact_label = Label(show_statement, text="Contact number * ")
    contact_label.pack()
    c1 = Entry(show_statement)
    c1.pack()
    Button(show_account, text="SHOW", height="2", width="10", fg='black', bg='orange', command=Show_Account_sql).pack()
    Button(deposit_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange', command=destroy_show_account).pack()

def destroy_show_account():
    show_account.destroy()

def Show_Account_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    contact = c1.get()
    sql = "SELECT * FROM Account_table WHERE ContactNumber=%s"
    cur.execute(sql, (contact))
    record = cur.fetchall()
    if (cur.rowcount == 0):
        msg.showinfo('No account is registered with this Contact Number')
    else:
        for a in cur:
            for j in range(len(a)):
                e = Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, a[j])
            i = i + 1

    con.close()


def Show_Statement():
    global show_statement
    show_statement = Toplevel(main_screen)
    show_statement.title("Show Statement")
    show_statement.geometry("3000x2500")
    Label(show_statement, text="Enter the below details to view Account Statement ").pack()
    Label(show_statement, text="").pack()
    account_label = Label(show_statement, text="Account number * ")
    account_label.pack()
    a1 = Entry(show_statement)
    a1.pack()
    Button(show_statement, text="SHOW", height="2", width="10", fg='black', bg='orange', command=Show_Statements_sql).pack()
    Button(deposit_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange',
           command=destroy_show_statement).pack()

def destroy_show_statement():
    show_statement.destroy()

def Show_Statement_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    acc_no=a1.get()
    sql="SELECT * FROM Account_table WHERE Account_Number=%s"
    cur.execute(sql,(acc_no))
    record = cur.fetchall()
    if(cur.rowcount ==0):
        msg.showinfo('Account Number does not exists')
    else:
        b="SELECT * FROM transaction WHERE Account_Number=%s ORDER BY Date"
        cur.exceute(b,(acc_no))
        if(cur.rowcount !=0 ):
            for a in cur:
                for j in range(len(a)):
                    e = Entry(my_w, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, a[j])
                i = i + 1
        else:
            msg.showinfo('No transaction happened with this account')

    con.close()



def Show_loan():
    global show_loan
    show_loan = Toplevel(main_screen)
    show_loan.title("Show Loan Details")
    show_loan.geometry("3000x2500")
    Label(show_loan, text="Enter the below details to view Loan Details ").pack()
    Label(show_loan, text="").pack()
    loan_label = Label(show_loan, text="Loan_id * ")
    loan_label.pack()
    id = Entry(show_loan)
    id.pack()
    Button(show_loan, text="SHOW", height="2", width="10", fg='black', bg='orange', command=Show_loan_sql).pack()
    Button(deposit_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange',
           command=destroy_show_loan).pack()

def destroy_show_loan():
    show_loan.destroy()

def Show_loan_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    r_set = cur.execute("SELECT * FROM loan WHERE loan_id=%d ORDER BY Date")

    if(r_set>=1):
        for student in r_set:
            for j in range(len(student)):
                e = Label(show_loan, width=10, text=student[j],
                      borderwidth=2, relief='ridge', anchor="w")
                e.grid(row=i, column=j)
                e.insert(END, student[j])
            i = i + 1
    else:
        msg.showinfo('Loan ID does not exists')

    con.close()
def create_newloan():
    global create_newloan_screen
    global principal_check
    global accountnumber_check

    principal_check= StringVar()
    accountnumber_check= StringVar()

    create_newloan_screen = Toplevel(main_screen)
    create_newloan_screen.title("Apply for loan")
    create_newloan_screen.geometry("1000x1000")

    Label(create_newloan_screen, text="Please enter details below", bg="red").pack()
    Label(create_newloan_screen, text="").pack()

    principal_label = Label(create_newloan_screen, text="Principal needed ")
    principal_label.pack()
    principal= Entry(create_newloan_screen,textvariable=principal_check)
    principal.pack()


    Label(create_newloan_screen, text="").pack()

    accountnumber_label = Label(create_newloan_screen, text="Account number to be linked ")
    accountnumber_label.pack()
    accountnumber = Entry(create_newloan_screen,textvariable=accountnumber_check)
    accountnumber.pack()

    Label(create_newloan_screen, text="").pack()



    global loan_type
    loan_type = IntVar()

    gender_label = Label(create_newloan_screen, text="Select Loan Type")
    gender_label.pack()
    L1 = Radiobutton(create_newloan_screen, text="Home Loan : Rate - 8%", variable=loan_type, value=1,
                     command=sel)
    L1.pack(anchor=W)

    L2 = Radiobutton(create_newloan_screen, text="Education Loan: Rate - 6.5%", variable=loan_type, value=2,
                     command=sel)
    L2.pack(anchor=W)

    L3 = Radiobutton(create_newloan_screen, text="Personal Loan: Rate - 7%", variable=loan_type, value=3,
                     command=sel)
    L3.pack(anchor=W)

    label1 = Label(create_newloan_screen, text="Time duration- based on Amount")
    label1.pack()
    label2 = Label(create_newloan_screen, text="2 years- if  Amount >= 100,000 and Amount < 500,000")
    label2.pack()
    label3 = Label(create_newloan_screen, text="3 years- if  Amount >= 500,000 and Amount < 10,00,000")
    label3.pack()
    label4 = Label(create_newloan_screen, text="10 years- if  Amount >= 10,00,000 and Amount < 15,00,000")
    label4.pack()
    label5 = Label(create_newloan_screen, text="15 years- if  Amount >= 15,00,000")
    label5.pack()

    Button(create_newloan_screen, text="Review", height="2", width="10", fg='black', bg='green', command=review).pack()
    Button(create_newloan_screen, text="Create", height="2", width="10", fg='black', bg='yellow', command=create_newloan_sql).pack()
    Button(deposit_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange',
           command=destroy_create_loan).pack()

def destroy_create_loan():
    create_newloan_screen.destroy()


def review():
    global review_screen
    global type
    global t
    global EMI
    global amount
    global i
    global p
    global r
    global ltype
    review_screen = Toplevel(main_screen)
    review_screen.title("Review")

    p=int(principal_check.get())
    type=int(loan_type.get())
    if(type == 1):
        r=8
        l_type="Home"
    elif(type==2):
        r = 6.5
        l_type="Education"
    elif(type ==3):
        r = 7
        l_type="Personal"

    if(p >= 100000 and p < 500000 ):
        time=2
    elif(p >= 500000 and p < 1000000):
        time=3
    elif(p >= 1000000 and p < 1500000):
        time =10
    else:
        time=15

    if(type == 1):
        rate=8
    elif(type == 2):
        rate=6.5
    else:
        rate=7




    i=(principal * rate * time)/100.00
    amount= i + (principal)
    EMI = float(amount / time)

    review_screen.geometry("1000x700")
    label1 = Label(review_screen, text="Amount is:" )
    label1.pack()
    label6=Label(review_screen, textvariable= amount, Relief= RAISED)
    label6.pack()

    label2 = Label(review_screen, text="Rate of Interest")
    label2.pack()
    label7 = Label(review_screen, textvariable=rate, Relief=RAISED)
    label7.pack()

    label3 = Label(review_screen, text="Interest")
    label3.pack()
    label8 = Label(review_screen, textvariable=Interest, Relief=RAISED)
    label8.pack()

    label4 = Label(review_screen, text="EMI")
    label4.pack()
    label9 = Label(review_screen, textvariable=EMI, Relief=RAISED)
    label9.pack()
    label5 = Label(review_screen, text="Time")
    label5.pack()
    label0 = Label(review_screen, textvariable=time, Relief=RAISED)
    label0.pack()

    Button(review_screen, text="OK", command=destroy_review_screen).pack()

def destroy_review_screen():
    review_screen.destroy()

def create_newloan_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    flag=0
    loan_id=0
    acc_no = accountnumber_check.get()
    while(flag==0):
        loan_id = random.randint(0, 99999999)
        a = cur.execute("SELECT loan_type from loan WHERE loan_id = %d" )
        cur.execute(a,(loan_id))
        record = cur.fetchall()
        con.commit()

        if (cur.rowcount != 0):
            continue
        else:
            flag=1

    sql = "Insert into loan values(%s,'%s',%s, %s,%s,%s,%s,%s)"
    id=str(loan_id)
    amt=str(amount)
    prin=str(principal)
    emi=str(EMI)
    rat=str(rate)
    t=str(t)
    cur.execute(sql, (id, ltype, amt ,acc_no, prin ,rat,emi,t))
    con.commit()

    c = "Your Loan_Id is:" + " " + str(loan_id)
    msg.showinfo('IMPORTANT', c)


    con.close()


def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.title("menu")
    menu_screen.geometry("3000x2500")
    Label(menu_screen, text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Deposit", height="2", width="30", fg='black', bg='violet', command=deposit).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Withdraw", height="2", width="30", fg='black', bg='orange', command=withdraw).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Balance", height="2", width="30", fg='black', bg='orange', command=balance).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Show Accounts", height="2", width="30", fg='black', bg='orange',
           command=Show_Account).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Create New Account", height="2", width="30", fg='black', bg='orange',
           command=create_account).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Logout", height="2", width="10", fg='black', bg='orange', command=logout2).pack()
    Label(menu_screen, text="").pack()




def exiting():
    main_screen.destroy()

def logout2():
    menu_screen.destroy()



def balance():
    global balance_screen
    balance_screen = Toplevel(main_screen)
    balance_screen.title("Balance enquiry")
    balance_screen.geometry("300x250")
    Label(balance_screen, text="Please enter details below to login").pack()
    Label(balance_screen, text="").pack()

    account_label = Label(balance_screen, text="Account number * ")
    account_label.pack()
    a1 = Entry(balance_screen)
    a1.pack()

    Button(text="Balance", height="5", width="50", fg='black', bg='green', font=("Arial Bold", 10), command=balance_sql).pack()
    Button(balance_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange',
           command=destroy_balance).pack()

def destroy_balance():
    balance_screen.destroy()

def balance_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    acc_no = a1.get()
    sql = "SELECT Balance FROM account_table WHERE Account_Number = %s"
    cur.execute(sql,(acc_no))
    rows=cur.fetchall()
    con.commit()
    if (cur.rowcount !=0):
        msg.showinfo('Information', 'Record Saved')
        for row in rows:
            Balance = row[3]
            Label(balance_screen, textvariable=Balance).pack()

    else:
        msg.showinfo('Account Number does not exists')

    a1.delete(0, 'end')
    con.close()


def delete_account():
    global delete_account_screen
    delete_account_screen = Toplevel(main_screen)
    delete_account_screen.title("Delete_Account")
    delete_account_screen.geometry("300x250")
    Label(delete_account_screen, text="Please enter Account you want to delete").pack()
    Label(delete_account_screen, text="").pack()

    account_label = Label(delete_account_screen, text="Account number * ")
    account_label.pack()
    a1 = Entry(delete_account_screen)
    a1.pack()

    Button(delete_account_screen,text="DELETE", height="5", width="50", fg='black', bg='green', font=("Arial Bold", 10),
           command=balance_sql).pack()
    Button(delete_account_screen, text="GO BACK", height="2", width="10", fg='black', bg='orange',
           command=destroy_balance).pack()


def destroy_delete_account():
    delete_account_screen.destroy()


def delete_account_screen_sql():
    con = mysql.connector.connect(db='bank', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    acc_no = a1.get()
    sql1 = "SELECT * FROM loan WHERE Account_Number = %s"
    cur.execute(sql1, (acc_no))
    rows = cur.fetchall()
    if(cur.rowcount !=0):
        msg.showinfo("Cant delete account; a loan id is linked with this Account ")
    else:
        sql2 = "SELECT * FROM account_table WHERE Account_Number = %s"
        cur.execute(sql2, (acc_no))
        if(cur.rowcount !=0)
            sql = "DELETE FROM account_table WHERE Account_Number = %s"
            cur.execute(sql, (acc_no))
            con.commit()
        else:
            msg.showinfo('Account Number does not exists')

    a1.delete(0, 'end')
    con.close()
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50", fg='black', bg='green', font=("Arial Bold", 10), command=login).pack()
    Label(text="").pack()
    Button(text="Create new username", height="5", width="50", fg='black', bg='blue', font=("Arial Bold", 10),command=create_user).pack()
    Label(text="").pack()
    Button(text="Exit", height="5", width="50", fg='black', bg='red', font=("Arial Bold", 10),
           command=exiting).pack()

    main_screen.mainloop()


main_account_screen()