
contactos = {}

def agregar_contacto():
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    contactos[nombre] = telefono
    print("Contacto guardado.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos.")
    else:
        print("\n--- CONTACTOS ---")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")

def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip()
    if nombre in contactos:
        print(f"Teléfono: {contactos[nombre]}")
    else:
        print("No encontrado.")

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado.")
    else:
        print("No encontrado.")

def main():
    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Adiós")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()