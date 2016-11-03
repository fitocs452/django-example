from __future__ import unicode_literals

from django.db import models


class Pais(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True)

    def __unicode__(self):
        return self.nombre


class Familia(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True)

    pais = models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        null=True)

    def __unicode__(self):
        return "%s (%s)" % (
            self.nombre,
            self.persona_set.count())


class Persona(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True)

    apellido = models.CharField(
        max_length=250,
        null=False,
        blank=True)

    edad = models.IntegerField(
        default=0,
        null=False,
        blank=True)

    familia = models.ForeignKey(
        Familia,
        null=False,
        on_delete=models.CASCADE)

    @property
    def edad_al_cuadrado(self):
        return self.edad ** 2

    def get_edad_cuadrado(self):
        return self.edad ** 2

    def __unicode__(self):
        return "%s %s" % (self.nombre, self.apellido)


class Curso(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True)

    integrantes = models.ManyToManyField(
        Persona,
        through='CursoIntegrante')

    def __unicode__(self):
        return self.nombre


class CursoIntegrante(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE)

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE)

    asignado_en = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s - %s" % (
            self.persona,
            self.curso,
            self.asignado_en)
