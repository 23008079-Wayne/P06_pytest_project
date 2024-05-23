import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        #arrange
        a=100
        b=50
        cal=Calculator()

        
        #act 
        result= cal.subtract(a,b)
        
        # assert
        expected = 50
        assert result == expected
    
    def test_multiply(self):
        #arrange
        a=55
        b=2
        cal=Calculator()
        
        #act 
        result= cal.multiply(a,b)
        # assert
        expected = 110
        assert result == expected

    def test_divide(self):
        #arrange
        a=50
        b=5
        cal=Calculator()
    
        #act 
        result= cal.divide(a,b)
        # assert
        expected = 10
        assert result == expected
        
    def test_divide_zero (self):
        #arrange
        a=4321
        b=0
        cal=Calculator()
        
        #Act and Assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
            
#need to start from pytest again 
#Then pip install coverage
#coverage run --branch -m pytest
#coverage report -m 
#coverage html 