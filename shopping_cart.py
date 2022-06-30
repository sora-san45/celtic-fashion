#this module is used to add, view, delete and edit the quantity of the items in the user’s shopping cart
import csv, billing, display_product
def add_to_cart(cart,cd):
    with open("Stock_details.csv",'r') as f:
        k=csv.reader(f,delimiter=',')
        lst2=[]
        for i in k:
            for j in i:
                lst2.append(j)
            break
        lst2.pop(0)
        print(lst2)
        c=0
        while True:
            size=input("Enter the size you want to add:")
            qty=int(input("Enter quantity:"))
            for jp in lst2:
                if jp==size:
                    s=lst2.index(jp)
            f.seek(0)
            for pl in k:
                if pl[0]==cd:
                    if pl[s+1]=='0':
                        print("Product out of stock")
                    else:
                        print("Stock Avilable:",pl[s+1])
                        if c==0:
                            cart[cd]=[size,qty]
                        else:
                            cart[cd].append(size)
                            cart[cd].append(qty)
            ch3=input("Want to add more sizes(Yes/No):")
            if ch3=="No":
                break
            else:
                c+=1

#the product code along with the selected sizes and quantity is added to a temporary dictionary called “cart” with product code as key and value as a list conating the sizes with their respective quantity selected

def view_cart(cart):
    for item in cart:
        display_product.display_product(item)
        print("Sizes","\t","Quantity")
        for i in range(0,len(cart[item]),2):
            if i<len(cart[item]):
                print(cart[item][i],"\t",cart[item][i+1])
    billing.total_price(cart)

def remove_item(cart):
    while True:
        cd=input("Enter the product code of the product you want to remove:")
        cart.pop(cd)
        ch=input("Want to delete more items from cart?(Yes/No)")
        if ch=="No":
            break

def update_stock(cart):
    while True:
        cd=input("Enter the product code of the product you want to update the stock:")
        for item in cart:
            if item==cd:
                si=input("Enter size whose stock is to be updated:")
                s=int(input("Enter updated quantity:"))
                for i in range(0,len(cart[item]),2):
                    if i<len(cart[item]):
                       if cart[item][i]==si:
                           cart[item][i+1]=s
        ch=input("Enter want to update the stock for other products in cart?(Yes/No)")
        if ch=="No":
            break
