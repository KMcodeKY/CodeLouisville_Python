from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Checklist


class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ('title', 'start_date', 'end_date', 'description', 'category', 'completed')

    def clean(self):
        cleaned_data = super(ChecklistForm, self).clean()

        start_date_clean = cleaned_data.get('start_date')
        end_date_clean = cleaned_data.get('end_date')

        if start_date_clean and end_date_clean:
            if start_date_clean > end_date_clean:
                self.add_error(None, ValidationError('End Date must be greater than Start Date'))