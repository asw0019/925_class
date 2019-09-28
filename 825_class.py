#%%
x = 5
#%%
def add1(x):
    x = x + 1
    return x

x = add1(x)
print(x)

#%%
sum = 0
secondSum = 0
for x in range(100):
    sum = sum + x
print(sum)

#%%
def exponent(x,y):
    z=x
    for n in range(1,y):
        z = z * x
    return z
exponent(8,4)
#%%
