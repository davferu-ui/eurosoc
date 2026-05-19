import requests
import json
from datetime import datetime

# ESPN Hidden API endpoint for Premier League (eng.1) scoreboard data
SCOREBOARD_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard"

def main():
    try:
        # Fetch the live scoreboard data
        response = requests.get(SCOREBOARD_URL)
        response.raise_for_status()
        score_res = response.json()
        
        # Parse match details out of the JSON response
        games = []
        for event in score_res.get('events', []):
            competition = event['competitions'][0]
            home_team = competition['competitors'][0]
            away_team = competition['competitors'][1]
            
            games.append({
                "match": event['name'],
                "status": event['status']['type']['detail'],
                "homeTeam": home_team['team']['displayName'],
                "awayTeam": away_team['team']['displayName'],
                "homeScore": home_team.get('score', '0'),
                "awayScore": away_team.get('score', '0'),
                "date": event['date']
            })

        # Structure the clean output for our web page
        output_data = {
            "lastUpdated": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "fixtures": games
        }

        # Save it as a local file inside the repository folder
        with open('data.json', 'w') as f:
            json.dump(output_data, f, indent=4)
        print("Successfully generated data.json")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
  Add python scraper script
