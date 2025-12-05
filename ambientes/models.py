from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('CONTRATISTA', 'Contratista'),
        ('INSTRUCTOR', 'Instructor'),
        ('SUPERVISOR', 'Supervisor'),
        ('ADMIN', 'Administrador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    numero_identidad = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    
    def _str_(self):
        return f"{self.nombre} - {self.tipo_usuario}"

class Ambiente(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADO', 'Ocupado'),
        ('MANTENIMIENTO', 'Mantenimiento'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')
    
    def _str_(self):
        return f"{self.codigo} - {self.nombre}"

class ItemInventario(models.Model):
    TIPO_ITEM_CHOICES = [
        ('SILLA', 'Silla'),
        ('MESA', 'Mesa'),
        ('COMPUTADOR', 'Computador'),
        ('MOUSE', 'Mouse'),
        ('TECLADO', 'Teclado'),
        ('TABLERO', 'Tablero'),
    ]
    
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='inventario')
    tipo_item = models.CharField(max_length=20, choices=TIPO_ITEM_CHOICES)
    cantidad_esperada = models.IntegerField()
    cantidad_actual = models.IntegerField()
    estado = models.TextField(blank=True)
    
    def _str_(self):
        return f"{self.ambiente.codigo} - {self.tipo_item}"

class Asignacion(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVA', 'Activa'),
        ('CERRADA', 'Cerrada'),
    ]
    
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asignaciones_instructor')
    contratista_entrega = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asignaciones_contratista')
    supervisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asignaciones_supervisor', null=True, blank=True)
    
    fecha = models.DateField(auto_now_add=True)
    hora_recepcion = models.TimeField()
    hora_devolucion = models.TimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)
    
    firma_contratista = models.TextField(blank=True)  # Base64 o texto
    firma_instructor = models.TextField(blank=True)
    firma_supervisor = models.TextField(blank=True)
    
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVA')
    
    def _str_(self):
        return f"{self.ambiente.codigo} - {self.instructor.nombre} - {self.fecha}"

class HorarioAmbiente(models.Model):
    DIAS_SEMANA = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
        ('SABADO', 'Sábado'),
    ]
    
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='horarios')
    instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    programa_formacion = models.CharField(max_length=200)
    
    def _str_(self):
        return f"{self.ambiente.codigo} - {self.dia_semana} {self.hora_inicio}"

class Novedad(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('RESUELTA', 'Resuelta'),
    ]
    
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name='novedades')
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    
    def _str_(self):
        return f"Novedad - {self.asignacion.ambiente.codigo}"