#%%
def half(sequence):
    result = []
    for element in sequence:
        result = result + [element * element]
    return result

half([1.0,2.0,3.0])

#%%
