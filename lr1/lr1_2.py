import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


def groupby(df):
    # Target_Churn - целевая переменная
    df.groupby('Target_Churn')['Total_Spend'].mean().plot(kind='bar')
    plt.ylabel('Total_Spend')
    plt.show()


def countplot(df):
    # Интересующие нас признаки
    df['Years_as_Customer'] = df['Years_as_Customer'].astype('int64')
    plt.figure(figsize=(30, 10))
    sns.countplot(x='Years_as_Customer', hue='Target_Churn', data=df)
    plt.show()


def scatter(df):
    ax1 = df.plot.scatter(x='Years_as_Customer',
                          y='Total_Spend',
                          c='DarkBlue')
    plt.show()

def joinplot(df):
    sns.jointplot(data=df, x="Years_as_Customer", y="Total_Spend")
    plt.show()

def pairplot(df,numeric):
    # Анализ корреляции числовых признаков
    sns.pairplot(df[numeric])
    plt.show()

def heatmap(df,numeric):
    sns.heatmap(df[numeric].corr())
    plt.show()


def crosstab(df):
    # Категориальный + категориальный
    print(pd.crosstab(df['Target_Churn'], df['Promotion_Response']))
    sns.heatmap(pd.crosstab(df['Target_Churn'], df['Promotion_Response']))
    plt.show()




sns.set()
warnings.simplefilter('ignore')
# Загрузка данных
df = pd.read_csv('./online_retail_customer_churn.csv', sep=',')
numeric = ['Customer_ID', 'Age', 'Annual_Income',
           'Total_Spend', 'Years_as_Customer', 'Num_of_Purchases',
           'Average_Transaction_Amount', 'Num_of_Returns',
           'Num_of_Support_Contacts', 'Satisfaction_Score', 'Last_Purchase_Days_Ago']

# Очистка NULL-данных
df = df.dropna()
groupby(df)
countplot(df)
scatter(df)
joinplot(df)
pairplot(df,numeric)
heatmap(df,numeric)
crosstab(df)

""" С использованием groupby
• С использованием countplot
• Диаграмма рассеяния (scatter)
• Совместное распределение(joinplot)
• Построение pairplot
• Построение heatmap
• Построить таблицу сопряженности crosstab
• Построить countplot и т.д.
• Определить и удалить нерелевантные (очевидно) признаки"""
