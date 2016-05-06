from .models import Post
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .forms import IngredientForm
from .models import Ingredient

def post_list(request):
	if request.method == "POST":
		form = IngredientForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request, 'blog/post_list.html', {})
	else:
		form = IngredientForm()
		return render(request, 'blog/post_list.html', {'form': form})
	
	
