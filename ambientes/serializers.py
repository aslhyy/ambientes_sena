from rest_framework import serializers
from .models import Usuario, Ambiente, ItemInventario, Asignacion, HorarioAmbiente, Novedad

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ItemInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInventario
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    inventario = ItemInventarioSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ambiente
        fields = '__all__'

class NovedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novedad
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    novedades = NovedadSerializer(many=True, read_only=True)
    instructor_nombre = serializers.CharField(source='instructor.nombre', read_only=True)
    contratista_nombre = serializers.CharField(source='contratista_entrega.nombre', read_only=True)
    ambiente_codigo = serializers.CharField(source='ambiente.codigo', read_only=True)
    
    class Meta:
        model = Asignacion
        fields = '__all__'

class HorarioAmbienteSerializer(serializers.ModelSerializer):
    instructor_nombre = serializers.CharField(source='instructor.nombre', read_only=True)
    ambiente_codigo = serializers.CharField(source='ambiente.codigo', read_only=True)
    
    class Meta:
        model = HorarioAmbiente
        fields = '__all__'