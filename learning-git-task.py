shopping_list = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

item_count = 0

for shop in shopping_list:
    item_count += len(shopping_list[shop])
    print(
        f"Idę do {shop.title()} i kupuję tam {list(map(lambda x: x.title(), shopping_list[shop]))}")
print(f"W sumie kupuję {item_count} produktów")