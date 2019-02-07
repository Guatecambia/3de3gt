from django.test import TestCase
from ..models import Candidato, District, Municipality, Party


class PartyTest(TestCase):
    """Test module for Party"""

    def setUp(self):
        Party.objects.create(name="Partido de Avanzada Nacional", shortName="PAN")
        Party.objects.create(name="Visión con Valores", shortName="VIVA")

    def test_party(self):
        pan = Party.objects.get(shortName="PAN")
        viva = Party.objects.get(shortName="VIVA")
        self.assertEqual(
            str(pan), "Partido de Avanzada Nacional"
        )
        self.assertEqual(
            str(viva), "Visión con Valores"
        )


class DistrictTest(TestCase):
    def setUp(self):
        District.objects.create(name="Distrito Central")
        District.objects.create(name="PARLACEN")

    def test_district(self):
        dcen = District.objects.get(name="Distrito Central")
        parlacen = District.objects.get(name="PARLACEN")
        self.assertEqual(
            str(dcen), "Distrito Central"
        )
        self.assertEqual(
            str(parlacen), "PARLACEN"
        )


class MunicipalityTest(TestCase):
    def setUp(self):
        Municipality.objects.create(name="Guatemala", department="Guatemala")
        Municipality.objects.create(name="Mixco", department="Guatemala")

    def test_municipality(self):
        gt = Municipality.objects.get(name="Guatemala")
        mix = Municipality.objects.get(name="Mixco")
        self.assertEqual(
            str(gt), "Municipio Guatemala en Guatemala"
        )
        self.assertEqual(
            str(mix), "Municipio Mixco en Guatemala"
        )


class CandidatoTest(TestCase):
    """ Test module for Candidato """

    def setUp(self):
        pan = Party.objects.create(name="Partido de Avanzada Nacional", shortName="PAN")
        nombre1 = Candidato.objects.create(
            name="Nombre1 Nombre2", lastname="Apellido1 Apellido2", gender="M", ethnicity="ML", twitter="candidato",
            maritalStatus="S", webpage="www.candidato.com", email="nombre@candidato.com", party=pan
        )
        solo = Candidato.objects.create(
            name="Solo", lastname="Obligatorios", gender="F", party=pan
        )
        nombre1.aspiredPosition = 'EX'
        nombre1.executivePosition = 'V'
        gt = Municipality.objects.create(name="Guatemala", department="Guatemala")
        nombre1.municipio = gt
        nombre1.save()
        parlacen = District.objects.create(name="PARLACEN")
        solo.aspiredPosition = 'L'
        solo.district = parlacen
        solo.seat = 1
        solo.municipio = gt
        solo.save()

    def test_candidato(self):
        nombre1 = Candidato.objects.get(email="nombre@candidato.com")
        solo = Candidato.objects.get(name="Solo")
        self.assertEqual(
            str(nombre1), "Nombre1 Nombre2 Apellido1 Apellido2"
        )
        self.assertEqual(
            nombre1.executivePosition, "V"
        )
        self.assertEqual(
            # check that it has no municipality, since it should erase it on save
            str(nombre1.municipality), str(None)
        )
        self.assertEqual(
            str(solo), "Solo Obligatorios"
        )
        self.assertEqual(
            str(solo.district), "PARLACEN"
        )
        self.assertEqual(
            solo.seat, 1
        )
        self.assertEqual(
            # check that it has no municipality, since it should erase it on save
            str(solo.municipality), str(None)
        )

    def test_candidatosave(self):
        nombre1 = Candidato.objects.get(email="nombre@candidato.com")
        solo = Candidato.objects.get(name="Solo")
        self.assertEqual(
            str(nombre1), "Nombre1 Nombre2 Apellido1 Apellido2"
        )
        self.assertEqual(
            str(solo), "Solo Obligatorios"
        )
