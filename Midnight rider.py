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
MAX_HUNGER = 50
MAX_DISTANCE = 100
TOFU_REFILL_PERCENTAGE = 0.1

ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL":2,
    "LOSE_HUNGER":3,
    "WIN":4
}

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
        hunger:Describes how hungry our player is.
            represented by number between 0 to 50.
            If hunger goes beyond 50, game is over
        endgame_reason: Shows the index of the game ending txt from midnight_rider_text_.py


    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_tofu = MAX_TOFU
        self.agents_distance = -25
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0


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

        if user_choice == "a":
            if self.amount_of_tofu > 0:
                self.amount_of_tofu -= 1
                self.hunger = 0
                print(midnight_rider_text.EAT_TOFU)
            else:
                print(midnight_rider_text.NO_TOFU)


        elif user_choice == "b":
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
            self.fuel -= random.randrange(5, 15)

            # Give the player some feedback
            print(f"\n-------ZOOOOOOOOOOM.")
            print(f"-------You traveled {player_distance_now} kms.\n")



        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += agents_distance_now

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

        if user_choice in ["a", "b", "c"]:
            self.hunger += random.randrange(10, 20)
    def upkeep(self) -> None:
        """Give the user reminders of hunger

        Process random events"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

            # A percentage of time, The tofu bag is filled
            #by the dog

        if random.random() <= TOFU_REFILL_PERCENTAGE and self.amount_of_tofu < MAX_TOFU:
            #Refill the tofu
            #display the text
            self.amount_of_tofu = MAX_TOFU
            print(midnight_rider_text.REFILL_TOFU)


    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
        If they're met, change the self.done flag"""
        #TODO: WIN - Reach the goal


        if self.agents_distance >= 0:
            #Allows us to quit the while loop
            self.done = True
            #Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]
        if self.fuel <= 0:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]

        if self.hunger >= MAX_HUNGER:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]

        if self.distance_traveled >= MAX_DISTANCE:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["WIN"]



def main() -> None:
    pass
    game = Game()
    #game.introduction()
    #Main game loop

    while not game.done:
        game.upkeep()
        game.show_choices()
        game.get_choice()
        game.check_endgame()
    time.sleep(3)
    #print out the ending
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )

if __name__ == "__main__":
    main()
