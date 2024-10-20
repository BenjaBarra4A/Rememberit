""" 
Maneja el control sobre la información de la vista
y los modelos de bases de datos
"""
from models import Usuario,Test, db

class ControladorUsuarios:
    @staticmethod
    def crear_usuario(p_nombre,p_apellido,s_nombre, s_apellido,rut,correo,genero,clave):
        usuario = Usuario()
        usuario.p_nombre = p_nombre 
        usuario.p_apellido = p_apellido
        usuario.s_nombre = s_nombre 
        usuario.s_apellido = s_apellido
        usuario.rut = rut
        usuario.correo = correo
        usuario.genero = genero
        usuario.establecer_clave(clave)
            
        #Agregamos a la base datos
        db.session.add(usuario)
        db.session.commit()
        return usuario