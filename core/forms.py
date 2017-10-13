from datetime import datetime

from django import forms
from django.forms.widgets import TimeInput

DAY_CHOICES = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
)


class FindForm(forms.Form):
    start = forms.TimeField(initial=datetime.now())
    end = forms.TimeField(initial=datetime.now())
    day = forms.ChoiceField(choices=DAY_CHOICES, initial=(datetime.today().isoweekday(), datetime.today().strftime("%A")))