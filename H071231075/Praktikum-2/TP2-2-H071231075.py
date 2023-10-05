x=input('masukkan input pertama :')
x=x.lower()
y=input('masukkan input kedua :')
y=y.lower()
z=input('masukkan input ketiga :')
z=z.lower() 

match x:
    case'vertebrado':
        if y=='ave':
         if z=='carnivoro':
            print('aguia')
         elif z=='onivoro':
            print('pomba')

        elif y=='mamifero':
           if z=='onivoro':
              print('homem') 
           elif z=='herbivoro':
              print('vaca')
        else:print('invalid input')  

    case'invertebrado':
        if y=='inseto':
           if z=='hematofago':
              print('pulga') 
           elif z=='herbivoro':
              print('lagarta')

        elif y=='anelideo':
           if z=='hematofago':
              print('sanguessuga')
           elif z=='onivoro':
              print('minhoca')
        else :print('invalid input')
    case _:
      print('invalid input')
      

            
         



    


