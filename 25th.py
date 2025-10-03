def fibonacci_seq():
    fibonacci = [0, 1]

    thousand_digits = 10**999

    while True:
        tempn = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(tempn)

        if fibonacci[-1] > thousand_digits:
            print("The index of the first thousand-digit Fibonacci number: ", len(fibonacci) - 1, "\nThe first thousand-digit Fibonacci number: ", fibonacci[-1])
            break


fibonacci_seq()