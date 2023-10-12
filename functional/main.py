import argparse
import importlib
from typing import Callable


type MusicPlayer = Callable[[], None]

def get_music_player(name: str) -> MusicPlayer:
    """Finds the right Music Player to create.
    Returns:
        music player (MusicPlayer)
    Raises:
        ModuleNotFoundError | AttributeError"""
    module_name = "players." + name.lower().strip()

    try:
        play = getattr(importlib.import_module(module_name), "play")
    except ModuleNotFoundError:
        print(f"Module {module_name} does not exist.")
        raise

    print(f"Initializing {name.upper()} player")
    return play


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="Player name: mp3, flac, wav, etc.",
        required=True,
    )
    args = parser.parse_args()

    name = args.name

    play = get_music_player(name)
    play()


if __name__ == "__main__":
    main()
