# Proyecto Django - CompraGamer

Este proyecto es una pequeña aplicación web desarrollada con **Django** que permite:
1. Cargar información de videojuegos mediante un formulario.
2. Listar todos los videojuegos cargados.
3. Navegar entre las distintas páginas usando rutas definidas en `urls.py`.

---

## Estructura principal

- **`inicio/forms.py`**  
  Contiene el formulario `FormularioVideojuegos` que define los campos:  
  - `nombre`
  - `desarrollador`
  - `categoria`
  - `fecha_lanzamiento`  

- **`inicio/models.py`**  
  Define el modelo `Videojuegos` que almacena la información en la base de datos.

- **`inicio/views.py`**  
  Contiene las vistas:
  - `inicio`: página principal.
  - `cargar_juego`: muestra y procesa el formulario para agregar un videojuego.
  - `listado_de_juegos`: lista todos los videojuegos guardados.

- **`inicio/urls.py`**  
  Configura las rutas:
  - `/` → Vista `inicio`
  - `/juego/` → Vista `listado_de_juegos`
  - `/cargar/juego/` → Vista `cargar_juego`

- **Templates (HTML)**  
  - `inicio.html`: página principal.  
  - `cargar_juego.html`: formulario de carga.  
  - `listado_de_juegos.html`: lista de videojuegos.

---

## Orden para probar la aplicación

1. **Ejecutar el servidor**  
   python manage.py runserver

2. **Ingresar a la pgina de Inicio**
    yendo a: http://127.0.0.1:8000/

3. **Cargar un juego**
    yendo a: http://127.0.0.1:8000/cargar/juego/
    completar el formulario y enviarlo

4. **Ingresar al listado de juegos**
    yendo a: http://127.0.0.1:8000/juego/ o dejando que el formulario te redireccione

