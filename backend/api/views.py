from .models import Candidato, District, Municipality, Party, Presentado
from .serializers import CandidatoAdminSerializer, CandidatoSerializer, DistrictSerializer, DistrictSelectSerializer
from .serializers import LoginUserSerializer, MunicipalitySelectSerializer, PartySelectSerializer
from .serializers import PresentadoAdminSerializer
from .serializers import PresentadoSerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


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


class DistrictListById(generics.ListAPIView):
    """
    List districts
    """
    permission_classes = (AllowAny, )
    queryset = District.objects.all().order_by('name')
    serializer_class = DistrictSelectSerializer


class MunicipalityList(generics.ListAPIView):
    """
    List municipalities for a html-select
    """
    permission_classes = (AllowAny, )
    queryset = Municipality.objects.all().order_by('department','name')
    serializer_class = MunicipalitySelectSerializer
    

class PartyListOnlyPP(generics.ListAPIView):
    """
    List of parties, ttype = PP
    """
    permission_classes = (AllowAny, )
    queryset = Party.objects.filter(tType='PP').order_by('name')
    serializer_class = PartySelectSerializer
    
    
class PartyListOnlyCC(generics.ListAPIView):
    """
    List of parties, ttype = CC
    """
    permission_classes = (AllowAny, )
    queryset = Party.objects.filter(tType='CC').order_by('name')
    serializer_class = PartySelectSerializer


class PartyList(generics.ListAPIView):
    """
    List of all parties, ttype CC and PP
    """
    permission_classes = (AllowAny, )
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySelectSerializer


class CandidatoAsk(generics.ListAPIView):
    """
    View Candidatos that haven't presented 3de3
    """
    permission_classes = (AllowAny, )
    serializer_class = CandidatoSerializer
    
    def get_queryset(self):
        partyParam = self.request.query_params.get('party')
        positionParam = self.request.query_params.get('position')
        queryset = Candidato.objects.filter(inAskList=True, )
        if (partyParam):
            queryset = queryset.filter(party=partyParam)
        if (positionParam):
            if (positionParam == 'LEG' or positionParam == 'M'):
                queryset = queryset.filter(aspiredPosition=positionParam)
            elif (positionParam == 'P' or positionParam == 'V'):
                queryset = queryset.filter(aspiredPosition='EX', executivePosition=positionParam)
        queryset = queryset.order_by('name','lastname')
        return queryset
      


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
