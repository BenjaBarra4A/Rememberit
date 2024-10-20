from app import db
from flask_login import UserMixin
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id             = db.Column(db.Integer, primary_key=True)
    img            = db.Column(db.BLOB, nullable=True)
    bio            = db.Column(db.String(250), nullable=True)
    p_nombre       = db.Column(db.String(45), nullable=False)
    s_nombre       = db.Column(db.String(45), nullable=False)
    p_apellido     = db.Column(db.String(45), nullable=False)
    s_apellido     = db.Column(db.String(45), nullable=False)
    rut            = db.Column(db.String(15), nullable=False)
    correo         = db.Column(db.String(100), nullable=False, unique=True)
    genero         = db.Column(db.String(10), nullable=False)
    clave          = db.Column(db.String(255), nullable=False)

    # Relaciones
    recordatorios  = db.relationship('Recordatorios', back_populates='usuario', cascade="all, delete-orphan", lazy=True)
    localidades    = db.relationship('Ubicacion', back_populates='usuario', cascade="all, delete-orphan", lazy=True)
    contactos      = db.relationship('Contactos', back_populates='usuario', cascade="all, delete-orphan", lazy=True)
    test           = db.relationship('Test', back_populates='usuario', cascade='all, delete-orphan')

    def establecer_clave(self, clave):
        self.clave = generate_password_hash(clave)

    def chequeo_clave(self, clave):
        return check_password_hash(self.clave, clave)

    @staticmethod
    def obtener_por_correo(correo):
        return Usuario.query.filter_by(correo=correo).first()

    @staticmethod
    def obtener_por_id(user_id):
        return Usuario.query.get(user_id)

class Recordatorios(db.Model):
    __tablename__ = "recordatorios"
    id            = db.Column(db.Integer, primary_key=True)
    titulo        = db.Column(db.String(255), nullable=False)
    fecha         = db.Column(db.Date, nullable=False)
    hora          = db.Column(db.Time, nullable=False) 
    usuario_id    = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    created_at    = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at    = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    # Relación
    usuario = db.relationship('Usuario', back_populates='recordatorios')

class Ubicacion(db.Model):
    __tablename__ = "localidades"
    id            = db.Column(db.Integer, primary_key=True)
    zona          = db.Column(db.String(10), nullable=False)
    ciudad        = db.Column(db.String(40), nullable=False)
    usuario_id    = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # Relación
    usuario = db.relationship('Usuario', back_populates='localidades')

class Contactos(db.Model):
    __tablename__ = 'contactos'
    id            = db.Column(db.Integer, primary_key=True)
    parentezco    = db.Column(db.String(10), nullable=False)
    nombre        = db.Column(db.String(50), nullable=False)
    apellido      = db.Column(db.String(50), nullable=False)
    numero        = db.Column(db.String(15), nullable=False) 
    correo        = db.Column(db.String(100), nullable=False)  
    usuario_id    = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='contactos')

class Test(db.Model):
    __tablename__ = "test"
    id              = db.Column(db.Integer, primary_key=True)
    p1              = db.Column(db.String(50), nullable=False)
    p2              = db.Column(db.String(50), nullable=False)
    p3              = db.Column(db.String(50), nullable=False)
    p4              = db.Column(db.String(50), nullable=False)
    p5              = db.Column(db.String(15), nullable=False)
    p6              = db.Column(db.String(100), nullable=False)
    
    puntaje         = db.Column(db.Integer, nullable=False)   # Campo para el puntaje
    grado_alzheimer = db.Column(db.String(50), nullable=False)  # Campo para el grado de Alzheimer

    usuario_id      = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='test')


