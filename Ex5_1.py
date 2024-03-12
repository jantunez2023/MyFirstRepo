#Printing out Total, count and avergae

#Initializig variables
suma = 0
contador = 0

user_data = input ("Hello! I will help u to count and calculate average. Type Done to end entering numbers. Enter a number:")
if user_data == "done" :
    print ("Total: ", suma, " Counter: ", contador)

else :
    while user_data != "done" :

        try :
             user_data = float (user_data)
             contador = contador + 1
             suma = suma + user_data
             user_data = input ("Enter a number:")
        except:
             print ("Invalid input. Number was expected: ", user_data)
             user_data = input ("Enter a number:")
             if user_data == "done" :
                 if contador == 0:
                    print ("Total: ", suma, " Counter: ", contador)
                    quit()
                 else :
                     print ("Total: ", suma, " Counter: ", contador, "Average:", suma/contador)
                     quit()
    print ("Total: ", suma, " Counter: ", contador, " Average:", suma/contador)
