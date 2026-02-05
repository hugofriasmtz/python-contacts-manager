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
    def showMainMenu():
        """Muestra el menú principal y retorna la opción seleccionada."""
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}    🌟 HUGOFRIASMTZ - PYTHON CONTACTS 🌟{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.YELLOW}1.{MainMenu.END} {MainMenu.GREEN}➕ Añadir contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}2.{MainMenu.END} {MainMenu.GREEN}📋 Listar contactos{MainMenu.END}")
        print(f"{MainMenu.YELLOW}3.{MainMenu.END} {MainMenu.GREEN}🔍 Buscar contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}4.{MainMenu.END} {MainMenu.GREEN}✏️  Editar contacto{MainMenu.END}")
        print(f"{MainMenu.YELLOW}5.{MainMenu.END} {MainMenu.RED}❌ Cerrar aplicación{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        
        while True:
            try:
                option = int(input(f"{MainMenu.BOLD}Seleccione una opción: {MainMenu.END}"))
                if 1 <= option <= 5:
                    return option
                else:
                    print(f"{MainMenu.RED}❌ Opción no válida. Ingrese un número entre 1 y 5.{MainMenu.END}")
            except ValueError:
                print(f"{MainMenu.RED}❌ Error: Debe ingresar un número.{MainMenu.END}")

    @staticmethod
    def showMenuAddContact():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       ➕ AÑADIR NUEVO CONTACTO ➕{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def addContact():
        name = input(f"{MainMenu.BOLD}📝 Ingrese el nombre: {MainMenu.END}")
        email = input(f"{MainMenu.BOLD}📧 Ingrese el correo: {MainMenu.END}")
        phone = input(f"{MainMenu.BOLD}☎️  Ingrese el teléfono: {MainMenu.END}")
        return name, email, phone

    @staticmethod
    def showMenuAllContacts():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       📋 LISTA DE CONTACTOS 📋{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.GREEN}{'Nombre':<15} | {'Correo':<20} | {'Teléfono':<12}{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'-'*55}{MainMenu.END}")

    @staticmethod
    def showMenuSearchContact():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       🔍 BUSCAR CONTACTO 🔍{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def searchContact():
        email = input(f"{MainMenu.BOLD}📧 Ingrese correo de contacto: {MainMenu.END}")
        return email

    @staticmethod
    def showMenuUpdate():
        print(f"\n{MainMenu.CYAN}{'='*55}{MainMenu.END}")
        print(f"{MainMenu.BLUE}{MainMenu.BOLD}       ✏️  EDITAR CONTACTO ✏️{MainMenu.END}")
        print(f"{MainMenu.CYAN}{'='*55}{MainMenu.END}\n")

    @staticmethod
    def getContactEmail():
        return input(f"{MainMenu.BOLD}📧 Ingrese correo de contacto: {MainMenu.END}")

    @staticmethod
    def getContactData():
        name = input(f"{MainMenu.BOLD}📝 Ingrese nombre de contacto: {MainMenu.END}")
        phone = input(f"{MainMenu.BOLD}☎️  Ingrese teléfono de contacto: {MainMenu.END}")
        return name, phone