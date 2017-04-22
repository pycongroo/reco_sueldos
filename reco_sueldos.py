from bs4 import BeautifulSoup as Bs
import requests
from sys import argv

def get_sueldos(html):
    c_html = Bs(html, 'lxml')
    divs = c_html.findAll('div',{'class':'sueldo'})
    return map(lambda div: div.find('a').get('href').split('sueldo/')[-1].split('pesos')[0], divs)

def get_totales(max_res, min_sueldo, path_res):
    arch = open(path_res, 'w')
    print "Scrapeo pag 1"
    cgr = requests.get("http://www.cuantogano.com/sueldos/it-programacion.html")
    sueldos = get_sueldos(cgr.text)
    pag = 1
    totales = []
    for sueldo in sueldos:
        if (eval(sueldo)>min_sueldo):
            totales.append(sueldo)
    while (len(totales) < max_res):
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

if (len(argv) == 1):
    print "Debe ingresar parametros:\n"
    print "python reco_sueldos.py <cantidad_resultados> [<sueldo_minimo>] [<ruta_resultado>]"
s_min = 2000
res_path = "sueldos.txt"
if (len(argv)>2):
    s_min = eval(argv[2])
    if (len(argv)>3):
        res_path = argv[3]

get_totales(eval(argv[1]), s_min, res_path)
