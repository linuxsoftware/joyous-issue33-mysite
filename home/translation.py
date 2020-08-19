from wagtail_modeltranslation.translation import TranslationOptions
from modeltranslation.decorators import register
from .models import HomePage
from ls.joyous.models import (
        EventCategory, EventBase, CancellationBase,
        GroupPage, CalendarPage, SimpleEventPage, MultidayEventPage,
        RecurringEventPage, MultidayRecurringEventPage, ExtraInfoPage,
        CancellationPage, PostponementPage, RescheduleMultidayEventPage,
        ExtCancellationPage, ClosedForHolidaysPage)

@register(HomePage)
class HomeTR(TranslationOptions):
    fields = (
    )

#from ls.joyous.models.calendar import CalendarPageForm
#CalendarPageForm.registerImportHandler = lambda *args: None

@register(CalendarPage)
class CalendarTR(TranslationOptions):
    fields = (
        'intro',
    )

@register(EventCategory)
class EventCategoryTR(TranslationOptions):
    fields = (
        'name',
    )

@register(GroupPage)
class GroupTR(TranslationOptions):
    fields = (
        'content',
    )

@register(SimpleEventPage)
class SimpleEventTR(TranslationOptions):
    fields = (
        'details',
    )

@register(MultidayEventPage)
class MultidayTR(TranslationOptions):
    fields = (
        'details',
    )

@register(RecurringEventPage)
class RecurringEventTR(TranslationOptions):
    fields = (
        'details',
    )

@register(MultidayRecurringEventPage)
class MultidayRecurringEventTR(TranslationOptions):
    fields = (
    )

@register(ExtraInfoPage)
class ExtraInfoTR(TranslationOptions):
    fields = (
        'extra_title',
        'extra_information',
    )

@register(CancellationBase)
class CancellationBaseTR(TranslationOptions):
    fields = (
        'cancellation_title',
        'cancellation_details',
    )

@register(CancellationPage)
class CancellationTR(TranslationOptions):
    fields = (
    )

@register(PostponementPage)
class PostponementTR(TranslationOptions):
    fields = (
        'postponement_title',
        'details',
    )

@register(RescheduleMultidayEventPage)
class RescheduleMultidayEventTR(TranslationOptions):
    fields = (
    )

@register(ExtCancellationPage)
class ExtCancellationTR(TranslationOptions):
    fields = (
    )

@register(ClosedForHolidaysPage)
class ClosedForHolidaysTR(TranslationOptions):
    fields = (
    )
