import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


class Solution():
    def task1(self, df):
        """
        Использование основных методов pandas для первичного анализа (info/head/tail/describe/shape)
        :param df: анализируемый датасет
        :return: ничего
        """
        "Вывод краткого описания о датафрейме"
        print('\n=======info======\n')
        print(df.info())

        "head(n) - просмотр первых n строк таблицы"
        "tail(n) - просмотр последних n строк"
        print('\n=======head======\n')
        print(df.head())
        print('\n=======tail======\n')
        print(df.tail())

        "Сбор статистики по каждому числовому признаку с транспонированием"
        print('\n=======describe======\n')
        print(df.describe().T)

        "Вывод размерности датафрейма"
        print('\n=======shape======\n')
        print(df.shape)

    def __do_only_numeric_properties(self, df):
        """
        Уберем не численные методы
        :param df:датасет
        :return: исправленный датасет
        """
        "избавимся от нечисленных признаков"
        warnings.simplefilter('ignore')
        for i in range(len(df['Gender'])):
            if str(df['Gender'][i]) == 'Male':
                df['Gender'][i] = 0
            elif str(df['Gender'][i]) == 'Female':
                df['Gender'][i] = 1
            else:
                df['Gender'][i] = 2

        for i in range(len(df['Email_Opt_In'])):
            if str(df['Email_Opt_In'][i]) == 'True':
                df['Email_Opt_In'][i] = 1
            else:
                df['Email_Opt_In'][i] = 0

        for i in range(len(df['Target_Churn'])):
            if str(df['Target_Churn'][i]) == 'True':
                df['Target_Churn'][i] = 1
            else:
                df['Target_Churn'][i] = 0

        for i in range(len(df['Promotion_Response'])):
            if str(df['Promotion_Response'][i]) == 'Responded':
                df['Promotion_Response'][i] = 1
            elif str(df['Promotion_Response'][i]) == 'Unsubscribed':
                df['Promotion_Response'][i] = -1
            else:  # Ignored
                df['Promotion_Response'][i] = 0
        return df

    def task2(self, df):
        """
        Определение числа пропущенных значений и избавление от пропусков
        Пустые значения заполним средними значениями
        :param df: анализируемый датасет
        :return: заполненный датасет
        """

        df = self.__do_only_numeric_properties(df)
        "Выведим тепловую карту пропусков"
        sns.heatmap(df.isnull(), cmap=sns.color_palette(['#000099', '#ffff00']))
        plt.show()

        "Найдем число пропусков"
        null_count = df.isnull().sum()
        print(null_count)

        "заполним пропуски средними значениями"
        if null_count.sum() > 0:
            df = df.fillna(df.mean())
        return df

    def __detect_non_informative_features(self, df):
        """
        Определение неинформативных
        такими будем считать, если столбец имеет слишком много одинаковых значений (больше 95%)
        :param df: анализируемый датасет
        :return: массив неинофрмативных
        """
        print('\n=======detect_non_informative_features======\n')
        "подсчет одинаковых значений"
        num_rows = len(df.index)
        low_information_cols = []
        for col in df.columns:
            value_counts = df[col].value_counts(dropna=False)
            top_pct = (value_counts / num_rows).iloc[0]

            if top_pct > 0.95:
                low_information_cols.append(col)
                print(f'{col}: {top_pct * 100:.5f}%')
                print(f'{value_counts}\n')

    def task3(self, df, column_to_analyze, strict_mode=False):
        """
        Определение выбросов,дубликатов, неинформативных признаков
        :param df: датафрейм
        :param column_to_analyze: для какого столбца будет построен boxplot и hist
        :param strict_mode: False = искать выбросы для переданного столбца, иначе для всех
        :return: ничего
        """
        if strict_mode:
            for column in df.columns:
                plt.figure(figsize=(8, 6))
                sns.boxplot(x=df[column])
                plt.title(f'Ящик с усами для {column}')
                plt.show()

            # Построение гистограмм для каждого столбца
            for column in df.columns:
                plt.figure(figsize=(8, 6))
                sns.histplot(df[column], bins=20, kde=True)
                plt.title(f'Гистограмма для {column}')
                plt.show()
        else:
            print('\n=======boxplot======\n')
            sns.boxplot(df[f'{column_to_analyze}'])
            plt.title(f'Ящик с усами для {column_to_analyze}')
            plt.show()

            print('\n=======hist======\n')
            df[f'{column_to_analyze}'].hist(bins=20)
            plt.title(f'Гистограмма для {column_to_analyze}')

            plt.show()

        "Определение дубликатов"
        duplicates = df[df.duplicated()]
        print('\n=======duplicates======\n')
        print(f'{duplicates}')

        "Определение неинформативных признаков"
        self.__detect_non_informative_features(df)

    def task4(self, df):
        """
        Метод определяет и выводит целевой признак
        :param df: датасет
        :return: ничего
        """
        print('\n=======main properties======\n')
        "харкод"
        print(df['Target_Churn'].value_counts(normalize=True))


def main():
    sns.set()
    "Загрузка данных"
    df = pd.read_csv('./online_retail_customer_churn.csv', sep=',')
    solution = Solution()
    solution.task1(df)
    df = solution.task2(df)
    solution.task3(df, '', strict_mode=True)
    solution.task4(df)


if __name__ == '__main__':
    main()
