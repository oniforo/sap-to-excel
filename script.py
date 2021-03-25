import pandas

with open('text.txt', 'r') as f:
    text = f.readlines()

find_string = '\x00\t\x00V\x00a\x00l\x00.\x00o\x00b\x00j\x00e\x00t\x00o'
indices = [i for i, x in enumerate(text) if x.startswith(find_string)]
indices.append(len(text))

dataset_compilation = []

for i in range(len(indices)-1):

    dataset = text[indices[i]:indices[i+1]]
    dataset = [row for row in dataset if row != '\x00\n']

    data = [row.split('\t') for row in dataset]
    
    try:
        df = pandas.DataFrame(data[1:], columns=data[0])
        dataset_compilation.append(df)
    except:
        print(f"Something went wrong.")

for index, dataframe in enumerate(dataset_compilation):
    if '\x00' in dataframe:
        dataset_compilation[index] = dataset_compilation[index].drop(columns=['\x00'])

complete_dataframe = pandas.concat(dataset_compilation)

compression = dict(method='zip', archive_name='data.csv')
complete_dataframe.to_csv(
    'output.zip', index=False, encoding='utf-8-sig', compression=compression
)
