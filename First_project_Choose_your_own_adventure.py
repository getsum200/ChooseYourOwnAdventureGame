print("Welcome to my first project")
print("This is a choose your own adventure game")
#name = str(input("What is your name? "))
#age = int(input("How old are you? "))

def save_player_info(name, age):
    # Save the player's name and age to a file
    with open("player_info.txt", "w") as file:
        file.write(name + "\n" + str(age))

def load_player_info():
    try:
        # Try to load the player's info from the file
        with open("player_info.txt", "r") as file:
            data = file.read().strip().split("\n")
            name = data[0]
            age = int(data[1])
            return name, age
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None, None

def get_player_info():
    name, age = load_player_info()
    if name is None:
        # If the player's info wasn't loaded from the file, ask the user to enter it
        name = input("What's your name? ")
        age = int(input("How old are you? "))
        save_player_info(name, age)
    return name, age


def game():
    health = 20
    name, age = get_player_info()
    if age >= 20:
        print("Great! You're old enough to play")
        wants_to_play = input("Do you think you're good enough to beat this game? ").lower()
        if wants_to_play == "yes":
            print("You start with ", health, "health")
            print("Let's begin")

            left_or_right = input("This one should be easy enough for you... Left or Right path? (left/right) ")
            if left_or_right == "left":
                ans = input("You follow a path and reach a large ominous castle... You going inside or following the path elsewhere? (castle/path) ")
                if ans == "path":
                    path_ans = ("After following the path for a while you find a lake... swim to the other side or fish for dinner? (swim/fish) ")
                    if path_ans == "swim":
                        print("You haven't learn how to swim")
                        print("You drowned and died")
                    elif path_ans == "fish":
                        print("Timmy finds you while your back is turned and shoots you")
                        print("He shoots you and you die")
                    else: 
                        print("Guess who just died... You")
                elif ans == "castle":
                    castle_ans = input("You found a locked chest... kick it or take the stairs further up the castle? (Kick/stairs) ")
                    if castle_ans == "kick":
                        print("The chest flies open, there's a white light...")
                        print("You died")
                    elif castle_ans == "stairs":
                        print("You found Timmy's room")
                        print("He shoots you and you die")
                    else:
                        print("Guess who just died... You")
                else:
                    print("Guess who just died... You")
            else:
                print("Timmy found you and shot you")
                print("You died on round 1... I should have known")
        else:
            print("Why did you bother wasting both of our times...")
            print("You can leave now")
    elif age >=13:
        print("You can play but bring a spare pare of pants")
    else:
        print("You're not old enough to play.")
        print("You can leave now")

game()