# Minesweeper Game

This project is an implementation of the classic Minesweeper game in Python. It was developed as a school project for Ada Tech School.

## Project Structure

The project is organized into several Python files:

- `game.py`: Contains the main `Game` class that manages the game flow.
- `grid.py`: Implements the `Grid` class representing the game board.
- `cell.py`: Defines the `Cell` class for each individual cell on the grid.
- `main.py`: to instanciate and run the program
  

## Features

- Random generation of game grids
- Command-line interface for gameplay
- Recursive revealing of empty cells
- End-game detection (win or lose)

## How to Play

1. Run the main file (main.py`).
2. Follow the on-screen instructions to choose a row and column.
3. Continue playing until you've revealed all non-bomb cells or hit a bomb.

## Unit Tests

Each Python file in the project is accompanied by a corresponding unit test file:

- `test_game.py`
- `test_grid.py`
- `test_cell.py`

These tests ensure the proper functioning of each game component.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/solena8/demineur.git
   ```
2. Navigate to the project folder:
   ```
   cd demineur
   ```
3. Run the game :
   ```
   python main.py
   ```

## Contribution

As this is a school project, external contributions are generally not accepted. However, feedback and suggestions are welcome!

## About Ada Tech School

This project was completed as part of the curriculum at [Ada Tech School](https://adatechschool.fr/), an innovative programming school based in France.
