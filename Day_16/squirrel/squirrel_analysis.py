import pandas

data = pandas.read_csv("squirrel_data.csv")

fur_counts = data['Primary Fur Color'].value_counts(dropna=True)
print(fur_counts)
fur_counts.to_csv("fur_counts.csv")