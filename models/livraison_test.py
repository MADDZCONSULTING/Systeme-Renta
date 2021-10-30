from marshmallow import Schema, fields, post_load


class LivraisonTest:
    def __init__(self, id,id_tournee,prix_livraison_vendeur,commune):
        self.id=id
        self.id_tournee=id_tournee
        self.prix_livraison_vendeur=prix_livraison_vendeur
        self.commune=commune

class LivraisonTestSchema(Schema):
    id = fields.String()
    id_tournee = fields.String()
    prix_livraison_vendeur = fields.Integer()
    commune = fields.String(missing=None)

    @post_load
    def make_cmd(self, data, **kwargs):
        return LivraisonTest(**data)
