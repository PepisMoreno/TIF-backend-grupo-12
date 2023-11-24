#antes de todo o más bien, transversalmente, habría que poner unos botones para volver para atrás, volver al inicio, tal vez un iframe para buscar info en internet en la misma página...
#también, no sé bien dónde, pero habría que agregar un loop que cuando se equivoquen de opción vuelva a hacer la pregunta, supongo que con un while...
def error():
    print("revisá por favor la opción ingresada.")

def eleccion():
    print ("ingresá el número de opción que decidiste:  ")

def mas_info(): 
    print ("Te dejamos aquí abajo más información acerca de dichos especímenes! ")

def chau():
    print ("Nos alegramos un montón. Nos vemos la próxima!!")

decision=input(eleccion)
if decision=="1":
    print ("Espectacular, avancemos entonces!")
elif decision=="2":
    chau
else:
    error
          

def continuar_indagando():
    continua_o_no=input("querés que sigamos indagando? hay muchas clases de esta planta y la familia no se acaba aquí!")
    if continua_o_no== "sí" or continua_o_no=="si":
        print (" Genial, sigamos indagando!")
        pass
    elif continua_o_no=="no" or continua_o_no=="No":
        print ("Ok, esperamos hayas encontrado lo que necesitabas!")
    else:
        error
        
         





print("hola, cómo estás? Bienvenido a este identificador de plantas :)")

inicio=input("Te vamos a hacer algunas preguntas para ir despejando opciones. Te animás?  ")

if inicio=="no" or inicio =="NO" or inicio=="No":
        print("Ok, te esperamos cuando tengas ganas de hacerlo!")

elif inicio=="si" or inicio== "sí" or inicio=="SI" or inicio== "SÍ" or inicio=="Sí":
        print("de acuerdo, empecemos!")

        #continuar preguntando

        print("Entonces...tenés una planta que querés identificar. cuál de estas dos condiciones es más similar al aspecto general de tu planta?")

        print("1. mi planta está pegada al piso o a alguna superficie, tiene poca altura")

        print ("2. mi planta tiene tallo, raíces y/o hojas" )

        briofita_o_cormofita=input(eleccion)
        if briofita_o_cormofita=="1":
            print ("genial! tu planta corresponde a la familia de briofitas, plantas prehistóricas")
            #acá habría que linkearlo con la hoja donde está la clase plantas, para que diga las principales características de la misma.
            mas_info            
            #acá habría que poner algo como un link que vaya a algún lugar que hable de las plantas briofitas. 
        elif briofita_o_cormofita=="2":
            print ("tu planta pertenece al orden de las cormófitas, la mayor variedad de plantas que existe.")
            #acá link con hoja de clase plantas para caract. principales.

            continuar_indagando() 
            decision
        
            print ("decinos:  a tu planta alguna vez le viste si tiene semillas, flores y/o frutos?")
            print ("1. No tiene ni tuvo semillas, ni flores, ni frutos")
            print ("2. Tuvo o tiene semillas y/o flores y/o frutos")
            pteridofita_o_espermatofita=input(eleccion )
            if pteridofita_o_espermatofita=="1":
                print ("Mirá vos, tu planta sin nada de eso pertenece a las pteridófitas. ")
                #acá poner link a clase plantas.
                mas_info
            elif pteridofita_o_espermatofita=="2":
                print ("Mirá vos! Tu planta, si tiene flor o fruto o semilla, pertenece a las espermatófitas")
                #acá poner link a clase plantas.
                continuar_indagando()
                decision
                print("bueno, ahora contanos, tu planta tuvo o tiene flores vistosas, o por ahí frutos? o tiene flores más bien pequeñas, que pasan desapercibidas, donde lo que más se ve son las semillas?")
                print("1. No parece tener flores vistosas, sí semillas")
                print("2. Tiene unas flores espectaculares, o bien, tiene frutos y flores que se diferencian bastante de las hojas")                
            gimnospermas_o_angiospermas=input(eleccion)
            if gimnospermas_o_angiospermas=="1":
                print("muy bien, entonces tu planta es una Gimnosperma, puede ser desde un pino hasta un gingko biloba, generalmente árboles y de áreas templadas o frías")
                #aca link a la clase gimnosperma
            elif gimnospermas_o_angiospermas=="2":
                print("tu planta entonces es una angiosperma, la mayor variedad de plantas terrestres que existe. Podría ser desde un diente de león hasta un jacarandá...")
                #acá poner link a la clase angiosperma.
                continuar_indagando()
                decision
                print("ya estamos en la recta final! Ya sabemos que tu planta es vascular, espermatófita, angiosperma... ahora vamos a definir si es dicotiledónea o monocotiledónea. Cuál de estos enunciados es correcto?")
                print("1. Mi planta tiene flores de 3 pétalos o múltiplos de 3")
                print("2. Mi planta tiene flores de 4 o 5 pétalos o múltiplos de 4 o 5")
            monocotiledoneas_o_dicotiledoneas=input(eleccion)
            if monocotiledoneas_o_dicotiledoneas=="1":
                print("Tu planta es una monocotiledónea. No posee cambium en su tronco, lo que hace que sus tallos sean poco leñosos. Posee solo un cotiledón (hojita que protege a la semilla)")
                #link clase monocotiledonea
            elif monocotiledoneas_o_dicotiledoneas=="2":
                print("Tu planta es una dicotiledónea, lo más top de lo top en materia vegetal. Podría ser desde un roble hasta una margarita, pero por ser de esta clase su tronco puede ser leñoso. ")
                #link clase dicotiledónea
else:
    error()
print("Gracias por utilizar el identificador de plantas!")

#usar parametros opcionales (lo mas choto ultimo)
#armar un objeto, para devolver varios valores, encapsular parámetros ahi)
