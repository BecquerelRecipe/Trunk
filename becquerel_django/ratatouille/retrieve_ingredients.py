from . import models

def retrieve(dico_ingredients):
    b = list(models.Ingredient.objects.all())
    #retriev ingredient names only

    a = [ing.ingredient_id for ing in b]
    for key, value in dico_ingredients.items():
       print(key)
       if key not in a:
            ingredient_object = models.Ingredient.objects.create(ingredient_id = key, calories_count = -1)
            ingredient_object.save()
    b = models.Ingredient.objects.all()
    a = [ing.ingredient_id for ing in b]
    print(a)
    return a
