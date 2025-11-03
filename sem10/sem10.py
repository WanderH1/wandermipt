#num1
# class Atbash:
#     alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#
#     def __init__(self):
#         lowercase_code = \
#             {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
#         uppercase_code = {
#             x.upper(): y.upper() for x, y in zip(
#                 self.alphabet,
#                 self.alphabet[::-1]
#             )
#         }
#         self._encode = lowercase_code
#         self._encode.update(uppercase_code)
#
#     def encode(self, text):
#         return ''.join([self._encode.get(char, char) for char in text])
#
#     def decode(self, text):
#         return ''.join([self._encode.get(char, char) for char in text])
#
# cipher = Atbash()
# line = input()
# while line != '.':
#     print(cipher.decode(line))
#     line = input()

#num2 (podborom key=14)
# class Caesar:
#     alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
#
#     def __init__(self, key):
#         self._encode = dict()
#         for i in range(len(self.alphabet)):
#             letter = self.alphabet[i]
#             encoded = self.alphabet[(i + key) % len(self.alphabet)]
#             self._encode[letter] = encoded
#             self._encode[letter.upper()] = encoded.upper()
#         self._decode = dict()
#         for i in range(len(self.alphabet)):
#             letter = self.alphabet[i]
#             encoded = self.alphabet[(i - key) % len(self.alphabet)]
#             self._decode[letter] = encoded
#             self._decode[letter.upper()] = encoded.upper()
#
#     def encode(self, text):
#         return ''.join([self._encode.get(char, char) for char in text])
#
#     def decode(self, text):
#         return ''.join([self._decode.get(char, char) for char in text])
#
#
# key = int(input('Ээъыцмъ фубз:'))
# cipher = Caesar(key)
# line = input()
# while line:
#     print(cipher.decode(line))
#     line = input()

#num3
# class Monoalphabet:
#     alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#
#     def __init__(self, keytable):
#         lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
#         uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
#         self._encode = lowercase_code
#         self._encode.update(uppercase_code)
#         self._decode = {v: k for k, v in self._encode.items()}
#
#     def encode(self, text):
#         return ''.join([self._encode.get(char, char) for char in text])
#
#     def decode(self, line):
#         return ''.join([self._decode.get(char, char) for char in line])
#
# correspondences = [
#     'ЕШ', 'ГИ', 'ПФ', 'ЖР', 'ОВ', 'НЖ', 'ЩЕ', 'ЮН', 'ЭА', 'БТ',
#     'ЭА', 'ЧК', 'МД', 'ЯЛ', 'ХЬ', 'ЫЙ', 'ЦО', 'ИЯ', 'ЛЧ', 'ДЁ',
#     'ШС', 'АП', 'РГ', 'СМ', 'ЙЗ', 'ЗЫ', 'ВХ', 'ЬБ', 'ЁЦ', 'КЭ',
#     'ТУ', 'ФЮ'
# ]
#
# decode_dict = {}
# for pair in correspondences:
#     encoded, decoded = pair[0], pair[1]
#     decode_dict[encoded] = decoded
#     decode_dict[encoded.lower()] = decoded.lower()
#
# encrypted_text = """Егпж Огнщющжэ (ацягэяпэогбюцы йэсщюз)
# Мэяхющыегс ажцмцянщюгщс егпжцо ажцшбцы йэсщюз иояищбши сюцрцэяпэогбюзщ егпжз. Эьт Эях-Чгюмг о шоцгв жэьцбэв ацчэйэя, лбц цьзлюзщ сцюцэяпэогбюзщ егпжз мцоцяхюц-бэчг ажцшбц ацммэфбши лэшбцбюцст чжгабцэюэягйт г ащжозс ажщмяцнгя гшацяхйцоэбх сюцрцэяпэогбюзщ егпжз. О Щожцащ бэчгщ егпжз ьзяг оащжозщ цагшэюз о 1467 рцмт гбэяхиюшчгс эжвгбщчбцжцс Ящцю Ьэббгшбэ Эяхьщжбг. О XVI ощчщ ющсщёчгы эььэб Гцрэюю Бжгбщсгы о шоцщы чюгрщ "Шбщюцржэпги" ажщмшбэогя швщст ацягэяпэогбюцрц егпжцоэюги о огмщ бэьягёз. Ьцящщ шяцнюзы оэжгэюб ш гшацяхйцоэюгщс шсщеэююзв эяпэогбцо ьзя цагшэю о 1563 рцмт Мнэсьэббгшбэ мщяяэ Ацжбэ о щрц чюгрщ "Ажц шчжзбтф йюэлгсцшбх цбмщяхюзв ьтчо". Ацшящмюгс шяцоцс о жэйогбгг ацягэяпэогбюзв егпжцо сцнюц шлгбэбх жцбцжюзщ сэегюз, ажгсщжцс чцбцжцы сцнюц шлгбэбх ющсщёчтф сэегют Enigma, жэйжэьцбэююэи о 1917 р. Штбх ацягэяпэогбюзв егпжцо йэчяфлщюэ о сюцрцчжэбюцс ажгсщющюгг жэйяглюзв егпжцо ажцшбцы йэсщюз ч цажщмщящююцст лгшят ьтчо егпжтщсцрц бщчшбэ. Бц щшбх ч чэнмцы ьтчощ ац цбмщяхюцшбг ажгсщюищбши цмгю гй егпжцо ажцшбцы йэсщюз.
#
# Егпж Огнщющжэ шцшбцгб гй ацшящмцоэбщяхюцшбг ющшчцяхчгв егпжцо Ёщйэжи ш жэйяглюзсг йюэлщюгисг шмогрэ. Мяи йэегпжцозоэюги сцнщб гшацяхйцоэбхши бэьягёэ эяпэогбцо, юэйзоэщсэи чоэмжэб (бэьягёэ) Огнщющжэ. Ажгсщюгбщяхюц ч жтшшчцст эяпэогбт бэьягёэ Огнщющжэ шцшбэояищбши гй шбжцч ац 33 шгсоцяцо, ажглдс чэнмэи шящмтфъэи шбжцчэ шмогрэщбши юэ ющшчцяхчц ацйгёгы. Бэчгс цьжэйцс, о бэьягёщ ацятлэщбши 33 жэйяглюзв егпжцо Ёщйэжи. Юэ жэйюзв кбэаэв чцмгжцочг егпж Огнщющжэ гшацяхйтщб жэйяглюзщ эяпэогбз гй кбцы бэьягёз. Юэ чэнмцс кбэащ егпжцоэюги гшацяхйтфбши жэйяглюзщ эяпэогбз, озьгжэщсзщ о йэогшгсцшбг цб шгсоцяэ чяфлщоцрц шяцоэ. Юэажгсщж, щшяг чяфлщоцщ шяцоц "ШЭБ", бц ащжоэи ьтчоэ цбчжзбцрц бщчшбэ егпжтщбши ш гшацяхйцоэюгщс эяпэогбэ "Ш', обцжэи "Э", бжщбхи "Б", лщбоджбэи шюцоэ "Ш" г бэч мэящщ.
#
# Ажцржэссэ егпжцоэюги егпжцс Огнщющжэ:
# Ацшящмюгы жэймщя жэьцбз йэегпжцоэю егпжцс Огнщющжэ ш ющгйощшбюзс чцмцозс шяцоцс. Ацмшчэйчэ мяи шэсзв шбцычгв чжгабцэюэягбгчцо: мягюэ чцмцоцрц шяцоэ 8."""
#
# partially_decoded = []
# for char in encrypted_text:
#     if char in decode_dict:
#         partially_decoded.append(decode_dict[char])
#     else:
#         partially_decoded.append(char)
# partially_decoded_text = ''.join(partially_decoded)
#
# def frequency_analysis(text):
#     text = text.lower()
#     freq = {}
#     total_letters = 0
#     for char in text:
#         if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
#             freq[char] = freq.get(char, 0) + 1
#             total_letters += 1
#     for char in freq:
#         freq[char] = freq[char] / total_letters
#     return freq
#
#
# standard_freq = {
#     'о': 0.090, 'е': 0.072, 'ё': 0.072, 'а': 0.062, 'и': 0.062,
#     'н': 0.053, 'т': 0.053, 'с': 0.045, 'р': 0.040, 'в': 0.038,
#     'л': 0.035, 'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023,
#     'у': 0.021, 'я': 0.018, 'ы': 0.016, 'з': 0.016, 'ь': 0.014,
#     'б': 0.014, 'г': 0.014, 'ч': 0.013, 'й': 0.012, 'х': 0.009,
#     'ж': 0.007, 'ш': 0.006, 'ю': 0.006, 'ц': 0.004, 'щ': 0.003,
#     'э': 0.003, 'ф': 0.002, 'ъ': 0.002
# }
#
# current_freq = frequency_analysis(partially_decoded_text)
# remaining_chars = [char for char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" if char not in decode_dict.values()]
#
# current_sorted = sorted([(freq, char) for char, freq in current_freq.items()
#                          if char in remaining_chars], reverse=True)
# standard_sorted = sorted([(freq, char) for char, freq in standard_freq.items()
#                           if char in remaining_chars], reverse=True)
#
# freq_decode_dict = {}
# for (f1, c1), (f2, c2) in zip(current_sorted, standard_sorted):
#     freq_decode_dict[c1] = c2
#     freq_decode_dict[c1.upper()] = c2.upper()
#
# full_decode_dict = {**decode_dict, **freq_decode_dict}
#
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#
# reverse_mapping = {}
# for enc_char, dec_char in full_decode_dict.items():
#     if enc_char in alphabet:
#         reverse_mapping[dec_char] = enc_char
#
# keytable = ''.join([reverse_mapping.get(letter, letter) for letter in alphabet])
#
# cipher = Monoalphabet(keytable)
# decoded_text = cipher.decode(encrypted_text)
# print(decoded_text)

#num4 (false)
# class Vigenere:
#     alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#
#     def __init__(self, keyword):
#         self.alphaindex = {ch: idx for idx, ch in enumerate(self.alphabet)}
#         self.key = [self.alphaindex[letter] for letter in keyword.lower()]
#
#     def caesar(self, letter, shift):
#         if letter in self.alphaindex:
#             index = (self.alphaindex[letter] + shift) % len(self.alphabet)
#             return self.alphabet[index]
#         elif letter.lower() in self.alphaindex:
#             return self.caesar(letter.lower(), shift).upper()
#         else:
#             return letter
#
#     def encode(self, line):
#         ciphertext = []
#         for i, letter in enumerate(line):
#             shift = self.key[i % len(self.key)]
#             cipherletter = self.caesar(letter, shift)
#             ciphertext.append(cipherletter)
#         return ''.join(ciphertext)
#
#     def decode(self, line):
#         plaintext = []
#         for i, letter in enumerate(line):
#             shift = self.key[i % len(self.key)]
#             if letter in self.alphaindex:
#                 index = (self.alphaindex[letter] - shift) % len(self.alphabet)
#                 plainletter = self.alphabet[index]
#             elif letter.lower() in self.alphaindex:
#                 index = (self.alphaindex[letter.lower()] - shift) % len(self.alphabet)
#                 plainletter = self.alphabet[index].upper()
#             else:
#                 plainletter = letter
#             plaintext.append(plainletter)
#         return ''.join(plaintext)
#
#
# encrypted_text = '''йвылщф
# (ключ-слово: мфти)
#
# ыцящгнюзрвхщдз щгхья дбахжтыи дгч эщтфхьтяхт дфыыачпг вчшэтфбффсявблы мыээф -- эчщдожящгцат ячрщюе еэжщм "саспбн". ёшщянъжн хсжбмыц ксбебкмвыз, хёвчшръчоффбхйдз о бтбхвтю йжбт ющгсх, эдшыаоратеъл шб ъхй вчэ.'''
#
# keyword = "частотный"
# cipher = Vigenere(keyword)
#
# decrypted_text = cipher.decode(encrypted_text)
# print(decrypted_text)


#itogovye texts
#Шифр Цезаря
# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.
#
# Шифр назван в честь римского императора Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами.
#
# Следующая часть работы зашифрована шифром Цезаря.
#Допишите метод decode и расшифруйте следующий раздел лабораторной работы. Подумайте, почему вам не сообщили ключ шифрования и что вам с этим делать.
#Шифр простой замены
# Поздравляем с расшифровкой раздела!
#
# Итак, вы догадались почему шифр Цезаря не является криптостойким: слишком мала мощность множества ключей и нужный ключ легко найти методом полного перебора.
#
# Можно ли увеличить криптостойкость, не меняя метод шифрования? Да, можно. Если заменять один символ алфавита на определённый другой символ того же алфавита по какой-то таблице замен, то сама таблица замен и является ключом.
#
# |а|б|в|г|д|е|ё|ж|з|и|й|к|л|м|н|о|п|р|с|т|у|ф|х|ц|ч|ш|щ|ъ|ы|ь|э|ю|я|
#
# |ь|з|ц|в|к|б|щ|х|ф|п|р|я|л|э|а|е|ы|ш|у|м|ъ|ж|ё|о|г|й|н|д|и|т|ч|ю|с|
#
# Множество ключей — это множество возможных таблиц простых замен.
#
# Для русского алфавита мощность множества таблиц простых замен равна факториалу от 33.
#
# 33! = 8683317618811886495518194401280000000
#
# Если тратить на проверку одного варианта 0.000001 секунды, получится 2.8e+23 лет.
# Может показаться, что шифр простой замены вполне криптостойкий, однако это не так.
#
# Его достаточно просто взломать при помощи йтдебеабхб татюыът. Дело в том, что частота появления заданной буквы алфавита в достаточно длинных текстах одна и та же для разных текстов одного языка.
#
# Если в шифротексте будет символ с вероятностью появления, аналогичной стандартной для языка, то можно предположить, что он и является указанной зашифрованной буквой.

#
# Метод частотного криптоанализа известен с IX-го века, хотя наиболее известным случаем его применения в реальной жизни, возможно, является дешифровка египетских иероглифов в 1822 году.
#
# Итак, следующая часть работы зашифрована при помощи следующей программы:
# Программу для частотного анализа следует написать самостоятельно. Успехов!
