import asyncio

from src.game import Game

game = Game()

async def main_loop():
    await game.run()

asyncio.run(main_loop())
