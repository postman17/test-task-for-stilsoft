# Generated by Django 3.1.5 on 2021-01-21 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'books__authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'books__books',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'books__publishers',
            },
        ),
        migrations.AddIndex(
            model_name='publisher',
            index=models.Index(fields=['title'], name='books__publ_title_a75af5_idx'),
        ),
        migrations.AddIndex(
            model_name='publisher',
            index=models.Index(fields=['created_at'], name='books__publ_created_7ecc2f_idx'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, related_name='books_written', to='books.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.publisher'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['title'], name='books__auth_title_0c9765_idx'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['created_at'], name='books__auth_created_1ebd90_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title'], name='books__book_title_1facbe_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['created_at'], name='books__book_created_062308_idx'),
        ),
    ]
