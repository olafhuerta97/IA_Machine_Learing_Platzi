from bokeh.plotting import figure, output_file, show

#como ejecutar:
#entrar a la carpeta y activar el enviroment
#en windows: source env/Scripts/activate
# en mac : source env/bin/activate
# deactivate para salir

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
