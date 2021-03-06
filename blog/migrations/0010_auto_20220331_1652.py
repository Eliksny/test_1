# Generated by Django 3.0.6 on 2022-03-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220331_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Tag'),
        ),
    ]
