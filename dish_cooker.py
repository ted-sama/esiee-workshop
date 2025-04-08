def favorite_dish(ingredients: dict):
    """
    Cooks my favorite dish.
    """
    # Check if the ingredients are available
    if not all(ingredient in ingredients for ingredient in ["onions", "tomato_sauce", "meat", "spices", "pasta"]):
        raise ValueError("Missing ingredients")

    # Cook the dish
    print(f"{ingredients['onions']['amount']} {ingredients['onions']['type']} onions cut into {ingredients['onions']['cut']} pieces")
    print(f"{ingredients['meat']['amount']} of {ingredients['meat']['type']} meat cooked")
    print(f"{ingredients['spices']['amount']} of {ingredients['spices']['type']} spices added")
    print(f"{ingredients['pasta']['amount']} of {ingredients['pasta']['type']} pasta boiled")
    print(f"{ingredients['tomato_sauce']['amount']} of {ingredients['tomato_sauce']['type']} tomato sauce added")
    print("Dish cooked successfully!")


ingredients = {
    "onions": {
        "amount": "2",
        "type": "red",
        "cut": "small dices"
    },
    "tomato_sauce": {
        "amount": "1 can",
        "type": "basilic"
    },
    "meat": {
        "amount": "500g",
        "type": "ground beef"
    },
    "spices": {
        "amount": "2 tablespoons",
        "type": "paprika, salt, pepper, oregano"
    },
    "pasta": {
        "amount": "200g",
        "type": "spaghetti"
    }
}

favorite_dish(ingredients)