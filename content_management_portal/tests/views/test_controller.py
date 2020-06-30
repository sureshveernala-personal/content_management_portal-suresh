def my_fun():
    return 2

def addition(first_number: int, second_number:  int):
    result = first_number + second_number
    return result

def test_mything(snapshot):
    return_value = my_fun()
    snapshot.assert_match(return_value, 'return_value')


def test_addition_when_both_positive(snapshot):
    first_number = 1
    second_number =2
    return_value = \
        addition(first_number=first_number, second_number=second_number)
    snapshot.assert_match(return_value, 'return_value')


def test_addition_when_both_negative(snapshot):
    first_number = -1
    second_number =-2
    return_value = \
        addition(first_number=first_number, second_number=second_number)
    snapshot.assert_match(return_value, 'return_value')


def test_addition_of_negative_and_positive(snapshot):
    first_number = 1
    second_number = -2
    return_value = \
        addition(first_number=first_number, second_number=second_number)
    snapshot.assert_match(return_value, 'return_value')
