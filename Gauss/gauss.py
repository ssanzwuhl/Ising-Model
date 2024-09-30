from sympy import *
init_printing()
nvar = 1
Delta = '\u0394'
class Variables_init:
    def __init__(self):

        self.errores = []
        self.variables = []
        self.parametros = [] 

    def get_variables(self):

        variables = self.variables
        var = input('Variable {}: '.format(nvar))
        
        while var != '' :
            #dvar = float(input('Error de la variable {}: '.format(var)))
            j = symbols(var)
            exec('%s = j' % var)
            variables.append(var)
            #errores.append(dvar)
            var = input('Variable {}: '.format(nvar))

        return variables

    def nvar(self):
        variables = self.variables
        return len(variables)

    def define_g():
        g = symbols('g', cls = Function)
        while True:
            try:
                g = eval(input('\nIntroduce relación entre dichas variables: '))
                break
            except:
                print('Parece que te has equivocado')
                pass
        return g

    def define_dg2():
        dg2 = symbols('dg2', cls = Function)   
    

dgsquared = symbols('dg2')
dgsquared = 0

for i in range(nvar):
    dgsquared += (diff(g, variables[i])*errores[i])**2

pprint(sqrt(dgsquared))
valor_variables = ()


g = lambdify(variables, g)

for i in range(nvar):
    valor_variables += (float(input('Valor de la variable {}: '.format(variables[i]))), )
dg = lambdify(variables, dgsquared)

print('Tu magnitud es:', g(*valor_variables), '\nEl error de tu magnitud es:', sqrt(dg(*valor_variables)))
