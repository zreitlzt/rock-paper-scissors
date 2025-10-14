# Multi-strategy Rock Paper Scissors player using frequency analysis and pattern recognition
# Designed to achieve >60% win rate against all four bot opponents

def player(prev_play, opponent_history=[], play_order=None):
    # Initialize play_order dictionary on first call
    if play_order is None:
        play_order = {}
    
    # Counter moves: what beats what
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    # Add previous play to history
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)
    
    # Default guess
    guess = 'R'
    
    # Need at least a few plays to start analyzing
    if len(opponent_history) < 3:
        # Start with Paper as it's statistically favorable
        return 'P'
    
    # Strategy 1: Frequency Analysis (for simple bots)
    # Count opponent's most frequent moves
    if len(opponent_history) >= 5:
        freq = {'R': 0, 'P': 0, 'S': 0}
        for move in opponent_history[-20:]:  # Look at recent history
            if move in freq:
                freq[move] += 1
        
        # Predict they'll use their most frequent move
        most_common = max(freq, key=freq.get)
        guess = ideal_response[most_common]
    
    # Strategy 2: Pattern Detection (for sequence-based bots)
    # Look for patterns of length 2-4
    if len(opponent_history) >= 6:
        # Check for repeating patterns
        pattern_length = min(4, len(opponent_history) // 3)
        
        for length in range(2, pattern_length + 1):
            recent_pattern = ''.join(opponent_history[-length:])
            
            # Count how many times this pattern has appeared
            pattern_count = 0
            next_moves = []
            
            for i in range(len(opponent_history) - length):
                window = ''.join(opponent_history[i:i+length])
                if window == recent_pattern:
                    pattern_count += 1
                    if i + length < len(opponent_history):
                        next_moves.append(opponent_history[i + length])
            
            # If pattern found multiple times, predict based on historical next move
            if len(next_moves) >= 2:
                next_freq = {'R': 0, 'P': 0, 'S': 0}
                for move in next_moves:
                    if move in next_freq:
                        next_freq[move] += 1
                predicted = max(next_freq, key=next_freq.get)
                guess = ideal_response[predicted]
                break
    
    # Strategy 3: Markov Chain Analysis (for adaptive bots)
    # Analyze transition probabilities
    if len(opponent_history) >= 10:
        # Build transition model from last play to next play
        if len(opponent_history) >= 2:
            last_play = opponent_history[-1]
            transitions = {'R': [], 'P': [], 'S': []}
            
            for i in range(len(opponent_history) - 1):
                current = opponent_history[i]
                next_move = opponent_history[i + 1]
                if current in transitions:
                    transitions[current].append(next_move)
            
            # Predict based on what usually follows the last play
            if last_play in transitions and len(transitions[last_play]) > 0:
                trans_freq = {'R': 0, 'P': 0, 'S': 0}
                for move in transitions[last_play]:
                    if move in trans_freq:
                        trans_freq[move] += 1
                predicted = max(trans_freq, key=trans_freq.get)
                guess = ideal_response[predicted]
    
    # Strategy 4: Meta-strategy - detect if opponent is counter-playing
    # Check if opponent seems to be beating our previous moves
    if len(opponent_history) >= 15:
        # This would require tracking our own history
        # For now, add randomization to avoid exploitation
        import random
        recent_window = opponent_history[-10:]
        
        # If opponent shows high variance, they might be counter-playing
        unique_recent = len(set(recent_window))
        if unique_recent == 3:  # High diversity suggests adaptive opponent
            # Add slight randomization while still favoring frequency analysis
            if random.random() < 0.15:  # 15% randomization
                guess = random.choice(['R', 'P', 'S'])
    
    return guess
