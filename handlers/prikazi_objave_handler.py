from models.models import Objava
from handlers.base_handler import BaseHandler

class PrikaziObjavoHandler(BaseHandler):
    def get(self, objava_id):
        objava = Objava.get_by_id(int(objava_id))
        if not objava:
            return self.write("Te objave ni")
        params = {"objava": objava}
        return self.render_template("objave.html", params=params)
