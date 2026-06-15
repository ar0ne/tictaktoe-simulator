from typing import Protocol


class IGameSimulator(Protocol):
    """
    Interface for game simulations
    """

    def run_simulation(self) -> None:
        ...

    def display_state(self) -> None:
        ...
