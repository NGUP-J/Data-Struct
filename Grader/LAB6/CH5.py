def asteroid_collision(asts):
    
    if len(asts) == 1:
        return asts

    result = asteroid_collision(asts[1:])  

    if len(result) > 0 and asts[0] > 0 and result[0] < 0:

        if asts[0] == abs(result[0]):
            if len(result) > 1:
                return result[1:]
            else:
                return []
        elif asts[0] < abs(result[0]):
            return result
        elif asts[0] > abs(result[0]):
            return asteroid_collision([asts[0]] + result[1:])

    else:
        return [asts[0]] + result

if __name__ == '__main__':

    x = input("Enter Input : ").split(",")
    x = list(map(int,x))
    print(asteroid_collision(x))