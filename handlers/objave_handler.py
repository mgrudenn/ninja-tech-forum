from google.appengine.api import users, memcache
from handlers.base_handler import BaseHandler
from models.models import Objava
import cgi, uuid

class DodajObjavoHandler(BaseHandler):
    def get(self):
        #random.randomint(0, 9999999)
        params = {
            "csrf_zeton": str(uuid.uuid4()) #generira skrivno kodo
        }
        memcache.add(params["csrf_zeton"], True, 60*10)
        return self.render_template("dodaj_objavo.html", params)

    def post(self):
        vrednost_csrf = self.request.get("csrf-zeton")
        if not memcache.get(vrednost_csrf):
            return self.write("CSRF napad v dogajanju :o")

        naslov = cgi.escape(self.request.get("title"))
        vsebina = cgi.escape(self.request.get("text"))
        uporabnik = users.get_current_user()
        email = uporabnik.email()
        nova_objava = Objava(naslov=naslov,
                             vsebina=vsebina,
                             uporabnik_email=email)
        nova_objava.put()
        #return self.write("Objava dodana.")

        uri= nova_objava.key.id()
        return self.redirect("prikazi-objavo/"+str(uri))