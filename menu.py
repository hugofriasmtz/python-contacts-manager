"""Módulo de interfaz de usuario con menús CLI."""


class MainMenu:
    """Clase con métodos estáticos para la interfaz de terminal."""

    # Colores ANSI
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"

    @staticmethod
    def show_main_menu():
        """Muestra el menú principal y retorna la opción seleccionada."""
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}    🌟 "
              f"HUGOFRIASMTZ - PYTHON CONTACTS 🌟{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.YELLOW}1.{MainMenu.END} "
              f"{MainMenu.GREEN}➕ Añadir contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}2.{MainMenu.END} "
              f"{MainMenu.GREEN}📋 Listar contactos{MainMenu.END}")
        print(f"{MainMenu.YELLOW}3.{MainMenu.END} "
              f"{MainMenu.GREEN}🔍 Buscar contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}4.{MainMenu.END} "
              f"{MainMenu.GREEN}✏️  Editar contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}5.{MainMenu.END} "
              f"{MainMenu.RED}❌ Cerrar aplicación{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")

        while True:
            try:
                option = int(input(f"{MainMenu.BOLD}Seleccione una "
                                   f"opción: {MainMenu.END}"))
                if 1 <= option <= 5:
                    return option
                else:
                    print(f"{MainMenu.RED}❌ Opción no válida. "
                          f"Ingrese un número entre 1 y 5."
                          f"{MainMenu.END}")
            except ValueError:
                print(f"{MainMenu.RED}❌ Error: Debe ingresar un "
                      f"número.{MainMenu.END}")

    @staticmethod
    def show_menu_add_contact():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       ➕ "
              f"AÑADIR NUEVO CONTACTO ➕{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def add_contact():
        name = input(f"{MainMenu.BOLD}📝 Ingrese el nombre: {MainMenu.END}")
        email = input(f"{MainMenu.BOLD}📧 Ingrese el correo: {MainMenu.END}")
        phone = input(f"{MainMenu.BOLD}☎️ Ingrese el teléfono: {MainMenu.END}")
        return name, email, phone

    @staticmethod
    def show_menu_all_contacts():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       📋 "
              f"LISTA DE CONTACTOS 📋{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.GREEN}{'Nombre':<15} | {'Correo':<20} | "
              f"{'Teléfono':<12}{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'-'*55}{MainMenu.END}")

    @staticmethod
    def show_menu_search_contact():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       🔍 "
              f"BUSCAR CONTACTO 🔍{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def search_contact():
        email = input(f"{MainMenu.BOLD}📧 Ingrese correo de "
                      f"contacto: {MainMenu.END}")
        return email

    @staticmethod
    def show_menu_update():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       ✏️  "
              f"EDITAR CONTACTO ✏️{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def get_contact_email():
        return input(f"{MainMenu.BOLD}📧 Ingrese correo de "
                     f"contacto: {MainMenu.END}")

    @staticmethod
    def get_contact_data():
        name = input(f"{MainMenu.BOLD}📝 Ingrese nombre de "
                     f"contacto: {MainMenu.END}")
        phone = input(f"{MainMenu.BOLD}☎️  Ingrese teléfono de "
                      f"contacto: {MainMenu.END}")
        return name, phone
