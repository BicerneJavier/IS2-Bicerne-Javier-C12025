# 📚 Sistema de Gestión de Biblioteca

Este proyecto es un **sistema de gestión de biblioteca** simple desarrollado en **Python**, que permite administrar las operaciones fundamentales de una biblioteca: registro de libros, autores, socios y gestión de préstamos.  

El sistema sigue una **arquitectura de 3 capas** para separar responsabilidades y mejorar la mantenibilidad y escalabilidad.

### 🏛️ <u>Características Principales</u>:

- **Gestión de Autores**: Registrar, listar y eliminar autores.  
- **Gestión de Categorías**: Registrar, listar y eliminar categorías de libros.  
- **Gestión de Libros**: Registrar, listar todos los libros o solo los disponibles, y eliminar libros.  
- **Gestión de Socios**: Registrar, listar todos los socios o solo los activos, activar y desactivar socios.  
- **Gestión de Préstamos**:  
  - Prestar y devolver libros.  
  - Listar todos los préstamos, los activos y por socio.  
  - Ver información detallada de un préstamo.  
- **Validaciones de Negocio**:  
  - No se puede eliminar un autor o categoría con libros asociados.  
  - No se puede eliminar un libro con préstamos activos.  
  - No se puede prestar un libro no disponible o a un socio inactivo.  
  - No se puede desactivar un socio con préstamos pendientes.  

### 🏗️ <u>Arquitectura del Proyecto</u>:

El sistema está organizado en **tres capas principales**:

### 1️⃣ Capa de Presentación (`src/UI`)
- Interfaz de usuario **consola**.  
- Contiene el menú principal y los submenús.  
- Se encarga de recibir entradas del usuario y mostrar resultados.  

### 2️⃣ Capa de Lógica de Negocio (`src/Negocio`)
- `bibliotecaService.py` es el núcleo del sistema.  
- Contiene todas las **reglas de negocio** y coordina operaciones entre la UI y la capa de datos.  
- Valida consistencia, como que un socio activo pueda tomar libros prestados.

### 3️⃣ Capa de Datos (`src/Datos`)
- **Entidades**: Clases que modelan objetos del dominio (`Autor`, `Libro`, `Socio`, `Categoria`, `Prestamo`).  
- **Gestores**: Administran las colecciones de entidades en memoria.
- Los gestores (`GestorAutores`, `GestorCategorias`, `GestorLibros`, `GestorSocios`, `GestorPrestamos`) heredan de `GestorBase`. 
- Utilizan el **patrón Singleton** para mantener un estado único de los datos.
- Para el problema de **acceso centralizado** a los datos, donde múltiples partes del sistema podrían necesitar acceder y manipular la misma información (autores, libros, socios,categorias o prestamos)                      el patrón Singleton es una solución ideal.
- El patrón Singleton garantiza que una clase tenga una **única instancia** en toda la aplicación y proporciona un punto de acceso global a ella.
- Aplicado a este sistema, cada clase Gestor podría ser un Singleton. Esto aseguraría que, sin importar qué parte del código necesite la lista de autores, siempre accederá a la misma y única instancia del gestor de         autores. Esto evita tener múltiples objetos gestores que puedan tener datos inconsistentes entre sí, centralizando el manejo de los datos y ahorrando memoria.
  
### 📁 <u>Estructura de Carpetas</u>:
```
.
├── docs/
│   ├── Diagrama de Entidades.PNG
│   └── Diagrama de Clases.PNG
│
├── src/
│   ├── Datos/
│   │   ├── Entidades/
│   │   └── Gestores/   
│   ├── Negocio/
│   │   
│   └── UI/
└── tests/
    ├── test_bibliotecaService.py
    └── test_gestores.py
```
- **`docs/`**: Contiene la documentación visual del proyecto, como el diagrama de entidades y el diagrama de clases.
- **`src/`**: Contiene el código fuente de la aplicación, separado en las tres capas.
- **`tests/`**: Contiene las pruebas unitarias para verificar el correcto funcionamiento del sistema.

### 🚀 <u>Cómo usar la biblioteca</u>:

### Requisitos
- Python 3.x

### Ejecutar la Aplicación
Para iniciar el sistema de gestión de biblioteca, ejecuta el siguiente comando desde el directorio raíz del proyecto:

```bash
python -m src.UI.main
```
Esto cargará automáticamente los datos iniciales (**`datos_iniciales.py`**) y permitirá interactuar con el menú.

### Ejecutar las Pruebas Unitarias
Para verificar la integridad y el correcto funcionamiento de la lógica de negocio y los gestores de datos, puedes ejecutar las pruebas unitarias.

- **Ejecutar todas las pruebas:**
  ```bash
  python -m unittest discover -s tests -p "*.py"
  ```

- **Ejecutar un conjunto de pruebas específico:**
  ```bash
  # Para las pruebas del servicio principal
  python -m unittest tests.test_bibliotecaService
  ```
  ```bash
  # Para las pruebas de los gestores de datos
  python -m unittest tests.test_gestores
  ```

### 💡 <u>Extensibilidad</u>:

- Para **agregar nuevas entidades**, crear la clase en `Datos/Entidades` y el gestor correspondiente en `Datos/Gestores`.  
- Para **nuevas validaciones**, agregarlas en `bibliotecaService.py`.  
- La **UI** puede expandirse agregando submenús en `main.py`.  

### ⚙️ <u>Tecnologías</u>:

- Lenguaje de Programación: **Python 3.x**
- Patrón Arquitectonico: **Arquitectura de 3 Capas**
- Patrón de Diseño: **Singleton** para Gestores  
- Tests: módulo `unittest`  

### 📝 <u>Licencia</u>:

Este proyecto es un **TP** de **Ingenieria de Software 2** para la **UNPAZ** y puede adaptarse para otros fines según las necesidades.
