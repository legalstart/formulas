# formula sample -> we cannot have A <- f(..,A,..)
# we will test this condition in unittests
# the third formula doesn't respect this condition
formula1 = ('B',(lambda a: ['b1', 'b2'][a], 'A'))
formula2 = ('X', (lambda x, y: x + y, ('x', 'y')))
formula3 = ('X', (lambda x, y: x + y, ('X', 'y')))
formula4 = ('X', (lambda x, y: x + y, ()))
