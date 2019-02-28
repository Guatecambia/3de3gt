from rest_framework import serializers
from .models import Candidato, District, Party, Presentado


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            'id',
            'name',
        )


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            'name',
            'shortname',
            'facebook',
            'twitter'
        )


class CandidatoSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    party_name = serializers.CharField(source='party.name', read_only=True)
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


class PresentadoSerializer(serializers.ModelSerializer):
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
