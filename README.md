# What is it

This is sandbox for game simulations without user interactions. All user's moves decided by randomizer.
At present, it could simulate following games:

- 'tictactoe'.

## How to use

### Setup environment
```commandline
uv sync
```

### Now you could use CLI application to run simulations

For example, you might want to run 'local' simulation for users *Bob* and *Alice*.
```commandline
uv run main.py Alice Bob
```

### Remote simulation

To simulate remote player you could run `server.py` that starts simple http server on port `:8080`.
For it, you need to install additional dependencies:

```commandline
uv sync --group demo
```

To run server, run:

```commandline
uv run server.py
```

Now you can use "remote" mode in CLI application:

```commandline
uv run main.py Alice Bob -m remote --remote-url=http://localhost:8080
```

To see all available options use help:

```commandline
uv run main.py --help
 
usage: Game Simulation [-h] [-m {remote,local}] [-t {tictactoe}] [-l {debug,info,warning,error}] [-r REMOTE_URL] player1 player2

Simulator of automated display rounds for TicTacToe

positional arguments:
  player1               Name of Player 1
  player2               Name of Player 2

options:
  -h, --help            show this help message and exit
  -m, --mode {remote,local}
                        Player simulation mode. Default: 'local'
  -t, --type {tictactoe}
                        Game type for simulation
  -l, --log-level {debug,info,warning,error}
                        Logging level. Default: 'info'
  -r, --remote-url REMOTE_URL
                        Uri for remote host simulation mode
```