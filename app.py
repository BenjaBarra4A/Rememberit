"""
Archivo app.py: módulo principal de la aplicación.
"""
from flask import Flask, render_template, flash, redirect, request, Response, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from datetime import datetime

# Iniciación y configuración de la app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi clave!"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/remember_it"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth"

# Importación de módulos propios
from forms import FormularioRegistro, FormularioAcceso, FormularioActualizarUsuario, FormularioRecordatorio, FormularioContactos, FormularioEditarContactos
from models import Usuario, Recordatorios, Ubicacion, Contactos
from controllers import ControladorUsuarios

# Inicialización de versiones de la bases de datos
Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.obtener_por_id(int(user_id))

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Rutas de autenticación
@app.route("/")
def auth(form_registro=None, form_acceso=None):
    if current_user.is_authenticated:
        return redirect("/home")
    
    if form_registro is None:
        form_registro = FormularioRegistro()
    if form_acceso is None:
        form_acceso = FormularioAcceso()
    return render_template("register.html", form_registro=form_registro, form_acceso=form_acceso)

@app.route("/register", methods=["POST", "GET"])
def register():
    form = FormularioRegistro()
    if form.validate_on_submit():
        p_nombre = form.p_nombre.data
        p_apellido = form.p_apellido.data
        s_nombre = form.s_nombre.data
        s_apellido = form.s_apellido.data
        rut = form.rut.data
        correo = form.correo.data 
        genero = form.genero.data
        clave = form.clave.data

        usuario_existente = Usuario.obtener_por_correo(correo)
        if usuario_existente:
            flash(f"El correo {correo} ya se encuentra registrado")
            return redirect("/")
        
        ControladorUsuarios().crear_usuario(p_nombre, p_apellido,s_nombre, s_apellido, rut, correo, genero, clave)
        flash(f"Usuario registrado exitosamente.")
        return redirect("/home")

    # Imprimir errores si la validación falla
    print(form.errors)
    return auth(form_registro=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("logear.html", form_acceso=FormularioAcceso())
    form_acceso = FormularioAcceso()
    if form_acceso.validate_on_submit():
        usuario = Usuario.obtener_por_correo(form_acceso.correo.data)
        if usuario and usuario.chequeo_clave(form_acceso.clave.data):
            login_user(usuario)
            flash("Correo o clave incorrectos")
            return redirect("/home")
        else:
            flash("El usuario no existe")
    return redirect("/")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

# Rutas de usuario
@app.route("/home")
@login_required
def home():
    usuario = Usuario.obtener_por_correo(current_user.correo)
    recordatorios = Recordatorios.query.filter_by(usuario_id=current_user.id).order_by(Recordatorios.fecha.asc(), Recordatorios.hora.asc()).all()
    if usuario is None:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('login'))
    
    contactos = usuario.contactos  # Obtener los contactos del usuario
    form = FormularioContactos()  
    
    return render_template("perfil.html", usuario=usuario, contactos=contactos, form=form, recordatorios=recordatorios)

@app.route("/update/<int:user_id>", methods=["GET", "POST"])
@login_required
def actualizar(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    form = FormularioActualizarUsuario(obj=usuario)

    usuario.p_nombre = form.p_nombre.data
    usuario.p_apellido = form.p_apellido.data
    usuario.s_nombre = form.s_nombre.data
    usuario.s_apellido = form.s_apellido.data

    # Inicializa la variable 'ubicacion'
    ubicacion = Ubicacion.query.filter_by(usuario_id=user_id).first()

    if form.validate_on_submit():
        # Actualizar la biografía del usuario
        usuario.bio = form.bio.data

        if form.img.data:  # Solo si hay un archivo subido
            try:
                usuario.img = form.img.data.read()  # Lee los datos de la imagen como bytes
            except Exception as e:
                print("Error al leer la imagen:", e)  # I   mprime el error en la consola

        # Si hay una ubicación existente, solo actualiza si se proporcionan nuevos datos
        if ubicacion:
            if form.zona.data:  # Si se proporciona nueva zona
                ubicacion.zona = form.zona.data
            if form.ciudad.data:  # Si se proporciona nueva ciudad
                ubicacion.ciudad = form.ciudad.data
        else:
            # Si no hay ubicación, crear una nueva
            ubicacion = Ubicacion(zona=form.zona.data, ciudad=form.ciudad.data, usuario_id=user_id)  
            db.session.add(ubicacion)
            
        db.session.commit()  # Guarda los cambios en la base de datos
        return redirect("/home")

    return render_template("update.html", form=form, usuario=usuario, ubicacion=ubicacion)
@app.route("/imagen/<int:user_id>")
def imagen(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    if usuario.img:
        return Response(usuario.img, mimetype='image/jpeg')
    else:
        return redirect(url_for('static', filename='default_avatar.png'))
    
@app.route("/verificar_imagen/<int:user_id>")
def verificar_imagen(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    return "Imagen encontrada" if usuario.img else "No hay imagen"
    
@app.route("/eliminar/<int:user_id>", methods=["POST", "GET"])
@login_required
def eliminar(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    
    db.session.delete(usuario)
    db.session.commit()
    
    flash(f"Usuario {usuario.correo} eliminado con éxito")
    return redirect("/home")

#Eliminar y agregar amigos/usuarios
@app.route("/agregar_contacto", methods=["GET", "POST"])
@login_required
def agregar_contacto():
    form = FormularioContactos()  # Instancia del formulario

    if form.validate_on_submit():
        parentezco = form.parentezco.data
        nombre = form.nombre.data
        apellido = form.apellido.data
        numero = form.numero.data
        correo = form.correo.data
        usuario_id = current_user.id  # ID del usuario actual

        # Verifica si el usuario con ese correo existe
        usuario_existente = Usuario.query.filter_by(correo=correo).first()

        if usuario_existente:
            nuevo_contacto = Contactos(
                parentezco=parentezco,
                nombre=nombre,
                apellido=apellido,
                numero=numero,
                correo=correo,
                usuario_id=usuario_id  # Asignar el ID del usuario actual
            )
            db.session.add(nuevo_contacto)
            db.session.commit()  # Guardar cambios
            flash('Contacto añadido exitosamente.', 'success')
        else:
            flash('El usuario con ese correo no existe.', 'error')

        return redirect(request.referrer)  # Redirige al lugar anterior

    return render_template("perfil.html", form=form, usuario=current_user)

@app.route("/eliminar_contacto/<int:contacto_id>", methods=["POST"])
@login_required
def eliminar_contacto(contacto_id):
    contacto = Contactos.query.get(contacto_id)
    
    if contacto and contacto.usuario_id == current_user.id:
        db.session.delete(contacto)
        db.session.commit()  
    
    return redirect("/home")
#Buscar Usuarios

def obtener_contactos(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    return usuario.contactos

# Rutas de recordatorios
@app.route("/agregar_recordatorio", methods=["POST"])
@login_required
def agregar_recordatorio():
    titulo = request.form.get("titulo")
    fecha = request.form.get("fecha")  # Por ejemplo: '2024-10-14'
    hora = request.form.get("hora")    # Por ejemplo: '20:35'

    if not hora:  # Verificar si la hora es None
        flash("La hora es obligatoria.")
        return redirect("/home")  # Redirigir o manejar el error

    # Convertir la fecha y la hora a objetos datetime
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    hora_obj = datetime.strptime(hora, '%H:%M').time()

    # Combinar fecha y hora en un solo objeto datetime
    fecha_hora = datetime.combine(fecha_obj, hora_obj)

    nuevo_recordatorio = Recordatorios(
        titulo=titulo,
        fecha=fecha_hora,  # Almacenar como DateTime
        hora=hora_obj,     # Guardar la hora si la necesitas
        usuario_id=current_user.id
    )
    
    db.session.add(nuevo_recordatorio)
    db.session.commit()

    flash(f"Recordatorio '{titulo}' agregado exitosamente.")
    return redirect("/home")

@app.route("/editar_recordatorio/<int:recordatorio_id>", methods=["GET", "POST"])
@login_required
def editar_recordatorio(recordatorio_id):
    recordatorio = Recordatorios.query.get_or_404(recordatorio_id)
    form = FormularioRecordatorio(obj=recordatorio)

    if form.validate_on_submit():  # Validar el formulario
        recordatorio.titulo = form.titulo.data  # Actualiza el título
        recordatorio.fecha = form.fecha.data  # Actualiza la fecha
        recordatorio.hora = form.hora.data  # Actualiza la hora
        
        db.session.commit()
        flash("Recordatorio actualizado exitosamente.")
        return redirect(url_for("home"))  # Redirige a la página principal o donde necesites

    return render_template("editar_recordatorio.html", form=form, recordatorio=recordatorio)

@app.route("/eliminar_recordatorio/<int:recordatorio_id>", methods=["POST", "GET"])
@login_required
def eliminar_recordatorio(recordatorio_id):
    Recordatorio = Recordatorios.query.get_or_404(recordatorio_id)
    
    db.session.delete(Recordatorio)
    db.session.commit()
    
    flash(f"Recordatorio {Recordatorio.titulo} eliminado con éxito")
    return redirect("/home")
@app.route("/test", methods=["GET","POST"])
@login_required
def hacer_test():
    return render_template("test_memoria.html")

@app.route("/editar_contacto/<int:contactos_id>", methods=["GET", "POST"])
@login_required
def editar_contacto(contactos_id):
    contactos = Contactos.query.get_or_404(contactos_id)
    form = FormularioEditarContactos(obj=contactos)

    usuario = Usuario.query.get(current_user.id)

    if form.validate_on_submit():
        print("Datos del formulario:", form.data)

        contactos.parentezco = form.parentezco.data
        contactos.nombre = form.nombre.data
        contactos.apellido = form.apellido.data
        contactos.numero = form.numero.data

        db.session.commit()
        print("Contacto actualizado exitosamente.")
        return redirect(url_for("home"))

    return render_template("perfil.html", form=form, contacto=contactos, usuario=usuario)