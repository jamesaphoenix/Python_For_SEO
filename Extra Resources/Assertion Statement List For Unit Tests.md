# The Complete List Of Python Assert Statements


```python
from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable
```

Knowing how to write assert statements in Python allows you to easily write mini-tests for your code. 

Additionally testing frameworks such as [PyTest](https://docs.pytest.org/en/latest/) can work directly with assert statements to form fully functioning UnitTests.

---

You can also find a list of all of the different standard [UnitTest Module examples here](#UnitTest).

Firstly let's review all of the different types of assert statements that we can make for [PyTest](https://docs.pytest.org/en/latest/).

------------------------------------------------------------

## PyTest Python Assert Statements List

### 1. Equal to or not equal to [value]


```python
assert 5 == 5 # Success Example
```


```python
assert 5 == 3 # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-106-db6ee5a4bb16> in <module>
    ----> 1 assert 5 == 3 # Fail Example
    

    AssertionError: 



```python
assert 5 != 3 # Success Example
```


```python
assert 5 != 5 # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-108-de24f583bfdf> in <module>
    ----> 1 assert 5 != 5 # Fail Example
    

    AssertionError: 


----------------------------------------------------------------

### 2. type() is [value]


```python
assert type(5) is int # Success Example
```


```python
assert type(5) is not int # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-110-e4cc0467bcd9> in <module>
    ----> 1 assert type(5) is not int # Fail Example
    

    AssertionError: 


-------------------------------------------------------

### 3. isinstance


```python
assert isinstance('5', str) # Success Example
```


```python
assert isinstance('5', int) # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-112-28175282ec92> in <module>
    ----> 1 assert isinstance('5', int) # Fail Example
    

    AssertionError: 



```python
assert not isinstance('5', int) # Success Example
```


```python
assert not isinstance('5', str) # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-116-1c215fe3a6a5> in <module>
    ----> 1 assert not isinstance('5', str) # Fail Example
    

    AssertionError: 


-----------------------------------------------------------------------------

### 4. Boolean is [Boolean Type]


```python
true = 5==5
assert true is True # Success Example
```


```python
assert true is False # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-118-45032f0eff77> in <module>
    ----> 1 assert true is False # Fail Example
    

    AssertionError: 


-----------------------------------------------------------------------------

### 5. in and not in [iterable]


```python
list_one = [1,3,5,6]
```


```python
assert 5 in list_one # Success Example
```


```python
assert 5 not in list_one # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-121-90e8a0f2ef02> in <module>
    ----> 1 assert 5 not in list_one # Fail Example
    

    AssertionError: 


------------------------------------------------

### 6. Greater than or less than [value]


```python
assert 5 > 4 # Success Example
```


```python
assert 5 > 7 # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-123-3068a8105e75> in <module>
    ----> 1 assert 5 > 7 # Fail Example
    

    AssertionError: 



```python
assert 2 < 4 # Success Example
```


```python
assert 4 < 2 # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-125-089b0fa99ac6> in <module>
    ----> 1 assert 4 < 2 # Fail Example
    

    AssertionError: 


------------------------------------------------------------------------------------

### 7. Modulus % is equal to [value]


```python
assert 2 % 2 == 0 # Success Example
```


```python
assert 2 % 2 == 1 # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-127-2c429e622b13> in <module>
    ----> 1 assert 2 % 2 == 1 # Fail Example
    

    AssertionError: 


--------------------------------------------------------

### 8. any() assert statements


```python
example = [5,3,1,6,6]
booleans = [False, False,True, False]
```


```python
any(example)
```




    True




```python
any(booleans)
```




    True



Notice that the example list python list is True because at least one of the numbers is not a 0, all numbers above 0 are 'Truthy'.


```python
assert any(example) == True # Success Example
assert any(example) == True # Success Example
```

-----------------------------------------------------------------------------

### 9. all() assert statements


```python
all(example)
```




    True




```python
all(booleans)
```




    False




```python
assert all(example) # Success Example
```


```python
assert all(booleans) # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-135-c422689f500e> in <module>
    ----> 1 assert all(booleans) # Fail Example
    

    AssertionError: 


----------------------------------------------------------------------------------------

### 10. Custom Python Objects

It's possible to identify if a class is a specific type of object. We can do this by using

~~~

type(obj).__name__

~~~


```python
df = pd.DataFrame()
```


```python
type(df).__name__
```




    'DataFrame'




```python
type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ is 'DataFrame' # True Boolean
```




    True




```python
type(df).__name__ == type([]).__name__ # False Boolean
type(df).__name__ is type([]).__name__ # False Boolean
```




    False




```python
assert(type(df).__name__ == 'DataFrame') # Success Example
```


```python
assert(type(df).__name__ == type([]).__name__) # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-147-2332f54f50a3> in <module>
    ----> 1 assert(type(df).__name__ == type([]).__name__) # Fail Example
    

    AssertionError: 


--------------------------------------------------------------------------------

### 11. Iterables

It's also possible to determine whether a variable is an iterable with:

~~~

from collections.abc import Iterable

~~~


```python
iterable_item = [3,6,4,2,1]
```


```python
isinstance(iterable_item, Iterable)
```




    True




```python
isinstance(5, Iterable)
```




    False




```python
assert isinstance(iterable_item, Iterable) # Success Example
```


```python
assert isinstance(3, Iterable) # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-153-e96805891245> in <module>
    ----> 1 assert isinstance(3, Iterable) # Fail Example
    

    AssertionError: 


--------------------------------------------------

## Combining Multiple And / Or Statements With Assert Statements:

It's also possible to combine multiple conditions with either <strong> OR or AND </strong> and to test the chained commands with the assert statement:


```python
true_statement = 5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2
```


```python
print(true_statement, false_statement)
```

    True False



```python
assert true_statement # Success Example
```


```python
assert false_statement # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-157-452ef20f327f> in <module>
    ----> 1 assert false_statement # Fail Example
    

    AssertionError: 


--------------------------------------------------------


```python
true_or_statement = 5 == 5 or 3 == 3
false_or_statement = 7 == 3 or 10 == 1
```


```python
print(true_or_statement, false_or_statement)
```

    True False



```python
assert true_or_statement # Success Example
```


```python
assert false_or_statement # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-161-38343a099bdc> in <module>
    ----> 1 assert false_or_statement # Fail Example
    

    AssertionError: 


------------------------------------------------------------------------------------

## Testing Multiple Commands

Also we can test more than one thing at a time by having multiple assert statements inside of the same Python method:


```python
class Test(object):
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name
        
    def test_all_class_arguments(self):
        print('Testing both of the class variables to see whether they are both strings!')
        
        for _ in [self.first_name, self.last_name]:
            assert(type(_) is str)
        print('------')
        print('Passed all of the tests')
```


```python
yay = Test('James' , 'Phoenix') # Success Example
yay.test_all_class_arguments()
```

    Testing both of the class variables to see whether they are both strings!
    ------
    Passed all of the tests



```python
yay = Test(5 , 'Phoenix') # Fail Example
yay.test_all_class_arguments()
```

    Testing both of the class variables to see whether they are both strings!



    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-164-64cb2bee07e3> in <module>
          1 yay = Test(5 , 'Phoenix') # Fail Example
    ----> 2 yay.test_all_class_arguments()
    

    <ipython-input-162-3ae9548ef4b7> in test_all_class_arguments(self)
          8 
          9         for _ in [self.first_name, self.last_name]:
    ---> 10             assert(type(_) is str)
         11         print('------')
         12         print('Passed all of the tests')


    AssertionError: 


-----------------------------------------------------------------

<a id='UnitTest'> </a>

## Python 3.x UnitTest Assert Methods

Below you'll find a list of all of the UnitTest Assert Methods:

| Method | Checks | Version | 
|---|---|---|
|[assertEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)|a == b| 3.x |
|[assertNotEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)|a != b| |
|[assertTrue](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)|bool(x) is True| |
|[assertFalse](https://docs.python.org/3/library/unittest.html#unittest.TestCase.ssertFalse)|bool(x) is False| |
|[assertIs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)|a is b|3.x |
|[assertIsNot](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)|a is not b|3.x |
|[assertIsNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)|x is None|3.x |
|[assertIsNotNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)|x is not None|3.x |
|[assertIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)|a in b|3.x |
|[assertNotIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)|a not in b|3.x |
|[assertIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)|is instance(a,b)|3.x |
|[assertNotIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance)|not is instance(a,b)|3.x |
|[assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)|fun(*args,**kwds) raises exc| 3.x |
|[assertRaisesRegexp](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegexp)|fun(*args,**kwds) raises exc(regex)|3.x |
|[assertAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual)|round(a-b,7) == 0| 3.x |
|[assertNotAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual)|round(a-b,7) != 0| 3.x |
|[assertGreater](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater)|a > b|3.x |
|[assertGreaterEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual)|a >= b|3.x |
|[assertLess](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess)|a < b|3.x |
|[assertLessEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual])|a <= b|3.x
|[assertRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegexpMatches)|r.search(s)|3.x
|[assertNotRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegexpMatches)|not r.search(s)|3.x
|[assertItemsEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertItemsEqual)|sorted(a) == sorted(b)|3.x
|[assertDictContainsSubset](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictContainsSubset)|all the key/value pairs in a exist in b|3.x
|[assertMultiLineEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual)|strings|3.x
|[assertSequenceEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual)|sequences|3.x
|[assertListEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual)|lists|3.x
|[assertTupleEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual)|tuples|3.x |
|[assertSetEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual)|sets or frozensets|3.x |
|[assertDictEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual)|dicts|3.x |

----------------------------------------------------------------------

## Typing Assert Statements

As well as using simple assert statements, by importing the [types module of python](https://docs.python.org/3/library/types.html) we can make more abstract assert statements on specific Types:


```python
class Example():
    def __init__(self, id_, name):
        self._id = id_
        self.name = name
    
    def subtract(self):
        answer = 5 + 5
        return answer
        
    def test_lambda_function(self):
        assert(lambda x: x is LambdaType)
        
    def test_subtract_function(self):
        assert(self.subtract is LambdaType)
```


```python
example_class = Example("123", 'James Phoenix')
```


```python
print(example_class._id, example_class.name)
```

    123 James Phoenix


------------------------------


```python
example_class.test_lambda_function() # Sucesss Example
```


```python
example_class.test_subtract_function() # Fail Example
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-169-e96c76763824> in <module>
    ----> 1 example_class.test_subtract_function() # Successs
    

    <ipython-input-165-28a62a6c7adf> in test_subtract_function(self)
         12 
         13     def test_subtract_function(self):
    ---> 14         assert(self.subtract is LambdaType)
    

    AssertionError: 


Above we've tested two class instance methods to see if <strong> either of them is a lambda: x style function! </strong>

You can find all of the [different types here.](https://docs.python.org/3/library/types.html)

----------------------------------------------------------------------------------------------------

Hopefully this provides you with an extensive list of assert statements and methods for your Unit Tests.
