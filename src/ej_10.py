#el puntaje de cada ronda es la suma de los tres jueces OK
#imprimir tabla de posiciones después de cada ronda OK
#indicar en cada ronda quien gano (max puntaje) y contabilizarlo
#imprimir tabla final con puntaje total acumulado, cantidad de
#rondas ganadas, mejor puntaje en una ronda, y promedio por ronda. La tabla
#debe estar en orden decreciente por puntaje total

# rounds = [
#     {
#         'theme': 'Entrada',
#         'scores': {
#             'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
#             'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
#             'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
#             'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
#             'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
#         }
#     },
# ]...

def ej10(rounds):
    stats = {}

    for i, round in enumerate(rounds, 1):
        round_name = round["theme"]
        scores = round["scores"]

        thisRound = []
        for name, judge_score in scores.items():
            total_score = sum(judge_score.values())
            thisRound.append((name, total_score))
            
            if name not in stats:
                stats[name] = {"total": 0, "wins": 0, "best": 0, "scores_list": []}
            stats[name]["total"] += total_score
            stats[name]["scores_list"].append(total_score)
            if total_score > stats[name]["best"]:
                stats[name]['best'] = total_score

        thisRound.sort(key = lambda score:score[1], reverse = True)
        winner, winnerPoints = thisRound[0]
        stats[winner]["wins"] += 1

        print()
        print(f"Ronda {i} - {round_name}:\n  Ganador: {winner} ({winnerPoints} pts)")
        print("Cocinero\tPuntaje")
        for name, score in thisRound:
            print(f"{name}    \t  {score}")
        
        
    final_scores = sorted(stats.items(), key = lambda x: x[1]["total"], reverse=True)

    print()
    print("Tabla de posiciones final:")
    print("Cocinero    \tPuntaje\tRondas ganadas\tMejor ronda\tPromedio")
    print("-"*65)
    for name, data in final_scores:
        avg = data["total"] / len(data["scores_list"])
        print(f"{name}    \t{data["total"]}\t{data["wins"]}\t\t{data["best"]}\t\t{avg}")
