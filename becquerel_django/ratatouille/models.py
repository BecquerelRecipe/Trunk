from django.db import models


class WebSite(models.Model):
    url = models.URLField
    user_guide_filter = models.CharField(blank=True, max_length=5000)
    ingredient_filter = models.CharField(blank=True,default=None, max_length=5000)


class Recipe(models.Model):
    user_guide = models.CharField(blank = True, max_length=200)
    website_link = models.ForeignKey(WebSite,blank=True, default=None,  on_delete=models.CASCADE)
    suffix = models.CharField(blank=True,default=None, max_length=200)


class Ingredient(models.Model):
    ingredient_id = models.CharField(max_length=200)
    calories_count = models.CharField(blank=True,default=None, max_length=200)
    ingredient_date = models.DateField('date published', default= "2010-01-01")

    def __str__(self):
        return self.ingredient_id


class IngredientList(models.Model):
#    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ManyToManyField(Ingredient)


class IngredientType(models.Model):
    ingredient_id = models.CharField(max_length=200)

