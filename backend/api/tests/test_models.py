from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status
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


class CandidatoAPITest(APITestCase):
    def setUp(self):
        pan = Party.objects.create(name="Partido de Avanzada Nacional", shortName="PAN")
        nombre1 = Candidato.objects.create(
            name="Nombre1 Nombre2", lastname="Apellido1 Apellido2", gender="M", ethnicGroup="ML", twitter="candidato",
            maritalStatus="S", webpage="www.candidato.com", email="nombre@candidato.com", party=pan
        )
        solo = Candidato.objects.create(
            name="Solo", lastname="Obligatorios", gender="F", party=pan
        )
        nombre1.aspiredPosition = 'EX'
        nombre1.executivePosition = 'V'
        nombre1.inAskList = False
        gt = Municipality.objects.create(name="Guatemala", department="Guatemala")
        nombre1.municipio = gt
        nombre1.published = True
        nombre1.save()
        parlacen = District.objects.create(name="PARLACEN")
        solo.aspiredPosition = 'LEG'
        solo.district = parlacen
        solo.seat = 1
        solo.municipio = gt
        solo.inAskList = True
        solo.published = False
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

    def test_asklistGetAList(self):
        # test that the api is responding 200 ok to the given method
        response = self.client.get(reverse('candidato-ask'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        solo = Candidato.objects.get(name="Solo")
        nombre1 = Candidato.objects.get(email="nombre@candidato.com")
        response = self.client.get(reverse('candidato-ask'), format="json")
        self.assertContains(response, str(solo.name))
        self.assertContains(response, "Diputado")
        self.assertNotContains(response, str(nombre1.name))

    def test_askPresentedList(self):
        response = self.client.get(reverse('presented-ask'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        solo = Candidato.objects.get(name="Solo")
        nombre1 = Candidato.objects.get(email="nombre@candidato.com")
        response = self.client.get(reverse('presented-ask'), format="json")
        self.assertContains(response, str(nombre1.name))
        self.assertNotContains(response, str(solo.name))

    def test_askPresentedListWithTypeFilter(self):
        nombre1 = Candidato.objects.get(email="nombre@candidato.com")
        # test to put nombre1 as ex, should appear only on ex
        nombre1.aspiredPosition = 'EX'
        nombre1.save()
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'EX'}), format="json")
        self.assertContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'LEG'}), format="json")
        self.assertNotContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'M'}), format="json")
        self.assertNotContains(response, str(nombre1.name))
        # test to put nombre1 as LEG, should appear only on LEG
        nombre1.aspiredPosition = 'LEG'
        nombre1.save()
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'LEG'}), format="json")
        self.assertContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'EX'}), format="json")
        self.assertNotContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'M'}), format="json")
        self.assertNotContains(response, str(nombre1.name))
        # test to put nombre1 as M, should appear only on M
        nombre1.aspiredPosition = 'M'
        nombre1.save()
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'M'}), format="json")
        self.assertContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'EX'}), format="json")
        self.assertNotContains(response, str(nombre1.name))
        response = self.client.get(reverse('presented-ask', kwargs={'aspirantType': 'LEG'}), format="json")
        self.assertNotContains(response, str(nombre1.name))


class DistrictLisCreateAPITest(APITestCase):
    def testList(self):
        response = self.client.get(reverse('district-admin', kwargs={}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testCreate(self):
        data = {"name": "prueba"}
        response = self.client.post(reverse("district-admin"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DistrictEdit(APITestCase):
    def setUp(self):
        district = District.objects.create(name="Distrito Central")
        district.save()

    def testGetInstance(self):
        district = District.objects.get(name="Distrito Central")
        response = self.client.get(reverse('district-admin-edit', kwargs={"pk": str(district.id)}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testEditInstance(self):
        district = District.objects.get(name="Distrito Central")
        response = self.client.put(reverse('district-admin-edit', kwargs={"pk": str(district.id)}),
                                   {"name": "pruebatest"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        district = District.objects.get(name="pruebatest")
        self.assertEqual(
            str(district), "pruebatest"
        )

    def testDeleteInstance(self):
        district = District.objects.get(name="Distrito Central")
        response = self.client.delete(reverse('district-admin-edit', kwargs={"pk": str(district.id)}), format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
