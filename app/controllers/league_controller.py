import tornado.web
from app.models.team import Team
from app.models.league import League

class LeagueController(tornado.web.RequestHandler):
    def post(self):
        # create
        league_name = self.get_body_argument("league_name")
        manager_team_name = self.get_body_argument("manager_team_name")
        league = League(name=league_name)
        team = Team(name=manager_team_name, league=league)
        league.manager = team
        self.session.add_all([league, team])
        self.session.commit()

    def put(self, league_id):
        # update
        arguments = self.get_body_arguments()
        
