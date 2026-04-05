def ej9(data):
    newDict = {}
    for item in data:
        name = item.get("name")
        grade = item.get("grade")
        status = item.get("status")
        if  name is not None and name.strip() != "" and grade is not None and grade != "" and not grade.isalpha():
            item["name"] = name.strip().title()
            item["status"] = status.strip().title()
            
            if name not in newDict:
                newDict[name] = item
            else:
                if int(newDict["grade"]) < int(grade):
                    newDict[name] = item
    dataList = sorted([item for item in newDict.values()], key=lambda x: x["name"])
    result = ""
    for student in dataList:
        result += f"Estudiante: {student["name"]}. Nota: {student["grade"]}. Estado: {student["status"]}.\n"
    return result

students = [
    {"name": " Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]

print(ej9(students))