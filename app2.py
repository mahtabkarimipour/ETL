from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import text

engine = create_engine("sqlite:///Resources/database.sqlite")
conn = engine.connect()

Base = automap_base()
Base.prepare(engine, reflect=True)
country = Base.classes.country
League = Base.classes.League
Match = Base.classes.Match
Player = Base.classes.Player
Team = Base.classes.Team
Player_Attributes = Base.classes.Player_Attributes
Team_Attributes = Base.classes.Team_Attributes
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def index():
    res = {}
    myapp_urls = str(app.url_map).split('\n')
    for i, u in enumerate(myapp_urls):
        print(i, u)    
    return jsonify(res)

@app.route('/api/v1.0/country')
def get_country():
    res = []
    records = session.query(country)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['name'] = r.name
        res.append(tmp)
    return jsonify(res)

@app.route('/api/v1.0/league')
def get_league():
    res = []
    records = session.query(League)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['country_id'] = r.country_id
        tmp['name'] = r.name
        res.append(tmp)
    return jsonify(res)


@app.route('/api/v1.0/match')
def get_match():
    res = []
    records = session.query(Match)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['country_id'] = r.country_id
        tmp['league_id	'] = r.league_id
        tmp['season'] = r.season
        tmp['stage'] = r.stage
        tmp['date'] = r.date
        tmp['match_api_id'] = r.match_api_id
        tmp['home_team_api_id'] = r.home_team_api_id
        tmp['away_team_api_id'] = r.away_team_api_id
        tmp['home_team_goal'] = r.home_team_goal
        res.append(tmp)
    return jsonify(res)

@app.route('/api/v1.0/player')
def get_player():
    res = []
    records = session.query(Player)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['player_api_id'] = r.player_api_id
        tmp['player_name'] = r.player_name
        tmp['player_fifa_api_id'] = r.player_fifa_api_id
        tmp['birthday'] = r.birthday
        tmp['weight'] = r.weight
        res.append(tmp)
    return jsonify(res)

@app.route('/api/v1.0/team')
def get_team():
    res = []
    records = session.query(Team)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['team_api_id'] = r.team_api_id
        tmp['team_fifa_api_id'] = r.team_fifa_api_id
        tmp['team_long_name'] = r.team_long_name
        tmp['team_short_name'] = r.team_short_name
        res.append(tmp)
    return jsonify(res)

@app.route('/api/v1.0/Playerattributes')
def get_Playerattributes():
    res = []
    records = session.query(Player_Attributes)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['player_api_id'] = r.player_api_id
        tmp['date'] = r.date
        tmp['overall_rating'] = r.overall_rating
        tmp['potential'] = r.potential
        tmp['preferred_foot'] = r.preferred_foot
        tmp['attacking_work_rate'] = r.attacking_work_rate
        tmp['defensive_work_rate'] = r.defensive_work_rate
        tmp['crossing'] = r.crossing
        tmp['vision'] = r.vision
        tmp['penalties'] = r.penalties
        tmp['marking'] = r.marking
        tmp['standing_tackle'] = r.standing_tackle
        tmp['sliding_tackle'] = r.sliding_tackle
        tmp['gk_diving'] = r.gk_diving
        tmp['gk_handling'] = r.gk_handling
        tmp['gk_kicking'] = r.gk_kicking
        tmp['gk_positioning'] = r.gk_positioning
        tmp['gk_reflexes'] = r.gk_reflexes
        res.append(tmp)
    return jsonify(res)

@app.route('/api/v1.0/teamattributes')
def get_teamattributes():
    res = []
    records = session.query(Team_Attributes)
    for r in records:
        tmp = {}
        tmp['id'] = r.id
        tmp['team_api_id'] = r.team_api_id
        tmp['team_fifa_api_id'] = r.team_fifa_api_id
        tmp['date'] = r.date
        tmp['buildUpPlaySpeed'] = r.buildUpPlaySpeed
        tmp['buildUpPlaySpeedClass'] = r.buildUpPlaySpeedClass
        tmp['buildUpPlayDribbling'] = r.buildUpPlayDribbling
        tmp['buildUpPlayDribblingClass'] = r.buildUpPlayDribblingClass
        tmp['buildUpPlayPassing'] = r.buildUpPlayPassing
        tmp['buildUpPlayPassingClass'] = r.buildUpPlayPassingClass
        tmp['chanceCreationShooting'] = r.chanceCreationShooting
        tmp['chanceCreationShootingClass'] = r.chanceCreationShootingClass
        tmp['chanceCreationPositioningClass'] = r.chanceCreationPositioningClass
        tmp['defencePressure'] = r.defencePressure
        tmp['defencePressureClass'] = r.defencePressureClass
        tmp['defenceAggression'] = r.defenceAggression
        tmp['defenceAggressionClass'] = r.defenceAggressionClass
        tmp['defenceTeamWidth'] = r.defenceTeamWidth
        tmp['defenceTeamWidthClass'] = r.defenceTeamWidthClass
        tmp['defenceDefenderLineClass'] = r.defenceDefenderLineClass   
        res.append(tmp)
    return jsonify(res)
if __name__ == '__main__':
   app.run(debug=True) 