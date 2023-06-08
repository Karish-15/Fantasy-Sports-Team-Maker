
# Fantasy Sports Team Maker

A Django REST API that forms teams from the provided data, sorted according to team performance provided.

The client demo shows how a POST request can be sent to the API and dealing with response.

## API Routes

#### /api
* `GET` : Returns 200 if server running

#### /api/formteams
* `POST` : Send `file` and form data to get formatted JSON output containing formed teams

## Screenshot
![Screenshot-Output](client-demo/Screenshot.png?raw=true "Title")

## Example Output
```json
{
   Match: "PBKS vs RR",
   "Time Taken": "3.6839942932128906seconds",
   Teams: [
      {
         index: 1,
         "Team Performance": 821,
         "Captain, Vice Captain": [
            "SAMSON",
            "RAHUL"
         ],
         "Player List": "SAMSON, RAHUL, HOODA, ARSHDEEP, PARAG, SHAMI, MORRIS, GAYLE, MAYANK, STOKES, TEWATIA",
         "Position Count": {
            bat: 3,
            bowl: 2,
            all: 4,
            wk: 2
         }
      },
      {
         index: 2,
         "Team Performance": 793,
         "Captain, Vice Captain": [
            "SAMSON",
            "RAHUL"
         ],
         "Player List": "SAMSON, RAHUL, HOODA, ARSHDEEP, PARAG, SHAMI, GAYLE, DUBE, MAYANK, STOKES, TEWATIA",
         "Position Count": {
            bat: 3,
            bowl: 2,
            all: 4,
            wk: 2
         }
      }
	  ]
   }
```

## Structure
### Main:

- **functions.py**: Contains functions used to
form teams from given data. If you want to change the minimum number of
batsmen/bowlers/all-rounders/wicket-keepers that should be picked for
each team, change the corresponding **min** variable in `findCombinations()`. **lst** is the list containing player data, K is target sum of points for each
team(usually 100) and N is the number of players in each team(11 here).
Then call this function from `makeTeams.py`.
- **makeTeams.py:** `makeTeams()` calls functions from modules to form teams. It shows the top 500 teams sorted according to Team performance in descending order. Returns the data to be used by backend.
- **sample.csv**: Contains data that will be used to form JSONs and eventually used for forming teams.

### backend/teams/giveTeams.py:

- Returns a pandas dataframe for the CSV that is sent in `request` variable.
- Checks if csv is valid and contains the required columns for team maker to work
- calls `makeTeams()` and returns a formatted response
