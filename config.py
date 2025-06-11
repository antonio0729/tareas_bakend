import os
from peewee import PostgresqlDatabase

# 📌 Obtener la URL de la base de datos desde la variable de entorno o usar la URL fija
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://lista_tareas_db_sd4e_user:GzRwoj33z9EobatPyVEuOjWK4Fgv8cbF@dpg-d14fd7euk2gs73aqq89g-a.oregon-postgres.render.com/lista_tareas_db_sd4e")

# 📌 Conectar PostgreSQL con Peewee
db = PostgresqlDatabase(
    "lista_tareas_db_sd4e",  # Nombre de la base de datos
    user="lista_tareas_db_sd4e_user",
    password="GzRwoj33z9EobatPyVEuOjWK4Fgv8cbF",
    host="dpg-d14fd7euk2gs73aqq89g-a.oregon-postgres.render.com",
    port=5432
)

