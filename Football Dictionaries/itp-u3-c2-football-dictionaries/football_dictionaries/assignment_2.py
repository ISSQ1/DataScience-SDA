def players_by_position(squads_list):
    result={}
    from football_dictionaries.assignment_1 import players_as_dictionaries
    players= players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        if position not in result:
            result[position] = []
        result[position].append(player)
    return result

