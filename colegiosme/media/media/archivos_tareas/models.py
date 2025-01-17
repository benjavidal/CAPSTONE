from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

## --- PERSONA --- ##
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    nombre_nacionalidad = models.CharField(max_length=60)

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=10)

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut = models.BigIntegerField()
    p_nombre = models.CharField(max_length=40)
    s_nombre = models.CharField(max_length=40)
    ap_paterno = models.CharField(max_length=40)
    ap_materno = models.CharField(max_length=40)
    email = models.CharField(max_length=45)
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.PROTECT, db_column='id_nacionalidad')
    genero = models.ForeignKey('Genero', on_delete=models.PROTECT, db_column='id_genero')

    def __str__(self):
        return f'{self.p_nombre} {self.s_nombre} {self.ap_paterno} {self.ap_materno}'

## -- USUARIOS -- ##
class EstadoUsuario(models.Model):
    id_estado_usuario = models.AutoField(primary_key=True)
    nombre_estado_usuario = models.CharField(max_length=40)

class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=40)

class Usuario(AbstractUser):
    estado_usuario = models.ForeignKey('EstadoUsuario', on_delete=models.PROTECT, db_column='id_estado_usuario')
    tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.PROTECT, db_column='id_tipo_usuario')
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT, db_column='id_persona')

## -- DIRECCION -- ##
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.PROTECT, db_column='id_region')

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=45)
    numero = models.IntegerField()
    departamento = models.CharField(max_length=45, blank=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.PROTECT, db_column='id_comuna')
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT, db_column='id_persona')

## -- FUNCIONARIO -- ##
class TipoEspecializacion(models.Model):
    id_tipo_especializacion = models.AutoField(primary_key=True)
    tipo_especializacion = models.CharField(max_length=45)

class Especializacion(models.Model):
    id_especializacion = models.AutoField(primary_key=True)
    nombre_especializacion = models.CharField(max_length=45)
    tipo_especializacion = models.ForeignKey('TipoEspecializacion', on_delete=models.PROTECT, db_column='id_tipo_especializacion')

class CargoFuncionario(models.Model):
    id_cargo_funcionario = models.AutoField(primary_key=True)
    nombre_cargo_funcionario = models.CharField(max_length=40)

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT, db_column='id_persona')
    cargo_funcionario = models.ForeignKey('CargoFuncionario', on_delete=models.PROTECT, db_column='id_cargo_funcionario')

    def __str__(self):
        return f'{self.persona}'

class FuncionarioEspecializacion(models.Model):
    id_funcionario_especializacion = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT, db_column='id_funcionario')

## -- NOTICIAS -- ##
class TipoNoticia(models.Model):
    id_tipo_noticia = models.AutoField(primary_key=True)
    nombre_tipo_noticia = models.CharField(max_length=40)

class PrioridadNoticia(models.Model):
    id_prioridad_noticia = models.AutoField(primary_key=True)
    nombre_prioridad_noticia = models.CharField(max_length=40)

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo_noticia = models.CharField(max_length=45)
    subtitulo_noticia = models.CharField(max_length=45)
    cuerpo_noticia = models.CharField(max_length=45)
    fecha_noticia = models.DateField()
    imagen_noticia = models.CharField(max_length=45)
    tipo_noticia = models.ForeignKey('TipoNoticia', on_delete=models.PROTECT, db_column='id_tipo_noticia')
    prioridad_noticia = models.ForeignKey('PrioridadNoticia', on_delete=models.PROTECT, db_column='id_prioridad_noticia')
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT, db_column='id_funcionario')

## -- ALUMNO -- ##
class EstadoAlumno(models.Model):
    id_estado_alumno = models.AutoField(primary_key=True)
    nombre_estado_alumno = models.CharField(max_length=40)

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    alumno_prioritario = models.BooleanField(default=False)
    enfermedad_cronica = models.CharField(max_length=45, blank=True)
    discapacidad_fisica = models.CharField(max_length=45, blank=True)
    seguro_escolar_particular = models.CharField(max_length=45, blank=True)
    evaluacion_profesional = models.BooleanField(default=False)
    colegio_procedencia = models.CharField(max_length=45, blank=True)
    razon_cambio_colegio = models.CharField(max_length=45, blank=True)
    medio_llego_colegio = models.CharField(max_length=45, blank=True)
    pie = models.BooleanField(default=False)
    estado_alumno = models.ForeignKey('EstadoAlumno', on_delete=models.PROTECT, db_column='id_estado_alumno')
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT, db_column='id_persona')

    def __str__(self):
        return f'{self.persona.p_nombre} {self.persona.s_nombre} {self.persona.ap_paterno} {self.persona.ap_materno}'

## -- APODERADO -- ##
class NivelAcademico(models.Model):
    id_nivel_academico = models.AutoField(primary_key=True)
    nombre_nivel_academico = models.CharField(max_length=40)

class Apoderado(models.Model):
    id_apoderado = models.AutoField(primary_key=True)
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT, db_column='id_persona')
    nivel_academico = models.ForeignKey('NivelAcademico', on_delete=models.PROTECT, db_column='id_nivel_academico')


## -- GRUPO FAMILIAR -- ##
class Parentesco(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=40)

class GrupoFamiliar(models.Model):
    id_grupo_familiar = models.AutoField(primary_key=True)
    es_responsable = models.BooleanField()
    alumno = models.ForeignKey('Alumno', on_delete=models.PROTECT, db_column='id_alumno')
    apoderado = models.ForeignKey('Apoderado', on_delete=models.PROTECT, db_column='id_apoderado')
    parentesco = models.ForeignKey('Parentesco', on_delete=models.PROTECT, db_column='id_parentesco')

## -- CURSOS -- ##
class EstadoCurso(models.Model):
    id_estado_curso = models.AutoField(primary_key=True)
    nombre_estado_curso = models.CharField(max_length=40)

class TipoCurso(models.Model):
    id_letra_curso = models.AutoField(primary_key=True)
    nombre_tipo_curso = models.CharField(max_length=1)

class ListaCurso(models.Model):
    id_lista_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=40)

class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    nombre_jornada = models.CharField(max_length=10)

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    anio_curso = models.IntegerField()
    matriculas_disponibles = models.IntegerField()
    lista_curso = models.ForeignKey('ListaCurso', on_delete=models.PROTECT, db_column='id_lista_curso')
    estado_curso = models.ForeignKey('EstadoCurso', on_delete=models.PROTECT, db_column='id_estado_curso')
    tipo_curso = models.ForeignKey('TipoCurso', on_delete=models.PROTECT, db_column='id_tipo_curso')
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT, db_column='id_profesor_jefe')
    jornada = models.ForeignKey('Jornada', on_delete=models.PROTECT, db_column='id_jornada')

    def __str__(self):
        return f'{self.lista_curso.nombre_curso} {self.tipo_curso.nombre_tipo_curso} - {self.jornada.nombre_jornada}'

## -- ASISTENCIA -- ##
class TipoAsistencia(models.Model):
    id_tipo_asistencia = models.AutoField(primary_key=True)
    nombre_tipo_asistencia = models.CharField(max_length=40)

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    fecha_asistencia = models.DateField()
    tipo_asistencia = models.ForeignKey('TipoAsistencia', on_delete=models.PROTECT, db_column='id_tipo_asistencia')
    alumno = models.ForeignKey('Alumno', on_delete=models.PROTECT, db_column='id_alumno')
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, db_column='id_curso')

## -- MATRICULA -- ##
class EstadoMatricula(models.Model):
    id_estado_matricula = models.AutoField(primary_key=True)
    nombre_estado_matricula = models.CharField(max_length=40)

class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    ultimo_curso_aprobado = models.CharField(max_length=40)
    fecha_matricula = models.DateField()
    estado_matricula = models.ForeignKey('EstadoMatricula', on_delete=models.PROTECT, db_column='id_estado_matricula')
    alumno = models.ForeignKey('Alumno', on_delete=models.PROTECT, db_column='id_alumno')
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, db_column='id_curso')

## -- MENSUALIDAD -- ##
class EstadoMensualidad(models.Model):
    id_estado_mensualidad = models.AutoField(primary_key=True)
    nombre_estado_mensualidad = models.CharField(max_length=40)

class TipoMensualidad(models.Model):
    id_tipo_mensualidad = models.AutoField(primary_key=True)
    nombre_tipo_mensualidad = models.CharField(max_length=40)

class Mensualidad(models.Model):
    id_mensualidad = models.AutoField(primary_key=True)
    monto_total = models.IntegerField()
    fecha_vencimiento = models.DateField()
    estado_mensualidad = models.ForeignKey('EstadoMensualidad', on_delete=models.PROTECT, db_column='id_estado_mensualidad')
    tipo_mensualidad = models.ForeignKey('TipoMensualidad', on_delete=models.PROTECT, db_column='id_tipo_mensualidad')
    matricula = models.ForeignKey('Matricula', on_delete=models.PROTECT, db_column='id_matricula')

## -- ASIGNATURAS -- ##
class ListaAsignatura(models.Model):
    id_lista_asignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre_asignatura}'

class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    lista_asignatura = models.ForeignKey('ListaAsignatura', on_delete=models.PROTECT, db_column='id_lista_asignatura')
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, db_column='id_curso')
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT, db_column='id_funcionario')

## -- ANOTACIONES -- ##
class TipoAnotacion(models.Model):
    id_tipo_anotacion = models.AutoField(primary_key=True)
    nombre_tipo_anotacion = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre_tipo_anotacion}'

class Anotacion(models.Model):
    id_anotacion = models.AutoField(primary_key=True)
    descripcion_anotacion = models.TextField()
    fecha_anotacion = models.DateField(default=timezone.now)
    tipo_anotacion = models.ForeignKey('TipoAnotacion', on_delete=models.PROTECT, db_column='id_tipo_anotacion')
    lista_asignatura = models.ForeignKey('ListaAsignatura', on_delete=models.PROTECT, db_column='id_lista_asignatura')
    matricula = models.ForeignKey('Matricula', on_delete=models.PROTECT, db_column='id_matricula')

## -- NOTAS -- ##
class Notas(models.Model):
    id_notas = models.AutoField(primary_key=True)
    nota = models.FloatField()
    matricula = models.ForeignKey('Matricula', on_delete=models.PROTECT, db_column='id_matricula')
    lista_asignatura = models.ForeignKey('ListaAsignatura', on_delete=models.PROTECT, db_column='id_lista_asignatura')