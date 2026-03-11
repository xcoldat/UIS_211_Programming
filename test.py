# Задача
# Имеется набор данных о поездках пассажиров в городском транспорте за месяц. Требуется:

# 1. Подсчитать общее число поездок;

# 2. Определить самые загруженные часы;

# 3. Выявить популярные маршруты;

# 4. Построить соответствующие графики.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")         

# Создание примерных данных (имитация реального датасета)
data = {
    'trip_id': range(1, 1001),
    'route': ['А1', 'Б2', 'А1', 'В3', 'Б2', 'А1', 'Г4', 'В3', 'А1', 'Б2'] * 100,
    'start_time': pd.date_range('2024-04-01 06:00', periods=1000, freq='15min'),
    'duration_min': [15, 20, 18, 25, 22, 16, 30, 24, 17, 19] * 100,
    'passenger_count': [1, 2, 1, 3, 1, 2, 1, 4, 1, 2] * 100
}

df = pd.DataFrame(data)

# Базовая аналитика
total_trips = len(df)
total_passengers = df['passenger_count'].sum()
avg_duration = df['duration_min'].mean()

print(f"Общее число поездок: {total_trips}")
print(f"Всего перевезено пассажиров: {total_passengers}")
print(f"Средняя продолжительность поездки: {avg_duration:.1f} мин")

# Анализ по часам
df['hour'] = df['start_time'].dt.hour
hourly_trips = df.groupby('hour').size()

# Анализ по маршрутам
route_trips = df['route'].value_counts()

#  Визуализация
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Аналитика поездок на общественном транспорте', fontsize=16)

# График 1: Число поездок по часам
axes[0, 0].bar(hourly_trips.index, hourly_trips.values, color='skyblue')
axes[0, 0].set_title('Число поездок по часам суток')
axes[0, 0].set_xlabel('Час суток')
axes[0, 0].set_ylabel('Число поездок')
axes[0, 0].grid(axis='y', alpha=0.3)

# График 2: Популярность маршрутов
axes[0, 1].pie(route_trips.values, labels=route_trips.index, autopct='%1.1f%%')
axes[0, 1].set_title('Распределение поездок по маршрутам')

# График 3: Распределение продолжительности поездок
axes[1, 0].hist(df['duration_min'], bins=15, color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Распределение продолжительности поездок')
axes[1, 0].set_xlabel('Продолжительность (мин)')
axes[1, 0].set_ylabel('Число поездок')
axes[1, 0].grid(axis='y', alpha=0.3)

# График 4: Число пассажиров по часам
hourly_passengers = df.groupby('hour')['passenger_count'].sum()
axes[1, 1].plot(hourly_passengers.index, hourly_passengers.values, marker='o', color='orange')
axes[1, 1].set_title('Число перевезённых пассажиров по часам')
axes[1, 1].set_xlabel('Час суток')
axes[1, 1].set_ylabel('Число пассажиров')
axes[1, 1].grid(True, alpha=0.3)

# Общая настройка
plt.tight_layout()
plt.show()

# 6. Дополнительные метрики
print("\nСамые загруженные часы (топ-3):")
print(hourly_trips.sort_values(ascending=False).head(3))

print("\nСамые популярные маршруты (топ-3):")
print(route_trips.head(3))


    