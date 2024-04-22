from datetime import datetime

try:
    now = datetime.now()
    print(now.strftime('%Y-%m-%d'))
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("dia11/logs/error.log", "a+") as log:
        log.seek(0)#posicionate al principio3
        print(log.read())#leer todo
        now = datetime.now()#crea una var llamada now con la fecha actual de ahora ya
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(3)#en byte
        print(log.read(40))#cant de byte a imprimir