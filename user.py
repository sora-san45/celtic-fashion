#this module is used to mange the user details, log and sign up info and display the orders made by the user
import csv
from datetime import date
def signup():
    with open("User_details.csv",'r') as qee:
        rea=csv.reader(qee,delimiter=',')
        name=input("Enter name:")
        ph=input("Enter phone number:")
        em=input("Enter Email id:")
        while True:
            pas=input("Set a password:")
            p=input("Confirm Password")
            if p!=pas:
                print("Password does not match")
            else:
                break
        g=input("Enter gender:")
        loc=input("Enter location:")
        L=[]
        for jk in rea:
            L.append(jk)
        L.append([name,ph,em,g,loc,pas])
        with open("User_details.csv",'w',newline="") as df:
            ov=csv.writer(df,delimiter=',')
            ov.writerows(L)
#if the confirmed password doesn’t match, the loop continues till the set password and confirmed password match
#the details enters into the User_details.csv file after the execution
def login():
    with open("User_details.csv",'r') as qee:
        rea=csv.reader(qee,delimiter=',')
        em=input("Enter email id:")
        pwd=input("Enter password:")
        for i in rea:
            if i[2]==em and i[5]==pwd:
                print("Logged in Successfully")
                print("Welcome ",i[0])
                return em
        else:
            print("Incorrect password or invalid email address ")
def profile(em):
    print("_*_*_*_*_*_*_*_*_*_*     YOUR PROFILE     *_*_*_*_*_*_*_*_*_*_\n")
    with open("User_details.csv",'r') as dee:
        rea=csv.reader(dee,delimiter=',')
        for user in rea:
            if user[2]==em:
                print("Name:",user[0],"\n","Phone Number:",user[1],"\n","Email id:",em,"\n","Gender:",user[3],"\n","Location:",user[4],"\n","Password:",user[5])
def edit_profile(em):
    print("Which Detail to be changed?")
    with open("User_details.csv",'r') as dee:
        reader=csv.reader(dee,delimiter=',')
        print("1.Name\n2.Gender\n3.Location\n4.Password")
        choice=int(input("Enter choice:"))
        D={1:"Name",2:"Gender",3:"Location"}
        L=[]
        for g in reader:
            L.append(g)
        for k in L:
            if k[2]==em and choice!=4:
                st="Enter updated "+D[choice]+":"
                var=input(st)
                k[choice-1]=var
            elif k[2]==em and choice==4:
                while True:
                    old=input("Enter old password:")
                    if old!=k[5]:
                        print("Incorrect password please try again")
                    else:
                        pas=input("Enter new password")
                        k[5]=pas
                        break
        with open("User_details.csv",'w',newline="") as dee:
            write=csv.writer(dee,delimiter=',')
            write.writerows(L)
def orders(em):
    with open("customer_details.csv",'r') as re:
        read=csv.reader(re,delimiter=',')
        lst1=[["Email address","Product Code","Product name","Brand","Date of Purchase","Delivery Location","Price per piece" ,"Sizes","Total Quantity","Total Price"]]
        for i in read:
            if i[0]==em:
                lst1.append(i)
    return lst1
