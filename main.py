import random
import time
from threading import Thread, Timer



class Player:
    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.technical_stats = {
            'finishing': 60,
            'passing': 60,
            'technique': 60,
            'dribbling': 60,
            'first touch': 60,
            'set pieces': 60,
            'penalties': 60,
            'tackling': 60,
            'long shots': 60,
            'crossing': 60,
            'heading': 60,
            'long throws': 60
        }

        self.mental_stats ={
            'aggression': 60,
            'anticipation': 60,
            'marking': 60,
            'concentration': 60,
            'decisions': 60,
            'composure': 60,
            'off ball': 60,
            'positioning': 60,
            'teamwork': 60,
            'vision': 60,
            'work rate': 60,            
        }

        self.physical_stats ={
            'stamina':60,
            'pace': 60,
            'acceleration': 60,
            'strength': 60,
            'jumping': 60,
            'agility': 60,
            'balance': 60
        }

        self.goalkeeping_stats = {
            'gk positioning': 60,
            'gk reflex': 60,
            'gk handling': 60,
            'gk one on one': 60,
            'gk diving': 60,
        }
        self.goals = 0
        self.assists = 0

        def __str__(self):
            return f"{self.name} ({self.age}y/o, {self.general_rating}, {self.position}) - Goals: {self.goals}, Assists: {self.assists}"

class Club:

    def __init__(self):
        self.goal = 0

    def change(self, score):
        self.goal+=1

    def show_squad(self):
        print(f"\n{self.name} Squad:")
        for player in self.players:
            print(f"- {player}")


class MatchEvent():
    
    
    
    def get_weight(self, player,attk_modifier,midf_modifier,def_modifier,gk_modifier):
        Base_weight = round(random.uniform(0.3,0.7),3) 
        position_modifier = round(random.uniform(0.9,1.1),2)
        if player.position in ['ST','SS','LW','RW']:
            position_modifier = attk_modifier
        elif player.position in ['LM','RM','CAM','CDM','CM','LWB','RWB']:
            position_modifier = midf_modifier
        elif player.position in ['LB','CB','RB']:
            position_modifier = def_modifier
        elif player.position == 'GK':
            position_modifier = gk_modifier
        return Base_weight*position_modifier

    def execute(self, player):
        pass

    def execute_match(self,player,club):
        pass

    def find_difficulty(self,player):
        difficulty = 0
        return difficulty

    def get_physical_stats_average(self,player):
        total_physical_stats = 0
        for x in player.physical_stats:
            total_physical_stats += player.physical_stats[x]
        return total_physical_stats/len(player.physical_stats)

class AttackEvent(MatchEvent):
    
   
    def find_difficulty(self,player):
        attribute_modifier = 1.0
        random_factor = random.uniform(-0.6,1)*10-3
        total_attack_attributes = player.technical_stats['finishing']+player.technical_stats['heading']+player.technical_stats['first touch']+player.technical_stats['heading']+player.technical_stats['long shots']+player.technical_stats['set pieces']/5+player.technical_stats['penalties']/5+player.mental_stats['composure']+player.mental_stats['anticipation']+player.mental_stats['decisions']+player.mental_stats['off ball']
        attack_attributes_average = total_attack_attributes/11
        average_physical_stats = super().get_physical_stats_average(player)
        attribute_modifier = (attack_attributes_average+average_physical_stats+1//10)//3.3+((attack_attributes_average+average_physical_stats//10)%3.3 >= 5)
        return (attribute_modifier+random_factor)//10 + (attribute_modifier%10 >= 5)

    def execute(self, player,club):
        player.goals += 1
        
        print(f" Goal by {player.last_name}!")

    def execute_match(self, player):
        return super().execute_match(player)
    
class AssistEvent(MatchEvent):
    
    
    def find_difficulty(self,player):
        attribute_modifier = 1.0
        random_factor = random.uniform(-0.6,1)*10-3
        total_assist_attributes = player.technical_stats['passing']+player.technical_stats['technique']+player.technical_stats['first touch']+player.technical_stats['dribbling']+player.technical_stats['crossing']+player.technical_stats['set pieces']/5+player.mental_stats['composure']+player.mental_stats['vision']+player.mental_stats['decisions']+player.mental_stats['off ball']+player.mental_stats['teamwork']
        assist_attributes_average = total_assist_attributes/11
        average_physical_stats = super().get_physical_stats_average(player)
        attribute_modifier = (assist_attributes_average+average_physical_stats//10)//3.3+((assist_attributes_average+average_physical_stats//10)%3.3 >= 5)
        return (attribute_modifier+random_factor)//10 + (attribute_modifier%10 >= 5)

    def execute(self, player):
        player.assists += 1
        print(f"Great creativity led to an assist by {player.last_name}!")

class PlaymakingEvent(MatchEvent):
     
    def find_difficulty(self,player):
        attribute_modifier = 1.0
        random_factor = random.uniform(-0.6,1)*10-3
        total_playmaking_attributes = player.technical_stats["long throws"]/5+player.technical_stats['passing']+player.technical_stats['technique']+player.technical_stats['first touch']+player.technical_stats['dribbling']+player.technical_stats['set pieces']/5+player.mental_stats['composure']+player.mental_stats['vision']+player.mental_stats['decisions']+player.mental_stats['off ball']+player.mental_stats['teamwork']
        playmaking_attributes_average = total_playmaking_attributes/10
        average_physical_stats = super().get_physical_stats_average(player)
        attribute_modifier = (playmaking_attributes_average+average_physical_stats//10)//3.3+((playmaking_attributes_average+average_physical_stats//10)%3.3 >= 5)
        return (attribute_modifier+random_factor)//10 + (attribute_modifier%10 >= 5)
    
    def execute(self, player):
        print(f" Brilliant playmaking by {player.last_name}!")

class DefendEvent(MatchEvent):
    
    def find_difficulty(self,player):
        attribute_modifier = 1.0
        random_factor = random.uniform(-0.6,1)*10-3
        total_defend_attributes = player.technical_stats['tackling']+player.technical_stats['heading']+player.mental_stats['marking']+player.mental_stats['positioning']+player.mental_stats['concentration']+player.mental_stats['decisions']+player.mental_stats['anticipation']+player.mental_stats['teamwork']+player.mental_stats['aggression']
        defend_attributes_average = total_defend_attributes/9
        average_physical_stats = super().get_physical_stats_average(player)
        attribute_modifier = (defend_attributes_average+average_physical_stats//10)//3.3+((defend_attributes_average+average_physical_stats//10)%3.3 >= 5)
        return (attribute_modifier+random_factor+random_factor)//10 + (attribute_modifier%10 >= 5)

    def execute(self, player):
        print(f"Great tackle by {player.last_name}!")

class GoalkeepingEvent(MatchEvent):

    def find_difficulty(self,player):
        random_factor = random.uniform(-0.6,1)*10-3
        attribute_modifier = 1.0
        total_gk_attributes = sum(stat for stat in player.goalkeeping_stats.values())+player.mental_stats["anticipation"]+player.mental_stats["decisions"]+player.mental_stats["concentration"]
        gk_attributes_average = total_gk_attributes/8
        average_physical_stats = super().get_physical_stats_average(player)
        attribute_modifier = (gk_attributes_average+average_physical_stats//10)//3.3+((gk_attributes_average+average_physical_stats//10)%3.3 >= 5)
        return (attribute_modifier+random_factor)//10 + (attribute_modifier%10 >= 5)


    def execute(self, player ):
        print(f"Great save by {player.last_name}!")
class MatchEngine:

    def __init__(self):

        self.event_strategies = [
            AttackEvent(),
            DefendEvent(),
            AssistEvent(),
            PlaymakingEvent(),
            GoalkeepingEvent(),
        ]
        
        self.answer = None
        self.correct = False
        

    def generate_question(self,difficulty):
        if difficulty == 0:
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)
            answer = n1+n2
            time_counted = 9
            question = f"what is {n1} + {n2}?"
        elif difficulty == 1:
            n1 = random.randint(1,10)
            n2 = random.randint(1,10)
            answer = n1*n2
            time_counted=5
            question = f"what is {n1} X {n2}?"
        elif difficulty == 2:
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)
            answer = n1-n2
            time_counted = 8
            question = f"what is {n1} - {n2}?"
        elif difficulty == 3:
            n1 = random.randint(10,100)
            n2 = random.randint(1,10)
            answer = n1/n2
            while n1%n2 != 0:
                n1 = random.randint(10,100)
                n2 = random.randint(1,10)
            answer = n1/n2
            time_counted = 6
            question = f"what is {n1} ÷ {n2}?"
        elif difficulty == 4:
            n1 = random.randint(20,100)
            n2 = random.randint(1,20)
            answer = n1%n2
            time_counted = 8
            question = f"what is the remainder of {n1} ÷ {n2}?"
        elif difficulty == 5:
            n1 = random.randint(1,1000)
            n2 = random.randint(1,1000)
            answer = n1+n2
            time_counted = 12
            question = f"what is {n1} + {n2}?"
        elif difficulty == 6:
            n1 = random.randint(1,21)
            n2 = random.randint(1,21)
            answer = n1*n2
            time_counted = 9
            question = f"What is {n1} X {n2}?"
        return [answer,time_counted,question]

    def check_timeout(self, question, correct_answer):
        if self.answer is None:
            print("\nTime's up! Please press enter to continue")

   

    def reload_weight(self,player):
        weight_list = [
            [self.event_strategies[0],self.event_strategies[0].get_weight(player,1.39,1.22,1.11,0)],
            [self.event_strategies[1],self.event_strategies[1].get_weight(player,1.34,1.4,1.12,0)],
            [self.event_strategies[2],self.event_strategies[2].get_weight(player,1.1,1.35,1.2,1.05)],
            [self.event_strategies[3],self.event_strategies[3].get_weight(player,1.05,1.2,1.41,0)],
            [self.event_strategies[4],self.event_strategies[4].get_weight(player,0,0,0,1.7)]
            ]
        return weight_list

    def simulate_match(self, player):
        injury_time = random.randint(1,11)
        events = []
        work_rate_balancer = random.randint(3,13)
        player_team_goals = 0
        opponent_team_goals = 0
        work_rate_modifier = player.mental_stats['work rate']/(79+work_rate_balancer)  
         
        for minute in range(1, 91+injury_time):
            event_roll = random.randint(1, 1000)
            if event_roll >= (900/(1.1*(work_rate_modifier))):
                events.append(minute)
        while len(events) <3:
            rand = random.randint(1,91+injury_time)
            while rand in events:
                rand = random.randint(1,91+injury_time)
            events.append(rand)
        
        for x in range(1,91+injury_time):
            if x in events:
                biggest_weight = 0
                event_chosen = None
                weight_list = self.reload_weight(player)
                '''
                for event in self.event_strategies:
                
                    weight = event.get_weight(player)
                    if biggest_weight < weight:
                        biggest_weight = weight
                        event_chosen = event
                '''
                for event_related in weight_list:
                    if biggest_weight < event_related[1]:
                        biggest_weight = event_related[1]
                        event_chosen = event_related[0]
                difficulty = event_chosen.find_difficulty(player)
                correct_answer, time_counted, question = self.generate_question(difficulty)
                
                timer = Timer(time_counted, self.check_timeout, args=(question, correct_answer))
                timer.daemon = True
                timer.start()
                
                print(f"{question} (You have {time_counted} seconds): ")
                user_answer = input()
                
                if not timer.is_alive():
                    print("You were too slow!")
                else:
                    timer.cancel()
                    if user_answer == str(correct_answer):
                        print("Correct!")
                        event_chosen.execute(player)
                        if isinstance(event_chosen, AttackEvent) or isinstance(event_chosen,AssistEvent):
                            player_team_goals += 1
                            print(f"{player_team_goals}:{opponent_team_goals}")
                    else:
                        print("Failed the opportunity!")
                        if isinstance(event_chosen, GoalkeepingEvent) or isinstance(event_chosen,DefendEvent):
                            opponent_team_goals += 1
                            print(f"A goal was conceded!\n{player_team_goals}:{opponent_team_goals}")
                
                
        print(f"Match Ended! \nFinal score: {player_team_goals}:{opponent_team_goals}")


def stat_points_handling(all_stats,stat_points):
    for stat in all_stats:
        print(stat, all_stats[stat])
        changed_stat = input(f"{stat} = {all_stats[stat]}: {stat_points} points left. How much would you like to upgrade this stat? ")
        torf = False
        while torf == False:
            try:
                changed_stat = int(changed_stat)
                torf = True
            except:
                changed_stat = input(f"invalid input: please enter again.\n{stat_points} points left. How much would you like to upgrade this stat? ")
        print(changed_stat,type(changed_stat))
        while stat_points - changed_stat <0 or all_stats[stat] + changed_stat > 99:
            changed_stat = input(f"not enough stat points left or exceeded limit: please enter again.\n{stat_points} points left. How much would you like to upgrade this stat? ")
            torf = False
            while torf == False:
                try:
                    changed_stat = int(changed_stat)
                    torf = True
                except:
                    changed_stat = input(f"invalid input: please enter again.\n{stat_points} points left. How much would you like to upgrade this stat? ")

        all_stats[stat] += changed_stat
        stat_points -= changed_stat
    return all_stats

    
def main():
    game = True
    positions = ["GK","LWB","LB","CB","RB","RWB","CDM","LM","CM","RM","CAM","LW","SS","RW","ST"]
    first_name = input("please enter your player's first name: ")
    last_name = input("please enter your player's last name: ")
    position = input("please enter your player's position: ").upper()
    while position not in positions:
        position = input("invalid positon, please select a valid position: ").upper() 
    user_player = Player(first_name,last_name,position)
    user_player.__str__()
    physical_stat_points = 110
    user_player.physical_stats = stat_points_handling(user_player.physical_stats,physical_stat_points)
    mental_stat_points = 120
    user_player.mental_stats = stat_points_handling(user_player.mental_stats,mental_stat_points)
    if position != "GK":
        technical_stat_points = 140
        user_player.technical_stats = stat_points_handling(user_player.technical_stats,technical_stat_points)
    else:
        gk_stat_points = 95
        user_player.goalkeeping_stats = stat_points_handling(user_player.goalkeeping_stats,gk_stat_points)
    game = True
    while game:
        print("Game Start!")
        curMatch = MatchEngine()
        curMatch.simulate_match(user_player)
        game = False

main()
    