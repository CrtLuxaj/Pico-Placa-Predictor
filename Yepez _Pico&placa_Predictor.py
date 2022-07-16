# -*- coding: utf-8 -*-

from datetime import datetime


def PicoyPlaca(placa,fecha,hora):



    nDay = noCircula(placa) #dia en que no puede circular en base al ultimo digito de la placa
    dayNumber= int(fecha)  # numero de dia ingresado por el usuario
    time = horaNoCircula(hora) #comprueba el rango de hora en el que puede circular


    try:

        if(dayNumber == 6 or dayNumber == 0):   #sabado y domingo

            print("Recuerda que los fines de semana no existe restriccion por pico y placa")
            return
        else:
            if(nDay!=dayNumber):
                print("Tranquilo el dia que ingresaste si puedes circular a cualquier hora")
                return
            else:
                if(time==False):
                    print("El dia y la hora que ingresaste no vas a poder circular con tu carro, mejor utiliza una bicicleta")
                    return
                else:
                    print("Tranquilo el dia que ingresaste tienes restriccion pero en la hora que piensas salir no aplica el pico y placa,"
                          "recuerda que los horarios libres son de 9:30 AM a 4:00 PM y de 9:00 PM a 6:00 AM. Maneja con precaucion" )
                    return
    except:
            print("Oh no, algo salio mal por favor verifica los datos que ingresaste y vuelve a intentar")
            return



def horaNoCircula(hora):

    aux = False
    hora = datetime.strptime(f"{hora}","%X").time()

    hora1 = datetime.strptime("21:00:00", "%X").time() #Horas sin pico y placa
    hora2 = datetime.strptime("06:00:00", "%X").time()
    hora3 = datetime.strptime("09:30:00", "%X").time()
    hora4 = datetime.strptime("16:00:00", "%X").time()


    if(hora>hora1 and hora<hora2):

        aux = True
        return aux
    elif(hora>hora3 and hora<hora4):
        aux = True
        return aux

    return aux





def noCircula(lastNumber):

    numberDay = 0

    if lastNumber == 1 or lastNumber == 2 :

        numberDay = 1

    elif lastNumber == 3 or lastNumber == 4:

        numberDay = 2

    elif lastNumber == 5 or lastNumber == 6:
        numberDay = 3

    elif lastNumber == 7 or lastNumber == 8:
        numberDay = 4

    elif lastNumber == 9 or lastNumber == 0:
        numberDay = 5

    return numberDay


if __name__ == '__main__':

    t = datetime.strptime("1:23","%H:%M")
    print(datetime.strptime("1:25:00", "%X").time())
    print("\n\t\t\t\t*****************************************************")
    print("\t\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t\t*")
    print("\t\t\t\t*\t\tSistema de validacion de pico y placa\t\t*")
    print("\t\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t\t*")
    print("\t\t\t\t*****************************************************\n\n")
    
    
    inputPlaca = input("Por favor ingresa tu placa:\n")
    try:
        placa = int(inputPlaca[len(inputPlaca) - 1]) #ingresar en cualquier formato lo importante es que el ultimo digito sea númerico entero

    except:
        print("Parece que la placa ingresada no es valida, por favor verificala y trata de nuevo.")
        exit()

    inputFecha = input("Por favor ingresa la fecha en la que piensa salir en formato dd-mm-aaaa:\n")
    try:
        formatDate = datetime.strptime(f"{inputFecha}","%d-%m-%Y")  # formato fecha dd-mm-aaa ingresar ejemeplo 15-7-2022
    except:
        print("Parece que la fehca ingresada no es valida, por favor verificala y trata de nuevo.")
        exit()


    inputHora = input("Por favor ingresa la hora en la que piensa salir en formato 24:00\n")
    try:
        inputHora = inputHora + ":00"
        formatHour = datetime.strptime(f"{inputHora}", "%H:%M:%S") #formato hora hh:mm ingresar ejemplo 15:35 no
    except:
        print("Parece que la hora ingresada no es valida, por favor verificala y trata de nuevo.")
        exit()

    PicoyPlaca(placa,formatDate.strftime("%w"),formatHour.strftime("%H:%M:%S"))
    
    