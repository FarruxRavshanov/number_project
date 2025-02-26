import math

class Number:
    def __init__(self,num):
        self.number = num

    def data_type(self):
        '''
        this method returns the type of the number.
        '''
    print(type(self.number))


    def len(self) -> int:
        '''
        this method returns the length of the number. 

        Args:
            No
        Returns: 
            int: the length of the number.
        '''
        pass

    def is_positive(self) -> bool:
        '''
        this mehtod returns true if number is positive otherwise false.

        Args:
            No
        Returns:
            bool: true if number is positive otherwise false.
        '''
        s = str(self.number)
        return s[0].isdigit()

    def is_negative(self) -> bool:
        '''
        this mehtod returns true if number is negative otherwise false.

        Args:
            No
        Returns:
            bool: true if number is negative otherwise false.
        '''
        s = str(self.number)
        return s[0] == '-'
    def is_zero(self) -> bool:
        '''
        this mehtod returns true if number is zero otherwise false.

        Args:
            No
        Returns:
            bool: true if number is zero otherwise false.
        '''
        return self.number == 0:

    def is_even(self) -> bool:
        '''
        this mehtod returns true if number is even number otherwise false.

        Args:
            No
        Returns:
            bool: true if number is even number otherwise false.
        '''
        return self.number // 2 == 0

    def is_odd(self) -> bool:
        '''
        this mehtod returns true if number is odd number otherwise false.

        Args:
            No
        Returns:
            bool: true if number is odd number otherwise false.
        '''
        return self.number // 2 == 1
 

    def is_prime(self) -> bool:
        '''
        this mehtod returns true if number is prime otherwise false.

        Args:
            No
        Returns:
            bool: true if number is prime otherwise false.
        ''' 
        pass 
    
    def int_to_str(self) -> str:
        '''
        this method converts to string.
        
        Args:
            No
        Returns:
            str: convert to string
        '''
        return str(self.number)
