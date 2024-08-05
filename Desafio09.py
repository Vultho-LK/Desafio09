# mostra a tabuada de um numero qualquer
n1 = int(input('digite um numero: '))
print('''a tabuada de {0}
1 X {0} = {0} | 2 X {0} = {1} | 3 X {0} = {2}

4 X {0} = {3} | 5 X {0} = {4} | 6 X {0} = {5} 

7 X {0} = {6} | 8 X {0} = {7} | 9 X {0} = {8}'''.format(n1, n1 * 2, n1 * 3, n1 * 4, n1 * 5, n1 * 6, n1 * 7, n1 * 8, n1 * 9, ))
