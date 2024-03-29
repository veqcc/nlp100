import MeCab
fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'


def parse_neko():
    with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neco_lines():
    with open(fname_parsed) as file_parsed:
        morphemes = []
        for line in file_parsed:
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration
            res_cols = cols[1].split(',')

            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []


parse_neko()

list_a_no_b = []
lines = neco_lines()
for line in lines:
    print(line)
    if len(line) > 2:
        for i in range(1, len(line) - 1):
            if line[i]['surface'] == 'の' \
                    and line[i - 1]['pos'] == '名詞' \
                    and line[i + 1]['pos'] == '名詞':
                list_a_no_b.append(line[i - 1]['surface'] + 'の' + line[i + 1]['surface'])

a_no_b = set(list_a_no_b)
print(sorted(a_no_b, key=list_a_no_b.index))
