def players_by_country_and_position(squads_list):
    result={}
    from football_dictionaries.assignment_1 import players_as_dictionaries
    players= players_as_dictionaries(squads_list)
    for player in players:
        country = player['country']
        position = player['position']
        if country not in result:
            result[country]={}
        if position not in result[country]:
            result[country][position]=[]
        result[country][position].append(player)
    return result

