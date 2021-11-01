# Midnight Rider
import random
import sys
import textwrap
import time
import midnight_rider_text


# A text-based game of intrigue and illusion

#CONSTANTS
MAX_FUEL = 50
MAX_TOFU = 3

class Game:
    """Represent our game engine

    Attributes:
        done:Discribes the game is finished or not - bool
        distance traaveled: describe the distances that we"ve traveled so far this game
        ,in km
        amount _of_tofu: how much tofu we  have left in our inventory
        agents_distance:describe the distance between the player and the agents
        fuel:describes amount of fuel remaining
            starts off at 50
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_tofu = MAX_TOFU
        self.agents_distance = -25
        self.fuel = MAX_FUEL


    def introduction(self) -> None:
        """Print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        #Get the user"s response
        user_choice = input().strip(" ,.?!@#").lower()
        #Based on their choice, change the attributes
        #of the class

        agents_distance_now = random.randrange(7, 15)

        if user_choice == "b":
            # Move the player
            player_distance_now = random.randrange(5, 10)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(3, 8)

            # Give the player some feedback
            print(f"\n-------You drive conservatively.")
            print(f"-------You traveled {player_distance_now} kms.\n")



        elif user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(5, 11)

            # Give the player some feedback
            print(f"\n-------ZOOOOOOOOOOM.")
            print(f"-------You traveled {player_distance_now} kms.\n")



        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += random.randomrange(7,15)

            #Give the user"s feedback
            print(midnight_rider_text.REFUEL)
            #Decide how far agents go
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled:{self.distance_traveled}kms")
            print(f"Tofu left:{self.amount_of_tofu}")
            print(f"Agents distance:{abs(self.agents_distance)}km away")
            print(f"Fuel remanings:{self.fuel}L")
            print("---")
            time.sleep(1)
        elif user_choice == "q":
            self.done = True





def main() -> None:
    pass
    game = Game()
    game.introduction()

    while not game.done:
        #TODO:Display the choices to the player.
        game.show_choices()
        #TODO:Ask the player what they want to do.
        #TODO:Change the state of the environment.

        game.get_choice()
        #TODO:Check win/lose condition.



if __name__ == "__main__":
    main()
