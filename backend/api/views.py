from .models import Candidato, DeclarationAnswer, District, Municipality, Party, Presentado
from .serializers import CandidatoAdminSerializer, CandidatoAdminSelectSerializer, CandidatoSerializer
from .serializers import DeclarationAnswerSerializer, DistrictSerializer, DistrictSelectSerializer, LoginUserSerializer
from .serializers import MunicipalitySelectSerializer, PartySelectSerializer, PresentadoAdminSerializer
from .serializers import PresentadoSerializer, UserSerializer
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from django.db.models import Count, Q
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
import gspread
import os


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


class CandidatoPatrimonial(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DeclarationAnswerSerializer

    def get_queryset(self):
        c_id = self.kwargs['pk']
        queryset = DeclarationAnswer.objects.filter(formType='P', candidato__id=c_id).order_by('position')
        return queryset

class CandidatoInterests(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DeclarationAnswerSerializer

    def get_queryset(self):
        c_id = self.kwargs['pk']
        queryset = DeclarationAnswer.objects.filter(formType='I', candidato__id=c_id).order_by('position')
        return queryset


class PresentedAsk(generics.ListAPIView):
    """
    View Candidatos that have presented 3de3
    """
    serializer_class = CandidatoSerializer

    def get_queryset(self):
        queryset = Candidato.objects.filter(published=True)
        partyParam = self.request.query_params.get('party')
        genderParam = self.request.query_params.get('gender')
        itemValueParam = self.request.query_params.get('itemValue')
        if 'aspirantType' in self.kwargs:
            aspirantType = self.kwargs['aspirantType']
            queryset = queryset.filter(aspiredPosition=aspirantType)
        if (partyParam):
            queryset = queryset.filter(party=partyParam)
        if (genderParam):
            queryset = queryset.filter(gender=genderParam)
        if (itemValueParam):
            if (aspirantType == 'EX'):
                queryset = queryset.filter(executivePosition=itemValueParam)
            if (aspirantType == 'LEG'):
                queryset = queryset.filter(district=itemValueParam)
            if (aspirantType == 'M'):
                queryset = queryset.filter(municipality=itemValueParam)
        return queryset


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
        status = self.kwargs['status']
        if (status != 'ALL'):
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
        status = self.kwargs['status']
        if (status != 'ALL'):
            if (status == 'PUB'):
                return Candidato.objects.filter(published=True).order_by('lastname')
            elif (status == 'ASK'):
                return Candidato.objects.filter(inAskList=True).order_by('lastname')
        else:
            return Candidato.objects.all().order_by('lastname')
            
    def create(self, request, *args, **kwargs):
        # set the original presented to "converted" status
        presentedId = request.data.get('presentedId')
        presentado = Presentado.objects.get(id=presentedId)
        presentado.status = 'C'
        presentado.save()
        return super(CandidatoAdminList, self).create(request, *args, **kwargs)


class CandidatoAdminEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit and delete specific Candidatos
    """
    permission_classes = (IsAuthenticated, )
    queryset = Candidato.objects.all()
    serializer_class = CandidatoAdminSerializer
      
    def update(self, request, *args, **kwargs):
        # if the request has the parameters patrimonialLine or interestsLine, it should reload the data of the GForm
        iLine = request.data.get('interestsLine')
        pLine = request.data.get('patrimonialLine')
        if (iLine and pLine):
            c_id = self.kwargs['pk']
            DeclarationAnswer.objects.filter(candidato__id=c_id).delete()
            scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
            fileName = os.path.join(settings.BASE_DIR, 'gt3de3/3de3gapps.json')
            credentials = ServiceAccountCredentials.from_json_keyfile_name(fileName, scope)
            gDrive = gspread.authorize(credentials)
            lineNumber = [iLine, pLine]
            formTypes = ["I","P"]
            for (i,gAppFile) in enumerate([settings.GAPP_INTERESTSFILE, settings.GAPP_PATRIMONIALFILE]):
                dataFile = gDrive.open_by_url(gAppFile).sheet1
                rowHead = dataFile.row_values(1)
                rowAns = dataFile.row_values(int(lineNumber[i])+1)
                for (it,val) in enumerate(rowHead):
                    if (it > 0): 
                        # skip first value, as it is timestamp.
                        answer = DeclarationAnswer()
                        answer.position = it
                        answer.fieldName = val
                        answer.fieldValue = rowAns[it]
                        answer.formType = formTypes[i]
                        answer.candidato_id = c_id
                        answer.save()
        return super(CandidatoAdminEdit, self).update(request, *args, **kwargs)


class CandidatoSelectList(generics.ListAPIView):
    """
    List of Candidatos, that are not published, in one field including name, lastname, party and aspiredPosition
    """
    permission_classes = (IsAuthenticated, )
    queryset = Candidato.objects.filter(published=False).order_by('name','lastname')
    serializer_class = CandidatoAdminSelectSerializer


class CandidatoStatisticsView(views.APIView):
    renderer_classes = (JSONRenderer, )
    
    def get(self, request, format=None):
        executiveCount = Candidato.objects.filter(published=True, aspiredPosition='EX').count()
        legislativeCount = Candidato.objects.filter(published=True, aspiredPosition='LEG').count()
        muniByPPCount = Candidato.objects.filter(published=True, aspiredPosition='M', party__tType='PP').count()
        muniByCCCount = Candidato.objects.filter(published=True, aspiredPosition='M', party__tType='CC').count()
        content = {
            'president': executiveCount,
            'congress': legislativeCount,
            'muniByParty': muniByPPCount,
            'civicComitee': muniByCCCount
        }
        return Response(content)
        
        
class StatisticsView(views.APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    
    def get(self, request, format=None):
        malePresident = Candidato.objects.filter(published=True, aspiredPosition='EX', executivePosition='P', gender='M').count()
        femalePresident = Candidato.objects.filter(published=True, aspiredPosition='EX', executivePosition='P', gender='F').count()
        maleVicepresident = Candidato.objects.filter(published=True, aspiredPosition='EX', executivePosition='V', gender='M').count()
        femaleVicepresident = Candidato.objects.filter(published=True, aspiredPosition='EX', executivePosition='V', gender='F').count()
        congressNac = Candidato.objects.filter(published=True, aspiredPosition='LEG', district__name='Nacional').count()
        congressDistr = Candidato.objects.filter(published=True, aspiredPosition='LEG').filter(~Q(district__name='Nacional'), ~Q(district__name='Parlacen')).count()
        maleCongressNac = Candidato.objects.filter(published=True, aspiredPosition='LEG', district__name='Nacional', gender='M').count()
        femaleCongressNac = Candidato.objects.filter(published=True, aspiredPosition='LEG', district__name='Nacional', gender='F').count()
        maleCongressDistr = Candidato.objects.filter(published=True, aspiredPosition='LEG', gender='M').filter(~Q(district__name='Nacional'), ~Q(district__name='Parlacen')).count()
        femaleCongressDistr = Candidato.objects.filter(published=True, aspiredPosition='LEG', gender='F').filter(~Q(district__name='Nacional'), ~Q(district__name='Parlacen')).count()
        maleMuni = Candidato.objects.filter(published=True, aspiredPosition='M', gender='M').count()
        femaleMuni = Candidato.objects.filter(published=True, aspiredPosition='M', gender='F').count()
        content = {
            'malePresident': malePresident,
            'femalePresident': femalePresident,
            'maleVicepresident': maleVicepresident,
            'femaleVicepresident': femaleVicepresident,
            'congressNac': congressNac,
            'congressDistr': congressDistr,
            'maleCongressNac': maleCongressNac,
            'femaleCongressNac': femaleCongressNac,
            'maleCongressDistr': maleCongressDistr,
            'femaleCongressDistr': femaleCongressDistr,
            'maleMuni': maleMuni,
            'femaleMuni': femaleMuni
        }
        return Response(content)
