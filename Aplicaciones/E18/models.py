from django.db import models

class EmpresaAgricola(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    contacto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(EmpresaAgricola, on_delete=models.CASCADE)
    bioinformatico_agrario = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='proyectos_liderados'
    )

    def __str__(self):
        return self.titulo
