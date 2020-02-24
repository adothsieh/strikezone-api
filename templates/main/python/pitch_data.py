import requests
import sys

from bs4 import BeautifulSoup
from datetime import datetime
from pitch_glossary import PitchGlossary
from csv_parser import CSVParser

class PitchData:

    def __init__(self, player_id, date, player_team, vs_team):
        self.player_id = player_id
        self.date = date
        self.vs_team = vs_team
        self.player_team = player_team
        self.team_dict = {}
        self.teamMap = './templates/main/python/data/SFBB MLB Team Map - SFBB Team Map.csv'
        
    def format_date(self):
        date = datetime.strptime(self.date, "%b %d %Y")
        date = date.strftime('%Y_%m_%d')
        return date

    def format_teams(self):
        teamParser = CSVParser(self.teamMap)
        self.team_dict = teamParser.csv_to_teamDict()
        print(self.team_dict)
        
        split = self.vs_team.split(' ')
        isHome = (split[0] == 'vs')

        self.player_team = self.team_dict[self.player_team][0]
        self.vs_team = self.team_dict[split[1]][0]

        if isHome:
            return f"{self.vs_team.lower()}mlb_{self.player_team.lower()}mlb_1"
        else:
            return f"{self.player_team.lower()}mlb_{self.vs_team.lower()}mlb_1"

    def format_url(self):
        date = self.format_date()
        teams = self.format_teams()

        return f"http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel={self.player_id}&game=gid_{date}_{teams}/&s_type=&h_size=700&v_size=500"
        

    def get_pitch_data(self):
        url = self.format_url()
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }

        try:
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code != 200:
                raise Exception
        except requests.ConnectionError:
            print("Please check that you are connected to the internet.")
            sys.exit()
        except requests.Timeout:
            print("The request has timed out. Please try again later.")
            sys.exit()
        except Exception:
            print(f"There was an error with connecting to the website. Please check that the url is correct.\n{url}")
            sys.exit()

        #print(res.status_code)
        soup = BeautifulSoup(res.content,'lxml')
        
        table = soup.find_all('tr')[1:]
        
        ptypes = []
        results = []

        pitches = {}
        if table:
            for row in table:
                data = row.find_all('td')
                if data:
                    pitch = {}
                    ab_id = data[7].text
                    pitch['px'] = data[-6].text
                    pitch['pz'] = data[-5].text
                    pitch['pt'] = data[15].text
                    pitch['pv'] = data[-7].text
                    pitch['call'] = data[9].text
                    pitch['strike_count'] = data[19].text
                    pitch['ball_count'] = data[20].text
                    pitch['ab_id'] = ab_id
                    pitch['result'] = data[8].text

                    if data[15].text not in ptypes:
                        ptypes.append(data[15].text)

                    if data[8].text not in results:
                        results.append(data[8].text)

                    if ab_id in pitches.keys():
                        pitches[ab_id].append(pitch)
                    else:
                        pitches[ab_id] = [pitch]
                else:
                    sys.exit("Pitch Information cannot be found")
        else:
            sys.exit("There was an error retrieving pitching data for this matchup.")
            
        return {'pitches':pitches, 'ptypes':ptypes, 'results':results}