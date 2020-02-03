from django import forms
from .models import Project

# class CommentForm(forms.Form):
# 	author = forms.CharField(
# 		max_length=60,
# 		widget=forms.TextInput(
# 			attrs={
# 				"class": "form-control",
# 				"placeholder": "Your Name:"
# 			})
# 	)
# 	body = forms.CharField(
# 		widget=forms.Textarea(
# 		attrs={
# 			"class": "form-control",
# 			"placeholder": "Leave a comment!"
# 		})
# 	)

# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     technology = models.CharField(max_length=20)
#     coordinator = models.CharField(max_length=70)
#     link = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images')
#     is_approved = models.BooleanField()

#     def __str__(self):
#         return self.title


# class CommentForm(forms.Form):
# 	author = forms.CharField(
# 		max_length=60,
# 		widget=forms.TextInput(
# 			attrs={
# 				"class": "form-control",
# 				"placeholder": "Your Name:"
# 			})
# 	)
# 	body = forms.CharField(
# 		widget=forms.Textarea(
# 		attrs={
# 			"class": "form-control",
# 			"placeholder": "Leave a comment!"
# 		})
# 	)

class ProposalForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label='Project title',
        max_length=100
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        )
    )

    technology = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label='Technology used',
        max_length=20
    )

    coordinator = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label='Project coordinator',
        max_length=70
    )

    coordinator_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ),
        label='Coordinator email'
    )

    link = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label='Github',
        max_length=100
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }
        ),
        label='Project image'
    )

    def process_proposal(self):
        data = self.cleaned_data

        project = Project()
        project.title = data['title']
        project.description = data['description']
        project.technology = data['technology']
        project.coordinator = data['coordinator']
        project.coordinator_email = data['coordinator_email']
        project.link = data['link']
        project.image = data['image']
        project.is_approved = False
        project.save()
