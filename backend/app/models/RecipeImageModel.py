from config.db import db, ma
from marshmallow import fields

class RecipeImage(db.Model):
    __tablename__ = 'recipe_images'

    id = db.Column(db.BigInteger, primary_key=True)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    download_url = db.Column(db.String(255))  
    file_name = db.Column(db.String(255))
    file_type = db.Column(db.String(255))
    image = image = db.Column(db.LargeBinary(length=(2**24)-1)) 

    def __init__(self, receta_id, download_url, file_name, file_type, image):
        self.receta_id = receta_id
        self.download_url = download_url
        self.file_name = file_name
        self.file_type = file_type
        self.image = image

class RecipeImageSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    receta_id = fields.Integer(required=True)
    download_url = fields.String()
    file_name = fields.String()
    file_type = fields.String()

    class Meta:
        fields = ('id', 'receta_id', 'download_url', 'file_name', 'file_type')
        model = RecipeImage

recipe_image_schema = RecipeImageSchema()
recipe_images_schema = RecipeImageSchema(many=True)