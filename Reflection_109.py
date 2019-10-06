
#%%
#Exercise 7-4
def fact(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Argument given is less than 0")
    else:
        return n * fact(n-1)

fact(-1)


#%%
