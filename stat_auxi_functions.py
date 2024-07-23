import random

# # Generating random data set with a given mean value
# def mean_dataset(mean, N=100, space:tuple=(0, 100), dp=2):
#     _range = range(space[0], space[1])
#     data_set = random.choices(_range, k=N)
#     if (x_target := round(mean*N, dp)) == (x_gained := round(sum(data_set), dp)):
#         return data_set
#     else:
#         loss = x_target - x_gained
#         cum = 0
#         while cum != loss:
#             i = (random.randint(0, int(loss-cum)))
#             i = 1 if i == 0 else i
#             # pos = data_set.index(random.choice(data_set))
#             num = data_set.pop(random.choice(range(len(data_set)))) + i
#             if num > space[1]:
#                 data_set.append(num-i)
#                 continue
#             data_set.append(num)
#             cum += i
#         return data_set

# def main(f, x=0):
#     return f(x)

def mean_dataset(mean, N=10, _range: tuple = (0, 100), _type = int, dp=2):
    # When N = 1
    if N == 1: return [mean]
    elif N < 1: return f"NullityError: Empty set cannot have a mean value of {mean}"

    # Creating the data space.
    space = range(*_range)
    
    # Generating the initial dataset.
    if _type == int:
        dataset = random.choices(space, k=N)
    else:
        dataset = list()
        for i in range(N):
            variate = random.random(10)*10**len(str(mean))
            dataset.append(round(variate, dp))

    # Validating mean
    diff = mean*N - sum(dataset)
    step = 1 if diff > 0 else -1

    # Adjusting dataset's mean to suit targeted mean
    while diff != 0:
        adder = random.choice(range(step, diff+step, step)) if diff > 1 or diff < -1 else step         # randomly choosing a value to be randomly added/subtracted to a variate in the dataset.
        num = dataset.pop(random.randint(0, N-1)) + adder     # removing a number from a random index and add the random value to increase/decrease our achieved sum.
        dataset.append(num)                                 # appending the adjusted value to the dataset.
        diff -= adder
    return dataset



if __name__ == "__main__":
    # print( main(mean_dataset, 50) )
    data = mean_dataset(0, N=10, _range=(-20, 100))
    print(data, "Avg =", sum(data)/10)
