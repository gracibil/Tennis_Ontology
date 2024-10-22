import csv

############# calculate data ################
def calculate_career_winnings_male_GS(position, prize_pool, winner_prize):
    if position == 'Win':
        return winner_prize
    if position == 'F':
        return round(0.09*prize_pool)
    if position == 'SF':
        return round(0.045*prize_pool)
    if position == 'QF':
        return round(0.0225*prize_pool)
    if position == 'R16':
        return round(0.01125*prize_pool)
    if position == 'R32':
        return round(0.005625*prize_pool)
    if position == 'R64':
        return round(0.0028125*prize_pool)
    if position == 'R128':
        return round(0.00140625*prize_pool)


def calculate_career_winnings_Masters(position, prize_pool, winner_prize):
    if position == 'Win':
        return winner_prize
    if position == 'F':
        return round(0.09*prize_pool)
    if position == 'SF':
        return round(0.045*prize_pool)
    if position == 'QF':
        return round(0.0225*prize_pool)
    if position == 'R16':
        return round(0.01125*prize_pool)
    if position == 'R32':
        return round(0.005625*prize_pool)
    if position == 'R64':
        return round(0.0028125*prize_pool)
    if position == 'R128':
        return round(0.00140625*prize_pool)


def calculate_career_winnings_500(position, prize_pool, winner_prize):
    if position == 'Win':
        return winner_prize
    if position == 'F':
        return round(0.09*prize_pool)
    if position == 'SF':
        return round(0.045*prize_pool)
    if position == 'QF':
        return round(0.0225*prize_pool)
    if position == 'R16':
        return round(0.01125*prize_pool)
    if position == 'R32':
        return round(0.005625*prize_pool)
    if position == 'R64':
        return round(0.0028125*prize_pool)
    if position == 'R128':
        return round(0.00140625*prize_pool)

#################### extract data #####################
def create_tournament_set(dataset):
    # use our own created tournament data set to create a set of tournaments were interested in
    with open(dataset, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        female_tournament_id = headers[0]
        male_tournament_id = headers[1]
        tournament_name = headers[2]
        tournament_city = headers[3]
        tournament_year = headers[4]
        tournament_level = headers[5]
        tournament_gender = headers[6]
        male_prize_pool = headers[7]
        female_prize_pool = headers[8]
        male_winner_prize = headers[9]
        female_winner_prize = headers[10]
        fan_attendance = headers[11]
        male_viewership = headers[12]
        female_viewership = headers[13]
        number_of_players = headers[14]

        tournaments = []

        for row in reader:
            # tournament = (female_id, male_id, name, players)
            tournament = {
                'female_id': row[female_tournament_id],
                'male_id': row[male_tournament_id],
                'name': row[tournament_name],
                'tournament_gender': row[tournament_gender],
                'city': row[tournament_city],
                'year': row[tournament_year],
                'level': row[tournament_level],
                'male_prize_pool': row[male_prize_pool],
                'female_prize_pool': row[female_prize_pool],
                'male_winner_prize': row[male_winner_prize],
                'female_winner_prize': row[female_winner_prize],
                'fan_attendance': row[fan_attendance],
                'male_viewership': row[male_viewership],
                'female_viewership': row[female_viewership],
                'number_of_players': row[number_of_players]
            }
            tournaments.append(tournament)

        # print(headers)
        #
        # print(tournaments)

        return tournaments


def extract_matches_male(tournaments, dataset, players_set=None):
    with open(dataset, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = reader.fieldnames
        tourney_id = headers[0]
        match_num = headers[6]
        winner_id = headers[7]
        winner_name = headers[10]
        looser_id = headers[15]
        looser_name = headers[18]
        round = headers[25]
        if players_set == None:
            all_players = set()
        else:
            all_players = players_set

        for tournament in tournaments:

            players = dict()

            for row in reader:
                if row[tourney_id] == tournament['male_id']:
                    players[row[looser_id]] = {'finish' : row[round]}
                    all_players.add(row[winner_id])
                    all_players.add(row[looser_id])
                    if row[round] == 'F':
                        players[row[winner_id]] = {'finish': 'Winner'}



            tournament['male_players'] = players
            csvfile.seek(1)

    return all_players, tournaments


def extract_player_data(dataset, gender, players):
    gender = gender
    with open(dataset, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        player_id = headers[0]
        first_name = headers[1]
        last_name = headers[2]
        birthdate = headers[4]
        height = headers[6]
        wikidata_id = headers[7]
        print('length of players:', len(players))
        players_dict = {}
        for player in players:
            for row in reader:
                if row[player_id] == player:
                    players_dict[player] = {
                        'entity_name': f'{row[first_name]}_{row[last_name]}',
                        'first_name': row[first_name],
                        'last_name': row[last_name],
                        'gender' : gender,
                        'birthdate': row[birthdate],
                        'height': row[height],
                        'wikidata_id': row[wikidata_id],
                        'participates_in': [],
                        'career_winnings': 0
                    }
                    # print(f'Player : {row[first_name]}_{row[last_name]}  || '
                    #       f'First_name : {row[first_name]}  || '
                    #       f'Last_Name : {row[last_name]} || '
                    #       f'Gender: {gender} || '
                    #       f'Player ID: {row[player_id]} || '
                    #       f'Birthdate: {row[birthdate]} || '
                    #       f'Height: {row[height]} || '
                    #       f'Wikidata ID: {row[wikidata_id]} || '
                    #       f'participatesIN: [Tournament list] || '
                    #       f'career_winnings: 0')
                    break

            csvfile.seek(1)
        print(headers)
        return players_dict

############# creating triples ################

def rdf_namespace(ent):
    rdf_namespace = '###  http://www.semanticweb.org/edmondagabekian/ontologies/2024/9/untitled-ontology-13#'
    return f'{rdf_namespace}{ent}'

def extract_tournament_to_triples(tournament):
    triples = f"""
        {rdf_namespace(f'{tournament["name"]}_{tournament["year"]}')}
         :{tournament['name']}_{tournament['year']} rdf:type owl:NamedIndividual ,
                                            :{tournament['name']} ;
                                    :hasTotalAttendance {tournament['fan_attendance']} ;
                                    :hasFemalePrizePool {tournament['female_prize_pool']};
                                    :hasFemaleViewership {tournament['female_viewership']};
                                    :hasMalePrizePool {tournament['male_prize_pool']};
                                    :hasMaleViewership {tournament['male_viewership']};
                                    :hasFemaleWinnerPrize {tournament['female_winner_prize']};
                                    :hasMaleWinnerPrize {tournament['male_winner_prize']};
                                    :hasLevel {tournament['level']} ;
                                    :inYear {tournament['year']} ;
        
    """
    return triples

def extract_player_to_triples(player):
    triples = f"""
        {rdf_namespace(f'{player["entity_name"]}')}
         :{player['entity_name']} rdf:type owl:NamedIndividual ,
                                            :{player['gender']}_Player ;
                                    :hasGender {player['gender']} ;
                                    :hasBirthdate {player['birthdate']} ;
                                    :hasHeight {player['height']} ;
                                    :hasWikidataID {player['wikidata_id']} ;
                                    :participatesIn {player['participates_in']} ;
                                    :careerWinnings {player['career_winnings']} ;
        """
    return triples

def test():
    tournament_set = create_tournament_set('./Data_Sets/Tournament_Data_Id.csv')
    players, male_matches = extract_matches_male(tournament_set, './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2010.csv')
    male_player_data = extract_player_data('./Data_Sets/ATP_Dataset/tennis_atp-master/atp_players.csv','Male', players)
    print(male_player_data)
    tournmant_triple = extract_tournament_to_triples(tournament_set[0])
    male_triple = extract_player_to_triples(male_player_data['104918'])
    print(male_triple)
    print(tournmant_triple)
    # print('players:', players)
    # print('tournaments:', tournament_set)
    #extract_men_to_triples()

test()