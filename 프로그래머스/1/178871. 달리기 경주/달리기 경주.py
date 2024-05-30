def solution(players, callings):
    player_call = {v : i for i, v in enumerate(players)}
    for val in callings:
        new = player_call[val] 
        name = players[new - 1] 
        players[new-1], players[new] = players[new], players[new-1]
        player_call[val],  player_call[name]= new -1, new 
    return players