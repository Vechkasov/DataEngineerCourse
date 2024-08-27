from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, \
    StringType, IntegerType, DateType

import os
import random
import argparse
from datetime import date

prepared_names = ['Леонид', 'Милий', 'Елизар', 'Лев', 'Аверкий', 'Тарас', 'Ярополк', 'Трифон', 'Поликарп',
                  'Владлен', 'Модест', 'Дементий', 'Агата', 'Октябрина', 'Лора', 'Любосмысл', 'Давыд', 'Стоян',
                  'Светозар', 'Тит', 'Любомир', 'Алевтина', 'Терентий', 'Велимир', 'Радован', 'Станислав', 'Варфоломей',
                  'Мартын', 'Ксения', 'Порфирий']
prepared_cities = ['к. Соль-Илецк', 'г. Котельнич', 'к. Клин', 'д. Старая Русса', 'с. Калач', 'п. Кунгур',
                   'клх Великий Устюг', 'п. Плес', 'ст. Холмогоры',
                   'ст. Нижнекамск', 'д. Клин', 'клх Дно', 'клх Чикола', 'г. Бологое', 'п. Пинега', 'к. Сладково',
                   'клх Ямбург', 'клх Черусти', 'п. Тулун',
                   'д. Калач-на-Дону', 'с. Туруханск', 'ст. Тамбей', 'г. Йошкар-Ола', 'п. Усть-Кулом', 'г. Оймякон',
                   'г. Семлячики', 'клх Эльтон', 'п. Яшалта',
                   'клх Курганинск', 'с. Малгобек']


def generate_list(num: int) -> list[tuple]:
    def generate_data(i) -> tuple:
        # Clean values
        name = random.choice(prepared_names)
        email = f'{name}@mail.ru'
        age = random.randint(18, 95)

        # Possible null values
        salary = random.randint(100, 350) * 1000 \
            if not (random.randint(1, 100) <= 5) else None
        registration_date = date.today() \
            if not (random.randint(1, 100) <= 5 and salary) \
            else None
        city = random.choice(prepared_cities) \
            if not (random.randint(1, 100) <= 5 and any([salary, registration_date])) \
            else None

        return i, name, email, city, age, salary, registration_date

    return [generate_data(i) for i in range(1, num + 1)]


def rename_part() -> str:
    path = 'data'
    to_file_renamed = os.path.join(path, f'{date.today()}-dev.csv')
    files = os.listdir(path)
    for file in files:
        to_file_path = os.path.join(path, file)
        if file.startswith('part'):
            os.rename(to_file_path, to_file_renamed)
        else:
            os.remove(to_file_path)
    return to_file_renamed


if '__main__' == __name__:
    parser = argparse.ArgumentParser(description="Script for generate synthetic data")
    parser.add_argument("--count", help="Number of generate rows",
                        nargs='?', type=int, default=1000)

    count = parser.parse_args().count

    spark = (
        SparkSession.builder
        .appName('synthetic_data')
        .master('local[*]')
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel('WARN')

    data_schema = StructType([
        StructField('id', IntegerType()),
        StructField('name', StringType()),
        StructField('email', StringType()),
        StructField('city', StringType(), True),
        StructField('age', IntegerType()),
        StructField('salary', IntegerType(), True),
        StructField('registration_date', DateType(), True)
    ])

    df_data = spark.createDataFrame(generate_list(count), schema=data_schema)
    cnt_data = df_data.count()
    """ Check empty values
    df_data.show()

    df_empty_values = (
      df_data.filter(df_data['salary'].isNull() | df_data['registration_date'].isNull() | df_data['city'].isNull())
    )
    print('Пример пустых строк:')
    df_empty_values.show(10)
    print(f'Общее количество пустых строк {df_empty_values.count()} из {df_data.count()} 
        записей ({df_data.count() / df_empty_values.count()})')
    """

    # Write df to CSV as one partition
    df_data.coalesce(1).write.mode('overwrite').format('csv').save('coalesced')
    filename = rename_part()
    print(f'{cnt_data} синтетических записей было записано в файл \'{filename}\'')

    spark.stop()
