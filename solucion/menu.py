def turistas_por_pais(pais):
    encontrados = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    print(encontrados if encontrados else "No hay turistas de ese pais.")

def turistas_por_mes(mes):
    total = len(turistas)
    if total == 0:
        return 0.0
    contador = sum(1 for datos in turistas.values() if int(datos[2].split("-")[1]) == mes)
    return round((contador / total) * 100, 1)

def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar: ")
    for id_turista, datos in list(turistas.items()):
        if datos[0].lower() == nombre.lower():
            del turistas[id_turista]
            print("Turista eliminado con éxito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")

def mostrar_menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")
        
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            pais = input("Ingrese pais a buscar: ")
            turistas_por_pais(pais)
        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese mes a buscar: "))
                    if 1 <= mes <= 12:
                        print(f"El número de turistas equivale al {turistas_por_mes(mes)} % del total.")
                        break
                    print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Debe ingresar un número válido.")
        elif opcion == "3":
            eliminar_turista()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    mostrar_menu()