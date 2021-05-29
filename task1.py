from random import randint


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print("")
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


def run():
    x = ([randint(0, 1) for num in range(0, 3)])
    return x


m = Matrix([run(), run(), run()])
print(m)
new_m = Matrix([run(), run(), run()])
print(m.__add__(new_m))
