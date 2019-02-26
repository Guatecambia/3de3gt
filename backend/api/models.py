from django.db import models


class Party(models.Model):
    name = models.CharField("Nombre del partido", max_length=200, null=False)
    shortName = models.CharField("Nombre corto", max_length=50, null=False)
    phone = models.CharField("teléfono", max_length=150)
    facebook = models.CharField("Página de Facebook", max_length=200)
    twitter = models.CharField("twitter", max_length=50)
    secretary = models.CharField("Secretario General", max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField("Nombre del distrito", max_length=150, null=False, unique=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField("Nombre del municipio", max_length=125, null=False)
    department = models.CharField("Nombre del departamento", max_length=125, null=False)

    def __str__(self):
        return 'Municipio '+self.name+' en '+self.department


class Candidato(models.Model):
    GENDERS = (
                ('M', 'Masculino'),
                ('F', 'Femenino'),
                ('O', 'Otro')
    )
    ETHNICITIES = (
                    ('I', 'Indígena'),
                    ('ML', 'Mestizo/Ladino'),
                    ('O', 'Otro')
    )
    STATUS = (
                ('S', 'Soltero'),
                ('C', 'Casado'),
                ('UH', 'En unión de hecho'),
                ('O', 'Otro')
    )
    POSITION_TYPES = (
                        ('EX', 'Ejecutivo'),
                        ('LEG', 'Diputado'),
                        ('M', 'Alcalde')
    )
    EXECUTIVE_POSITIONS = (
                            ('P', 'Presidente'),
                            ('V', 'Vicepresidente')
    )

    class Meta:
        verbose_name_plural = 'Candidatos'
        verbose_name = 'Candidato'

    name = models.CharField("Nombres", max_length=200, null=False)
    lastname = models.CharField("Apellidos", max_length=200, null=False)
    gender = models.CharField("Género", max_length=1, choices=GENDERS, null=False)
    genderOther = models.CharField("Especifique género", max_length=50)
    ethnicity = models.CharField("Grupo étnico", max_length=2, choices=ETHNICITIES)
    ethnicOther = models.CharField("Especifique grupo étnico", max_length=50)
    twitter = models.CharField("Cuenta de twitter @", max_length=50)
    facebook = models.CharField("Página de Facebook", max_length=200)
    maritalStatus = models.CharField("Estado Civil (al momento de presentar la declaración)", max_length=2,
                                     choices=STATUS)
    webpage = models.CharField("Página Web", max_length=300)
    email = models.CharField("Correo electrónico", max_length=300)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    aspiredPosition = models.CharField("Posición a la que aspira", max_length=3, choices=POSITION_TYPES)
    # executiveFields
    executivePosition = models.CharField("Cargo al que aspira", max_length=1, choices=EXECUTIVE_POSITIONS, null=True)
    # legislativeFields
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    seat = models.PositiveSmallIntegerField(null=True)
    # MunicipalityFields
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True)
    inAskList = models.BooleanField("En lista de exige #3de3", default=True)
    published = models.BooleanField("En lista de los que publicaron", default=False)

    def __str__(self):
        return self.name+' '+self.lastname

    def save(self, *args, **kwargs):
        if (self.aspiredPosition == 'Ejecutivo'):
            # null the legislative fields
            self.district = None
            self.seat = None
            # null the municipality fields
            self.municipality = None
        elif (self.aspiredPosition == 'Legislativo'):
            # null the executive fields
            self.executivePosition = None
            # null the municipality fields
            self.municipality = None
        elif (self.aspiredPosition == 'Alcalde'):
            # null the executive fields
            self.executivePosition = None
            # null the legislative fields
            self.district = None
            self.seat = None
        super(Candidato, self).save(*args, **kwargs)
