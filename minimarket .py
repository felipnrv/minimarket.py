#Bienvenido al MiniMarket ...(Elaborado por Felipe Narvaez,Jose Herrera ,Esteban Moya)
#Con el apoyo de la Celula Microsoft UIsrael

print(" ***Bienvenido al MiniMarket .... *** ")


def menu():
        print('\n')
        print("1. Ingresar la informacion " )
        print("2. Ordenar el inventario de mayor a menor " )
        print("3. Ordenar el inventario de menor a mayor " )
        print("4 .Salir ")
    
        
while True:
        menu()        


        opc=str(input("Ingrese la opcion que desee "))
        if opc=="1":
                print()
                
                num=int(input("Ingrese el numero de producto que desee ingresar: "))
                product=[str(input("ingrese el producto: "))for x in range(num)] 
                listinvt=[int(input("Ingrese los numeros de inventario: "))for x in range(num)] 
                
        
        if opc=="2":
                print("*****Ordenar Mayor a Menor***** ")
                for i in range(len(listinvt)-1):
                        index=i
                        for j in range(i+1,len(listinvt)):
                                if listinvt[j]> listinvt[index]: 
                                        index=j
                    
                        if listinvt[i] != listinvt[index]:        
                                listinvt[i],listinvt[index]=listinvt[index],listinvt[i]
               
                for item in (listinvt):
                        print(item)
                        
                             
                        
        if opc=='3':
                print("*****Ordenar Menor a Mayor***** ")        
                for i in range(len(listinvt)-1):
                        index=i
                        for j in range(i+1,len(listinvt)):
                                if listinvt[j]< listinvt[index]: 
                                        index=j
                    
                        if listinvt[i] != listinvt[index]:        
                                listinvt[i],listinvt[index]=listinvt[index],listinvt[i]
                    
                for item in (listinvt):
                        print(item)     
        if opc=="4":
                print("Elaborado por Felipe Narvaez,Jose Herrera ,Esteban Moya")
                break
                



    
  
        
                    

                
