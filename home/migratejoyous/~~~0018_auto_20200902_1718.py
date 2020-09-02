# Generated by Django 3.0.9 on 2020-09-02 17:18

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('joyous', '0017_extcancellationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introductory text.', null=True, verbose_name='intro'),
        ),
        migrations.AddField(
            model_name='calendarpage',
            name='intro_fr',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introductory text.', null=True, verbose_name='intro'),
        ),
        migrations.AddField(
            model_name='cancellationpage',
            name='cancellation_details_en',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='cancellationpage',
            name='cancellation_details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='cancellationpage',
            name='cancellation_title_en',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='cancellationpage',
            name='cancellation_title_fr',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='closedforholidayspage',
            name='cancellation_details_en',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='closedforholidayspage',
            name='cancellation_details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='closedforholidayspage',
            name='cancellation_title_en',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='closedforholidayspage',
            name='cancellation_title_fr',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='eventcategory',
            name='name_en',
            field=models.CharField(max_length=80, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='eventcategory',
            name='name_fr',
            field=models.CharField(max_length=80, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='extcancellationpage',
            name='cancellation_details_en',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='extcancellationpage',
            name='cancellation_details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='extcancellationpage',
            name='cancellation_title_en',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='extcancellationpage',
            name='cancellation_title_fr',
            field=models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='extrainfopage',
            name='extra_information_en',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Information just for this date', null=True, verbose_name='extra information'),
        ),
        migrations.AddField(
            model_name='extrainfopage',
            name='extra_information_fr',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Information just for this date', null=True, verbose_name='extra information'),
        ),
        migrations.AddField(
            model_name='extrainfopage',
            name='extra_title_en',
            field=models.CharField(blank=True, help_text='A more specific title for this occurence (optional)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='extrainfopage',
            name='extra_title_fr',
            field=models.CharField(blank=True, help_text='A more specific title for this occurence (optional)', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='grouppage',
            name='content_en',
            field=wagtail.core.fields.RichTextField(blank=True, default='', help_text='An area of text for whatever you like', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='grouppage',
            name='content_fr',
            field=wagtail.core.fields.RichTextField(blank=True, default='', help_text='An area of text for whatever you like', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='multidayeventpage',
            name='details_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='multidayeventpage',
            name='details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='postponementpage',
            name='details_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='postponementpage',
            name='details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='postponementpage',
            name='postponement_title_en',
            field=models.CharField(help_text='The title for the postponed event', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postponementpage',
            name='postponement_title_fr',
            field=models.CharField(help_text='The title for the postponed event', max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='recurringeventpage',
            name='details_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='recurringeventpage',
            name='details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='simpleeventpage',
            name='details_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
        migrations.AddField(
            model_name='simpleeventpage',
            name='details_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='details'),
        ),
    ]