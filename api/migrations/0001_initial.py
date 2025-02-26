# Generated by Django 5.1.6 on 2025-02-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitais',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('hora_funcionamento', models.CharField(max_length=100)),
                ('especialidades', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='hospitais')),
            ],
        ),
    ]
