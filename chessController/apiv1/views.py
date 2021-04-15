from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GameOpeningsSerializers
from .serializers import CreateGameOpeningSerializer
from .models import GameOpenings


class GameOpeningView(generics.CreateAPIView):
    queryset = GameOpenings.objects.all()
    serializer_class = GameOpeningsSerializers


class CreateGameOpeningView(generics.UpdateAPIView):
    queryset = GameOpenings.objects.all()
    serializer_class = CreateGameOpeningSerializer


class UpdateAPIView(APIView):
    serializer = CreateGameOpeningSerializer

    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            # create the session
            self.request.session.create()

        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            openingName = serializer.data.openingName
            winner = serializer.data.winner
            whiteRating = serializer.data.whiteRating
            blackRating = serializer.data.blackRating
            games = serializer.data.games
            totalStrength = serializer.data.totalStrength
            openingEco = serializer.data.openingEco

            querySet = GameOpenings.objects.create(openingName, winner, whiteRating, blackRating, games, totalStrength,
                                                   openingEco)
            if querySet.exists():
                gameOpening = queryset[0]
                gameOpening.winner = winner
                gameOpening.whiteRating = whiteRating
                gameOpening.blackRating = blackRating
                gameOpening.openingName = openingName

                gameOpening.save(
                    update_fields=['openingName', 'games', 'openingEco', 'whiteRating', 'blackRating', 'winner',
                                   'totalStrength'])
                self.request.session['openingName'] = gameOpening.openingName
                return Response(CreateGameOpeningSerializer(gameOpening).data, status=status.HTTP_200_OK)
            else:
                gameOpening = GameOpenings(openingName, games, openingEco, whiteRating, blackRating, winner,
                                           totalStrength)
                gameOpening.save()

                self.request.session['openingName'] = gameOpening.openingName
                return Response(CreateGameOpeningSerializer(gameOpening).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
# end
