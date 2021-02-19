with open("input.txt") as read_file, open("output.txt", "w") as write_file:
    lines = [line.strip() for line in read_file]
    lines.reverse()
    write_file.writelines(line + "\n" for line in lines)

"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab"""