if __name__ == '__main__':
    n = int(input("Digite um número: ").strip())
    
    is_odd = n % 2 == 1
    
    if is_odd :
        print("Weird")
    else:
        if n in range(2,6):
            print("Not Weird")
        if n in range(6,21):
            print("Weird")
        if n > 20:
            print("Not Weird")