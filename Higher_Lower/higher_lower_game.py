from game_data import data
from random import choice

my_celebs = data
some_dic = {}

def get_new_celebrity(list_dic_celebs):
    celeb = choice(list_dic_celebs)
    list_dic_celebs.remove(celeb)
    return celeb

def display_celeb_info(celeb_info):
    return f"{celeb_info["name"]}, a {celeb_info["description"]}, from {celeb_info["country"]}."

def check_followers(celeb1, celeb2):
    if celeb1["follower_count"] > celeb2["follower_count"]:
        return celeb1
    else:
        return celeb2


some_dic["A"] = get_new_celebrity(my_celebs)
some_dic["B"] = get_new_celebrity(my_celebs)
score = 0

while True:
    print("A: " + display_celeb_info(some_dic["A"]))
    print("B: " + display_celeb_info(some_dic["B"]))

    answer = input("Who has more followers on Instagram? A or B? ").upper()
    print("\n" * 100)

    if some_dic[answer] == check_followers(some_dic["A"], some_dic["B"]):
        score += 1
        print(f"You're right! Current score: {score}")
        if not my_celebs:
            print(f"You win! Final score: {score}")
            break
        some_dic["A"] = some_dic[answer]
        some_dic["B"] = get_new_celebrity(my_celebs)
    else:
        print(f"Nope, You lose! Final score: {score}")
        break    




