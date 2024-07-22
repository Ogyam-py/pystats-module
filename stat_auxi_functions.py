import random

# Generating random data set with a given mean value
def mean_dataset(mean, N=100, _range:tuple=(0, 100), dp=2):
    _range = range(_range[0], _range[1])
    data_set = random.choices(_range, k=N)
    if (x_target := round(mean*N, dp)) == (x_gained := round(sum(data_set), dp)):
        return data_set
    else:
        loss = x_target - x_gained
        cum = 0
        while cum <= loss:
            i = (random.randint(0, int(loss-cum)))
            i = 1 if i == 0 else i
            # pos = data_set.index(random.choice(data_set))
            num = data_set.pop(random.choice(range(len(data_set)))) + i
            if num > _range[1]:
                data_set.append(num-i)
                continue
            data_set.append(num)
            cum += i
        return data_set

# def main(f, x=0):
#     return f(x)

if __name__ == "__main__":
    # print( main(mean_dataset, 50) )
    data = mean_dataset(50, N=10)
    print(data)
