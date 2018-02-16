from google.appengine.ext import ndb
'''
SQL INJECTION
class Objava:
    def preberi_objavo(self, objava_id):
        objava_id = int(objava_id) -> eden izmed nacinov, da se branis
        rezultat = baza.execute("SELECT naslov, vsebina FROM objava WHERE id="+str(objava_id))
        return rezultat[0]
 '''
class Objava(ndb.Model):
    vsebina = ndb.TextProperty()
    naslov = ndb.StringProperty()
    uporabnik_email = ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty(auto_now_add=True)
    cas_posodobitve = ndb.DateTimeProperty()
    cas_izbrisa = ndb.DateTimeProperty()


class Komentar(ndb.Model):
    objava_id = ndb.StringProperty()
    vsebina = ndb.TextProperty()
    uporabnik_email = ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty()
    cas_posodobitve = ndb.DateTimeProperty()
    cas_izbrisa = ndb.DateTimeProperty()
