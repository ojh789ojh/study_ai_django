class User:
    def __init__(self, auth):
        self.is_authenticated = auth


def decorators(func):
    def decorate(num1, num2, user):
        num1, num2 = int(num1), int(num2)
        if num1 > 0 and num2 > 0:
            func(num1, num2, user)
        else:
            raise ValueError('음수가 입력되었습니다')
    return decorate


@decorators
def tri(num1, num2, user):
    if user.is_authenticated:
        print(num1*num2/2)
    else:
        raise ValueError('No authenticated')


@decorators
def rec(num1, num2, user):
    if user.is_authenticated:
        print(num1*num2)
    else:
        raise ValueError('No authenticated')


# user1 = User(True)
# tri(5, 5, user1)
# user2 = User(False)
# rec(5, 5, user2)



