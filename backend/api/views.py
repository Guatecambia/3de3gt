from .models import Candidato
from .serializers import CandidatoSerializer

from rest_framework import generics


class CandidatoAsk(generics.ListAPIView):
    """
    View Candidatos that haven't presented 3de3
    """
    queryset = Candidato.objects.filter(inAskList=True)
    serializer_class = CandidatoSerializer
