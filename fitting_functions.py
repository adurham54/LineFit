def linear(m , x, b):
    return m*x+b

def slope_units(x_units, y_units):
    return x_units.rstrip('s') + '/' + y_units.rstrip('s')

def print_equation(m, b, x_units, y_units):
    print("The equation of the line is: y=", m, slope_units(x_units, y_units),"+", b, y_units)
