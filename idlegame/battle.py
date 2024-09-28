from typing import List
from idlegame.data import AutosavedPlayer
from idlegame.nanobots import Nanobot
import random

def simulate_defense(player: AutosavedPlayer, defending_bots: List[Nanobot]) -> int:
    """Simulate defense against invasions using the given nanobots.

    Args:
        player (AutosavedPlayer): The player who owns the nanobots.
        defending_bots (List[Nanobot]): The nanobots assigned to defend.

    Returns:
        int: The number of nanobots that were broken during the defense.
    """
    if not defending_bots:
        return 0  # No bots to defend

    # Calculate total defense power from the defending bots
    total_defense_power = sum(bot.defense_rating for bot in defending_bots)

    # Simulate the invasion strength (could be a random number or based on game state)
    invasion_strength = random.randint(1, 10)  # Example invasion strength
    print(f"Invasion strength: {invasion_strength}, Total defense power: {total_defense_power}")

    # Calculate the ratio of defense power to invasion strength
    defense_ratio = total_defense_power / invasion_strength if invasion_strength > 0 else 1

    # Determine the chance of breaking bots based on defense ratio
    # If defense_ratio is high, break chance is low; if low, break chance is high
    # Exponential scaling for break chance:
    if defense_ratio >= 2:
        break_chance = 0  # Strong advantage
    elif defense_ratio >= 1:
        break_chance = (1 - (defense_ratio - 1) / 1) * 0.5  # Linear decrease
    else:
        # Exponential growth in break chance for heavily disadvantaged scenario
        break_chance = min(1, 0.5 * (1 - defense_ratio))  # Break chance up to 50% max

    bots_broken = 0

    # Determine how many bots break based on calculated break chance
    for bot in defending_bots:
        if random.random() < break_chance:
            player.nanos.remove(bot)  # Remove the broken bot from the player's list
            print(f"One of your defending bots, '{bot.name}', was broken during an invasion!")
            bots_broken += 1

    if bots_broken == 0:
        print(f"Your defenses held against an invasion (Strength: {invasion_strength}).")

    return bots_broken
