"""Módulo de gestión de contactos."""


class BaseClass:
    """Clase base para operaciones CRUD de contactos."""
    
    contacts = []

    def add_contact(self, name, email, phone):
        """Agrega un nuevo contacto a la lista."""
        user_data = {"name": name, "email": email, "phone": phone}
        self.contacts.append(user_data)

    def update_contact(self, email, name, phone):
        """Actualiza un contacto existente."""
        contact = self.search_contact(email)
        if contact is not None:
            contact["name"] = name
            contact["phone"] = phone
            return True
        return False

    @classmethod
    def search_contact(cls, email):
        """Busca un contacto por email."""
        for contact in cls.contacts:
            if contact["email"] == email:
                return contact
        return None

    @classmethod
    def all_contacts(cls):
        """Retorna todos los contactos."""
        return cls.contacts


class Contacts(BaseClass):
    """Interfaz pública para gestionar contactos."""

    def add(self, name, email, phone):
        """Añade un contacto."""
        self.add_contact(name, email, phone)

    def show_all_contacts(self):
        """Muestra todos los contactos en formato legible."""
        contacts = self.all_contacts()
        for contact in contacts:
            print(f"{contact['name']} - {contact['email']} - {contact['phone']}")

    def search(self, email):
        """Busca un contacto por email."""
        return self.search_contact(email)

    def update(self, email, name, phone):
        """Actualiza un contacto existente."""
        return self.update_contact(email, name, phone)