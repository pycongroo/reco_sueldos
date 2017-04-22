import requests
from bs4 import BeautifulSoup as Bs



def get_sueldos(html):
    c_html = Bs(html, 'lxml')
    divs = c_html.findAll('div',{'class':'sueldo'})
    return map(lambda div: div.find('a').get('href').split('sueldo/')[-1].split('pesos')[0], divs)

def get_totales(cant):
    arch = open('sueldos.txt', 'w')
    print "Scrapeo pag 1"
    cgr = requests.get("http://www.cuantogano.com/sueldos/it-programacion.html")
    sueldos = get_sueldos(cgr.text)
    pag = 1
    totales = []
    for sueldo in sueldos:
        if (eval(sueldo)>1000):
            totales.append(sueldo)
    while (len(totales) < cant):
        pag += 1
        print "Scrapeo pag %i" % pag
        cgr = requests.get("http://www.cuantogano.com/sueldos/it-programacion.html/pagina%i"%pag)
        sueldos = get_sueldos(cgr.text)
        for sueldo in sueldos:
            totales.append(sueldo)
    for sueldo in totales:
        arch.write(sueldo)
        arch.write('\n')
    print "FINALIZO"
