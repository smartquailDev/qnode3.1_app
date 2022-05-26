from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    admin_user = models.CharField(max_length=50,null=True,verbose_name='Nombre del Administrador')
    direccion = models.CharField(max_length=50,null=True,verbose_name='Direccion del edificio')
    telefono = models.CharField(max_length=50,null=True,verbose_name='Número de contacto de administración')
    pisos = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='Número de pisos')
    comunal = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='Número de áreas comunales')
    RUC = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)],blank=True,verbose_name='Registro único de contribuyente' )
    #date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True,verbose_name='Foto de Usuario')

    def __str__(self):
        return '{}'.format(self.direccion)
        #return 'Perfil del edificio: {}'.format(self.user.username)


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from,
                                      self.user_to)


# Add following field to User dynamically
User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
