import time
import random
import sys


def print_pause(message):
    print(message)
    time.sleep(2)


def start(enemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                f" and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def door_or_cave(weapon, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    player_input = validate_input("(Please enter 1 or 2.)", ["1", "2"])
    if player_input == "1":
        house(weapon, enemy)
    else:
        cave(weapon, enemy)


def house(weapon, enemy):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_pause(f"You feel a bit under-prepared for this,"
                    f" what with only having a tiny {weapon}.")
        fight_or_run(weapon, enemy)
    else:
        fight_or_run(weapon, enemy)


def fight_or_run(weapon, enemy):
    player_input = validate_input(
        "Would you like to (1) fight or (2) run away?\n", ["1", "2"])
    if player_input == "1":
        if weapon == "dagger":
            enemy_win(enemy)
            play_again()
        else:
            player_win(enemy)
            play_again()
    else:
        run_away(weapon, enemy)


def run_away(weapon, enemy):
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been followed.\n")
    door_or_cave(weapon, enemy)


def cave(weapon, enemy):
    print_pause("You peer cautiously into the cave.")
    if weapon == "dagger":
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    " take the sword with you.")
        print_pause("You walk back out to the field.")
        weapon = "magical Sword of Ogoroth"

    else:
        here_before()
        weapon = "magical Sword of Ogoroth"
    door_or_cave(weapon, enemy)


def here_before():
    print_pause("You've been here before, "
                "and gotten all the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")


def player_win(enemy):
    print_pause(f"As the {enemy} moves to attack, "
                f"you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your"
                " hand as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your"
                f" shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")


def play_again():
    player_input = validate_input(
        "Would you like to play again? (y/n)", ["y", "n"])
    if player_input == "y":
        print_pause("Excellent!!!\nRestarting the game...\n")
        game_start()
    else:
        print_pause("Thanks for playing. See you later")
        sys.exit()


def enemy_win(enemy):
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")


def validate_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option not in options:
            print_pause("Please enter a valid input\n")
        else:
            return option


def game_start():
    enemy_list = ["pirate", "troll", "dragon", "gorgon", "wicked fairie"]
    enemy = random.choice(enemy_list)
    weapon = "dagger"
    start(enemy)
    door_or_cave(weapon, enemy)


if __name__ == "__main__":
    game_start()
