document.addEventListener("DOMContentLoaded", loadTasks);

function loadTasks() {
    fetch("https://tareas-bakend.onrender.com/tareas")
        .then(response => response.json())
        .then(data => {
            if (!Array.isArray(data)) {
                console.error("Error: La API no devuelve un array", data);
                return;
            }
            const list = document.getElementById("task-list");
            list.innerHTML = "";
            data.forEach(task => {
                const li = document.createElement("li");
                li.classList.add("list-group-item");
                li.innerHTML = `
                    <input type="checkbox" ${task.completado ? "checked" : ""} onchange="toggleTask(${task.id}, this.checked)">
                    <input type="text" value="${task.titulo}" onchange="updateTask(${task.id}, this.value)">
                    <button class="btn btn-danger btn-sm float-end" onclick="deleteTask(${task.id})">Eliminar</button>
                `;
                list.appendChild(li);
            });
        })
        .catch(error => console.error("Error al obtener tareas:", error));
}

function addTask() {
    const taskTitle = document.getElementById("task-input").value;

    if (!taskTitle.trim()) {
        console.error("El título de la tarea está vacío");
        return;
    }

    fetch("https://tareas-bakend.onrender.com/tareas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo: taskTitle, descripcion: "Sin descripción", completado: false })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById("task-input").value = ""; // Limpiar campo después de agregar tarea
        loadTasks();
    })
    .catch(error => console.error("Error al agregar tarea:", error));
}

function toggleTask(id, completed) {
    fetch(`https://tareas-bakend.onrender.com/tareas/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completado: completed })
    })
    .then(() => loadTasks())
    .catch(error => console.error("Error al actualizar tarea:", error));
}

function updateTask(id, newTitle) {
    fetch(`https://tareas-bakend.onrender.com/tareas/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo: newTitle })
    })
    .then(() => loadTasks())
    .catch(error => console.error("Error al actualizar título:", error));
}

function deleteTask(id) {
    fetch(`https://tareas-bakend.onrender.com/tareas/${id}`, {
        method: "DELETE"
    })
    .then(() => loadTasks())
    .catch(error => console.error("Error al eliminar tarea:", error));
}




