from django import forms

class UserInputForm(forms.Form):
    input_text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Input Text'
    )
    submit = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Submit'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop('disabled', False)
        super().__init__(*args, **kwargs)
        if disabled:
            self.fields['input_text'].widget.attrs['disabled'] = 'disabled'
            self.fields['submit'].widget.attrs['disabled'] = 'disabled'