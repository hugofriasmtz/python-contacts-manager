"""
Aplicación de gestión de contactos con interfaz CLI.

Permite agregar, listar, buscar y editar contactos.
"""
from contacts import Contacts
from menu import MainMenu


if __name__ == "__main__":
    contacts = Contacts()

    while True:
        option = MainMenu.show_main_menu()

        match (option):
            case 1:  # Añadir contacto
                MainMenu.show_menu_add_contact()
                name, email, phone = MainMenu.add_contact()
                contacts.add(name, email, phone)

            case 2:  # Listar contactos
                MainMenu.show_menu_all_contacts()
                contacts.show_all_contacts()

            case 3:  # Buscar contacto
                MainMenu.show_menu_search_contact()
                email = MainMenu.search_contact()
                contact = contacts.search(email)
                if contact:
                    print(f"\n{MainMenu.GREEN}✅ Contacto "
                          f"encontrado:{MainMenu.END}")
                    print(f"{MainMenu.CYAN}{'─'*55}{MainMenu.END}")
                    print(f"{MainMenu.YELLOW}Nombre:{MainMenu.END} "
                          f"{contact['name']}")
                    print(f"{MainMenu.YELLOW}Email:{MainMenu.END} "
                          f"{contact['email']}")
                    print(f"{MainMenu.YELLOW}Teléfono:{MainMenu.END} "
                          f"{contact['phone']}")
                    print(f"{MainMenu.CYAN}{'─'*55}{MainMenu.END}")
                else:
                    print(f"{MainMenu.RED}❌ El contacto no existe"
                          f"{MainMenu.END}")

            case 4:  # Editar contacto
                # Muestra el encabezado del menú de edición
                MainMenu.show_menu_update()
                # Muestra el encabezado de la lista de contactos
                MainMenu.show_menu_all_contacts()
                # Lista todos los contactos para que el usuario pueda
                # ver cuál editar
                contacts.show_all_contacts()
                # Solicita el email del contacto a editar
                email = MainMenu.search_contact()
                # Busca el contacto por email
                contact = contacts.search(email)
                # Verifica si el contacto existe
                if contact:
                    # Solicita los nuevos datos (nombre y teléfono)
                    name, phone = MainMenu.get_contact_data()
                    # Actualiza el contacto con los nuevos datos
                    resp = contacts.update(contact["email"], name,
                                           phone)
                    # Muestra mensaje de confirmación en color verde
                    print(f"{MainMenu.GREEN}✅ Contacto actualizado "
                          f"exitosamente{MainMenu.END}")

            # Caso 5: Cerrar la aplicación
            case 5:
                # Muestra el borde superior del mensaje de despedida
                # en cian
                print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
                # Muestra el mensaje de despedida en azul con
                # negritas
                print(f"{MainMenu.BLUE}{MainMenu.BOLD}👋 ¡Hasta luego! "
                      f"Gracias por usar la app 👋{MainMenu.END}")
                # Muestra el borde inferior del mensaje de despedida
                print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")
                # Sale del bucle while y termina el programa
                break
