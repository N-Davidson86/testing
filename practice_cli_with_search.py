import os                                 # Для проверки существования файлов
import sys                                # Для чтения аргументов из терминала
import glob                               # НОВАЯ библиотека: умеет искать файлы по шаблону (типа *.txt)

def process_files(files_list):            # Функция проверки файлов (старая логика, без изменений)
    """Проверяет файлы и возвращает список строк отчёта."""
    report_lines = []
    report_lines.append("📁 ОТЧЁТ (с автопоиском)")
    report_lines.append("-" * 30)
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            line = f"✅ {file_name} — найден"
        else:
            line = f"❌ {file_name} — НЕ найден"
        
        report_lines.append(line)
    
    return report_lines

# --- ГЛАВНАЯ ЛОГИКА: разбираем аргументы и добавляем автопоиск ---

all_args = sys.argv[1:]                    # Берём все аргументы, кроме имени скрипта

# Если ничего не передали — дефолт
if len(all_args) == 0:
    output_filename = "default_report.txt"
    files_to_check = ["README.md", "Dockerfile"]
else:
    # Первый аргумент — имя выходного файла
    output_filename = all_args[0]
    
    # Остальные аргументы — это то, что пользователь хочет проверить
    raw_files = all_args[1:]
    
    # Здесь начинается новая логика: превращаем спец-слова в реальные файлы
    final_files = []                        # Сюда соберём итоговый список файлов
    
    for item in raw_files:                  # Проходим по каждому слову, которое ты ввёл
        if item == "all_txt":              # Если ты написал "all_txt" — ищем все .txt
            matches = glob.glob("*.txt")   # glob.glob вернёт список всех файлов, заканчивающихся на .txt
            final_files.extend(matches)    # Добавляем найденные файлы в наш список
        elif item == "all_md":            # Если "all_md" — ищем все .md
            matches = glob.glob("*.md")
            final_files.extend(matches)
        elif item == "all_py":             # Если "all_py" — ищем все .py
            matches = glob.glob("*.py")
            final_files.extend(matches)
        else:
            # Если это НЕ спец-слово — считаем, что это обычное имя файла
            # Например: README.md, Dockerfile, config.txt
            final_files.append(item)
    
    # Страховка: если после всех поисков список пустой (например, ты написал all_txt, но .txt нет)
    if len(final_files) == 0:
        final_files = ["README.md"]         # Подставим хотя бы один файл, чтобы отчёт не был пустым
    
    files_to_check = final_files

# Вызываем функцию проверки с итоговым списком
report = process_files(files_to_check)

# Записываем отчёт в файл (имя пришло из терминала)
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")

print(f"💾 Готово! Отчёт сохранён в: {output_filename}")
print(f"📂 Проверено файлов: {len(files_to_check)}")

