import sities_methods
def play_word(player_id):
    target_letter = sities_methods.get_session_data(player_id)['cities'][-1][-1]

