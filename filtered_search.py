#This module is used for the user to apply filters and discover products easier according to their interests
#This module also includes a search button for the user to search products under any category
import csv, display_product, shopping_cart
def search(cart):`
    with open("product1_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        x=input("Search for product:")
        print("_*_*_*_*_*_*_*_*_*_*     SEARCH RESULTS     *_*_*_*_*_*_*_*_*_*_")
        print("PRODUCT CODE","\t\t","PRODUCT NAME")
        for i in y:
            if x in i[1]:
                print(i[0],"\t\t",i[1])
        cd=input("Enter the Product code of the product you want to view:")
        display_product.display_product(cd)
        display_product.stock_display(cd)
        ch1=input("Add to cart?(Yes/No):")
        if ch1=="Yes":
            shopping_cart.add_to_cart(cart,cd)
#the use of this search button is that you don’t need to know the full name of the product which you are trying to find it will display results according to the data you entered
def category_search(cart,m_f):
    with open("product1_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        print("1.Tops, Tees and Shirts\n2.Bottom Wear\n3.Jackets and Coats\n4.Sweatshirts and Hoodies")
        ch=int(input("Enter choice:"))
        D1={1:"Tops, Tees and Shirts",2:"Bottom Wear",3:"Jackets and Coats",4:"Sweatshirts and Hoodies"}
        print("_*_*_*_*_*_*_*_*_*_*     ",D1[ch].upper(),"      *_*_*_*_*_*_*_*_*_*_")
        print("PRODUCT CODE","\t\t","PRODUCT NAME")
        for item in y:
            if m_f in item[1] and item[3]==D1[ch]:
                print(item[0],"\t\t",item[1])
        while True:
            cd=input("Enter the Product code of the product you want to view:")
            display_product.display_product(cd)
            display_product.stock_display(cd)
            ch1=input("Add to cart?(Yes/No):")
            if ch1=="Yes":
                shopping_cart.add_to_cart(cart,cd)
            ch2=input("Want to view the products again under this category(Yes/No)?")
            if ch2=="No":
                break
def brand_search(cart,m_f):
    with open("product1_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        L1=[]
        for i in y:
            if m_f in i[1]:
                L1.append(i[2])
        L1=list(set(L1))
        print("_*_*_*_*_*_*_*_*_*_*     BRANDS     *_*_*_*_*_*_*_*_*_*_")
        for i in L1:
            print(i)
        br=input("Enter the brand whose products you want to view:")
        print("BRAND","\t\t","PRODUCT CODE","\t\t","PRODUCT NAME")
        x.seek(0)
        for b in y:
            if m_f in b[1] and b[2]==br:
                print(br,"\t\t",b[0],"\t\t",b[1])
        while True:
            cd=input("Enter the Product code of the product you want to view:")
            display_product.display_product(cd)
            display_product.stock_display(cd)
            ch1=input("Add to cart?(Yes/No):")
            if ch1=="Yes":
                shopping_cart.add_to_cart(cart,cd)
            ch2=input("Want to view the products again under this category(Yes/No)?")
            if ch2=="No":
                break
def price_search(cart,m_f):
    with open("product1_details.csv",'r') as x:
        y=csv.reader(x,delimiter=',')
        print("1.500-999\n2.1000-1299\n3.Above 1300")
        ch=int(input("Enter choice:"))
        D2={"500-999":[1,500,1000],"1000-1300":[2,1000,1300],"Above 1300":[3,1300,1000000]}
        for i in D2:
            if D2[i][0]==ch:
                print("_*_*_*_*_*_*_*_*_*_*     PRICE RANGE: ",i,"     *_*_*_*_*_*_*_*_*_")
                print("PRODUCT CODE","\t\t","PRODUCT NAME")
                for item in y:
                        if m_f in item[1] and D2[i][1]<int(item[6])<D2[i][2] :
                            print(item[0],"\t\t",item[1])
        while True:
            cd=input("Enter the Product code of the product you want to view:")
            display_product.display_product(cd)
            display_product.stock_display(cd)
            ch1=input("Add to cart?(Yes/No):")
            if ch1=="Yes":
                shopping_cart.add_to_cart(cart,cd)
            ch2=input("Want to view the products again under this category(Yes/No)?")
            if ch2=="No":
                break      

