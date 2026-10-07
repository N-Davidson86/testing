import os
import sys
import glob
from datetime import datetime
import stat

def process_files(files_list):
    # ИСПРАВЛЕНО: сразу присваиваем пустой список, а не оставляем строку незавершённой
    report_lines = []
    report_lines.append("📁 ОТЧЁТ (с метриками: размер и дата)")
    report_lines.append("-" * 60)
    report_lines.append(f"{'Файл':<30} | {'Статус':<10} | {'Размер (байт)':<15} | {'Дата изменения'}")
    report_lines.append("-" * 60)

    for file_name in files_list:
        exists = os.path.exists(file_name)
        size_str = "N/A"
        date_str = "N/A"
        status_text = "НЕ найден"

        if exists:
            status_text = "Найден"
            try:
                size_bytes = os.path.getsize(file_name)
                size_str = str(size_bytes)
                mtime = os.path.getmtime(file_name)
                date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
            except OSError:
                size_str = "Ошибка чтения"
                date_str = "Ошибка чтения"

        line = f"{file_name:<30} | {status_text:<10} | {size_str:<15} | {date_str}"
        report_lines.append(line)

    return report_lines

all_args = sys.argv[1:]

# Справка
if "--help" in all_args or "-h" in all_args:
    print("📘 Справка: python3 practice_cli_final_step.py <output_file> [файлы...]")
    print("Спец-слова: all_txt, all_md, all_py")
    print("Пример: python3 practice_cli_final_step.py report.txt all_md Dockerfile")
    sys.exit(0)

# Дефолт при полном отсутствии аргументов
if len(all_args) == 0:
    output_filename = "default_report.txt"
    files_to_check = ["README.md", "Dockerfile"]
else:
    # ИСПРАВЛЕНО: берём именно первый элемент списка, а не весь список
    output_filename = all_args[0]

    # Защита: если первым аргументом идёт спец-слово — это ошибка
    if output_filename in ["all_txt", "all_md", "all_py"]:
        print("⚠️ Ошибка: похоже, ты перепутал порядок аргументов!")
        print(f"Ты использовал '{output_filename}' как имя файла отчёта.")
        print("Порядок: python3 script.py <ИМЯ_ФАЙЛА_ОТЧЁТА> [файлы...]")
        sys.exit(1)

    # Проверка прав на запись в целевую папку
    dir_name = os.path.dirname(output_filename) if os.path.dirname(output_filename) else '.'

    if not os.path.exists(dir_name):
        print(f"⚠️ Ошибка: Папка '{dir_name}' не существует!")
        sys.exit(1)

    if not os.access(dir_name, os.W_OK):
        print(f"⚠️ Ошибка: У тебя нет прав на запись в папку '{dir_name}'!")
        print("Это защита от случайной попытки записать файл в системные директории (например, /etc).")
        sys.exit(1)

    # Если файл уже существует, проверяем, можем ли мы его перезаписать
    if os.path.exists(output_filename) and not os.access(output_filename, os.W_OK):
        print(f"⚠️ Ошибка: У тебя нет прав на изменение файла '{output_filename}'!")
        sys.exit(1)

    raw_files = all_args[1:]
    final_files = []

    for item in raw_files:
        if item == "all_txt":
            final_files.extend(glob.glob("*.txt"))
        elif item == "all_md":
            final_files.extend(glob.glob("*.md"))
        elif item == "all_py":
            final_files.extend(glob.glob("*.py"))
        else:
            final_files.append(item)

    if len(final_files) == 0:
        final_files = ["README.md"]

    files_to_check = final_files

# Вызываем функцию проверки
report = process_files(files_to_check)

# Записываем отчёт
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")

print(f"✅ Отчёт сохранён в '{output_filename}'")

