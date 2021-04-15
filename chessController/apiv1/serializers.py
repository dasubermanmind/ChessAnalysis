from rest_framework import serializers
from .models import GameOpenings


class GameOpeningsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameOpenings
        fields = ('id', 'openingName', 'games', 'openingEco', 'whiteRating', 'blackRating', 'winner', 'totalStrength')


'''
Update using winner from session
'''


class CreateGameOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameOpenings
        fields = fields = (
        'id', 'openingName', 'games', 'openingEco', 'whiteRating', 'blackRating', 'winner', 'totalStrength')
