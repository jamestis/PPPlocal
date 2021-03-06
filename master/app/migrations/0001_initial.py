# Generated by Django 3.0.7 on 2020-06-13 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('parent_challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('parent_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='parent_course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course'),
        ),
    ]
