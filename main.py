from pprint import pprint


def beolvas():
    lista = []
    with open('sneakers.csv', 'r', encoding='utf-8') as forrasfajl:
        forrasfajl.readline()
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            datum = adatok[4].split('T')
            sneaker = {'title': adatok[0],
                       'color': adatok[1],
                       'full_price': float(adatok[2]),
                       'current_price': float(adatok[3]),
                       'publish_date': datum[0]}
            lista.append(sneaker)
    return lista


def rendez(lista, szam):
    kulcsok = ['title', 'color', 'full_price', 'current_price', 'publish_date']
    kulcs = kulcsok[(szam - 1)]
    rendezett_lista = sorted(lista, key=lambda elem: elem[kulcs])
    return rendezett_lista


def main():
    lista = beolvas()
    print('Válassz, melyik szempont alapján rendezzem a cipőket!\n'
          '1 - title\n'
          '2 - color\n'
          '3 - full price\n'
          '4 - current price\n'
          '5 - publish date')
    rendezett_lista = rendez(lista, (int(input('Add meg a lehetőség számát! '))))
    pprint(rendezett_lista)


main()
