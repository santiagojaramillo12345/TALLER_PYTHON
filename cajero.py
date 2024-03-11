def registrar():
    print("Ingrese la siguiente información:")
    identificacion = input("Ingrese su identificación: ")
    usuario = input("Ingrese su usuario: ")
    x = 0
    while x == 0:
        correo = input("Ingrese su correo electrónico: ")
        if "@" in correo:
            print("Correo válido")
            break
        else:
            print("Correo no válido")
    
    clave= input("Ingrese su correo electrónico: ")
    return identificacion, usuario, correo

identificacion, usuario, correo = registrar()

def iniciar(identificacion, usuario, correo):
    print("iniciar sesion")
    
    i=0
    user=input("digite su usuario")
    while i<=3 :
        if user==usuario:
            