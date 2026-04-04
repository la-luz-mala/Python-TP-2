def ej9(data):
    newDict = {}
    for item in data:
        name = item.get("name")
        grade = item.get("grade")
        status = item.get("status")
        if  name is not None and name.strip() != "" and grade is not None and grade != "" and not grade.isalpha():
            item["name"] = name.strip().title()
            item["status"] = status.strip().title()
            
            newList.append(item)

for student in newList:
    print(f"Estudiante: {student["name"]}. Nota: {student["grade"]}. Estado: {student["status"]}.")


    # EN PROGRESO #

    # EN PROGRESO #

    # EN PROGRESO #