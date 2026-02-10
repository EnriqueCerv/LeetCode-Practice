class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        can_make_recipe = {}
        supplies = set(supplies)
        recipes_set = set(recipes)
        recipe_to_idx = {recipe : idx for idx, recipe in enumerate(recipes)}

        visit = {}

        def can_make(recipe):
            if recipe in can_make_recipe:
                return can_make_recipe[recipe]

            if visit.get(recipe, 0) == 1:
                can_make_recipe[recipe] = False
                return False
            
            visit[recipe] = 1
            recipe_idx = recipe_to_idx[recipe]

            for ingredient in ingredients[recipe_idx]:
                if ingredient not in recipes_set:
                    if ingredient not in supplies:
                        can_make_recipe[recipe] = False
                        visit[recipe] = 2
                        return False
                else:
                    can_make_cur = can_make(ingredient)
                    if not can_make_cur:
                        can_make_recipe[ingredient] = False
                        visit[recipe] = 2
                        return False

            can_make_recipe[recipe] = True
            visit[recipe] = 2
            return True
        
        for recipe in recipes:
            can_make(recipe)
        
        return [recipe for recipe, boolean in can_make_recipe.items() if boolean]