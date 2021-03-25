import pandas

with open('text.txt', 'r') as f:
    text = f.readlines()

text = [x.replace('\x00', '') for x in text]

find_string = '\tVal.objeto'
indices = [i for i, x in enumerate(text) if x.startswith(find_string)]
indices.append(len(text))

dataset_compilation = []

for i in range(len(indices)-1):

    dataset = text[indices[i]:indices[i+1]]
    dataset = [row for row in dataset if row != '\n']

    data = [row.split('\t') for row in dataset]
    
    try:
        df = pandas.DataFrame(data[1:], columns=data[0])
        dataset_compilation.append(df)
    except:
        print("Something went wrong.")

for index, dataframe in enumerate(dataset_compilation):
    if '' in dataframe:
        dataset_compilation[index] = dataset_compilation[index].drop(columns=[''])

complete_dataframe = pandas.concat(dataset_compilation)

compression = dict(method='zip', archive_name='data.csv')
complete_dataframe.to_csv(
    'output.zip', index=False, encoding='utf-8-sig', compression=compression
)
