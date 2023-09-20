def main():
    tabla_nutri = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemno": 15,
        "lime" : 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "peneapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine" : 50,
        "watermelon": 80
    }

    fruta = input("Item: ").lower().strip()
    if fruta not in tabla_nutri:
        return False

    print(f"Calories : {tabla_nutri[fruta]}")

main()
