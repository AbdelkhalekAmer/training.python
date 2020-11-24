import math

print("================================================================================\n")

print("====================Start Bisection Search Algorithm Program====================\n")

number = int(input("search for: "))

def get_medium_range(min_range,max_range):
    return math.ceil((max_range - min_range)/2)

def search_using_bisection_algorithm(_number, _from = 0, _to = 10):
    
    iterations = 0
    
    medium = get_medium_range(_from,_to)

    while _number != medium:
    
        iterations += 1

        if _number < medium:
            _to = medium

        if _number > medium:
            _from = medium
    
        medium = get_medium_range(_from,_to)
    
    return iterations

def search(_number, _from = 0, _to = 10):
    
    bisection_iterations = search_using_bisection_algorithm(_number,_from,_to)
    
    return [bisection_iterations]

results = search(number,0,1000)

print(f"I found number {number} after {results} iteration(s).\n")

print("================================================================================\n")
