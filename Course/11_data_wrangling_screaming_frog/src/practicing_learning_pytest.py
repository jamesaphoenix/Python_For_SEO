import pytest




# 1. Simpler Fixture:
def some_amazing_function(name):
    return name

@pytest.fixture
def male_name():
    return 'James'

@pytest.fixture
def female_name():
    return 'Alice'

def test_male_prefix_success(male_name):
    assert 'James' == some_amazing_function(male_name)

def test_female_prefix_success(female_name):
    assert 'Alice' == some_amazing_function(female_name)

def test_male_prefix_fail(male_name):
    assert 'fail' == some_amazing_function(male_name)

def test_female_prefix_fail(female_name):
    assert 'fail' == some_amazing_function(female_name)

#####

# 2. For Loops With Fixtures:
'''This is still not enough for some scenarios. Let’s suppose you want to test your
code against a set of different names and actions: a solution could be iterating over elements of a “list” fixture.'''

@pytest.fixture
def male_names():
    return ['James', 'James', 'James']

def test_all_male_names_success(male_names):
    for name in male_names:
        assert 'James' == some_amazing_function(name)

def test_all_male_names_fail(male_names):
    for name in male_names:
        assert 'Fail' == some_amazing_function(name)


######

# 3. Parameterised Tests:

'''pytest.mark.parametrize to the rescue!
The above decorator is a very powerful functionality, it permits to call a test function multiple times, changing the parameters input at each iteration.
The first argument lists the decorated function’s arguments, with a comma separated string. The second argument is an iterable for call values.
Let’s see how it works.'''

# These will all fail:
@pytest.mark.parametrize('name', ['James', 'Gloria', 'Haley'])
def test_female_prefix_v2_fail(name):
    assert 'Mrs.' == some_amazing_function(name)

# These will all succeed:
@pytest.mark.parametrize('name', ['James', 'James', 'James'])
def test_male_success_all(name):
    assert 'James' == some_amazing_function(name)


# 3.1 Paratermised Tests With Expected Results:
@pytest.mark.parametrize(
    'name, expected', [('Claire', 'Lol'), ('James', 'James')]
)
def test_expected_all(name, expected):
    assert expected == some_amazing_function(name)

########

'''Another thing the parametrize is good for is making permutations.
In fact, using more than one decorator, instead of a single one with multiple arguments, you will obtain every permutation possible.'''

def is_odd(number):
    return number % 2 != 0

@pytest.mark.parametrize('odd', range(1, 11, 2))
@pytest.mark.parametrize('even', range(0, 10, 2))
def test_sum_odd_even_returns_odd(odd, even):
    assert is_odd(odd + even)



# 4. Object Orientated Fixture:
@pytest.fixture
def data():
    class Test():
        def __init__(self):
            self.awesome = 5
    return Test

def test_learning(data):
    sweet = data()
    assert sweet.awesome == 10
