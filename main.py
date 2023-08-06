# class Method:
#     def __init__(self):
#         ...
#
#     def length(self):
#         pass
#
#     def is_include(self):
#         pass
#
#
# class String(Method):
#     def __init__(self, some_obj, value, some_str, old_word, new_word, new_str):
#         self.some_obj = some_obj
#         self.value = value
#         self.some_str = some_str
#         self.old_word = old_word
#         self.new_word = new_word
#         self.new_str = new_str
#
#     def length(self):
#         count = 0
#         for i in self.some_obj:
#             count += 1
#         return count
#
#     def is_include(self):
#         for i in self.some_str:
#             if i == self.value:
#                 return True
#         return False
#
#     def replace(self):
#         ne_str = ''
#         for i in self.new_str:
#             if i == self.old_word:
#                 ne_str += self.new_word
#             else:
#                 ne_str += i
#         return ne_str
#
#
# class List(Method):
#     def __init__(self, some_obj, value, some_str, new_list, old_list):
#         self.some_obj = some_obj
#         self.value = value
#         self.some_str = some_str
#         self.new_list = new_list
#         self.old_list = old_list
#
#     def length(self):
#         count = 0
#         for i in self.some_obj:
#             count += 1
#         return count
#
#     def is_include(self):
#         for i in self.some_str:
#             if i == self.value:
#                 return True
#         return False
#
#
#     def add(self):
#         return self.new_list + self.old_list
#
#
#
# def length(some_obj):
#     return some_obj.length()
#
#
# def is_include(some_obj):
#     return some_obj.is_include()
#
#
# def replace(some_obj):
#     return some_obj.replace()
#
#
# def add(some_obj):
#     return some_obj.add()
#
#
# str1 = String('some_obj', 'a', 'old_word', 'a', 'b', 'aaaabbbb')
# print(length(str1))
# print(is_include(str1))
# print(replace(str1))
# list1 = List('some_obj', 'a', 'old_word', ['a', 'b'], ['a', 'b'])
# print(length(list1))
# print(is_include(list1))
# print(add(list1))