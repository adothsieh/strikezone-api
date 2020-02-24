from flask import render_template, Blueprint, jsonify, make_response, send_from_directory
import logging
import sys
import os
sys.path.insert(0, './templates/main/python/')

import previous_starts as ps
import pitch_data as pd
from csv_parser import CSVParser
from pitch_data import PitchData


main_blueprint = Blueprint('main',__name__)
fileName = './templates/main/python/data/master.csv'
playerParser = CSVParser(fileName)
player_dict = playerParser.csv_to_playerDict()



@main_blueprint.route('/starts/<pid>', methods=["GET"])
def get_starts(pid):
    starts = ps.PrevStarts(pid)
    data = starts.get_previous_starts()
    return data

@main_blueprint.route('/graphs/<pid>/<date>/<player_team>/<opp_team>', methods=['GET'])
def get_data(pid, date, player_team, opp_team):
    mlb_id = player_dict[pid][0]
    pitch_data = PitchData(mlb_id, date, player_team, opp_team)
    return pitch_data.get_pitch_data()

@main_blueprint.route('/', defaults={'path': ''})
@main_blueprint.route('/<path:path>/')
def catch_all(path):
    path_dir = os.path.abspath("../strike-zone/templates/static") #path react build
    return send_from_directory(path_dir, "index.html")  