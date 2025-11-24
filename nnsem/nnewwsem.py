# num1
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def search(self, target):
#         current = self.head
#         while current:
#             if current.data == target:
#                 return True
#             current = current.next
#         return False
#
#
# linked_list = LinkedList()
# for i in [5, 12, 8, 3, 15]:
#     linked_list.insert_at_end(i)
#
# search_element = int(input())
# result = linked_list.search(search_element)
# print(result)
#
#num2
# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.nref = None
#         self.pref = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.start_node = None
#
#     def insert_at_end(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#             return
#         n = self.start_node
#         while n.nref is not None:
#             n = n.nref
#         new_node = Node(data)
#         n.nref = new_node
#         new_node.pref = n
#
#     def print_reverse(self):
#         if self.start_node is None:
#             print("Список пуст")
#             return
#
#         last = self.start_node
#         while last.nref is not None:
#             last = last.nref
#
#         current = last
#         while current is not None:
#             print(current.item, end=" ")
#             current = current.pref
#         print()
#
#
# dll = DoublyLinkedList()
# for number in [10, 20, 30, 40, 50]:
#     dll.insert_at_end(number)
#
# print("Обратный порядок:")
# dll.print_reverse()
#
#num3
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> " if current.next else "")
#             current = current.next
#         print()
#
#     def difference(self):
#         if self.head is None:
#             return []
#
#         last = self.head
#         while last.next:
#             last = last.next
#         a_n = last.data
#
#         result = []
#         current = self.head
#         while current:
#             result.append(current.data - a_n)
#             current = current.next
#
#         return result
#
#
# simple_list = LinkedList()
# for num in [5, 3, 12, 5, 9]:
#     simple_list.add(num)
#
# simple_list.print_list()
#
# differences = simple_list.difference()
# print(differences)
#
#num4 (acknowledgements to deepseek)
# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.nref = None
#         self.pref = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.start_node = None
#
#     def insert_at_end(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#         else:
#             n = self.start_node
#             while n.nref is not None:
#                 n = n.nref
#             new_node = Node(data)
#             n.nref = new_node
#             new_node.pref = n
#
#     def delete_element(self, value):
#         if self.start_node is None:
#             print("Список пуст")
#             return False
#
#         if self.start_node.item == value:
#             if self.start_node.nref is None:
#                 self.start_node = None
#             else:
#                 self.start_node = self.start_node.nref
#                 self.start_node.pref = None
#             return True
#
#         n = self.start_node
#         while n.nref is not None:
#             if n.item == value:
#                 break
#             n = n.nref
#
#         if n.item == value:
#             if n.nref is not None:
#                 n.pref.nref = n.nref
#                 n.nref.pref = n.pref
#             else:
#                 n.pref.nref = None
#             return True
#
#         print(f"Элемент {value} не найден")
#         return False
#
#     def display(self):
#         if self.start_node is None:
#             print("Список пуст")
#             return
#         n = self.start_node
#         while n is not None:
#             print(n.item, end=" <-> " if n.nref else "")
#             n = n.nref
#         print()
#
#
# dll = DoublyLinkedList()
#
# for i in [10, 20, 30, 40, 50]:
#     dll.insert_at_end(i)
#
# print("Исходный список:")
# dll.display()
#
# try:
#     value_to_delete = int(input("Введите элемент для удаления: "))
#     if dll.delete_element(value_to_delete):
#         print(f"Элемент {value_to_delete} удален")
#         print("Обновленный список:")
#         dll.display()
#     else:
#         print(f"Не удалось удалить элемент {value_to_delete}")
# except ValueError:
#     print("Ошибка: введите целое число")
#
#num5
# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.nref = None
#         self.pref = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.start_node = None
#
#     def insert_at_end(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#         else:
#             n = self.start_node
#             while n.nref is not None:
#                 n = n.nref
#             new_node = Node(data)
#             n.nref = new_node
#             new_node.pref = n
#
#     def compute_mirror_differences(self):
#         if self.start_node is None:
#             return []
#
#         left = self.start_node
#
#         right = self.start_node
#         while right.nref is not None:
#             right = right.nref
#
#         result = []
#
#         while left != right and left.pref != right:
#             result.append(left.item - right.item)
#             left = left.nref
#             right = right.pref
#
#         return result
#
#
# dll = DoublyLinkedList()
# for num in [10, 20, 30, 40, 50]:
#     dll.insert_at_end(num)
#
# differences = dll.compute_mirror_differences()
# print(differences)
#
#num6
# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.nref = None
#         self.pref = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self._size = 0
#
#     def push(self, data):
#         new_node = Node(data)
#         if self.top:
#             new_node.pref = self.top
#             self.top.nref = new_node
#         self.top = new_node
#         self._size += 1
#
#     def pop(self):
#         if not self.top:
#             return None
#         popped = self.top.item
#         self.top = self.top.pref
#         if self.top:
#             self.top.nref = None
#         self._size -= 1
#         return popped
#
#     def top_element(self):
#         return self.top.item if self.top else None
#
#     def size(self):
#         return self._size
#
#     def is_empty(self):
#         return self.top is None
#
#     def printstack(self):
#         current = self.top
#         while current:
#             print(current.item, end=" -> " if current.pref else "")
#             current = current.pref
#         print()
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.printstack()
# print(stack.pop())
# stack.printstack()
#
#num1.1
# class Node:
#     def __init__(self, key=None, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right
#
#
# def is_symmetric(root):
#
#     def check_mirror(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         return (check_mirror(left.left, right.right) and
#                 check_mirror(left.right, right.left))
#
#     return not root or check_mirror(root.left, root.right)
#
#
# if __name__ == "__main__":
#     tree1 = Node(1)
#     tree1.left = Node(2)
#     tree1.right = Node(3)
#     tree1.left.left = Node(4)
#     tree1.left.right = Node(5)
#     tree1.right.left = Node(6)
#     tree1.right.right = Node(7)
#
#     print(f"Дерево 1 симметрично: {is_symmetric(tree1)}")
#
#     tree2 = Node(1)
#     tree2.left = Node(2)
#     tree2.right = Node(3)
#     tree2.left.left = Node(4)
#     tree2.left.right = Node(5)
#     tree2.right.left = Node(6)
#
#     print(f"Дерево 2 симметрично: {is_symmetric(tree2)}")
#
#num1.2
# class Node:
#     def __init__(self, key=None, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right
#
#
# def mirror_tree(root):
#     if root is None:
#         return None
#
#     root.left, root.right = root.right, root.left
#
#     mirror_tree(root.left)
#     mirror_tree(root.right)
#
#     return root
#
#
# def print_inorder(root):
#     if root:
#         print_inorder(root.left)
#         print(root.key, end=" ")
#         print_inorder(root.right)
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Оригинальное дерево:")
# print_inorder(root)
# print()
#
# mirror_tree(root)
#
# print("Зеркальное дерево:")
# print_inorder(root)
# print()

#num1.3
# class Node:
#     def __init__(self, key=None, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right
#
#
# def find_ancestors(root, target):
#
#     def find_node_path(node, path):
#         if not node:
#             return False
#
#         path.append(node.key)
#
#         if node.key == target:
#             return True
#
#         if find_node_path(node.left, path) or find_node_path(node.right, path):
#             return True
#
#         path.pop()
#         return False
#
#     path = []
#     find_node_path(root, path)
#
#     return path[:-1] if len(path) > 1 else []
#
#
# if __name__ == "__main__":
#
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)
#
#     test_cases = [4, 5, 6, 2, 1, 7]
#
#     for target in test_cases:
#         ancestors = find_ancestors(root, target)
#         if ancestors:
#             print(f"Предки узла {target}: {ancestors}")
#         else:
#             print(f"Узел {target} не найден или является корнем")
#

# Рассматриваем дерево вида:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
