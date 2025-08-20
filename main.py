import asyncio

from src.game import Game

game = Game()

async def main_loop():
    await game.run_async()

asyncio.run(main_loop())
