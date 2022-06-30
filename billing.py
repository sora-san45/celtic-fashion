#this module is used to perform the functions involving billing which are finding the total price of the items ordered, to append the customer details to a csv file called customer.csv, change the stock and generating a bill
import csv
from datetime import date
def total_price(cart):
    d={}
    with open("product1_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        for p in y:
            for k in  cart :
                if p[0]==k:
                    d[p[0]]=p[6]
        tot=0
        for im in cart:
            s=0
            for j in range(1,len(cart[im]),2):
                s+=cart[im][j]
            tot+=s*int(d[im])
    print("Total price : ",tot)
def stock_change(cart):
    with open("Stock_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        L=["Product Code","XS","S","M","L","XL"]
        lst=[]
        for km in y:
            lst.append(km)
        for im in cart:
            for kp in lst:
                if kp[0]==im:
                    for g in range(0,len(cart[im]),2):
                        if g<len(cart[im]):
                            index1=L.index(cart[im][g])
                            s=cart[im][g+1]
                            kp[index1]=str(int(kp[index1])-int(s))
        with open("Stock_details.csv",'w',newline="") as ma:
            mp=csv.writer(ma,delimiter=',')
            mp.writerows(lst)
#changes the stock in the Stock_details.csv file after purchase
def customer_append(em,cart):
    de=input("Enter delivery location:")
    dt=date.today()
    dt1=dt.strftime("%d/%m/%Y")
    L=[]
    with open("customer_details.csv",'r') as mr:
        reader=csv.reader(mr,delimiter=',')
        for c in reader:
            L.append(c)
    lst1=[["Email address","Product Code","Product name","Brand","Date of Purchase","Delivery Location","Price per piece" ,"Sizes","Total Quantity","Total Price"]]
    lst=[]
    for it in cart:
        lst.append(it)
    with open("product1_details.csv",'r') as f:
        g=csv.reader(f,delimiter=',')
        for t in g:
            for ip in lst:
                if ip==t[0]:
                    lst1.append([em,t[0],t[1],t[2],dt1,de,t[6]])
        for i in lst1:
            for p in cart:
                if i[1]==p:
                    st=""
                    ct=0
                    total_stock=0
                    for h in range(0,len(cart[p]),2):
                        if (h+1)<len(cart[p]):
                            st+="("+cart[p][h]+"-"+str(cart[p][h+1])+")"
                            total_stock+=cart[p][h+1]
                    total_p=total_stock*int(i[6])
                    ct+=1
                    i.extend([st,total_stock,total_p])
                    L.append(i)
        with open("customer_details.csv",'w',newline="") as qp:
            wr=csv.writer(qp,delimiter=',')
            wr.writerows(L)
    return lst1

#appends customer details to the file customer_details.csv and the list containing the user’s ordered  items is returned and passed to display the bill using Tkinter Python GUI code in the home page and the total price is also printed from using the total_price function in module
