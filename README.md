# Sistema de Asignación de Ambientes - SENA/Institución Educativa

## 1.1 Nombre de la aplicación
**SIGAS** - Sistema Integral de Gestión de Ambientes y Salones

## 1.2 Problema que resuelve
Actualmente, el control de asignación de ambientes se hace manualmente en papel, 
generando:
- Pérdida de planillas
- Dificultad para rastrear quién tiene un ambiente
- Falta de control de inventarios
- Conflictos de horarios
- No hay respaldo digital de las firmas

## 1.3 Tipo de usuarios
1. **Contratista**: Persona que entrega las llaves del ambiente
2. **Instructor**: Recibe y usa el ambiente para clases
3. **Supervisor de Contrato**: Valida y supervisa entregas
4. **Administrador del Sistema**: Gestiona usuarios, ambientes e inventarios

## 1.4 Objetivos

### Objetivo General
Digitalizar y automatizar el proceso de asignación, entrega y devolución 
de ambientes de formación, garantizando trazabilidad y control de inventarios.

### Objetivos Específicos
1. Registrar digitalmente cada entrega y devolución de ambientes
2. Mantener un inventario actualizado por ambiente
3. Gestionar horarios y asignaciones de instructores
4. Generar reportes de uso y novedades
5. Reducir uso de papel y mejorar la trazabilidad

# Requisitos del Sistema SIGAS

## 2.1 Requisitos Funcionales

### Módulo de Usuarios
RF01. El sistema debe permitir registrar contratistas con: nombre, cédula, 
      teléfono y correo
RF02. El sistema debe permitir registrar instructores
RF03. El sistema debe permitir registrar supervisores de contrato

### Módulo de Ambientes
RF04. El sistema debe permitir registrar ambientes (ej: B04, A201)
RF05. El sistema debe permitir registrar inventario por ambiente 
      (sillas, mesas, computadores, etc.)
RF06. El sistema debe verificar el estado del inventario en cada entrega

### Módulo de Asignaciones
RF07. El sistema debe registrar quién recibe el ambiente
RF08. El sistema debe registrar fecha y hora de recepción
RF09. El sistema debe registrar fecha y hora de devolución
RF10. El sistema debe permitir agregar observaciones
RF11. El sistema debe registrar firmas digitales (contratista, instructor, 
      supervisor)

### Módulo de Horarios
RF12. El sistema debe mostrar horarios de ambientes ocupados
RF13. El sistema debe asignar instructores a horarios específicos
RF14. El sistema debe alertar conflictos de horarios

### Reportes
RF15. El sistema debe generar reporte de asignaciones por fecha
RF16. El sistema debe generar reporte de novedades
RF17. El sistema debe generar historial por ambiente

## 2.2 Requisitos No Funcionales

RNF01. **Seguridad**: El sistema debe validar usuarios con autenticación
RNF02. **Rendimiento**: Debe responder consultas en menos de 2 segundos
RNF03. **Usabilidad**: Interfaz intuitiva y fácil de usar
RNF04. **Disponibilidad**: Disponible 24/7 con 99% uptime
RNF05. **Escalabilidad**: Soportar hasta 500 usuarios concurrentes

## 2.3 Historias de Usuario

**HU01**: Como contratista, quiero registrar la entrega de un ambiente para 
          tener control de a quién le entregué las llaves.

**HU02**: Como instructor, quiero ver mi horario de ambientes asignados para 
          planificar mis clases.

**HU03**: Como contratista, quiero verificar el inventario del ambiente antes 
          de entregarlo para asegurar que todo esté completo.

**HU04**: Como supervisor, quiero revisar las asignaciones del día para 
          validar que todo esté en orden.

**HU05**: Como administrador, quiero generar reportes mensuales de uso de 
          ambientes para analizar la ocupación.

**HU06**: Como instructor, quiero reportar novedades al devolver un ambiente 
          para dejar constancia de problemas encontrados.

**HU07**: Como contratista, quiero consultar el historial de un ambiente para 
          ver quién lo ha usado.

# Modelo de datos para documentar

## Diagrama de arquitectura general

<img width="240" height="462" alt="image" src="https://github.com/user-attachments/assets/3295f57d-2e56-4c4f-9129-73ec4d9b06cf" />

## Modelado de datos

<img width="283" height="478" alt="image" src="https://github.com/user-attachments/assets/ef474dab-c29b-49e7-a37d-fe4bf36228be" />

# Modelo de datos para documentar

Entidades principales:

1. Usuario
   - id
   - nombre
   - tipo_usuario (Contratista/Instructor/Supervisor/Admin)
   - numero_identidad
   - telefono
   - correo
   - contraseña (hash)

2. Ambiente
   - id
   - codigo (ej: B04)
   - nombre
   - capacidad
   - estado (Disponible/Ocupado/Mantenimiento)

3. ItemInventario
   - id
   - ambiente_id (FK)
   - tipo_item (Silla/Mesa/Computador/Mouse/Teclado)
   - cantidad_esperada
   - cantidad_actual
   - estado

4. Asignacion
   - id
   - ambiente_id (FK)
   - instructor_id (FK - Usuario)
   - contratista_entrega_id (FK - Usuario)
   - supervisor_id (FK - Usuario)
   - fecha
   - hora_recepcion
   - hora_devolucion
   - observaciones
   - firma_contratista (texto o imagen base64)
   - firma_instructor (texto o imagen base64)
   - firma_supervisor (texto o imagen base64)
   - estado (Activa/Cerrada)

5. HorarioAmbiente
   - id
   - ambiente_id (FK)
   - instructor_id (FK)
   - dia_semana
   - hora_inicio
   - hora_fin
   - programa_formacion

6. Novedad
   - id
   - asignacion_id (FK)
   - descripcion
   - fecha_reporte
   - estado (Pendiente/Resuelta)

Relaciones:
- Un Ambiente tiene muchos ItemInventario (1:N)
- Un Ambiente tiene muchas Asignaciones (1:N)
- Un Usuario (Instructor) tiene muchas Asignaciones (1:N)
- Una Asignación tiene muchas Novedades (1:N)
- Un Ambiente tiene muchos HorarioAmbiente (1:N)
