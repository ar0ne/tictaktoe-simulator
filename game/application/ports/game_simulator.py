from typing import Protocol


class IGameSimulator(Protocol):

    def run_simulation(self) -> None:
        ...

    def display_state(self) -> None:
        ...