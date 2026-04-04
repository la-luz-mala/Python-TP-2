def ej2(playlist):
    # Lista por comprensión donde guardo todos los valores en segundos, para operar
    seconds_list = [(int(item['duration'].split(':')[0])*60 + int(item['duration'].split(':')[1])) for item in playlist]

    # Saco longitud total y la formateo en mm:ss
    result = "Duración total: {}m {}s\n".format(int(sum(seconds_list)/60), int(sum(seconds_list)%60))

    # Opero sobre la lista de segundos y la uso para acceder a mi lista original
    result += "Canción más larga: \"{}\" ({})\n".format(playlist[seconds_list.index(max(seconds_list))]["title"],playlist[seconds_list.index(max(seconds_list))]["duration"])
    result += "Canción más corta: \"{}\" ({})\n".format(playlist[seconds_list.index(min(seconds_list))]["title"],playlist[seconds_list.index(min(seconds_list))]["duration"])
    return result
