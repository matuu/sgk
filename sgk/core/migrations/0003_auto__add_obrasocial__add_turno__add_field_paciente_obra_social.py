# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ObraSocial'
        db.create_table(u'core_obrasocial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='obrasocial', null=True, to=orm['core.Contacto'])),
        ))
        db.send_create_signal(u'core', ['ObraSocial'])

        # Adding model 'Turno'
        db.create_table(u'core_turno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dia', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('hora', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.TimeField')()),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('asistio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aviso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('profesional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profesion'])),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Paciente'], null=True)),
        ))
        db.send_create_signal(u'core', ['Turno'])

        # Adding field 'Paciente.obra_social'
        db.add_column(u'core_paciente', 'obra_social',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ObraSocial'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ObraSocial'
        db.delete_table(u'core_obrasocial')

        # Deleting model 'Turno'
        db.delete_table(u'core_turno')

        # Deleting field 'Paciente.obra_social'
        db.delete_column(u'core_paciente', 'obra_social_id')


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
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'core.obrasocial': {
            'Meta': {'object_name': 'ObraSocial'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'obrasocial'", 'null': 'True', 'to': u"orm['core.Contacto']"}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'core.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'altura': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obra_social': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ObraSocial']", 'null': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "u'soltero'", 'max_length': '255'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'profesion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Profesion']", 'null': 'True'})
        },
        u'core.profesion': {
            'Meta': {'object_name': 'Profesion'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.profesional': {
            'Meta': {'object_name': 'Profesional'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"})
        },
        u'core.turno': {
            'Meta': {'object_name': 'Turno'},
            'asistio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aviso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dia': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.TimeField', [], {}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Paciente']", 'null': 'True'}),
            'profesional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Profesion']"})
        }
    }

    complete_apps = ['core']