'''
Transformando essa função em lambda:

T = 250

if (T > 200):
    rate = 'more than 200'
else:
    rate = 'less than 200'

return (rate)

'''

rate = lambda T: 'more than 200' if T>200 else 'less than 200'

T = 50
print(rate(T))