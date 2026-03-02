import csv
from collections import defaultdict

# выручка по дням
revenue_by_day = defaultdict(float)

# количество по товарам (чтобы найти самый продаваемый)
qty_by_product = defaultdict(int)

total_revenue = 0.0

with open("sales.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        day = row["дата"]
        product = row["товар"]

        # важно: из CSV всё приходит строками → приводим типы
        qty = int(row["количество"])
        price = float(row["цена_за_единицу"])

        revenue = qty * price

        revenue_by_day[day] += revenue
        qty_by_product[product] += qty
        total_revenue += revenue

# 1) выручка за каждый день
print("Выручка по дням:")
for day in sorted(revenue_by_day):
    print(f"{day}: {revenue_by_day[day]:.2f}")

# 2) выручка за весь период
print(f"\nОбщая выручка за период: {total_revenue:.2f}")

# 3) самый продаваемый товар по количеству
best_product, best_qty = max(qty_by_product.items(), key=lambda x: x[1])
print(f"\nСамый продаваемый товар: {best_product} (кол-во: {best_qty})")