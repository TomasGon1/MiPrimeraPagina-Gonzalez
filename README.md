# Proyecto Django - CompraGamer

Este proyecto es una pequeña aplicación web desarrollada con **Django** que permite:
🔹 Videojuegos
1. Cargar información de videojuegos mediante un formulario.
2. Listar todos los videojuegos cargados y hacer una busqueda por nombre, categoria o desarrollador.
3. Navegar entre las distintas páginas usando rutas definidas en `urls.py`.
4. Ver detalle de un videojuego.
5. Actualizar y eliminar videojuegos (solo usuarios logueados).
6. Cargar una imagen opcional para cada videojuego.

🔹 Usuarios
1. Registro de usuarios.
2. Login / Logout de usuarios registrados.
3. Perfil de usuario con posibilidad de:
   • Actualizar datos personales.
   • cambiar contraseña.
---

## Estructura principal

- **`inicio/forms.py`**  
  Contiene los formularios relacionados con videojuegos:
  • FormularioVideojuegos → para cargar un nuevo videojuego.
  • FormularioBuscarVideojuego → para buscar videojuegos en el listado.
  • VideojuegoActualizar (ModelForm) → para editar un videojuego existente.

- **`inicio/models.py`**  
  Define el modelo `Videojuegos` con los siguientes campos:
  • nombre
  • desarrollador
  • descripcion (por defecto "Sin descripción")
  • categoria
  • fecha_lanzamiento
  • imagen (opcional)

- **`inicio/views.py`**  
  Contiene las vistas:
  - `inicio`: página principal.
  - `cargar_juego`: muestra y procesa el formulario para agregar un videojuego.
  - `listado_de_juegos`: lista todos los videojuegos guardados.
  - `detalle_juego`: Ver detalle de un videojuego.
  - `BorrarJuego`: Vista genérica para eliminar.
  - `ActualizarJuego`: Vista genérica para editar.
  - `acerca_de_mi`: Página de presentación.

- **`inicio/urls.py`**  
  - `/` → Vista `inicio`
  - `juegos/` → Vista `listado_de_juegos`
  - `juegos/cargar/` → Vista `cargar_juego`
  - `juegos/<int:id_juego>/` → Vista `detalle_juego`
  - `juegos/<int:pk>/borrar` → Clase como vista `borrar_juego` 
  - `juegos/<int:pk>/actualizar` → Clase como vista `actualizar_juego`
  - `acerca_de_mi/` → Vista `acerca_de_mi`

- **Templates (HTML)**  
  - `inicio.html`: página principal.  
  - `cargar_juego.html`: formulario de carga.  
  - `listado_de_juegos.html`: lista de videojuegos.
  - `detalle_juego.html`: detalle del videojuego.
  - `borrar_juego.html`: borrar videojuego.
  - `actualizar_juego.html`: actualizar los campos del videojuego.
  - `acerca_de_mi.html`: pagina con breve precentacion.

- **usuarios/forms.py**
  - `FormularioRegistro` → Registro de usuarios.
  - `FormularioLogin` → Inicio de sesión.
  - `FormularioActualizacion` → Actualizar datos del usuario.
  - `FormularioNuevaContraseña` → Cambio de contraseña.

- **usuarios/forms.py**
  - `login_view`: Iniciar sesión.
  - `register_view`: Registro de usuario.
  - `profile_view`: Página de perfil.
  - `update_data`: Actualizar datos y contraseña.

- **`usuario/urls.py`** 
  - `login/` → Vista `login`
  - `register/` → Vista `register`
  - `logout/` → Clase como vista `logout`
  - `profile/` → Vista `profile`
  - `update_data/` → Vista `update_data`

- **Templates (HTML)**
  - `login.html`: página para iniciar sesion.
  - `logout.html`: Vista de confirmacion de logout.
  - `profile.html`: Perfil del usuario.
  - `register.html`: página para registrar un usuario nuevo.
  - `update_data.html`: página para actualizar los datos y la contraseña del usuario.

---

## Orden para probar la aplicación

1. **Ejecutar el servidor**  
  • Utilizar: python manage.py runserver

2. **Ingresar a la pgina de Inicio**
  • Yendo a: http://127.0.0.1:8000/

3. **Registrar un usuario**
  • Yendo a: /usuarios/register/
  • Completar el formulario de registro.

4. **Inisiar sesion**
  • Yendo a: /usuarios/login/
  • Completar el formulario de inicio de sesion.

5. **Cargar una videojuego**
  • Yendo a /cargar/juego/, completar formulario y enviar.

6. **Listar los videojuegos**
  • Yendo a /juegos/ para ver todos los videojuegos (y usar buscador).

7. **Visualizar los detalles**
  • yendo a /juegos/(id_juego)

8. **Editar o eliminar**
  • Desde el listado acceder a editar o borrar un juego.  

9. **Perfil de usuario**
  • Yendo a /usuarios/profile/ para visualizar, actualizar datos o cambiar contraseña.
    

