from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']

   

    def clean(self):
        # data is feteched using the super function of django
        super(CommentForm, self).clean()

        name  = self.cleaned_data.get('name')
        comment = self.cleaned_data.get('comment')


        if len(name) < 3:
            self._errors['name'] = self.error_class([
                '3 characters and more is required for this field'
            ])
        if len(comment) < 4:
            self._errors['comment'] = self.error_class([
                'comments should be more than 4 characters'
            ])
        return self.cleaned_data

