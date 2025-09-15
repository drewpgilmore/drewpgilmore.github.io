import pandas as pd
from espn_api.football import League

LEAGUE_ID = 138431
OLD_ESPN_S2 = "AEB3IQLceBbHwMKj64haFAPYjtxQaTN4La2Sf4q2QwsMGMZ8DT5ZMasw97RaSVz4z5epIYn7YGnEPLOuOmWZDuYKjLut79zS7Zf%2Bdg0z1C0W%2F%2BsjuMkZqQhi7RiRVrVpZ6GR4ZuzLNWSGHsXg91aU6Y8UwbpFz02%2BH0XSKvI3Zl873EL%2FekHOs3T%2B9pW4Omkr8wzuyiSys5YueosMOxYSECaHmT5w1mzj5Ub%2BDLgjFbMiEZBWhChrnHtn4GUuNThuAQt0x9S6LhNtlQsYgZZsGeD1ZJg3sy8oq1C6L4hv%2B6fyg%3D%3D"
ESPN_S2 = "AECt54RHSOR6ItyGj9JhBshKMuJze6SMgTv0zGy8burJ9rWoXzD03LVFoxV6Z8DzFhqrhpL0h6IYQeqRkPkEjkyhvGbU3Q6wMdoaHTcimqnV16NjFNjznmiMesOpSj%2FL4QWAXG3j24DFjYYZ2QGAJdLQ5AJnmluD8z5WJ7eLgA35ly86QSXRqxLlNOQYG3yw%2Br1TYy%2F4MZ0RBnFFRoXYAZd0y%2Bz5gRDsU4WbXxz0RrIS%2FzXvQTlY5s%2F9ZXollzaao0310wG3qX4XJZchjPgLkDX4uidmlNewgz2uOyIq81JKww%3D%3D"
SWID = "{5748B7A9-5115-4E78-88B7-A951152E78DE}"

DIV = {
    "Drew":   "Leucadia",
    "Cal":    "Leucadia",
    "Carter": "Leucadia",
    "Noah":   "Leucadia",
    "Isaac":  "Leucadia",
    "Mason": "Cardiff",
    "Kyle": "Cardiff",
    "Marcus": "Cardiff",
    "Cody": "Cardiff",
    "Jordan": "Cardiff"
}

l = League(LEAGUE_ID, 2025, ESPN_S2, SWID)
#week = l.current_week
week = 2
isProjected = True

def get_score(matchup, home_away, isProjected): 
    if home_away == "home":
        t = matchup.home_team
        if isProjected:
            score = matchup.home_projected
        else: 
            score = matchup.home_score
    else: 
        t = matchup.away_team
        if isProjected:
            score = matchup.away_projected
        else: 
            score = matchup.away_score
    name = t.owners[0]["firstName"].title()
    return (name, score)

scores = []


for matchup in l.box_scores(week):
    scores.append(get_score(matchup, "home", isProjected))
    scores.append(get_score(matchup, "away", isProjected))

data = pd.DataFrame(scores)
data["Week"] = week
data.columns = ["Team", "Points", "Week"]
data.set_index("Team", inplace=True)
data["Division"] = data.index.map(DIV)
data["Score"] = data["Points"].rank().astype(int)
data.to_clipboard()
print("Done")

                  
    

