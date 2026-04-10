class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        # Initialize sum to 0
        total_sum = 0
        
        # Iterate from 1 to n (inclusive)
        for i in range(1, n + 1):
            # If n is divisible by i, it's a divisor
            if n % i == 0:
                total_sum += i
                
        return total_sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
