# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookCache'
        db.create_table(u'game_facebookcache', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'game', ['FacebookCache'])

        # Adding model 'UserProfile'
        db.create_table(u'game_userprofile', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=22, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['game.FacebookCache'], unique=True, null=True, blank=True)),
            ('games_finished', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('games_won', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
        ))
        db.send_create_signal(u'game', ['UserProfile'])

        # Adding model 'Player'
        db.create_table(u'game_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('has_tnt', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_move', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.UserProfile'])),
        ))
        db.send_create_signal(u'game', ['Player'])

        # Adding model 'Game'
        db.create_table(u'game_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mine', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('state', self.gf('django.db.models.fields.SmallIntegerField')(default=0, db_index=True)),
            ('seq_num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=22, null=True, blank=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=22, unique=True)),
            ('p1', self.gf('django.db.models.fields.related.OneToOneField')(related_name='game_as_p1', unique=True, to=orm['game.Player'])),
            ('p2', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='game_as_p2', unique=True, null=True, to=orm['game.Player'])),
        ))
        db.send_create_signal(u'game', ['Game'])


    def backwards(self, orm):
        # Deleting model 'FacebookCache'
        db.delete_table(u'game_facebookcache')

        # Deleting model 'UserProfile'
        db.delete_table(u'game_userprofile')

        # Deleting model 'Player'
        db.delete_table(u'game_player')

        # Deleting model 'Game'
        db.delete_table(u'game_game')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.facebookcache': {
            'Meta': {'object_name': 'FacebookCache'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        u'game.game': {
            'Meta': {'object_name': 'Game'},
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '22', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mine': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'p1': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'game_as_p1'", 'unique': 'True', 'to': u"orm['game.Player']"}),
            'p2': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'game_as_p2'", 'unique': 'True', 'null': 'True', 'to': u"orm['game.Player']"}),
            'seq_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True', 'blank': 'True'})
        },
        u'game.player': {
            'Meta': {'object_name': 'Player'},
            'has_tnt': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_move': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.UserProfile']"})
        },
        u'game.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'facebook': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['game.FacebookCache']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'games_finished': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'games_won': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'total_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game']