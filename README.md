# Boggle

Boggle is a word game played by humans. The humans share a 4x4 board of letters and create words by stringing adjacent
letters on the board to form sequences within some time limit. Each word formed is given a certain number of points
depending on the number of letters it has and whether other players in the group have found the word. The human with the 
highest score is declared the victor.

This project obviates the humans' game by automating the solving of any Boggle board, including boards that are of
a general size NxN. Specifically, given a Boggle board of some size, a word list is generated that contains all
possible words that can be made from the board. A dictionary (`dictionary.txt`) of valid words is provided.

# Run the project

Python 2.7.10 was used to develop this project.

Create a virtual environment and activate it.
Then, install the requirements:

``` 
pip install -r requirements.txt
```

Choose a board to evaluate in one of the problem folders and run the following:

```
python boggle_solver.py problem1/problem.txt dictionary.txt
```

# Run the tests

```
python -m unittest discover .
```