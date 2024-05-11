



#Calculator
def sizer(num:any) -> int:
    
    """This function will give you all shapes you need to reshape your matriz in numpy
    Args:
        num(int): any number
    Returns:
        list: a list with tuples that they will represent the real combinations you can use to reshape your object
    """
    #object that will be returned as the real combinations.
    numbers_valid = []
    if num is None or num == 0:
        return False
    
    for i in range(1,num + 1):
        if num % i == 0:
            a = num // i
            if a * i == num:
                numbers_valid.append((i,a))
    return numbers_valid



#Start the program
def run():
    num_dim = int(input("Tamaño de la matriz: "))
    dimensions = sizer(num_dim)
    if dimensions == False:
        print("No puedo realizar esta operacion")
    print(f'Posibles combinaciones de tamaño para la matriz de {num_dim}: ')
    for dim in dimensions:
        print(dim)


if __name__ == "__main__":
    run()
    