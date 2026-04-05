def ej9(data):
    newDict = {}
    for item in data:
        name = item.get("name")
        grade = item.get("grade")
        status = item.get("status")
        if  name is not None and name.strip() != "" and grade is not None and grade != "" and not grade.isalpha():
            name = name.strip().title()
            item["name"] = name
            item["status"] = status.strip().title()
            
            if name not in newDict:
                newDict[name] = item
            else:
                if int(newDict[name]["grade"]) < int(grade):
                    newDict[name] = item
    dataList = sorted([item for item in newDict.values()], key=lambda x: x["name"])
    result = "Registros limpios de alumnos:\nNombre\t\tNota\tEstado\n------------------------------------------\n"
    for student in dataList:
        result += f"{student["name"]}\t{student["grade"]}\t{student["status"]}\n"
    result += f"Total de alumnos válidos: {len(dataList)}"
    return result