cube = lambda x: x**3 

def fibonacci(n):
    if n in [0,1]:
        return [] if n == 0 else [0]
    else:
        series = [0,1]
        list(map(lambda _: series.append(sum(series[-2:])), range(2,n)))
        return series

if __name__ == '__main__':
    try:
        n = int(input())
    except Exception as e:
        print("please enter integer value.")
        exit()
    print(list(map(cube, fibonacci(n))))
