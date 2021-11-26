# Fantasy Sports Team Maker

## Structure:

### Main:

- **functions.py**: Contains functions used to form teams from given data. If you want to change the minimum number of batsmen/bowlers/all-rounders/wicket-keepers that should be picked for each team, change the corresponding **min** variable in `findCombinations()`. **lst** is the list containing player data, K is target sum of points for each team(usually 100) and N is the number of players in each team(11 here). Then call this function from `main.py`. 

- **prepare_json.py**: Uses `json` module to prepare a JSON which is used to store a dictionary containing player data. Uses `pandas` module to read from `sample.csv` and prepare a JSON to be used by `main.py`.

  Choose the column which you want to use as performance for each player and put it as the value for `temp_dict['performance']`. You can add data for more matches, just make sure that the said column is updated for the newly added matches.

- **main.py**: makes use of functions to return us a list that contains all formed teams. The teams are also sorted in descending order of sum of each player's **performance** **points**.
- **sample.csv**: Contains data that will be used to form JSONs and eventually used for forming teams. After running `main.py`, a new file **new_data.csv** will be formed which will have updated values for *FREQ* column which is the number of times a player was included in a formed team. Everything else in **new_data.csv** will be identical to **sample.csv**

### Update_Pandas:

- **data_model.py**: defines `player` and `Database` classes
- **set_csv.py**: Prepare the **sample.csv** file for it to be used by **prepare_json.py**. Adds *mean, standard deviation and median* column which will be based on player's performance from recent matches.

---

Thanks for attending my Ted Talk.

Currently I'm working on to automate the formation of **sample.csv** and finding an appropriate value to be used as "Performance" for each player.

![Alt Text](https://media.giphy.com/media/LllA2dKt1qZuE/giphy.gif?cid=ecf05e47x7id135827j1im8uxkii9s77x1jivdx80uqzass3&rid=giphy.gif&ct=g)

