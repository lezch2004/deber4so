
num_procesos = 0 
num_recursos = 0 
lista_recursos = []
max_procesos = []
lista_asignados = []

def run_config():
    while(True):
        num_procesos = input("\nIngresa el número de procesos: ")
        try: 
            if (int(num_procesos) > 0):
                num_procesos = int(num_procesos)
                break
            else: 
                print("Error! Debe ser un número entero mayor a 0!")
                continue
        except: 
            print("Error! Debe ser un número entero mayor a 0!")

    while(True):
        num_recursos = input("\nExcelente! \nAhora ingresa el número de recursos en el sistema: ")
        try: 
            if (int(num_recursos) > 0):
                num_recursos = int(num_recursos)
                break
            else: 
                print("Error! Debe ser un número entero mayor a 0!")
                continue
        except: 
            print("Error! Debe ser un número entero mayor a 0!")

    print("\nPerfecto! \nAhora ingresa la cantidad disponible total de cada recurso!")

    for i in range (1, num_recursos+1): 
        while(True):
            entry = input(f"\nRecurso {i}: ")
            try: 
                if (int(entry) > 0):
                    lista_recursos.append(int(entry))
                    break
                else: 
                    print("Error! Debe ser un número entero mayor a 0!")
                    print("Ingresa la cantidad disponible total del recurso!")
                    continue
            except: 
                print("Error! Debe ser un número entero mayor a 0!")
                print("Ingresa la cantidad disponible total del recurso!")    

    print("\n**** Resumen disponibilidad por recurso: ****")
    for i in range (1, num_recursos+1): 
        print(f"Recurso {i}: {lista_recursos[i-1]}") 

    print ("\nYa falta poco! Ahora ingresa cuanto de cada recurso necesitan todos los procesos:")
    for i in range (1, num_procesos+1): 
        print ("\nIngresa la cantidad que requiere el proceso para cada recurso!")
        print (f"**** Proceso {i} ****")
        recursos = []
        for k in range (1, num_recursos+1): 
            while(True):
                entry = input(f"\n  Recurso {k}: ")
                try: 
                    if (int(entry) >= 0):
                        recursos.append(int(entry))
                        #print(recursos)
                        break
                    else: 
                        print("Error! Debe ser un número entero positivo!")
                        print(f"Ingresa la cantidad necesaria del recurso por el proceso {i}!")
                        continue
                except: 
                    print("Error! Debe ser un número entero positivo!")
                    print(f"Ingresa la cantidad necesaria del recurso por el proceso {i}!")
        max_procesos.append(recursos.copy())
        recursos.clear()


    print("\n**** Resumen necesidad por proceso: ****")
    for i in range (1, num_procesos+1): 
        print(f"\nProceso {i}: ") 
        for k in range (1, num_recursos+1): 
            print(f"    Recurso {k}: {max_procesos[i-1][k-1]}") 


    print ("\nUn requisito más! Ingresa cuanto de cada recurso ya ha sido asignado a los procesos:")
    print ("Recuerda que la alocación de un recurso no puede superar al total disponible!")
    aux_lista_recursos = lista_recursos.copy()
    for i in range (1, num_procesos+1): 
        print ("\nIngresa la cantidad asignada por recurso de cada proceso!")
        print (f"**** Proceso {i} ****")
        asignados = []
        for k in range (1, num_recursos+1): 
            while(True):
                entry = input(f"\n  Recurso {k}: ")
                try:
                    valor = int(entry)
                    if valor < 0:
                        print("Error! Debe ser un número entero positivo!")
                        print(f"Ingresa la cantidad ya asignada del recurso al proceso {i}!")
                    elif valor > max_procesos[i-1][k-1]:
                        print(f"Error! No puede superar el máximo del proceso ({max_procesos[i-1][k-1]})!")
                        print(f"Ingresa la cantidad ya asignada del recurso al proceso {i}!")
                    elif valor > aux_lista_recursos[k-1]:
                        print(f"Error! No hay suficientes recursos disponibles (quedan {aux_lista_recursos[k-1]})!")
                        print(f"Ingresa la cantidad ya asignada del recurso al proceso {i}!")
                    else:
                        asignados.append(valor)
                        aux_lista_recursos[k-1] -= valor
                        break
                except:
                    print("Error! Debe ser un número entero positivo!")
                    print(f"Ingresa la cantidad ya asignada del recurso al proceso {i}!")
        lista_asignados.append(asignados.copy())
        asignados.clear()

    print("\n**** Resumen asignados por proceso: ****")
    for i in range (1, num_procesos+1): 
        print(f"\nProceso {i}: ") 
        for k in range (1, num_recursos+1): 
            print(f"    Recurso {k}: {lista_asignados[i-1][k-1]}") 
    
    print("Enhorabuena! Ahora estamos listos para simular!")
    return num_procesos, num_recursos, lista_recursos, max_procesos, lista_asignados


def run_banquero(num_procesos, num_recursos, lista_recursos, max_procesos, lista_asignados):

    # ---- Calcular Need ----
    need = []
    for i in range(num_procesos):
        need_proceso = []
        for k in range(num_recursos):
            need_proceso.append(max_procesos[i][k] - lista_asignados[i][k])
        need.append(need_proceso)

    # ---- Calcular Available ----
    available = lista_recursos.copy()
    for i in range(num_procesos):
        for k in range(num_recursos):
            available[k] -= lista_asignados[i][k]

    print("\n**** Resumen Need por proceso: ****")
    for i in range(num_procesos):
        print(f"\n  Proceso {i+1}:")
        for k in range(num_recursos):
            print(f"    Recurso {k+1}: {need[i][k]}")

    print(f"\n**** Available inicial: ****")
    for k in range(num_recursos):
        print(f"  Recurso {k+1}: {available[k]}")

    # ---- Algoritmo del banquero ----
    terminados = [False] * num_procesos
    secuencia = []

    for _ in range(num_procesos):
        encontrado = False
        for i in range(num_procesos):
            if terminados[i]:
                continue
            puede = True
            for k in range(num_recursos):
                if need[i][k] > available[k]:
                    puede = False
                    break
            if puede:
                print(f"\n  → Proceso {i+1} puede ejecutarse (Need ≤ Available)")
                for k in range(num_recursos):
                    available[k] += lista_asignados[i][k]
                terminados[i] = True
                secuencia.append(i+1)
                encontrado = True
                print(f"    Available actualizado: {available}")
                break

        if not encontrado:
            break

    # ---- Resultado ----
    print("\n" + "="*50)
    if all(terminados):
        print("✅ ESTADO SEGURO")
        print("Secuencia segura: " + " → ".join([f"P{p}" for p in secuencia]))
    else:
        print("❌ ESTADO INSEGURO - posible deadlock")
        procesos_bloqueados = [i+1 for i in range(num_procesos) if not terminados[i]]
        print(f"Procesos bloqueados: {procesos_bloqueados}")
    print("="*50)

def main():
    print("******** Bienvenido al algoritmo del banquero! ********")
    num_procesos, num_recursos, lista_recursos, max_procesos, lista_asignados = run_config()
    run_banquero(num_procesos, num_recursos, lista_recursos, max_procesos, lista_asignados)
    


main()