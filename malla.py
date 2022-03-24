import graphviz  

def graph(lista, titulo):
 
    h = graphviz.Graph(titulo)  
    table = '<<TABLE  border="10" cellspacing="1" cellpadding="40" style="rounded">'
    for fila in lista:
        table += '<TR>'
        for columna in fila:
            if columna == 'B':
                table += '<TD  border="3"  height="40" bgcolor="black"></TD>'
            if columna == 'W':
                table += '<TD  border="3"  height="40" bgcolor="white"></TD>'
        table += '</TR>'

    table += '</TABLE>>'    

    h.node( 'tab', shape='rect', label = table, fontsize="80")
    h.format = 'png'

    h.render(directory='grafica-patrones', view=True).replace('\\', '/')
    'grafica-patrones/'+titulo +'.gv.png'
