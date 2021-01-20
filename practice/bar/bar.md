# [bar.py](./bar.py)
## This is how I made [bar.py](./bar.py),

___

### Part 1
- > At first I imported `json`, `random` and `os`.

- > I created a random value from 1 - 3 in the bar variable.

- > I then use that variable to decide which bar I use in the [bar_rules.json](./bar_rules.json).

- > When the bar is chosen, It titles the rules. e.g. ted ace bounce's rules.

### Part 2
- > I create a variable for later use just containing strings to show what rule they are looking at.

- > I tell python to check if the file exists by using 
```python
os.path.exists
```
- >If it finds the [bar_rules.json](./bar_rules.json), it opens that file and reads the content as json by using
```python
rules_data = json.load(bar_rules)
```
- > It then checks if the bars dictionary is in the .json.

- > If you have the .json file, it will read check if the random bar that has been chosen is in the dictionary.

- > When it finds the title of the bar, it will then read the rules inside of it and print out on screen.

### Part 3
