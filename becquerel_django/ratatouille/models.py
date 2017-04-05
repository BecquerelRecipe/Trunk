from django.db import models


class WebSite(models.Model):
    url = models.URLField
    userGuideFilter = models.TextField
    ingredientFilter = models.TextField


class Recipe(models.Model):
    user_guide = models.TextField
    website_link = models.ForeignKey(WebSite, on_delete=models.CASCADE)
    suffix = models.TextField


class Ingredient(models.Model):
    ingredient_id = models.CharField(max_length=200)


class IngredientList(models.Model):
#    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ManyToManyField(Ingredient)



