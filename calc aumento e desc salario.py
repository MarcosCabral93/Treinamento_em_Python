s=float(input('digite o salario do funcionário'))
ad=float(input('digite o valor do acréscimo ou desconto do salario em %'))
z=ad/100
ns=s*z
print(' o salario com aumento é {:.2f}'.format(ns+s))
