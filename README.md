# Connect-Four
This project is a Python implementation of the classic Connect Four game, featuring a command-line interface, AI opponent, and error handling for robust gameplay. It provides an engaging experience for players while showcasing key programming concepts such as algorithms, object-oriented design, and testing. Below is a detailed description of its components and features.

Key Features
Command-Line Interface (CLI):
The game is played through a user-friendly CLI implemented in the UI class.
Players can take turns with the AI by inputting their desired column for placing their token.
The interface includes prompts for restarting the game or exiting after a match.

AI Opponent:
The AI uses the Minimax Algorithm with alpha-beta pruning to make strategic decisions.
The algorithm evaluates possible moves up to a certain depth to determine the best move for the computer.
The AI ensures challenging gameplay by simulating competitive decision-making.

Game Mechanics:
Players alternate turns, placing tokens in one of seven columns on the board.
The game ends when a player or the AI connects four tokens horizontally, vertically, or diagonally, or when the board is full (resulting in a draw).
The Game class manages player and AI moves while checking for win conditions.

Error Handling:
Custom exceptions (GameError and BoardError) ensure that invalid moves (e.g., selecting a full column or invalid input) are handled gracefully without crashing the program.
Players are notified of errors and prompted to try again.

Unit Testing:
Comprehensive testing is implemented using Python's unittest framework.
Tests validate core functionalities such as board updates, AI behavior, and game logic to ensure correctness and reliability.

Object-Oriented Design:
The program is modular, with separate classes for the board (Board), AI (AI), game logic (Game), and user interface (UI).
This structure promotes code reusability and scalability.

How It Works

Game Initialization:
The program starts by displaying a welcome message and initializing the game board.
Players are prompted to take their turn by entering a column number (0-6).

Player vs AI Gameplay:
The player places their token ("red") in the selected column.
The AI responds by evaluating the board using the Minimax algorithm and placing its token ("yellow") strategically.
After each move, the board is displayed to show progress.

Win Conditions:
The game checks for four connected tokens horizontally, vertically, or diagonally after each move.
If no winner is found and the board is full, the game declares a draw.

Restart or Exit:
After a match ends, players are prompted to restart or exit the game.

This project demonstrates key programming concepts such as:
Implementation of advanced algorithms (Minimax with alpha-beta pruning).
Modular design using object-oriented programming principles.
Error handling with custom exceptions for robust applications.
Writing unit tests for validating functionality and ensuring code reliability.
