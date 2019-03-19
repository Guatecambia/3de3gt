from django.db import models
from django.core.validators import FileExtensionValidator


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

PARTY_TYPES = (
                ('PP', 'Partido Político'),
                ('CC', 'Comité Civico')
)
VERIFICATION_STATUS = (
                        ('N', 'Nuevo'),
                        ('C', 'Convertido'),
                        ('BV', 'Verificando'),
                        ('D', 'Descartado')
)
G_DECLARATIONS = (
                    ('I', 'Declaración de interés'),
                    ('P', 'Declaración patrimonial')
)


class Party(models.Model):
    name = models.CharField("Nombre del partido", max_length=200, null=False)
    tType = models.CharField("Tipo de entidad", max_length=2, choices=PARTY_TYPES, null=False)
    shortName = models.CharField("Nombre corto", max_length=50, null=True)
    phone = models.CharField("teléfono", max_length=150, null=True)
    facebook = models.CharField("Página de Facebook", max_length=200, null=True)
    twitter = models.CharField("twitter", max_length=50, null=True)
    secretary = models.CharField("Secretario General", max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField("Nombre del distrito", max_length=150, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField("Nombre del municipio", max_length=125, null=False)
    department = models.CharField("Nombre del departamento", max_length=125, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Municipio '+self.name+' en '+self.department


class Candidato(models.Model):
    class Meta:
        verbose_name_plural = 'Candidatos'
        verbose_name = 'Candidato'

    name = models.CharField("Nombres", max_length=200, null=False)
    lastname = models.CharField("Apellidos", max_length=200, null=False)
    gender = models.CharField("Género", max_length=1, choices=GENDERS, null=True)
    genderOther = models.CharField("Especifique género", max_length=50, null=True)
    ethnicGroup = models.CharField("Grupo étnico", max_length=2, choices=ETHNICITIES, null=True)
    ethnicOther = models.CharField("Especifique grupo étnico", max_length=50, null=True)
    twitter = models.CharField("Cuenta de twitter @", max_length=50, null=False)
    facebook = models.CharField("Página de Facebook", max_length=200, null=True)
    maritalStatus = models.CharField("Estado Civil (al momento de presentar la declaración)", max_length=2,
                                     choices=STATUS, null=True)
    aspiredPosition = models.CharField("Posición a la que aspira", max_length=3, choices=POSITION_TYPES, null=False)
    # executiveFields
    executivePosition = models.CharField("Cargo al que aspira", max_length=1, choices=EXECUTIVE_POSITIONS, null=True)
    # legislativeFields
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)
    seat = models.PositiveSmallIntegerField(null=True)
    # MunicipalityFields
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT, null=True)

    party = models.ForeignKey(Party, on_delete=models.PROTECT, null=False)
    email = models.CharField("Correo electrónico", max_length=300, null=True)
    celphone = models.CharField("Celular", max_length=40, null=True)
    phone = models.CharField("Oficina/Casa", max_length=40, null=True)
    webpage = models.CharField("Página Web", max_length=300, null=True)

    helpName = models.CharField("Nombres", max_length=200, null=True)
    helpLastname = models.CharField("Apellidos", max_length=200, null=True)
    helpEmail = models.CharField("Correo electrónico", max_length=300, null=True)
    helpCelphone = models.CharField("Celular", max_length=40, null=True)

    authLetter = models.FileField(upload_to='documents/', null=True)
    solvencia = models.FileField(upload_to='documents/', null=True)

    inAskList = models.BooleanField("En lista de exige #3de3", default=True, null=False)
    published = models.BooleanField("En lista de los que publicaron", default=False)
    patrimonialLine = models.PositiveSmallIntegerField(null=True)
    interestsLine = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class Presentado(models.Model):
    class Meta:
        verbose_name_plural = 'Presentados'
        verbose_name = 'Presentado'

    name = models.CharField("Nombres", max_length=200, null=False)
    lastname = models.CharField("Apellidos", max_length=200, null=False)
    gender = models.CharField("Género", max_length=1, choices=GENDERS, null=False)
    genderOther = models.CharField("Especifique género", max_length=50, null=True)
    ethnicGroup = models.CharField("Grupo étnico", max_length=2, choices=ETHNICITIES, null=False)
    ethnicOther = models.CharField("Especifique grupo étnico", max_length=50, null=True)
    twitter = models.CharField("Cuenta de twitter @", max_length=50, null=False)
    facebook = models.CharField("Página de Facebook", max_length=200, null=False)
    maritalStatus = models.CharField("Estado Civil (al momento de presentar la declaración)", max_length=2,
                                     choices=STATUS, null=False)
    aspiredPosition = models.CharField("Posición a la que aspira", max_length=3, choices=POSITION_TYPES, null=False)
    # executiveFields
    executivePosition = models.CharField("Cargo al que aspira", max_length=1, choices=EXECUTIVE_POSITIONS, null=True)
    # legislativeFields
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)
    seat = models.PositiveSmallIntegerField(null=True)
    # MunicipalityFields
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT, null=True)

    party = models.ForeignKey(Party, on_delete=models.PROTECT, null=False)
    email = models.CharField("Correo electrónico", max_length=300, null=False)
    celphone = models.CharField("Celular", max_length=40, null=False)
    phone = models.CharField("Oficina/Casa", max_length=40, null=False)
    webpage = models.CharField("Página Web", max_length=300, null=True)

    helpName = models.CharField("Nombres", max_length=200, null=True)
    helpLastname = models.CharField("Apellidos", max_length=200, null=True)
    helpEmail = models.CharField("Correo electrónico", max_length=300, null=True)
    helpCelphone = models.CharField("Celular", max_length=40, null=True)

    authLetter = models.FileField(
                                    upload_to='documents/',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                                    null=False)
    solvencia = models.FileField(
                                    upload_to='documents/',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                                    null=False)

    status = models.CharField("Estado", max_length=2, choices=VERIFICATION_STATUS, null=False, default="N")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        super(Presentado, self).save(*args, **kwargs)
        

class DeclarationAnswer(models.Model):
    class Meta:
        verbose_name_plural = 'DeclarationAnswers'
        verbose_name = 'DeclarationAnswer'

    position = models.PositiveSmallIntegerField(null=False)
    fieldName = models.CharField("Pregunta", max_length=350, null=False)
    fieldValue = models.TextField("Respuesta", null=True)
    formType = models.CharField("Formulario", max_length=1, null=False, choices=G_DECLARATIONS)
    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
