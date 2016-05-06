from django import forms

from .models import Post, Ingredient

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
		
class IngredientForm(forms.ModelForm):
	class Meta:
		model=Ingredient
		fields=('ingredient',)