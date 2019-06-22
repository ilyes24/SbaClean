# Generated by Django 2.2.1 on 2019-05-24 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0003_auto_20190524_1728'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Post.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pictures',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Post.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='Address.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reaction',
            name='reaction_owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reaction',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='Post.Post'),
        ),
    ]