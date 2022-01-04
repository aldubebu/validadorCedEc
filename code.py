ced = input("Ingrese numero de cedula: ")
if len(ced)== 10:
    if ced.isnumeric():
        codp = int(ced[0:2])
        if codp > 0 and codp < 25:
            SPI = 0
            SPP = int(ced[1]) + int(ced[3]) + int(ced[5]) + int(ced[7])
            for i in range(0,9,2):
                if ((int(ced[i])*2) > 9):
                   SPI = SPI + ((int(ced[i])*2)-9)
                else:
                   SPI = SPI + (int(ced[i])*2)   
            ST = SPP + SPI
            if ST % 10 == 0:
                UD = 0
            else:
                DS = (ST - (ST % 10)) + 10
                UD = DS - ST
            if UD == int(ced[9]): 
                print("Numero de cedula es correcto")
                #Aqui determinar a q provincia pertenece

                province = ["", "Pertenece a la provincia de Azuay", "Pertenece a la provincia de Bolivar", "Pertenece a la provincia de Cañar", "Pertenece a la provincia de Carchi", "Pertenece a la provincia de Cotopaxi", "Pertenece a la provincia de Chimborazo", "Pertenece a la provincia de El Oro", "Pertenece a la provincia de Esmeraldas", "Pertenece a la provincia de Guayas", "Pertenece a la provincia de Imbabura", "Pertenece a la provincia de Loja", "Pertenece a la provincia de Los Rios", "Pertenece a la provincia de Manabi", "Pertenece a la provincia de Morona Santiago", "Pertenece a la provincia de Napo", "Pertenece a la provincia de Pastaza", "Pertenece a la provincia de Pichincha", "Pertenece a la provincia de Tungurahua", "Pertenece a la provincia de Zamora Chinchipe", "Pertenece a la provincia de Galapagos", "Pertenece a la provincia de Sucumbios", "Pertenece a la provincia de Orellana", "Pertenece a la provincia de Santo Domingo de los Tsachilas", "Pertenece a la provincia de Santa Elena"]
                print("Este numero ",province[codp])

            else:
                print("Numero de cedula incorrecto")    
        else:
            print("Error los dos primeros digitos no corresponden a una provincia")    
    else:
        print("El valor ingresado no es valido. Debe ingresar numeros")    
else:
    print("El valor ingresado no tiene 10 digitos")