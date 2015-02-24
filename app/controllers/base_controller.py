import tornado.web
from app.models.team import Team
from app.models.league import League

class BaseController(tornado.web.RequestHandler):
    def initialize(self, session):
        self.session = session
        self._current_user = None
        self._current_league = None

    def current_user(self):
        if not self._current_user:
            user_id = self.path_kwargs["user_id"]
            self._current_user = self.session.query(Team).filter(User.id == user_id).one()
        return self._current_user

    def current_league(self):
        if not self._current_league:
            self._current_league = self.current_user.league
        return self._current_league
