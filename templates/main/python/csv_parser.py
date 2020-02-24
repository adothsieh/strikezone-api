import csv

class CSVParser:
    def __init__(self, filename):
        self.filename = filename

    def csv_to_playerDict(self):
        player_db = {}
        with open(self.filename, encoding='mac_iceland') as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                player_id_mlb = str(row[0])
                player_id_espn = str(row[14])
                player_name = str(row[1])
                player_team = str(row[3])
                player_db[player_id_espn] = [player_id_mlb, player_name, player_team]

        return player_db

    def csv_to_teamDict(self):
        team_db = {}
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                team_abbr_espn = str(row[8])
                team_abbr_bp = str(row[9])
                team_db[team_abbr_espn] = [team_abbr_bp]

        return team_db


