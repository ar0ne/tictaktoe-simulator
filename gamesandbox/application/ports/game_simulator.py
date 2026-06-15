from typing import Protocol


class IGameSimulator(Protocol):
    """
    Interface for gamesandbox simulations
    """

    def run_simulation(self) -> None: ...

    def display_state(self) -> None: ...
