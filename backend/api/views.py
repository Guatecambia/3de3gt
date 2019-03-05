from .models import Candidato, District, Presentado
from .serializers import CandidatoAdminSerializer, CandidatoSerializer, PresentadoAdminSerializer
from .serializers import PresentadoSerializer, DistrictSerializer, LoginUserSerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DistrictEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit and delete specific districts
    """
    permission_classes = (IsAuthenticated, )
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictList(generics.ListCreateAPIView):
    """
    List and create districts
    """
    permission_classes = (IsAuthenticated, )
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


class PresentadoEdit(generics.RetrieveUpdateAPIView):
    """
    Retrieve and edit specific form answers
    """
    permission_classes = (IsAuthenticated, )
    queryset = Presentado.objects.all()
    serializer_class = PresentadoAdminSerializer


class PresentadoList(generics.ListAPIView):
    """
    List form answers
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = PresentadoAdminSerializer

    def get_queryset(self):
        if 'status' in self.kwargs:
            status = self.kwargs['status']
            return Presentado.objects.filter(status=status).order_by('-created_at')
        else:
            return Presentado.objects.all().order_by('-created_at')


class CandidatoAdminList(generics.ListCreateAPIView):
    """
    List and create Candidatos
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = CandidatoAdminSerializer

    def get_queryset(self):
        if 'status' in self.kwargs:
            status = self.kwargs['status']
            if (status == 'PUB'):
                return Candidato.objects.filter(published=True).order_by('lastname')
            elif (status == 'ASK'):
                return Candidato.objects.filter(inAskList=True).order_by('lastname')
        else:
            return Candidato.objects.all().order_by('lastname')


class CandidatoAdminEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit and delete specific Candidatos
    """
    permission_classes = (IsAuthenticated, )
    queryset = Candidato.objects.all()
    serializer_class = CandidatoAdminSerializer
