from wagtail_modeltranslation.translation import TranslationOptions
from modeltranslation.decorators import register
from .models import HomePage
from ls.joyous.models import GroupPage, CalendarPage, SimpleEventPage, MultidayEventPage, RecurringEventPage

@register(HomePage)
class HomeTR(TranslationOptions):
    fields = (
    )

from ls.joyous.models.calendar import CalendarPageForm
CalendarPageForm.registerImportHandler = lambda *args: None

@register(CalendarPage)
class CalendarTR(TranslationOptions):
    fields = (
    )

@register(GroupPage)
class GroupTR(TranslationOptions):
    fields = (
    )

@register(SimpleEventPage)
class SimpleEventTR(TranslationOptions):
    fields = (
    )

@register(MultidayEventPage)
class MultidayTR(TranslationOptions):
    fields = (
    )

@register(RecurringEventPage)
class RecurringEventTR(TranslationOptions):
    fields = (
    )
