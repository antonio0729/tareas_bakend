from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Tarea  # Importamos el modelo desde models.py

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir conexiones desde el frontend

@app.route("/")
def health_check():
    return {"status": "ok", "message": "API corriendo"}

# 📌 Crear una tarea (POST)
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    tarea = Tarea.create(
        titulo=data['titulo'],
        descripcion=data.get('descripcion'),
        completado=data.get('completado', False)
    )
    return jsonify(modelo_a_diccionario(tarea)), 201

# 📌 Obtener todas las tareas (GET)
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.select()
    return jsonify([modelo_a_diccionario(t) for t in tareas])

# 📌 Obtener una tarea por ID (GET)
@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    try:
        tarea = Tarea.get(Tarea.id == id)
        return jsonify(modelo_a_diccionario(tarea))
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

# 📌 Actualizar una tarea por ID (PUT)
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    try:
        tarea = Tarea.get(Tarea.id == id)
        data = request.get_json()
        tarea.titulo = data.get('titulo', tarea.titulo)
        tarea.descripcion = data.get('descripcion', tarea.descripcion)
        tarea.completado = data.get('completado', tarea.completado)
        tarea.save()
        return jsonify(modelo_a_diccionario(tarea))
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

# 📌 Eliminar una tarea por ID (DELETE)
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:
        tarea = Tarea.get(Tarea.id == id)
        tarea.delete_instance()
        return jsonify({"mensaje": "Tarea eliminada correctamente"})
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

# 📌 Función auxiliar para convertir un modelo a diccionario
def modelo_a_diccionario(tarea):
    return {
        "id": tarea.id,
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "completado": tarea.completado
    }

# 📌 Punto de entrada
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
    