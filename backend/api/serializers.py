from rest_framework import serializers
from .models import Candidato, District, Municipality, Party, Presentado
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            'id',
            'name',
        )


class DistrictSelectSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    text = serializers.CharField(source='name')
    
    class Meta:
        model = District
        fields = (
            'value',
            'text',
        )


class MunicipalitySelectSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    text = serializers.SerializerMethodField('form_text')
    
    class Meta:
        model = Municipality
        fields = (
          'value',
          'text',
        )

    def form_text(self, obj):
        return obj.department + ' - ' + obj.name
    

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            'name',
            'shortname',
            'facebook',
            'twitter'
        )


class PartySelectSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    text = serializers.CharField(source='name')
    
    class Meta:
        model = Party
        fields = (
            'value',
            'text',
        )


class CandidatoSerializer(serializers.ModelSerializer):
    """
    Used to display data on the frontend
    """
    gender = serializers.SerializerMethodField()
    party_name = serializers.CharField(source='party.name', read_only=True)
    partyIcon = serializers.CharField(source='party.twitter', read_only=True)
    aspiredPosition = serializers.SerializerMethodField()

    class Meta:
        model = Candidato
        fields = (
            'name',
            'lastname',
            'gender',
            'twitter',
            'facebook',
            'party_name',
            'partyIcon',
            'aspiredPosition',
            'district',
            'seat',
            'municipality'
        )

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_aspiredPosition(self, obj):
        if (obj.aspiredPosition == 'EX'):
            return obj.get_executivePosition_display()
        else:
            return obj.get_aspiredPosition_display()


class CandidatoAdminSerializer(serializers.ModelSerializer):
    """
    used to manage Candidato model, on the admin section
    """
    partyType = serializers.CharField(source='party.tType', read_only=True)

    class Meta:
        model = Candidato
        fields = (
            'id',
            'name',
            'lastname',
            'gender',
            'genderOther',
            'ethnicGroup',
            'ethnicOther',
            'twitter',
            'facebook',
            'maritalStatus',
            'aspiredPosition',
            'executivePosition',
            'district',
            'seat',
            'municipality',
            'partyType',
            'party',
            'email',
            'celphone',
            'phone',
            'webpage',
            'helpName',
            'helpLastname',
            'helpEmail',
            'helpCelphone',
            'authLetter',
            'solvencia',
            'inAskList',
            'published'
        )


class PresentadoSerializer(serializers.ModelSerializer):
    """
    used to insert data in Presentado model, from the form on the frontend
    """
    class Meta:
        model = Presentado
        fields = (
            'name',
            'lastname',
            'gender',
            'genderOther',
            'ethnicGroup',
            'ethnicOther',
            'twitter',
            'facebook',
            'maritalStatus',
            'aspiredPosition',
            'executivePosition',
            'district',
            'seat',
            'municipality',
            'party',
            'email',
            'celphone',
            'phone',
            'webpage',
            'helpName',
            'helpLastname',
            'helpEmail',
            'helpCelphone',
            'authLetter',
            'solvencia'
        )


class PresentadoAdminSerializer(serializers.ModelSerializer):
    partyType = serializers.CharField(source='party.tType', read_only=True)
    authLetter = serializers.URLField(read_only=True)
    solvencia = serializers.URLField(read_only=True)

    class Meta:
        model = Presentado
        fields = (
            'id',
            'name',
            'lastname',
            'gender',
            'genderOther',
            'ethnicGroup',
            'ethnicOther',
            'twitter',
            'facebook',
            'maritalStatus',
            'aspiredPosition',
            'executivePosition',
            'district',
            'seat',
            'municipality',
            'partyType',
            'party',
            'email',
            'celphone',
            'phone',
            'webpage',
            'helpName',
            'helpLastname',
            'helpEmail',
            'helpCelphone',
            'authLetter',
            'solvencia',
            'status'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Acceso denegado")
