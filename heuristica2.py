import numpy as np

# Crear el modelo de datos
# Cada [i][j] es el costo de asignar al trabajador i, la tarea j
def create_data_model():
    data = {}
    data['cost_matrix'] = [
        [90, 800, 75, 800], # Costos para el trabajador 0
        [35, 85, 55, 65], # Costos para el trabajador 1
        [125, 95, 90, 105], # Costos para el trabajador 2
        [45, 130, 5, 115], # Costos para el trabajador 3
        [50, 100, 90, 100], # Costos para el trabajador 4
    ]
    # Se puede leer como;
    # la tarea 0, le cuesta al trabajador 0,  90 pesos, minutos, etc.
    # la tarea 1, le cuesta al trabajador 0, 800 pesos, minutos, etc.
    # la tarea 2, le cuesta al trabajador 0, 75 pesos, minutos, etc.
    # la tarea 3, le cuesta al trabajador 0, 800 pesos, minutos, etc
    data['num_workers'] = len(data['cost_matrix'])
    data['num_tasks'] = len(data['cost_matrix'][0])
    return data

# Crear el modelo de datos con los datos propuestos arriba
data = create_data_model()

# Se convierte la matriz de costos a un array de NumPy
cost_matrix = np.array(data['cost_matrix'])

# Inicializar las variables de asignación
num_workers = data['num_workers']
num_tasks = data['num_tasks']
assignments = [-1] * num_tasks
assigned_workers = set()

# Heurística de asignación basada en el costo mínimo
for task in range(num_tasks):
    min_cost = float('inf')
    best_worker = -1
    for worker in range(num_workers):
        if worker not in assigned_workers and cost_matrix[worker, task] < min_cost:
            min_cost = cost_matrix[worker, task]
            best_worker = worker
    assignments[task] = best_worker
    assigned_workers.add(best_worker)

# Imprimir la solución
print("Asignación de tareas a trabajadores:")
for task in range(num_tasks):
    print(f"Tarea {task} asignada al trabajador {assignments[task]} con costo {cost_matrix[assignments[task], task]}")

# Calcular el costo total
total_cost = sum(cost_matrix[assignments[task], task] for task in range(num_tasks))
print(f"Costo total de la asignación: {total_cost}")
