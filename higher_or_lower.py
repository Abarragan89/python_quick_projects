import game_data 
import art
import random


print(art.logo)
def pick_two_random_number():
  """Picks two random numbers and ensures they are different"""
  random_num_1 = random.randint(0, len(game_data.data) - 1)
  random_num_2 = random.randint(0, len(game_data.data) - 1)
  while random_num_1 == random_num_2:
    random_num_2 = random.randint(0, len(game_data.data) - 1)
  return [random_num_1, random_num_2]

def pick_one_random_person(past_person):
  """Picks one random person and ensures it is not a duplicate of another"""
  random_person = game_data.data[random.randint(0, len(game_data.data) - 1)]
  while random_person['name'] == past_person['name']:
    random_person = game_data.data[random.randint(0, len(game_data.data) - 1)]
  return random_person

def determine_higher(person_1, person_2):
  """Determines the higher person between two"""
  if person_1['follower_count'] > person_2['follower_count']:
    return person_1
  else:
    return person_2
  


  
def game_loop(person_1, person_2, score):
  #determine higher person: 
  higher_person = determine_higher(person_1, person_2)
  # show score if score is higher than 1:
  if score > 0: 
    print(f"You're right! Current score: {score}")
  print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
  print(art.vs)
  print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")
  # determine what the user picked
  user_answer = input("Who has more followers? Type 'A' or 'B' ").lower()
  if user_answer == 'a':
    user_response = person_1['name']
  elif user_answer == 'b':
    user_response = person_2['name']
  else:
    print('Invalid response')
  # evaluate results
  if user_response == higher_person['name']:
    print('correct')
    score += 1
    next_person = pick_one_random_person(higher_person)
    game_loop(higher_person, next_person, score)
  elif user_response != higher_person:
    print('wrong')

    
def start_game():
  """Starts Holds all the game logic"""
  # start with two random numbers
  random_two_array = pick_two_random_number()
  person_1 = game_data.data[random_two_array[0]]
  person_2 = game_data.data[random_two_array[1]]
  #start loop
  game_loop(person_1, person_2, score=0)
       
    

start_game()
