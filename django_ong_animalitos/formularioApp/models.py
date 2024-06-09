from django.db import models

# Create your models here.

class usuarioAdopcion(models.Model):
    uuid = models.AutoField(db_column='idUsuario',primary_key='True')
    nombre = models.CharField(max_length=20 , blank=False , null=False )
    apellidoP = models.CharField(max_length=20 , blank=False , null=False )
    apellidoM = models.CharField(max_length=20 , blank=False , null=False )
    rut = models.CharField(max_length=10 , blank=False , null=False )
    fecha_nacimiento = models.DateField(blank=False , null=False )
    edad = models.IntegerField(blank=False,null=False)
    profesion = models.CharField(max_length=100 , blank=False , null=False )
    genero = models.ForeignKey('generoUsuario',on_delete=models.CASCADE,db_column='genero')
    email = models.CharField(max_length=100 , blank=False , null=False )
    celular = models.CharField(max_length=12 , blank=False , null=False )
    direccion = models.CharField(max_length=200 , blank=False , null=False )
    direccion2 = models.CharField(max_length=200 , blank=True , null=True )
    region = models.CharField(max_length=200 , blank=False , null=False )
    comuna = models.CharField(max_length=200 , blank=False , null=False )
    cod_postal = models.CharField(max_length=10 , blank=False , null=False )
    observacion = models.CharField(max_length=350 , blank=False , null=False )
    check_correos = models.BooleanField()  
    
    def __str__(self) :
        return str(self.uuid) 
    
#Profesiones

#Genero
class generoUsuario(models.Model):
    id_genero = models.AutoField(db_column='idUsuario',primary_key='True')
    genero = models.CharField(max_length=20 , blank=False , null=False )
    
    def __str__(self) :
        return str(self.genero)
    