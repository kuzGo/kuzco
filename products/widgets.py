from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ('Remove')
    initial_text = _('')
    template_name = 'watches/custom_widget_templates/custom_clearable_file_input.html'