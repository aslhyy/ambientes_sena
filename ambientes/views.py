from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario, Ambiente, ItemInventario, Asignacion, HorarioAmbiente, Novedad
from .serializers import (
    UsuarioSerializer, AmbienteSerializer, ItemInventarioSerializer,
    AsignacionSerializer, HorarioAmbienteSerializer, NovedadSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    @action(detail=False, methods=['get'])
    def instructores(self, request):
        instructores = Usuario.objects.filter(tipo_usuario='INSTRUCTOR')
        serializer = self.get_serializer(instructores, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def contratistas(self, request):
        contratistas = Usuario.objects.filter(tipo_usuario='CONTRATISTA')
        serializer = self.get_serializer(contratistas, many=True)
        return Response(serializer.data)

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    
    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        disponibles = Ambiente.objects.filter(estado='DISPONIBLE')
        serializer = self.get_serializer(disponibles, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def inventario(self, request, pk=None):
        ambiente = self.get_object()
        items = ambiente.inventario.all()
        serializer = ItemInventarioSerializer(items, many=True)
        return Response(serializer.data)

class ItemInventarioViewSet(viewsets.ModelViewSet):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    
    @action(detail=False, methods=['get'])
    def activas(self, request):
        activas = Asignacion.objects.filter(estado='ACTIVA')
        serializer = self.get_serializer(activas, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def cerrar(self, request, pk=None):
        asignacion = self.get_object()
        asignacion.estado = 'CERRADA'
        asignacion.hora_devolucion = request.data.get('hora_devolucion')
        asignacion.save()
        
        # Cambiar estado del ambiente
        asignacion.ambiente.estado = 'DISPONIBLE'
        asignacion.ambiente.save()
        
        serializer = self.get_serializer(asignacion)
        return Response(serializer.data)

class HorarioAmbienteViewSet(viewsets.ModelViewSet):
    queryset = HorarioAmbiente.objects.all()
    serializer_class = HorarioAmbienteSerializer
    
    @action(detail=False, methods=['get'])
    def por_ambiente(self, request):
        ambiente_id = request.query_params.get('ambiente_id')
        horarios = HorarioAmbiente.objects.filter(ambiente_id=ambiente_id)
        serializer = self.get_serializer(horarios, many=True)
        return Response(serializer.data)

class NovedadViewSet(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    serializer_class = NovedadSerializer