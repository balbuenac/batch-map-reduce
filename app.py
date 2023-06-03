from functools import reduce
from multiprocessing import Pool

# mapper function
def count_words(names):
    count_names = {}
    for name in names:
        if not name in count_names:
            count_names[name] = 0
        count_names[name] += 1
    #print(count_names)
    return count_names   

# reduce function
# dict1: es el resultado previo que se va acumulando
# dict2: es el nuevo diccionario
def calculate(dict1, dict2):
    combined = {}

    #print(dict1, dict2)

    for key in dict1:
        combined[key] = dict1[key]

    for key in dict2:
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined


if __name__ == "__main__":
    list_of_names = [["Maria", "Pedro", "Juan"], ["Pedro"], ["Maria"]]

    with Pool() as pool:
        results = pool.map(count_words, list_of_names) # MAP

    words = reduce(calculate, results)

    for key, val in words.items():
        print("El total para {} es {}".format(key, val))

# python3 -m pip install multiprocess
# sample source: https://chryswoods.com/parallel_python/mapreduce2_answer2.html