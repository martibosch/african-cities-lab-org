# Generated by Django 4.0.8 on 2023-06-06 16:51

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('one_column_block', wagtail.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('col_classes', wagtail.blocks.CharBlock()), ('one_column', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock())]))]))], blank=True, use_json_field=None),
        ),
    ]