
from django.db.models import fields
from rest_framework import serializers
from products.models import Manufacturer, Product





class ProductSerializer(serializers.ModelSerializer):

    # manufacturer = serializers.StringRelatedField()
    # manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name should not the same as description.')
        return data

    def validate_name(self, value):
        if len(value) > 60:
            raise serializers.ValidationError('Name too long.')
        return value

class ManufacturerSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Manufacturer
        fields = '__all__'


    