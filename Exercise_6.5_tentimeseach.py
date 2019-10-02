
#%%
def ten_times_each(sequence):
    result = []
    t = 1
    while t <= 10:
        for element in sequence:
            result = result + [element * 2]
        t = t + 1
    return result

ten_times_each(['hi'])
#%%
