from item.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemName', 'description', 'price', 'quantity', 'photo', 'authorName', 'barcode_id', 'inStock', 'deliveryDuration']