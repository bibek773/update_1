# Generated by Django 4.2.2 on 2023-09-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userinfo_name', models.CharField(max_length=150)),
                ('userinfo_Uname', models.CharField(max_length=150)),
                ('userinfo_Ftname', models.CharField(max_length=150)),
                ('userinfo_Mtname', models.CharField(max_length=150)),
                ('userinfo_email', models.EmailField(max_length=150)),
                ('userinfo_userpic', models.ImageField(max_length=150, upload_to='')),
                ('userinfo_phoneno1', models.CharField(max_length=150)),
                ('userinfo_phoneno2', models.CharField(max_length=150)),
                ('userinfo_phoneno3', models.CharField(max_length=150)),
                ('userinfo_password', models.CharField(max_length=150)),
                ('userinfo_gender', models.CharField(max_length=150)),
                ('userinfo_Edulvl', models.CharField(max_length=150)),
                ('userinfo_Expedu', models.CharField(max_length=150)),
                ('userinfo_State', models.CharField(max_length=150)),
                ('userinfo_City', models.CharField(max_length=150)),
                ('userinfo_Zip', models.CharField(max_length=150)),
                ('userinfo_DoB', models.DateField()),
                ('userinfo_jdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
