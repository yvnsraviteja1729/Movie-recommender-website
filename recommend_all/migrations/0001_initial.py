# Generated by Django 3.2.6 on 2022-02-18 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=199)),
            ],
        ),
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='watched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous', models.IntegerField()),
                ('watch_time', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_all.signup')),
            ],
        ),
        migrations.CreateModel(
            name='movie_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_index', models.IntegerField()),
                ('comment', models.TextField()),
                ('watch_time', models.DateTimeField(auto_now_add=True)),
                ('positive', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_all.signup')),
            ],
        ),
        migrations.AddConstraint(
            model_name='watched',
            constraint=models.UniqueConstraint(fields=('username', 'previous'), name='watched_constraint'),
        ),
        migrations.AlterUniqueTogether(
            name='watched',
            unique_together={('username', 'previous')},
        ),
        migrations.AddConstraint(
            model_name='movie_comment',
            constraint=models.UniqueConstraint(fields=('username', 'watch_time', 'movie_index'), name='watched_constraint3'),
        ),
        migrations.AlterUniqueTogether(
            name='movie_comment',
            unique_together={('username', 'watch_time', 'movie_index')},
        ),
    ]
