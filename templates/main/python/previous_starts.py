import requests
import sys
from bs4 import BeautifulSoup

class PrevStarts:
    
    def __init__(self, player_id):
        self.url = f"http://www.espn.com/mlb/player/gamelog/_/id/{player_id}/year/2019"

    def get_previous_starts(self):
        dates = {}
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        try:
            res = requests.get(self.url, headers=headers, timeout=5)
            if res.status_code != 200:
                raise Exception
        except requests.ConnectionError:
            print("Please check that you are connected to the internet.")
            sys.exit()
        except requests.Timeout:
            print("The request has timed out. Please try again later.")
            sys.exit()
        except Exception:
            print(f"There was an error with connecting to the website. Please check that the url is correct.\n{self.url}")
            sys.exit()
        
        
        soup = BeautifulSoup(res.text,'lxml')
        table = soup.find_all(lambda tag: tag.name == 'tr' and 
            tag.get('class') == ['oddrow'] or tag.get('class') == ['evenrow'])

        if table:
            for idx,row in enumerate(table):
                date = row.find_all('td')
                if date:
                    dates[idx] = {'date':date[0].text, 'opp':date[1].text, 'result':date[2].text} 
                else:
                    sys.exit("Previous start dates cannot be found.")
        else:
            sys.exit("There was an error getting the previous starts for this pitcher.")

        return dates
