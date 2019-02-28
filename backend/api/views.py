from .models import Candidato, District
from .serializers import CandidatoSerializer, PresentadoSerializer, DistrictSerializer

from rest_framework import generics


class DistrictEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and edit specific districts
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictList(generics.ListCreateAPIView):
    """
    List and create districts
    """
    queryset = District.objects.all().order_by('id')
    serializer_class = DistrictSerializer


class CandidatoAsk(generics.ListAPIView):
    """
    View Candidatos that haven't presented 3de3
    """
    queryset = Candidato.objects.filter(inAskList=True)
    serializer_class = CandidatoSerializer


class PresentedAsk(generics.ListAPIView):
    """
    View Candidatos that have presented 3de3
    """
    serializer_class = CandidatoSerializer

    def get_queryset(self):
        if 'aspirantType' in self.kwargs:
            aspirantType = self.kwargs['aspirantType']
            return Candidato.objects.filter(published=True, aspiredPosition=aspirantType)
        else:
            return Candidato.objects.filter(published=True)


class PresentedForm(generics.CreateAPIView):
    """
    View for Presentado model
    """
    serializer_class = PresentadoSerializer
