import csv

############# calculate data ################

def calculate_match_winnings(ko_round, total_players, prize_pool, winner_prize=0, gender=None):
    remaining_prize_pool = prize_pool - winner_prize
    if total_players == 128 or 256:
        return  calculate_career_winnings_GS(ko_round, remaining_prize_pool)
    if total_players == 96 or 56:
        return calculate_career_winnings_Masters(ko_round, remaining_prize_pool)
    if total_players == 48:
        return calculate_career_winnings_48(ko_round, remaining_prize_pool)
    if total_players == 32:
        if gender == 'Male':
            return calculate_career_winnings_32M(ko_round, remaining_prize_pool)
        else:
            return calculate_career_winnings_32F(ko_round, remaining_prize_pool)
    if total_players == 30:
        return calculate_career_winnings_48(ko_round, remaining_prize_pool)
    if total_players == 28:
        return calculate_career_winnings_48(ko_round, remaining_prize_pool)



def calculate_career_winnings_GS(position, prize_pool):
    if position == 'F':
        return round(0.091851463*prize_pool)
    if position == 'SF':
        return round(0.046909854*prize_pool)
    if position == 'QF':
        return round(0.02460307*prize_pool)
    if position == 'R16':
        return round(0.01482745*prize_pool)
    if position == 'R32':
        return round(0.009381971*prize_pool)
    if position == 'R64':
        return round(0.006101561*prize_pool)
    if position == 'R128':
        return round(0.003936491*prize_pool)


def calculate_career_winnings_Masters(position, prize_pool):
    if position == 'F':
        return round(0.14145829*prize_pool)
    if position == 'SF':
        return round(0.077351931*prize_pool)
    if position == 'QF':
        return round(0.042191962*prize_pool)
    if position == 'R16':
        return round(0.022567389*prize_pool)
    if position == 'R32':
        return round(0.01210211*prize_pool)
    if position == 'R64':
        return round(0.006704047*prize_pool)


def calculate_career_winnings_48(position, prize_pool):
    if position == 'F':
        return round(0.161834238*prize_pool)
    if position == 'SF':
        return round(0.083951213*prize_pool)
    if position == 'QF':
        return round(0.043833215*prize_pool)
    if position == 'R16':
        return round(0.023094681*prize_pool)
    if position == 'R32':
        return round(0.012644441*prize_pool)
    if position == 'R64':
        return round(0.006741373*prize_pool)

def calculate_career_winnings_32F(position, prize_pool):
    if position == 'F':
        return round(0.157766872*prize_pool)
    if position == 'SF':
        return round(0.092163458*prize_pool)
    if position == 'QF':
        return round(0.044834034*prize_pool)
    if position == 'R16':
        return round(0.024464598*prize_pool)
    if position == 'R32':
        return round(0.017678331*prize_pool)

def calculate_career_winnings_32M(position, prize_pool):
    if position == 'F':
        return round(0.179917969*prize_pool)
    if position == 'SF':
        return round(0.095885908*prize_pool)
    if position == 'QF':
        return round(0.048990263*prize_pool)
    if position == 'R16':
        return round(0.026152979*prize_pool)
    if position == 'R32':
        return round(0.013945333*prize_pool)

def calculate_career_winnings_30(position, prize_pool):
    if position == 'F':
        return round(0.163549434*prize_pool)
    if position == 'SF':
        return round(0.095541486*prize_pool)
    if position == 'QF':
        return round(0.046477317*prize_pool)
    if position == 'R16':
        return round(0.025361288*prize_pool)
    if position == 'R32':
        return round(0.018326287*prize_pool)


def calculate_career_winnings_28(position, prize_pool):
    if position == 'F':
        return round(0.169772015*prize_pool)
    if position == 'SF':
        return round(0.099176562*prize_pool)
    if position == 'QF':
        return round(0.048245644*prize_pool)
    if position == 'R16':
        return round(0.026326212*prize_pool)
    if position == 'R32':
        return round(0.019023549*prize_pool)


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
        male_tournaments = []
        female_tournaments = []
        mixed_tournaments = []
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

            if row[female_tournament_id] != '' and row[male_tournament_id] !='':
                mixed_tournaments.append(tournament)
            elif row[male_tournament_id] != '':
                male_tournaments.append(tournament)
            elif row[female_tournament_id] != '':
                female_tournaments.append(tournament)
            else:
                pass

        # print(headers)
        #
        # print(tournaments)

        return male_tournaments, female_tournaments, mixed_tournaments






def extract_matches_male(tournaments, dataset, players=None):
    with open(dataset, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = reader.fieldnames
        if len(headers) <= 1:
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, delimiter=',')
            headers = reader.fieldnames
        tourney_id = headers[0]
        winner_id = headers[7]
        looser_id = headers[15]
        round = headers[25]
        if players == None:
            players = dict()

        for tournament in tournaments:
            tournament_prize_pool = int(tournament['male_prize_pool'])
            winner_prize = int(tournament['male_winner_prize'])
            total_players = tournament['number_of_players']
            tournament_name = tournament['name']
            t_gender = tournament['tournament_gender']

            for row in reader:
                tournament_id = row[tourney_id]
                if tournament_id == tournament['male_id']:
                    tournament_id = tournament_name+'_'+tournament['year']

                    t_round = row[round] # tournamnet round
                    round_looser = row[looser_id] # round looser

                    if round_looser in players:
                        earnings = calculate_match_winnings(t_round,
                                                            total_players,
                                                            tournament_prize_pool,
                                                            winner_prize,
                                                            t_gender)

                        players[round_looser]['tournaments'][tournament_id] = {'finish': t_round,
                                                                               'earnings': earnings
                                                                               }

                    else:
                        earnings = calculate_match_winnings(t_round,
                                                            total_players,
                                                            tournament_prize_pool,
                                                            winner_prize,
                                                            t_gender)

                        players[round_looser] = {'tournaments':
                                                     {tournament_id:
                                                          {'finish': t_round,
                                                           'earnings': earnings
                                                            },
                                                     }
                                                }

                    if row[round] == 'F':
                        round_winner = row[winner_id] # round winner only needed in final
                        if round_winner in players:
                            players[round_winner]['tournaments'][tournament_id] = {'finish': 'Win',
                                                                                   'earnings': winner_prize
                                                                                   }
                        else:
                            players[round_winner] = {'tournaments':
                                                         {tournament_id:
                                                              {'finish': 'Win',
                                                               'earnings': winner_prize
                                                                },
                                                         }
                                                    }
            csvfile.seek(1)

    return players

def extract_matches_female(tournaments, dataset, players=None):
    with open(dataset, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = reader.fieldnames
        if len(headers) <= 1:
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, delimiter=',')
            headers = reader.fieldnames
        tourney_id = headers[18]
        winner_id = headers[25]
        looser_id = headers[6]
        round = headers[14]

        if players == None:
            players = dict()

        for tournament in tournaments:
            tournament_prize_pool = int(tournament['female_prize_pool'])
            winner_prize = int(tournament['female_winner_prize'])
            total_players = tournament['number_of_players']
            tournament_name = tournament['name']
            t_gender = tournament['tournament_gender']
            for row in reader:
                tournament_id = row[tourney_id]
                if tournament_id == tournament['female_id']:
                    tournament_id = tournament_name+'_'+tournament['year']

                    t_round = row[round] # tournamnet round
                    round_looser = row[looser_id] # round looser

                    if round_looser in players:
                        earnings = calculate_match_winnings(t_round,
                                                            total_players,
                                                            tournament_prize_pool,
                                                            winner_prize,
                                                            t_gender
                                                            )

                        players[round_looser]['tournaments'][tournament_id] = {'finish': t_round,
                                                                               'earnings': earnings
                                                                               }

                    else:
                        earnings = calculate_match_winnings(t_round,
                                                            total_players,
                                                            tournament_prize_pool,
                                                            winner_prize
                                                            ,t_gender
                                                            )

                        players[round_looser] = {'tournaments':
                                                     {tournament_id:
                                                          {'finish': t_round,
                                                           'earnings': earnings
                                                            },
                                                     }
                                                }

                    if row[round] == 'F':
                        round_winner = row[winner_id] # round winner only needed in final
                        if round_winner in players:
                            players[round_winner]['tournaments'][tournament_id] = {'finish': 'Win',
                                                                                   'earnings': winner_prize
                                                                                   }
                        else:
                            players[round_winner] = {'tournaments':
                                                         {tournament_id:
                                                              {'finish': 'Win',
                                                               'earnings': winner_prize
                                                                },
                                                         }
                                                    }
            csvfile.seek(1)

    return players


def extract_player_data_male(dataset, players):
    gender = 'Male'
    with open(dataset, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        player_id = headers[0]
        first_name = headers[1]
        last_name = headers[2]
        birthdate = headers[4]
        height = headers[6]
        wikidata_id = headers[7]
        for player in players:
            for row in reader:
                if row[player_id] == player:
                    if ' ' in row[first_name]:  # replace spaces in last name with underscores for two last names
                        row[first_name] = row[first_name].replace(' ', '_')

                    if ' ' in row[last_name]: # replace spaces in last name with underscores for two last names
                        row[last_name] = row[last_name].replace(' ', '_')

                    players[player]['entity_name'] = f'{row[first_name]}_{row[last_name]}'
                    players[player]['first_name'] = row[first_name]
                    players[player]['last_name'] = row[last_name]
                    players[player]['gender'] = gender
                    players[player]['birthdate'] = row[birthdate]
                    players[player]['height'] = row[height]
                    players[player]['wikidata_id'] = row[wikidata_id]
                    players[player]['participates_in'] = [t for t in players[player]['tournaments']]
                    players[player]['career_winnings'] = sum([players[player]['tournaments'][t]['earnings'] for t in players[player]['tournaments']])
                    break
            csvfile.seek(1)
        return players

def extract_player_data_female(dataset, players):
    gender = 'Female'
    with open(dataset, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        print('headers in ectract plater data fem:', headers)
        player_id = headers[0]
        first_name = headers[1]
        last_name = headers[2]
        birthdate = headers[4]
        for player in players:
            for row in reader:
                if row[player_id] == player:

                    if row[player_id] == player:
                        if ' ' in row[first_name]:  # replace spaces in last name with underscores for two last names
                            row[first_name] = row[first_name].replace(' ', '_')

                    if ' ' in row[last_name]: # replace spaces in last name with underscores for two last names
                        row[last_name] = row[last_name].replace(' ', '_')

                    players[player]['entity_name'] = f'{row[first_name]}_{row[last_name]}'
                    players[player]['first_name'] = row[first_name]
                    players[player]['last_name'] = row[last_name]
                    players[player]['gender'] = gender
                    players[player]['birthdate'] = row[birthdate]
                    players[player]['participates_in'] = [t for t in players[player]['tournaments']]
                    players[player]['career_winnings'] = sum([players[player]['tournaments'][t]['earnings'] for t in players[player]['tournaments']])
                    break
            csvfile.seek(1)
        return players



############# creating triples ################

def rdf_namespace(ent):
    rdf_namespace = '###  http://www.semanticweb.org/edmondagabekian/ontologies/2024/9/untitled-ontology-13#'
    return f'{rdf_namespace}{ent}'

def extract_tournament_to_triples(tournament):
    if tournament['tournament_gender'] == 'Male':
        return male_tournament_triples(tournament)
    elif tournament['tournament_gender'] == 'Female':
        return female_tournament_triples(tournament)
    elif tournament['female_id'] == '':
        return male_tournament_triples(tournament)
    elif tournament['male_id'] == '':
        return female_tournament_triples(tournament)
    elif tournament['tournament_gender'] == 'Both':
        return mixed_tournament_triples(tournament)

def male_tournament_triples(tournament):
    triples = f"""
        {rdf_namespace(f'{tournament["name"]}_{tournament["year"]}')}
         :{tournament['name']}_{tournament['year']} rdf:type owl:NamedIndividual ,
                                            :{tournament['name']} ;
                                    :hasTotalAttendance {tournament['fan_attendance']} ;
                                    :isMaleTournament "true"^^xsd:boolean ;
                                    :hasMalePrizePool {int(tournament['male_prize_pool'])} ;
                                    :hasTotalPrizePool {int(tournament['male_prize_pool'])} ;
                                    :hasMaleFinalsAttendance {tournament['male_viewership']} ;
                                    :hasMaleWinnerPrize {tournament['male_winner_prize']} ;
                                    :hasLevel "{tournament['level']}" ;
                                    :inYear {tournament['year']} .

    """
    return triples

def female_tournament_triples(tournament):
    triples = f"""
        {rdf_namespace(f'{tournament["name"]}_{tournament["year"]}')}
         :{tournament['name']}_{tournament['year']} rdf:type owl:NamedIndividual ,
                                            :{tournament['name']} ;
                                    :hasTotalAttendance {tournament['fan_attendance']} ;
                                    :hasFemalePrizePool {int(tournament['female_prize_pool'])} ;
                                    :isFemaleTournament "true"^^xsd:boolean ;
                                    :hasFemaleFinalsAttendance {tournament['female_viewership']} ;
                                    :hasTotalPrizePool {int(tournament['female_prize_pool'])} ;
                                    :hasFemaleWinnerPrize {tournament['female_winner_prize']} ;
                                    :hasLevel "{tournament['level']}" ;
                                    :inYear {tournament['year']} .

    """
    return triples

def mixed_tournament_triples(tournament):
    print(tournament)
    triples = f"""
        {rdf_namespace(f'{tournament["name"]}_{tournament["year"]}')}
         :{tournament['name']}_{tournament['year']} rdf:type owl:NamedIndividual ,
                                            :{tournament['name']} ;
                                    :hasTotalAttendance {tournament['fan_attendance']} ;
                                    :hasFemalePrizePool {int(tournament['female_prize_pool'])} ;
                                    :hasFemaleFinalsAttendance {tournament['female_viewership']} ;
                                    :hasMalePrizePool {int(tournament['male_prize_pool'])} ;
                                    :isMixedTournament "true"^^xsd:boolean ;
                                    :hasTotalPrizePool {int(tournament['male_prize_pool'])+int(tournament['female_prize_pool'])} ;
                                    :hasMaleFinalsAttendance {tournament['male_viewership']} ;
                                    :hasFemaleWinnerPrize {tournament['female_winner_prize']} ;
                                    :hasMaleWinnerPrize {tournament['male_winner_prize']} ;
                                    :hasLevel "{tournament['level']}" ;
                                    :inYear {tournament['year']} .

    """
    return triples


def extract_male_player_to_triples(player):
    triples = f"""
{rdf_namespace(f'{player["entity_name"]}')}
:{player['entity_name']} rdf:type owl:NamedIndividual ,
                                  :{player['gender']}_Player ;
                        {participatesIn_triple(player['participates_in'])}
                        :hasGender "{player['gender']}" ;
"""
    if player['height'] != '':
        triples+=f"                        :hasHeight {player['height']} ;\n"
    if player['birthdate'] != '':
        triples+=f"                         :hasBirthdate {player['birthdate']} ;\n"
    if player['wikidata_id'] != '':
        triples+=f"""                        :hasWikidataId "{player['wikidata_id']}" ;"""

    triples+=f"""                        :hasCarreerWinnings "{player['career_winnings']}"^^xsd:integer."""

    return triples

def extract_fem_player_to_triples(player):
    if player['birthdate'] == '':
        player['birthdate'] = 0
    triples = f"""
{rdf_namespace(f'{player["entity_name"]}')}
:{player['entity_name']} rdf:type owl:NamedIndividual ,
                                  :{player['gender']}_Player ;
                        {participatesIn_triple(player['participates_in'])}
                        :hasGender "{player['gender']}" ;
        """

    if player['birthdate'] != '':
        triples+=f"                         :hasBirthdate {player['birthdate']} ;\n"

    triples+=f"""                        :hasCarreerWinnings "{player['career_winnings']}"^^xsd:integer."""

    return triples

def participatesIn_triple(tournaments):
    triples = f':participatesIn :{tournaments[0]} ,\n'
    for t in tournaments[1:-1]:
        triples += f'                                        :{t} ,\n'
    triples += f'                                        :{tournaments[-1]} ;'
    return triples

######################## main running functions ##################################


def handle_male_players(male_tournaments, mixed_tournaments):
    # function to go over all atp datasets and extract participating male players, and their rankings in each tournament
    players = None
    datasets = ['./Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2010.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2011.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2012.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2013.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2014.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2015.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2016.csv',
                './Data_Sets/ATP_Dataset/tennis_atp-master/atp_matches_2017.csv'
                ]
    for file in datasets:
        players = extract_matches_male(male_tournaments,file, players)
        players = extract_matches_male(mixed_tournaments, file, players)

    return players

def handle_female_players(female_tournaments, mixed_tournaments):
    # function to go over all atp datasets and extract participating male players, and their rankings in each tournament
    players = None
    datasets = ['./Data_Sets/WTA_Dataset/matches.csv']

    for file in datasets:
        players = extract_matches_female(female_tournaments,file, players)
        players = extract_matches_female(mixed_tournaments, file, players)

    return players


def create_turtle_file(triples):
    if './ontology-entities.ttl':
        open('./ontology-entities.ttl', 'w').close()
    with open('./ontology-no-entities.txt', 'r') as f1, open('./ontology-entities.ttl', 'w') as file:
        for line in f1:
            file.write(line)
        for trip in triples:
            file.write('\n\n')
            file.writelines(trip)
        file.close()



def run_extract_data():
    # get data about torunaments as dict
    male_tournaments, female_tournaments, mixed_tournaments = create_tournament_set('./Data_Sets/tournament_data_id.csv')
    # get matches and calculate winnings of male players as dict
    male_players = handle_male_players(male_tournaments, mixed_tournaments)
    # get matches and calculate winnings of female players as dict
    female_players = handle_female_players(female_tournaments, mixed_tournaments)

    # get male player data into dict with winnings and matches participated
    male_player_data = extract_player_data_male('./Data_Sets/ATP_Dataset/tennis_atp-master/atp_players.csv', male_players)
    # get female player data into dict with winnings and matches participated
    female_player_data = extract_player_data_female('./Data_Sets/WTA_Dataset/players.csv', female_players)

    triples = []

    for tournament in male_tournaments:
        triples.append(extract_tournament_to_triples(tournament))
    for tournament in female_tournaments:
        triples.append(extract_tournament_to_triples(tournament))
    for tournament in mixed_tournaments:
        triples.append(extract_tournament_to_triples(tournament))


    for player in male_player_data:
        triples.append(extract_male_player_to_triples(male_player_data[player]))

    for player in female_player_data:
        triples.append(extract_fem_player_to_triples(female_player_data[player]))


    create_turtle_file(triples)


run_extract_data()
