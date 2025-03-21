# Generated by Django 5.1.4 on 2025-03-17 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ipfs_id', models.CharField(max_length=100, unique=True)),
                ('ip', models.CharField(max_length=45)),
                ('port', models.IntegerField(default=5001)),
                ('is_active', models.BooleanField(default=True)),
                ('load', models.FloatField(default=0.0)),
                ('consecutive_failures', models.IntegerField(default=0)),
                ('last_seen', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('ipfs_hash', models.CharField(max_length=255)),
                ('size', models.BigIntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('checksum', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FileChunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk_index', models.IntegerField()),
                ('ipfs_hash', models.CharField(max_length=255, unique=True)),
                ('reference_hash', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.BigIntegerField(null=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='storage.file')),
            ],
        ),
        migrations.CreateModel(
            name='ChunkDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chunk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributions', to='storage.filechunk')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunk_distributions', to='storage.node')),
            ],
            options={
                'unique_together': {('chunk', 'node')},
            },
        ),
    ]
