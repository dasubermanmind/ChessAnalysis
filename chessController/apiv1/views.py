from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GameOpeningsSerializers
from .serializers import CreateGameOpeningSerializer
from .models import GameOpenings

class GameOpeningView(generics.CreateAPIView):
    querset = GameOpenings.objects.all()
    serializer_class = GameOpeningsSerializers

class CreateGameOpeningView(APIView):
    serializer = CreateGameOpeningSerializer

    def post(self,request,format=None):
        if not self.request.session.exists(self.requet.session.session_key):
            #create the session
            self.request.session.create()
    
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            openingName  = serializer.data.openingName
            winner = self.request.session.session_key #this is what we are updating in relation to
            whiteRating= serializer.data.whiteRating
            blackRating = serializer.data.blackRating
            querySet = GameOpenings.objects.filter(winner=winner)
            if querySet.exists():
                gameOpening = queryset[0]
                gameOpening.winner = winner
                gameOpening.whiteRating = whiteRating
                gameOpening.blackRating = blackRating

                gameOpening.save(update_fields=['winner', 'whiteRating','blackRating','openingName'])
                self.request.session['openingName'] = gameOpening.openingName
                return Response(CreateGameOpeningSerializer(gameOpening).data, status=status.HTTP_200_OK)
            else:
                gameOpening = GameOpenings()
                gameOpening.save()
                self.request.session['openingName'] = gameOpening.openingName
                return Response(CreateGameOpeningSerializer(gameOpening).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


