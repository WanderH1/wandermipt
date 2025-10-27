# num1(acknowledgements to deepseek (sorry))
# import re
#
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# def tokenize(expression):
#     token_pattern = r"(\d+\.\d+|\d+|[()+\-*/])"
#     tokens = re.findall(token_pattern, expression)
#     return tokens
#
#
# def infix_to_postfix(tokens):
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
#     output = []
#     stack = []
#
#     for token in tokens:
#         if token not in precedence and token not in ['(', ')']:
#             output.append(token)
#         elif token in precedence:
#             while (stack and stack[-1] != '(' and
#                    precedence.get(stack[-1], 0) >= precedence[token]):
#                 output.append(stack.pop())
#             stack.append(token)
#         elif token == '(':
#             stack.append(token)
#         elif token == ')':
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             if stack and stack[-1] == '(':
#                 stack.pop()
#
#     while stack:
#         output.append(stack.pop())
#
#     return output
#
# def build_ast(postfix_tokens):
#     stack = []
#     operators = set(['+', '-', '*', '/'])
#
#     for token in postfix_tokens:
#         if token not in operators:
#             stack.append(Node(token))
#         else:
#             if len(stack) < 2:
#                 raise ValueError("Недостаточно операндов для оператора")
#             right = stack.pop()
#             left = stack.pop()
#             stack.append(Node(token, left, right))
#
#     if len(stack) != 1:
#         raise ValueError("Некорректное выражение")
#     return stack[0]
#
#
# def prefix_traversal(node):
#     if node is None:
#         return []
#     left_list = prefix_traversal(node.left)
#     right_list = prefix_traversal(node.right)
#     return [node.value] + left_list + right_list
#
#
# def infix_to_prefix(tokens):
#     postfix_tokens = infix_to_postfix(tokens)
#     ast_root = build_ast(postfix_tokens)
#     prefix_tokens = prefix_traversal(ast_root)
#     return prefix_tokens
#
#
# def main(expression):
#     tokens = tokenize(expression)
#     postfix = infix_to_postfix(tokens)
#     prefix = infix_to_prefix(tokens)
#
#     return ' '.join(prefix), ' '.join(postfix)
#
# if __name__ == "__main__":
#     exam = "(3 + 4 * (2 - 1))/5"
#     prefix_expr, postfix_expr = main(exam)
#     print("Прямая польская нотация:", prefix_expr)
#     print("Обратная польская нотация:", postfix_expr)


# num2
# def evaluate(expression):
#     if not expression.strip():
#         return "Ошибка: пустое выражение"
#
#     tokens = expression.split()
#     stack = []
#
#     operators = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y if y != 0 else float('inf')
#     }
#
#     for token in tokens:
#         if token.replace('.', '').replace('-', '').isdigit() or \
#                 (token[0] == '-' and token[1:].replace('.', '').isdigit()):
#             try:
#                 number = float(token)
#                 stack.append(number)
#             except ValueError:
#                 return f"Ошибка: некорректное число '{token}'"
#
#         elif token in operators:
#             if len(stack) < 2:
#                 return f"Ошибка: недостаточно операндов для оператора '{token}'"
#
#             b = stack.pop()
#             a = stack.pop()
#
#             try:
#                 result = operators[token](a, b)
#
#                 if token == '/' and b == 0:
#                     return "Ошибка: деление на ноль"
#
#                 stack.append(result)
#
#             except Exception as e:
#                 return f"Ошибка при выполнении операции '{token}': {str(e)}"
#
#         else:
#             return f"Ошибка: неизвестный токен '{token}'"
#
#     if len(stack) == 0:
#         return "Ошибка: пустой стек после вычислений"
#     elif len(stack) > 1:
#         return f"Ошибка: в стеке осталось несколько значений: {stack}"
#
#     return stack[0]
#
#
# def calculate(expression):
#     result = evaluate(expression)
#
#     if isinstance(result, str) and result.startswith("Ошибка"):
#         return result
#     else:
#         if result == float('inf'):
#             return "Ошибка: деление на ноль"
#         return round(result, 6)
#
# def calculator():
#
#     while True:
#         try:
#             expression = input("\nВведите выражение: ").strip()
#
#             if expression.lower() in ['quit', 'exit', 'q']:
#                 print("Выход из калькулятора.")
#                 break
#
#             result = calculate(expression)
#             print(f"Результат: {result}")
#
#         except KeyboardInterrupt:
#             print("\nВыход из калькулятора.")
#             break
#         except Exception as e:
#             print(f"Неожиданная ошибка: {e}")
#
# calculator()

# num3
# import re
#
# def tokenize(expression):
#     token_pattern = r"(\d+\.\d+|\d+|[()+\-*/])"
#     tokens = re.findall(token_pattern, expression)
#     return tokens
#
#
# def infix_to_postfix(expression):
#
#     tokens = tokenize(expression)
#     output = []
#     stack = []
#
#     precedence = {
#         '+': 1,
#         '-': 1,
#         '*': 2,
#         '/': 2
#     }
#
#     associativity = {
#         '+': True,
#         '-': True,
#         '*': True,
#         '/': True
#     }
#
#     for token in tokens:
#         if token.replace('.', '').isdigit():
#             output.append(token)
#
#         elif token in precedence:
#             while (stack and stack[-1] != '(' and
#                    (precedence.get(stack[-1], 0) > precedence[token] or
#                     (precedence.get(stack[-1], 0) == precedence[token] and
#                      associativity[token]))):
#                 output.append(stack.pop())
#             stack.append(token)
#
#         elif token == '(':
#             stack.append(token)
#
#         elif token == ')':
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#
#             if not stack:
#                 raise ValueError("Несогласованные скобки")
#
#             stack.pop()
#
#     while stack:
#         if stack[-1] == '(':
#             raise ValueError("Несогласованные скобки")
#         output.append(stack.pop())
#
#     return ' '.join(output)
#
#
# def evaluate_postfix(expression):
#     tokens = expression.split()
#     stack = []
#
#     operators = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y
#     }
#
#     for token in tokens:
#         if token.replace('.', '').isdigit():
#             stack.append(float(token))
#         elif token in operators:
#             if len(stack) < 2:
#                 raise ValueError("Недостаточно операндов")
#
#             b = stack.pop()
#             a = stack.pop()
#             result = operators[token](a, b)
#             stack.append(result)
#         else:
#             raise ValueError(f"Неизвестный токен: {token}")
#
#     if len(stack) != 1:
#         raise ValueError("Некорректное выражение")
#
#     return stack[0]
#
#
# def process_expression(expression):
#     try:
#         postfix = infix_to_postfix(expression)
#         result = evaluate_postfix(postfix)
#         return postfix, result
#     except Exception as e:
#         return None, str(e)
#
# def demonstrate(expression):
#     print(f"\nВведите выражение: {expression}")
#     print("=" * 50)
#
#     tokens = tokenize(expression)
#     output = []
#     stack = []
#
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
#     associativity = {'+': True, '-': True, '*': True, '/': True}
#
#     print(f"{'Токен':<10} {'Стек':<20} {'Выход':<20}")
#     print("-" * 50)
#
#     for token in tokens:
#         if token.replace('.', '').isdigit():
#             output.append(token)
#             print(f"{token:<10} {str(stack):<20} {str(output):<20}")
#
#         elif token in precedence:
#             while (stack and stack[-1] != '(' and
#                    (precedence.get(stack[-1], 0) > precedence[token] or
#                     (precedence.get(stack[-1], 0) == precedence[token] and
#                      associativity[token]))):
#                 output.append(stack.pop())
#             stack.append(token)
#             print(f"{token:<10} {str(stack):<20} {str(output):<20}")
#
#         elif token == '(':
#             stack.append(token)
#             print(f"{token:<10} {str(stack):<20} {str(output):<20}")
#
#         elif token == ')':
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             print(f"{token:<10} {str(stack):<20} {str(output):<20}")
#
#     while stack:
#         output.append(stack.pop())
#         print(f"{' ': <10} {str(stack):<20} {str(output):<20}")
#
#     result = ' '.join(output)
#     print(f"\nРезультат: {result}")
#
# demonstrate(input())

# num4
# class Box:
#     def __init__(self, cat=None):
#         self.cat = cat
#         self.nextcat = None
#         self.prevcat = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self._length = 0
#
#     def __len__(self):
#         return self._length
#
#     def insert(self, index, newcat):
#         if index < 0 or index > self._length:
#             raise IndexError("Индекс вне диапазона")
#
#         newbox = Box(newcat)
#
#         if index == 0:
#             if self.head is None:
#                 self.head = newbox
#                 self.tail = newbox
#             else:
#                 newbox.nextcat = self.head
#                 self.head.prevcat = newbox
#                 self.head = newbox
#         elif index == self._length:
#             self.tail.nextcat = newbox
#             newbox.prevcat = self.tail
#             self.tail = newbox
#         else:
#             current = self.head
#             for _ in range(index):
#                 current = current.nextcat
#
#             newbox.nextcat = current
#             newbox.prevcat = current.prevcat
#             current.prevcat.nextcat = newbox
#             current.prevcat = newbox
#
#         self._length += 1
#
#     def get(self, index):
#         if index < 0 or index >= self._length:
#             raise IndexError("Индекс вне диапазона")
#
#         current = self.head
#         for _ in range(index):
#             current = current.nextcat
#         return current.cat
#
#     def removeByIndex(self, index):
#         if index < 0 or index >= self._length:
#             raise IndexError("Индекс вне диапазона")
#
#         if index == 0:
#             removed = self.head.cat
#             if self._length == 1:
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = self.head.nextcat
#                 self.head.prevcat = None
#         elif index == self._length - 1:
#             removed = self.tail.cat
#             self.tail = self.tail.prevcat
#             self.tail.nextcat = None
#         else:
#             current = self.head
#             for _ in range(index):
#                 current = current.nextcat
#             removed = current.cat
#             current.prevcat.nextcat = current.nextcat
#             current.nextcat.prevcat = current.prevcat
#
#         self._length -= 1
#         return removed
#
# if __name__ == "__main__":
#     lst = LinkedList()
#
#     for i, cat in enumerate(["Барсик", "Мурзик", "Васька"]):
#         lst.insert(i, cat)
#
#     print(f"Длина списка: {len(lst)}")
#
#     for i in range(len(lst)):
#         print(f"Элемент {i}: {lst.get(i)}")
#
#     removed = lst.removeByIndex(1)
#     print(f"Удален: {removed}")
#     print(f"Новая длина: {len(lst)}")
#
#     lst.insert(1, "Рыжик")
#     print(f"После вставки в середину:")
#     for i in range(len(lst)):
#         print(f"Элемент {i}: {lst.get(i)}")
