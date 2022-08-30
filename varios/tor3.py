import turtle
def arriba(): 
    flecha.setheading(90) 
    flecha.forward(100)

def derecha(): 
    flecha.setheading(0) 
    flecha.forward(100)

def abajo(): 
    flecha.setheading(270) 
    flecha.forward(100)

def izquierda(): 
    flecha.setheading(180) 
    flecha.forward(100)

if __name__ == "__main__":
    ventana = turtle.Screen()
    flecha = turtle.Turtle() 
    ventana.onkeypress(arriba, "w") 
    ventana.onkeypress(derecha, "Right") 
    ventana.onkeypress(abajo, "Down") 
    ventana.onkeypress(izquierda, "Left") 
    ventana.listen()
    ventana.mainloop()