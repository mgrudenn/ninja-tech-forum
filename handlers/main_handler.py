from handlers.base_handler import BaseHandler
from models.models import Objava

class MainHandler(BaseHandler):
    def get(self):
        seznam = Objava.query().order(-Objava.cas_objave).fetch()
        params = {"seznam": seznam}
        return self.render_template("home.html", params=params)