from peewee import Model, CharField, TextField, BooleanField
from config import db  # Importamos la conexión desde config.py

class BaseModel(Model):
    class Meta:
        database = db

class Tarea(BaseModel):
    titulo = CharField()
    descripcion = TextField(null=True)
    completado = BooleanField(default=False)

# 📌 Conectar la base de datos y crear las tablas si no existen con manejo de errores
try:
    db.connect()
    db.create_tables([Tarea])
    db.close()  # Cerramos la conexión después de crear las tablas
except Exception as e:
    print(f"❌ Error al conectar con la base de datos: {e}")
    