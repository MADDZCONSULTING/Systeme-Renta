from marshmallow import Schema, fields, post_load

class TourneeTest:
    def __init__(self,idTournee,date_tournee,hub,secteur,livreur,performance):
        self.idTournee = idTournee
        self.date_tournee=date_tournee
        self.hub=hub
        self.secteur= secteur
        self.livreur=livreur
        self.performance= performance


class TourneeTestSchema(Schema):
    idTournee = fields.String()
    date_tournee= fields.String()
    hub= fields.String()
    secteur=fields.String()
    livreur=fields.String()
    performance= fields.String()


    @post_load
    def make_tournee(self, data, **kwargs):
        return TourneeTest(**data)
