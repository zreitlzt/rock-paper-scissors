def player(prev_play, opponent_history=[]):
        opponent_history.append(prev_play)
        counter = {'P': 'S', 'R': 'P', 'S': 'R'}
        if not prev_play:
                    return 'R'
                game_count = len(opponent_history)
    if game_count >= 5:
                last_five = opponent_history[-5:]
                if last_five == ['R', 'R', 'P', 'P', 'S']:
                                quincy_counter = ['P', 'P', 'S', 'S', 'R']
                                return quincy_counter[game_count % 5]
                        play_order = {}
    for i in range(1, len(opponent_history)):
                seq = opponent_history[i-1] + opponent_history[i]
        play_order[seq] = play_order.get(seq, 0) + 1
    if game_count >= 3:
                last_move = opponent_history[-1]
        potential_next = {}
        for move in ['R', 'P', 'S']:
                        pattern = last_move + move
                        potential_next[move] = play_order.get(pattern, 0)
                    if potential_next:
                                    predicted = max(potential_next, key=potential_next.get)
                                    if potential_next[predicted] > 0:
                                                        return counter[predicted]
                                            if game_count > 2:
                                                        window_size = min(10, game_count)
                                                        recent = opponent_history[-window_size:]
                                                        freq = {'R': recent.count('R'), 'P': recent.count('P'), 'S': recent.count('S')}
                                                        most_frequent = max(freq, key=freq.get)
                                                        return counter[most_frequent]
                                                    return counter.get(opponent_history[-1], 'R')
