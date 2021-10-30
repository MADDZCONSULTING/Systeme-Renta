from marshmallow import Schema, fields, post_load

class VariableGlobale:
    def __init__(self,cpt):
        self.cpt= cpt

class VariableGlobaleSchema(Schema):
    cpt = fields.Integer()

    @post_load
    def make_tournee(self, data, **kwargs):
        return VariableGlobale(**data)
