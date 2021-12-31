#Kontrolle der Zahlen, ob diese ein Pythoagoras Dreieck darstellen
#code is self-made
#print("Henlo World")

def quest():
    z=input("Die drei Zahlen bitte mit Komma trennen:\n\n")
    z=z.split(",")
    o=[]
    if len(z) == 3:
        k=0
        while k<3:
            z.insert(k, int(z[k]))
            z.pop(k+1)
            k+=1
        z=numbsort(z)
        if checker(z) == True:
            print("\nJuhuu, deine Zahlen ergeben ein Pythagoras Dreieck!")
        else:
            print("\nOch nee, kein Pythagoras Dreieck für dich :(")
    else:
        print("Zahlen leider falsch eingegeben\n")
    n=input("Noch ein mal versuchen? (Y|n)\n\n")
    if n.lower()=="y":
        quest()
        n="n"
    else:
        print("Byebye")
        
def numbsort(num):
    #Zahlen sortieren
    re=[]
    #Return this array
    iz=0
    while iz<3:
        i=0
        while i<len(num):
            if i==0:
                sm=num[0]
                pos=0
                #Declare first number as minimum for later comparison
            elif num[i]<sm:
                #If number is smaller than reference, then...
                sm=num[i]
                #... new smallest number (temporary) is num[position]
                pos=i
                #... position of the smallest number (temporary) is noted
            if i==len(num)-1:
                re.append(num[pos])
                num.pop(pos)
            i+=1
        iz+=1
    return re

def checker(num):
    # |\
    # | \
    # |  \
    # - - - 
    if int(num[0])**2+int(num[1])**2==int(num[2])**2:
        return True
    else:
        return False

quest()
