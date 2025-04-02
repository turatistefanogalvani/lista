def aggiungi():
    elemento = str(input("Inserisci un elemento della spesa: "))
    lista.append(elemento)

def rimuovi():
    visualizza()
    indice = int(input())
    lista.pop(indice-1)

def visualizza():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def conta():
    print(len(lista))

def svuota():
    lista.clear()

lista=[]
while True:
    n = int(input("Premere 0 per interrompere; Premere 1 per inserire un elemento alla lista; Premi 2 per rimuovere un elemento; Premi 3 per visualizzare: "))
    if n == 0:
        break
    elif n == 1:
        aggiungi()
    elif n == 2:
        rimuovi()
    elif n == 3:
        visualizza()
    elif n == 4:
        conta()
    elif n == 5:
        svuota()