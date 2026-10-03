import os                                 # Модуль для проверки, существует ли файл
import sys                                # Модуль для чтения аргументов из терминала

def process_files(files_list):            # Функция проверки файлов (без изменений, логика та же)
    """Проверяет файлы и возвращает список строк отчёта."""
    report_lines = []                     # Пустой список для строк отчёта
    report_lines.append("📁 ОТЧЁТ (гибкий CLI)")  # Заголовок
    report_lines.append("-" * 30)          # Разделитель
    
    for file_name in files_list:           # Проходим по каждому файлу из списка
        exists = os.path.exists(file_name)  # Проверяем: файл есть на диске? (True/False)
        
        if exists:                         # Если есть:
            line = f"✅ {file_name} — найден"  # Строка с галочкой
        else:                              # Если нет:
            line = f"❌ {file_name} — НЕ найден"  # Строка с крестиком
        
        report_lines.append(line)          # Добавляем строку в список
    
    return report_lines                    # Возвращаем весь список наружу

# --- ГЛАВНАЯ ЛОГИКА: разбираем аргументы из терминала ---

# sys.argv — это весь список того, что ты ввёл в терминале.
# Пример: python3 practice_cli_flex.py report.txt README.md Dockerfile
# Тогда sys.argv будет: ['practice_cli_flex.py', 'report.txt', 'README.md', 'Dockerfile']

all_args = sys.argv[1:]                    # Берём всё, кроме имени скрипта (пропускаем [0])

# Если пользователь вообще ничего не передал (запустил просто python3 script.py),
# all_args будет пустым []. Тогда зададим значения по умолчанию.
if len(all_args) == 0:
    output_filename = "default_report.txt"   # Имя файла отчёта по умолчанию
    files_to_check = ["README.md", "Dockerfile"]  # Файлы для проверки по умолчанию
else:
    # Логика разделения:
    # Первый аргумент — это всегда имя выходного файла
    output_filename = all_args[0]
    
    # Все остальные аргументы — это файлы, которые нужно проверить
    files_to_check = all_args[1:]
    
    # Страховка: если передали только имя файла, но не передали сами файлы для проверки
    if len(files_to_check) == 0:
        files_to_check = ["README.md"]  # Подставим хотя бы один файл, чтобы скрипт не был бесполезным

# Вызываем функцию проверки, передавая ей список файлов
report = process_files(files_to_check)

# Записываем отчёт в файл (имя файла берём из output_filename, который пришёл из терминала)
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:                   # Проходим по каждой строке отчёта
        f.write(line + "\n")              # Пишем строку и добавляем перенос строки (\n)

print(f"💾 Готово! Отчёт сохранён в: {output_filename}")  # Сообщаем, куда записали
print(f"📂 Проверено файлов: {len(files_to_check)}")      # Показываем, сколько файлов проверили

