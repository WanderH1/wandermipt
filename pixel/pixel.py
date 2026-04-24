#pixel (acknowledgements to gemini)
# class Fact:
#
#     def __init__(self, text: str, importance: int):
#         self.text = text
#         self.importance = importance
#         self.access_count = 0
#         self.age = 0
#
#     def get_retention_score(self) -> int:
#         return (self.importance * 5) + (self.access_count * 3) - (self.age * 1)
#
#     def __repr__(self):
#         return (f"[{self.get_retention_score():>3}] '{self.text}' "
#                 f"(Важность: {self.importance},"
#                 f"Обращений: {self.access_count}, Возраст: {self.age})")
#
#
# class PixelMemory:
#
#     def __init__(self, max_capacity: int = 10):
#         self.max_capacity = max_capacity
#         self.notebook = []
#
#     def add_fact(self, text: str, importance: int):
#
#         for fact in self.notebook:
#             fact.age += 1
#
#         if len(self.notebook) >= self.max_capacity:
#             self._evict_forgotten_fact()
#
#         new_fact = Fact(text, importance)
#         self.notebook.append(new_fact)
#         print(f"✍️ Пиксель записал: '{text}' (Важность: {importance})")
#
#     def recall_fact(self, keyword: str):
#         print(f"\nХозяин спрашивает про: '{keyword}'...")
#
#         for fact in self.notebook:
#             if keyword.lower() in fact.text.lower():
#                 fact.access_count += 1
#                 print(f"💡 Пиксель вспомнил! -> {fact.text}")
#                 return fact.text
#
#         print("❓ Пиксель грустно виляет хвостом. Он этого не помнит.")
#         return None
#
#     def _evict_forgotten_fact(self):
#
#         fact_to_forget = min(self.notebook,
#                              key=lambda f: f.get_retention_score())
#
#         self.notebook.remove(fact_to_forget)
#         print(f"🗑️ Память заполнена! Пиксель вырвал страницу:"
#               f"'{fact_to_forget.text}' "
#               f"(Индекс удержания был слишком мал:"
#               f"{fact_to_forget.get_retention_score()})")
#
#     def show_notebook(self):
#         print("\n=== БЛОКНОТ ПИКСЕЛЯ (отсортирован по Индексу Удержания) ===")
#         sorted_facts = sorted(self.notebook,
#                               key=lambda f: f.get_retention_score(),
#                               reverse=True)
#         for i, fact in enumerate(sorted_facts, 1):
#             print(f"{i}. {fact}")
#         print("===========================================================\n")
#
#
# if __name__ == "__main__":
#     pixel = PixelMemory(max_capacity=5)
#
#     pixel.add_fact("Любимая еда хозяина - пицца", importance=9)
#     pixel.add_fact("Мячик лежит под диваном", importance=5)
#     pixel.add_fact("Сегодня шел дождь", importance=2)
#     pixel.add_fact("Завтра нужно к ветеринару", importance=7)
#     pixel.add_fact("Хозяин не любит рано вставать", importance=8)
#
#     pixel.show_notebook()
#
#     pixel.recall_fact("еда")
#     pixel.recall_fact("вставать")
#     pixel.recall_fact("еда")
#
#     pixel.show_notebook()
#
#     pixel.add_fact("Почтальон приходит в 10 утра", importance=3)
#
#     pixel.add_fact("Соседская кошка злая", importance=6)
#
#     pixel.show_notebook()
# 
