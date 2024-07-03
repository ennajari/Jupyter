class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.predecessors = []
        self.ES = 0
        self.LF = 0
        self.MF = 0
        self.MT = 0

# Définition des tâches avec leurs durées
tasks = {
    'A': Task('A', 5),
    'B': Task('B', 3),
    'C': Task('C', 4),
    'D': Task('D', 4),
    'E': Task('E', 5),
    'F': Task('F', 2),
    'G': Task('G', 2),
    'H': Task('H', 4)
}

# Définition des antériorités
tasks['B'].predecessors = ['A']
tasks['C'].predecessors = ['A']
tasks['D'].predecessors = ['A']
tasks['E'].predecessors = ['B', 'C']
tasks['F'].predecessors = ['D', 'E']
tasks['G'].predecessors = ['E']
tasks['H'].predecessors = ['F']

# Calcul des dates au plus tôt (ES) et au plus tard (LF)
def calculate_dates(tasks):
    # Calcul des dates au plus tôt (ES)
    for name, task in tasks.items():
        if not task.predecessors:
            task.ES = 0
        else:
            task.ES = max(tasks[pre].ES + tasks[pre].duration for pre in task.predecessors)
    
    # Calcul des dates au plus tard (LF) en ordre inverse
    task_list = list(tasks.values())
    for task in reversed(task_list):
        if task.name == 'H':
            task.LF = task.ES
        else:
            task.LF = min(tasks[suc].LF - tasks[task.name].duration for suc in task.predecessors)

# Calcul des marges libres (MF) et marges totales (MT)
def calculate_margins(tasks):
    for name, task in tasks.items():
        task.MF = task.LF - task.ES
        task.MT = task.LF - task.ES

# Déterminer le chemin critique
def find_critical_path(tasks):
    critical_path = []
    for name, task in tasks.items():
        if task.MT == 0:
            critical_path.append(task.name)
    return critical_path

# Exécuter les calculs
calculate_dates(tasks)
calculate_margins(tasks)
critical_path = find_critical_path(tasks)

# Affichage des résultats
print("Dates au plus tôt (ES) et au plus tard (LF) :")
for name, task in tasks.items():
    print(f"Tâche {name}: ES = {task.ES}, LF = {task.LF}")

print("\nMarges libres (MF) et marges totales (MT) :")
for name, task in tasks.items():
    print(f"Tâche {name}: MF = {task.MF}, MT = {task.MT}")

print("\nChemin critique : ", critical_path)
