import argparse
import importlib
import json
import string
from typing import Any, Protocol


class MusicPlayer(Protocol):
    """Defines the Music Player interface, to be implemented by objects that can play music
    in a format they want."""

    def play(self) -> None:
        """Plays music"""
        ...


class MusicPlayerFactory:
    """Dynamic factory that creates MusicPlayers. It automatically looks for the
    right MusicPlayer in the `players` module given the potential name of it."""

    def __init__(self, name: str) -> None:
        """Initializes the class, parsing the given name.
        Args:
            name (str): service name."""
        self.module_name = "players." + name.lower().strip()
        self.player_name = name.upper() + "Player"

    def get_music_player(self, init: dict[str, Any]) -> MusicPlayer:
        """Finds the right Music Player to create.
        Returns:
            initialized music player (MusicPlayer)
        Raises:
            ModuleNotFoundError | AttributeError"""
        try:
            player = getattr(
                importlib.import_module(self.module_name), self.player_name
            )
        except ModuleNotFoundError:
            print(f"Module {self.module_name} does not exist.")
            raise
        except AttributeError:
            print(f"Music Player {self.player_name} has not been implemented yet.")
            raise

        print(f"Initializing {self.player_name}")
        return player(**init)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="Player name: mp3, flac, wav, etc.",
        required=True,
    )
    parser.add_argument(
        "--init",
        help="Init arguments to initialize the music players",
        required=True,
    )
    args = parser.parse_args()

    name = args.name
    init = json.loads(args.init)

    factory = MusicPlayerFactory(name)

    player = factory.get_music_player(init)
    player.play()


if __name__ == "__main__":
    main()
