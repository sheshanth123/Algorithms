"""
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:
add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11

"""
class CallableInt(int):
    shouldAdd = True

    def __new__(self, val):
        return super(CallableInt, self).__new__(self, val)

    def __call__(self, val):
        if self.shouldAdd:
            result = CallableInt(self + val)
        else:
            result = CallableInt(self - val)
        result.shouldAdd = not result.shouldAdd
        return result

def add_subtract(val):
    return CallableInt(val)

print(add_subtract(3)(6)(6))
