"""
    Archivo donde se definen los formularios del sistema
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, RadioField, DateTimeField , SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.fields import TimeField

class FormularioRegistro(FlaskForm):    
    
    p_nombre          = StringField('Primer Nombre', validators=[DataRequired(), Length(min=3)])
    s_nombre          = StringField('Segundo Nombre', validators=[DataRequired(), Length(min=3)])
    p_apellido        = StringField('Primer Apellido', validators=[DataRequired(), Length(min=3)])
    s_apellido        = StringField('Segundo Apellido', validators=[DataRequired(), Length(min=3)])
    rut               = StringField('Rut', validators=[DataRequired(), Length(min=11, max=12)])
    correo            = EmailField('Correo', validators=[DataRequired(), Email()])
    genero            = SelectField('Género', choices=[('', 'Escoja su género'), ('Femenino', 'Femenino'), ('Masculino', 'Masculino')], validators=[DataRequired()])
    clave             = PasswordField('Clave', validators=[DataRequired(), EqualTo('confirmar_clave', message="Las claves deben ser iguales.")])
    confirmar_clave   = PasswordField('Confirmar clave', validators=[DataRequired()])
    submit            = SubmitField('Registrarme')

class FormularioAcceso(FlaskForm):    
    correo    = EmailField('Ingrese su correo:', validators=[DataRequired(), Email()])
    clave     = PasswordField('Ingrese su contraseña:', validators=[DataRequired()])    
    submit    = SubmitField('Acceder')

class FormularioActualizarUsuario(FlaskForm):
    img        = FileField('Foto de perfil (opcional)', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Formato no permitido')])
    p_nombre     = StringField('Primer Nombre', validators=[DataRequired(), Length(min=3)])
    p_apellido   = StringField('Apellido Paterno', validators=[DataRequired(), Length(min=3)])
    s_nombre     = StringField('Segundo Nombre', validators=[DataRequired(), Length(min=3)])
    s_apellido   = StringField('Apellido Materno', validators=[DataRequired(), Length(min=3)])
    rut        = StringField('Rut', validators=[DataRequired(), Length(min=8, max=12)])
    correo     = EmailField('Correo', validators=[DataRequired(), Email()])
    bio        = StringField('Sobre Mi', validators=[Length(min=0)])
    zona       = SelectField('Zona de Chile', choices=[('', "¿En qué zona del país vive?"), ('Norte', 'Norte'), ('Centro', 'Centro'), ('Sur', 'Sur')], validators=[])
    ciudad = SelectField(
    'Ciudad de residencia o ciudad cercana',
    choices=[
        ('', 'Seleccione su ciudad o ciudad cercana'),
        ('Arica', 'Arica'),
        ('Iquique', 'Iquique'),
        ('Antofagasta', 'Antofagasta'),
        ('Calama', 'Calama'),
        ('Copiapó', 'Copiapó'),
        ('La Serena', 'La Serena'),
        ('Coquimbo', 'Coquimbo'),
        ('Valparaíso', 'Valparaíso'),
        ('Santiago', 'Santiago'),
        ('Rancagua', 'Rancagua'),
        ('Talca', 'Talca'),
        ('Curicó', 'Curicó'),
        ('Concepción', 'Concepción'),
        ('Talcahuano', 'Talcahuano'),
        ('Los Ángeles', 'Los Ángeles'),
        ('Temuco', 'Temuco'),
        ('Valdivia', 'Valdivia'),
        ('Osorno', 'Osorno'),
        ('Puerto Montt', 'Puerto Montt'),
        ('Coyhaique', 'Coyhaique'),
        ('Punta Arenas', 'Punta Arenas'),
        ('Castro', 'Castro'),
        ('Chillán', 'Chillán'),
        ('Arica', 'Arica'),
        ('Putre', 'Putre'),
        ('Ovalle', 'Ovalle'),
        ('San Fernando', 'San Fernando'),
        ('Los Andes', 'Los Andes'),
        ('Quillota', 'Quillota'),
        ('Limache', 'Limache'),
        ('Viña del Mar', 'Viña del Mar'),
        ('Pudahuel', 'Pudahuel'),
        ('Peñaflor', 'Peñaflor'),
        ('San Pedro de la Paz', 'San Pedro de la Paz'),
        ('La Unión', 'La Unión'),
        ('Linares', 'Linares'),
        ('Curanilahue', 'Curanilahue'),
        ('San Javier', 'San Javier')
    ],
)
    submit  = SubmitField('Actualizar Perfil')

class FormularioRecordatorio(FlaskForm):
    titulo  = StringField('Descripción del Recordatorio', validators=[DataRequired()])
    fecha   = DateTimeField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    hora    = TimeField('Hora', format='%H:%M', validators=[DataRequired()]) 
    submit  = SubmitField('Actualizar Recordatorio')

class FormularioContactos(FlaskForm):
    parentezco = SelectField('Parentezco', choices=[('', "¿Cual es su parentezco con usted?"), ('Hijo', 'Hijo'), ('Hija', 'Hija'), ('Mamá', 'Mamá'), ('Papá', 'Papá'), ('Abuelo', 'Abuelo'), ('Abuela', 'Abuela'), ('Amig@', 'Amig@')], validators=[DataRequired()])
    nombre     = StringField('Nombre', validators=[DataRequired()])
    apellido   = StringField('Apellido', validators=[DataRequired()])
    numero     = StringField('Número de telefono (+56)', validators=[DataRequired()])
    correo     = EmailField('Correo', validators=[DataRequired(), Email()])
    submit     = SubmitField('Añadir Contacto')

class FormularioEditarContactos(FlaskForm):
    parentezco = SelectField('Parentezco', choices=[
        ('', "¿Cual es su parentezco con usted?"),
        ('Hijo', 'Hijo'),
        ('Hija', 'Hija'),
        ('Mamá', 'Mamá'),
        ('Papá', 'Papá'),
        ('Abuelo', 'Abuelo'),
        ('Abuela', 'Abuela'),
        ('Amig@', 'Amig@')
    ])
    nombre   = StringField('Nombre')
    apellido = StringField('Apellido')
    numero   = StringField('Número de telefono (+56)')
    correo  = StringField('Correo')
    submit  = SubmitField('Editar Contacto')

class FormularioTest(FlaskForm):
    p1       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)
    p2       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)
    p3       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)
    p4       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)
    p5       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)
    p6       = RadioField(choices=[('1', 'Sí'), ('0', 'No')], default='0', coerce=int)

    submit_t       = SubmitField('Terminar Test')
