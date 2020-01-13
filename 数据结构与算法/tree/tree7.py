# dd = 0
# def test_nonlocal():
#     def test2():
#         global dd
#         dd += 10
#         print(dd)
#     test2()
#     dd += 2
#     print(dd)
#
# print(dd)
# test_nonlocal()
# print(dd)
#
#
# dd = 0
# def test_global():
#     def test2():
#         global dd
#         dd += 2
#         print(dd)
#     test2()
# test_global()
def test():
    def local_test():
        spam = "local spam"
    def nonlocal_test():
        nonlocal  spam
        spam = "nonlocal spam"
    def global_test():
        global spam
        spam = "global spam"
    spam = "test spam"
    local_test()
    print("After local assignmane:", spam)
    nonlocal_test()
    print("After nonlocal assignment:",spam)
    global_test()
    print("After global assignment:",spam)
# test()

# inorder = ['a', 'b', 'c']
# idx_map = {val:idx for idx, val in enumerate(inorder)}
# print(idx_map)
# print(idx_map['a'])
a = [1, 2, 3, 4, 5, 6]
print(a[1:2])
# print(a.index(5))
# list()