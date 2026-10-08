"""Задание №11. Таблица «Магазины» и диаграмма Matplotlib.

Запуск из PyCharm: установить matplotlib и нажать Run для main.py.
"""

from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


# Первые 4 магазина — из условия. Следующие 4 добавлены для задания.
# Объем продаж задан в рублях, торговая площадь — в кв. м.
MAGAZINY = [
    {"№": 1, "магазин": "Заря", "товары": 500, "продажи": 98.4,
     "площадь": 100, "тип": "прод.", "район": "Ленинский"},
    {"№": 2, "магазин": "Зорька", "товары": 350, "продажи": 95.25,
     "площадь": 120, "тип": "пром.", "район": "Советский"},
    {"№": 3, "магазин": "Радуга", "товары": 2000, "продажи": 106.8,
     "площадь": 1000, "тип": "прод.", "район": "Ленинский"},
    {"№": 4, "магазин": "Рассвет", "товары": 1001, "продажи": 120.5,
     "площадь": 560, "тип": "пром.", "район": "Калининский"},
    {"№": 5, "магазин": "Виктория", "товары": 820, "продажи": 110.4,
     "площадь": 350, "тип": "прод.", "район": "Центральный"},
    {"№": 6, "магазин": "Маяк", "товары": 420, "продажи": 75.6,
     "площадь": 180, "тип": "пром.", "район": "Московский"},
    {"№": 7, "магазин": "Орион", "товары": 700, "продажи": 89.2,
     "площадь": 280, "тип": "пром.", "район": "Ленинский"},
    {"№": 8, "магазин": "Семья", "товары": 1500, "продажи": 132.5,
     "площадь": 600, "тип": "прод.", "район": "Советский"},
]


TIPY = {"прод.": "Продовольственные", "пром.": "Промышленные"}


def zagolovok(nomer, tekst):
    print(f"\n{nomer}. {tekst}")
    print("-" * 80)


def pechat_tablicu(spisok):
    """Выводит читаемую таблицу без дополнительных библиотек."""
    print(f"{'№':>2}  {'Магазин':<13} {'Товары':>7} {'Продажи, руб.':>14} "
          f"{'Площадь, м²':>13}  {'Тип':<6} {'Район'}")
    print("-" * 85)
    for m in spisok:
        print(f"{m['№']:>2}  {m['магазин']:<13} {m['товары']:>7} "
              f"{m['продажи']:>14.2f} {m['площадь']:>13}  "
              f"{m['тип']:<6} {m['район']}")


def punkt_1():
    """Списки по типам: продажи / площадь ниже среднего по 8 магазинам."""
    zagolovok(1, "Магазины с коэффициентом продаж на 1 м² ниже среднего")
    sredniy = sum(m["продажи"] / m["площадь"] for m in MAGAZINY) / len(MAGAZINY)
    print(f"Средний коэффициент (все магазины): {sredniy:.4f} руб./м²")

    for tip, nazvanie in TIPY.items():
        print(f"\n{nazvanie} магазины:")
        naydeny = [m for m in MAGAZINY
                   if m["тип"] == tip and m["продажи"] / m["площадь"] < sredniy]
        if not naydeny:
            print("  Нет магазинов с коэффициентом ниже среднего.")
            continue
        for m in naydeny:
            coefficient = m["продажи"] / m["площадь"]
            print(f"  {m['магазин']}: {coefficient:.4f} руб./м²")


def punkt_2():
    zagolovok(2, "Магазины по возрастанию торговой площади")
    for m in sorted(MAGAZINY, key=lambda x: x["площадь"]):
        print(f"{m['магазин']:<13} — {m['площадь']} м²")


def punkt_3():
    zagolovok(3, "Два продовольственных магазина с минимальной площадью")
    prodovolstvennye = [m for m in MAGAZINY if m["тип"] == "прод."]
    dva = sorted(prodovolstvennye, key=lambda x: x["площадь"])[:2]
    for m in dva:
        print(f"{m['магазин']}: {m['площадь']} м²")


def punkt_4():
    zagolovok(4, "Объем продаж и средняя торговая площадь по типам")
    gruppy = defaultdict(list)
    for m in MAGAZINY:
        gruppy[m["тип"]].append(m)

    for tip, nazvanie in TIPY.items():
        spisok = gruppy[tip]
        obem_prodazh = sum(m["продажи"] for m in spisok)
        srednyaya_ploshchad = sum(m["площадь"] for m in spisok) / len(spisok)
        print(f"{nazvanie} ({len(spisok)} шт.):")
        print(f"  Общий объем продаж: {obem_prodazh:.2f} руб.")
        print(f"  Средняя торговая площадь: {srednyaya_ploshchad:.2f} м²")


def punkt_5():
    zagolovok(5, "Магазины по алфавиту")
    for m in sorted(MAGAZINY, key=lambda x: x["магазин"].casefold()):
        print(m["магазин"])


def punkt_6():
    zagolovok(6, "Диаграмма торговых площадей (Matplotlib)")
    spisok = sorted(MAGAZINY, key=lambda x: x["площадь"])
    nazvaniya = [m["магазин"] for m in spisok]
    ploshchadi = [m["площадь"] for m in spisok]

    plt.rcParams["font.family"] = "DejaVu Sans"  # Кириллица
    fig, ax = plt.subplots(figsize=(10, 6))
    stolbcy = ax.barh(nazvaniya, ploshchadi)
    ax.set_title("Торговые площади магазинов", fontsize=15, pad=16)
    ax.set_xlabel("Площадь (кв. м)")
    ax.set_ylabel("Магазин")
    ax.set_xlim(0, max(ploshchadi) * 1.18)
    ax.bar_label(stolbcy, fmt="%.0f", padding=4)
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()

    put_k_faylu = Path(__file__).resolve().parent / "diagramma_torgovyh_ploshchadey.png"
    fig.savefig(put_k_faylu, dpi=160, bbox_inches="tight")
    print(f"Диаграмма сохранена: {put_k_faylu}")
    print("Откроется окно с диаграммой. Закройте его для завершения программы.")
    plt.show()


def main():
    print("ЗАДАНИЕ №11 — МАГАЗИНЫ")
    print("Исходная таблица: 8 записей")
    pechat_tablicu(MAGAZINY)
    punkt_1()
    punkt_2()
    punkt_3()
    punkt_4()
    punkt_5()
    punkt_6()


if __name__ == "__main__":
    main()
