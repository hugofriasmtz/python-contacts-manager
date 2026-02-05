# 📇 Python Contacts Manager

Una aplicación de gestión de contactos desarrollada en Python con interfaz de línea de comandos (CLI) colorida y moderna.

## ✨ Características

- ➕ **Agregar contactos** - Registra nombre, email y teléfono
- 📋 **Listar contactos** - Visualiza todos los contactos guardados
- 🔍 **Buscar contactos** - Encuentra contactos por email
- ✏️ **Editar contactos** - Actualiza la información de tus contactos
- 🎨 **Interfaz colorida** - Terminal con colores ANSI y emojis

## 🚀 Instalación

### Requisitos

- Python 3.10 o superior

### Configuración

```bash
# Clonar el repositorio
git clone https://github.com/hugofriasmtz/python-contacts-manager.git
cd python-contacts-manager

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Ejecutar la aplicación
python main.py
```

## 📖 Uso

Al ejecutar el programa, verás un menú interactivo con las siguientes opciones:

```text
🌟 PYTHON CONTACTS 🌟
═══════════════════════════════════════════════════════════
1. ➕ Añadir contacto
2. 📋 Listar contactos
3. 🔍 Buscar contacto
4. ✏️  Editar contacto
5. ❌ Cerrar aplicación
═══════════════════════════════════════════════════════════
```

### Ejemplos

**Agregar un contacto:**

```text
Seleccione una opción: 1
📝 Ingrese el nombre: Hugo Frías
📧 Ingrese el correo: hugofriasmtz@github.com
☎️  Ingrese el teléfono: 525-538
```

**Buscar un contacto:**

```text
Seleccione una opción: 3
📧 Ingrese correo de contacto: hugofriasmtz@github.com

✅ Contacto encontrado:
─────────────────────────────────────────────────────────
Nombre: Hugo Frías
Email: hugofriasmtz@github.com
Teléfono: 525-538
─────────────────────────────────────────────────────────
```

## 🏗️ Estructura del Proyecto

```text
proyecto/
│
├── main.py          # Punto de entrada de la aplicación
├── contacts.py      # Lógica de gestión de contactos
├── menu.py          # Interfaz de usuario (menús y prompts)
└── README.md        # Documentación
```

## 🧩 Arquitectura

El proyecto utiliza **Programación Orientada a Objetos** con los siguientes componentes:

- **`BaseClass`** - Clase base con operaciones CRUD de contactos
- **`Contacts`** - Hereda de BaseClass y expone métodos públicos
- **`MainMenu`** - Clase con métodos estáticos para la interfaz de usuario

### Conceptos POO Aplicados

- ✅ Herencia (`Contacts` hereda de `BaseClass`)
- ✅ Encapsulamiento (separación de lógica y presentación)
- ✅ Métodos de clase (`@classmethod`)
- ✅ Métodos estáticos (`@staticmethod`)

## 🎨 Personalización

Los colores de la interfaz se pueden modificar en `menu.py`:

```python
class MainMenu:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Desarrollado por

Hugo Frias

[![GitHub](https://img.shields.io/badge/GitHub-hugofriasmtz-181717?style=for-the-badge&logo=github)](https://github.com/hugofriasmtz)

---

### ⭐ ¿Te gustó el proyecto?

Si este proyecto te fue útil, considera darle una estrella ⭐

Hecho con ❤️ y Python 🐍
