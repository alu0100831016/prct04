#! /usr/bin/python
#! encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
  x = -b/a
  print 'Solucion: ', x
if (a == 0) and (b != 0):
  print 'La ecuación no tiene solucion.'
if (a == 0) and (b == 0):
  print 'Tiene soluciones infinitas.'
