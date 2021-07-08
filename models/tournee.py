from marshmallow import Schema, fields, post_load

class Tournee:
    def __init__(self,idTournee,Livreur_id,date_tournee,type,cloture,enveloppe_prepare,hub,etat_tournee,lanceur,admin_cloture,date_lancement):
        self.idTournee = idTournee
        self.Livreur_id=Livreur_id
        self.date_tournee=date_tournee
        self.type=type
        self.cloture=cloture
        self.enveloppe_prepare=enveloppe_prepare
        self.hub=hub
        self.etat_tournee=etat_tournee
        self.lanceur=lanceur
        self.admin_cloture=admin_cloture
        self.date_lancement=date_lancement

class TourneeSchema(Schema):
    idTournee = fields.String()
    Livreur_id=fields.String()
    date_tournee= fields.String()
    type= fields.String()
    cloture= fields.String()
    enveloppe_prepare= fields.String()
    hub= fields.String()
    etat_tournee= fields.String()
    lanceur= fields.String()
    admin_cloture= fields.String()
    date_lancement= fields.String()


    @post_load
    def make_tournee(self, data, **kwargs):
        return Tournee(**data)
