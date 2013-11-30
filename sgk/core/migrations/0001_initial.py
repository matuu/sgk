# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacto'
        db.create_table(u'core_contacto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('horario', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Contacto'])

        # Adding model 'Profesion'
        db.create_table(u'core_profesion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Profesion'])

        # Adding model 'Persona'
        db.create_table(u'core_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dni', self.gf('django.db.models.fields.IntegerField')()),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Contacto'], null=True)),
            ('profesion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profesion'], null=True)),
        ))
        db.send_create_signal(u'core', ['Persona'])

        # Adding model 'Profesional'
        db.create_table(u'core_profesional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'])),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Profesional'])

        # Adding model 'Paciente'
        db.create_table(u'core_paciente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'])),
            ('peso', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('altura', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Paciente'])


    def backwards(self, orm):
        # Deleting model 'Contacto'
        db.delete_table(u'core_contacto')

        # Deleting model 'Profesion'
        db.delete_table(u'core_profesion')

        # Deleting model 'Persona'
        db.delete_table(u'core_persona')

        # Deleting model 'Profesional'
        db.delete_table(u'core_profesional')

        # Deleting model 'Paciente'
        db.delete_table(u'core_paciente')


    models = {
        u'core.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'horario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'core.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'altura': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'core.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Contacto']", 'null': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.IntegerField', [], {}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'profesion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Profesion']", 'null': 'True'})
        },
        u'core.profesion': {
            'Meta': {'object_name': 'Profesion'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {})
        },
        u'core.profesional': {
            'Meta': {'object_name': 'Profesional'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"})
        }
    }

    complete_apps = ['core']