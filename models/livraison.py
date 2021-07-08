from marshmallow import Schema, fields, post_load


class Livraison:
    def __init__(self, id_livraison,vendeur,tracking,id_echange,last_etat_liv,prix_panier,prix_livraison,qty,etat,label_produit,id_vendeur,
                 nb_tentative,nom_client,prenom_client,tel,email_client,adresse_client,commune_client,wilaya_client,nb_appel_livreur,
                 bureau,heure_rdv,type_serv,type_service,designation):
        self.id_livraison=id_livraison
        self.vendeur = vendeur
        self.tracking=tracking
        self.id_echange=id_echange
        self. last_etat_liv=last_etat_liv
        self.prix_panier=prix_panier
        self.prix_livraison=prix_livraison
        self.qty=qty
        self.etat=etat
        self.label_produit=label_produit
        self.id_vendeur=id_vendeur
        self.nb_tentative=nb_tentative
        self.nom_client=nom_client
        self.prenom_client=prenom_client
        self.tel=tel
        self.email_client=email_client
        self.adresse_client=adresse_client
        self.commune_client=commune_client
        self.wilaya_client=wilaya_client
        self.nb_appel_livreur=nb_appel_livreur
        self.bureau=bureau
        self.heure_rdv=heure_rdv
        self.type_serv=type_serv
        self.type_service=type_service
        self.designation=designation



class LivraisonSchema(Schema):
    id_livraison=fields.String()
    vendeur=fields.String()
    tracking=fields.String()
    id_echange=fields.String(missing=None)
    last_etat_liv=fields.String(missing=None)
    prix_panier=fields.Integer()
    prix_livraison=fields.Integer()
    qty=fields.Integer()
    etat=fields.String(missing=None)
    label_produit = fields.String(missing=None)
    id_vendeur=fields.String(missing=None)
    nb_tentative=fields.String(missing=None)
    nom_client=fields.String(missing=None)
    prenom_client=fields.String(missing=None)
    tel=fields.String(missing=None)
    email_client=fields.String(missing=None)
    adresse_client=fields.String(missing=None)
    commune_client=fields.String(missing=None)
    wilaya_client=fields.String(missing=None)
    nb_appel_livreur=fields.String(missing=None)
    bureau=fields.String(missing=None)
    heure_rdv=fields.String(missing=None)
    type_serv=fields.String(missing=None)
    type_service=fields.String(missing=None)
    designation=fields.String(missing=None)
    @post_load
    def make_cmd(self, data, **kwargs):
        return Livraison(**data)
