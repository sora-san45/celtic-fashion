import csv
def display_product(cd):
    with open("product1_details.csv",'r') as m:
        n=csv.reader(m,delimiter=',')
        print("\n___________________________________________________________________________________________________________")
        for pro in n:
            if pro[0]==cd:
                print("PRODUCT CODE :",pro[0],"\nPRODUCT NAME :",pro[1],"\nBRAND :",pro[2],"\nCATEGORY :",pro[3],"\nDESCRIPTION :",pro[4],"\nMATERIAL AND CARE :")
                for j in pro[5].split(', '):
                      print(j)
                print("PRICE :",pro[6],"\nSUPPLIER:",pro[7])
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                st=cd+'().png'
                plt.axis("off")
                img=mpimg.imread(st)
                imgplot=plt.imshow(img)
                plt.show()
#the code displays the product details and the image of the product using Python’s matplotlib
 
def stock_display(cd):
    with open("Stock_details.csv",'r') as f:
        km=csv.reader(f,delimiter=',')
        print("SIZES","\t\t"," AVAILABLE ")
        for st_k in km:
            if st_k[0]==cd:
                print("XS\t\t",st_k[1],"\nS\t\t",st_k[2],"\nM\t\t",st_k[3],"\nL\t\t",st_k[4],"\nXL\t\t",st_k[5])
                break
        print("___________________________________________________________________________________________________________\n")


