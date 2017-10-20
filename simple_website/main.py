import json

dados = {
    'exemplo-num': 1000,
    'exemplo-string': 'sou uma string',
    'exemplo-lista': [
        'item-1',
        'item-2'
    ],
    'exemplo-lista-dict': [
        { # item-1
            'dado-1': '123',
            'dado-2': '456'
        },
        { # item-2
            'dado-1': '789',
            'dado-2': 'ABC'
        }
    ]
}

print dados

dados_json = json.dumps(dados)

print dados_json

f = open('simple_website/dados.js', 'w+')
f.write(u'DADOS = ' + dados_json)
f.close()