print("_*_*_*_*_*_*_*_*_*_*_*____CELTIC   CLOTHING____*_*_*_*_*_*_*_*_*_*_*_*_")
import csv, billing, user, shopping_cart, filtered_search, sys
from tkinter import *
cart={}
while True:
    print("\n1.Your Account\n2.Search Button\n3.Mens Fashion\n4.Womens Fashion\n5.Your cart\n6.Place Order\n7.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        choice=input("Have an account?(Yes/No)")
        if choice=="No":
            user.signup()
            print("Please log in to proceed")
            em=user.login()
        elif choice=="Yes":
            print("Please log in to proceed")
            em=user.login()
        print("_*_*_*_*_*_*_*_*_*_*     YOUR ACCOUNT   *_*_*_*_*_*_*_*_*_*_\n")
        while True:
            print("1.Your Profile\n2.Edit Profile\n3.Your Orders\n4.Exit")
            ch=int(input("Enter choice:"))
            if ch==1:
                user.profile(em)
            elif ch==2:
                user.edit_profile(em)
            elif ch==3:
                lst1=user.orders(em)
                class Table:
                    def __init__(self,root):
                        for i in range(total_rows):
                            for j in range(total_columns):
                                self.e = Entry(root, width=20, fg='black', font=('Arial',9,'bold'))
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, lst1[i][j])
                total_rows = len(lst1)
                total_columns = len(lst1[0])
                root = Tk()
                t = Table(root)
                root.mainloop()
            elif ch==4:
                break
    elif ch==2:
        filtered_search.search(cart)
    elif ch==3:
        print("_*_*_*_*_*_*_*_*_*_*       MEN'S FASHION      *_*_*_*_*_*_*_*_*_*_\n")
        while True:
            print("Search By Filters")
            print("1.Shop Category wise\n2.Shop Brand wise\n3.Shop Price wise\n4..Exit")
            ch=int(input("Enter choice:"))
            if ch==1:
                filtered_search.category_search(cart,"Men")
            elif ch==2:
                filtered_search.brand_search(cart,"Men")
            elif ch==3:
                filtered_search.price_search(cart,"Men")
            elif ch==4:
                break
    elif ch==4:
        print("_*_*_*_*_*_*_*_*_*_*       WOMEN'S FASHION      *_*_*_*_*_*_*_*_*_*_\n")
        while True:
            print("Search By Filters")
            print("1.Shop Category wise\n2.Shop Brand wise\n3.Shop Price wise\n4.Exit")
            ch=int(input("Enter choice:"))
            if ch==1:
                filtered_search.category_search(cart,"Women")
            elif ch==2:
                filtered_search.brand_search(cart,"Women")
            elif ch==3:
                filtered_search.price_search(cart,"Women")
            elif ch==4:
                break
    elif ch==5:
        print("_*_*_*_*_*_*_*_*_*_*       SHOPPING CART      *_*_*_*_*_*_*_*_*_*_\n")
        while True:
            print("1.View your cart\n2.Remove product from cart\n3.Update product stock\n4.Exit")
            ch=int(input("Enter choice:"))
            if ch==1:
                shopping_cart.view_cart(cart)
            elif ch==2:
                shopping_cart.remove_item(cart)
            elif ch==3:
                shopping_cart.update_stock(cart)
            elif ch==4:
                break
    elif ch==6:
        print("_*_*_*_*_*_*_*_*_*_*       BILLING      *_*_*_*_*_*_*_*_*_*_\n")
        choice=input("Have an account?(Yes/No)")
        if choice=="No":
            user.signup()
            print("Please log back in to proceed")
            em=user.login()
        else:
            print("Please log back in to proceed")
            em=user.login()
            lst1=billing.customer_append(em,cart)
            billing.stock_change(cart)
            class Table:
                def __init__(self,root):
                    for i in range(total_rows):
                        for j in range(total_columns):
                            self.e = Entry(root, width=20, fg='black', font=('Arial',9,'bold'))
                            self.e.grid(row=i, column=j)
                            self.e.insert(END, lst1[i][j])
            total_rows = len(lst1)
            total_columns = len(lst1[0])
            root = Tk()
            t = Table(root)
            root.mainloop()
            billing.total_price(cart)
            print("Thank You for Shopping")
    elif ch==7:
        print("*******************PROGRAM TERMINATING*******************")
        sys.exit()
