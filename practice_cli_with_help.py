import os                                 # Для проверки существования файлов
import sys                                # Для чтения аргументов из терминала
import glob                               # Для поиска файлов по шаблону (*.txt и т.д.)

def process_files(files_list):            # Функция проверки файлов (старая логика, без изменений)
    """Проверяет файлы и возвращает список строк отчёта."""
    report_lines = []
    report_lines.append("📁 ОТЧЁТ (с автопоиском и справкой)")
    report_lines.append("-" * 30)
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            line = f"✅ {file_name} — найден"
        else:
            line = f"❌ {file_name} — НЕ найден"
        
        report_lines.append(line)
    
    return report_lines

# --- ГЛАВНАЯ ЛОГИКА: разбираем аргументы, добавляем справку и автопоиск ---

all_args = sys.argv[1:]                    # Берём все аргументы, кроме имени скрипта

# Если пользователь явно запросил справку — сразу показываем и выходим
if "--help" in all_args or "-h" in all_args:
    print("📘 Справка по скрипту practice_cli_with_help.py")
    print("---------------------------------------------")
    print("Запуск:")
    print("  python3 practice_cli_with_help.py <output_file> [файлы...]")
    print("")
    print("Правила:")
    print("  1-й аргумент — имя выходного файла (обязательно).")
    print("  Остальные аргументы — что проверять.")
    print("")
    print("Спец-слова для автопоиска:")
    print("  all_txt  — все файлы с расширением .txt")
    print("  all_md   — все файлы с расширением .md")
    print("  all_py   — все файлы с расширением .py")
    print("")
    print("Примеры:")
    print("  python3 practice_cli_with_help.py report.txt all_md Dockerfile")
    print("  python3 practice_cli_with_help.py txt_report.txt all_txt")
    sys.exit(0)                            # Завершаем работу скрипта — дальше ничего не делаем

# Если ничего не передали — дефолт
if len(all_args) == 0:
    output_filename = "default_report.txt"
    files_to_check = ["README.md", "Dockerfile"]
else:
    # Первый аргумент — имя выходного файла
    output_filename = all_args[0]
    
    # Остальные аргументы — это то, что пользователь хочет проверить
    raw_files = all_args[1:]
    
    final_files = []                        # Сюда соберём итоговый список файлов
    
    for item in raw_files:                  # Проходим по каждому слову, которое ты ввёл
        if item == "all_txt":              # Если ты написал "all_txt" — ищем все .txt
            matches = glob.glob("*.txt")
            final_files.extend(matches)
        elif item == "all_md":             # Если "all_md" — ищем все .md
            matches = glob.glob("*.md")
            final_files.extend(matches)
        elif item == "all_py":             # Если "all_py" — ищем все .py
            matches = glob.glob("*.py")
            final_files.extend(matches)
        else:
            # Если это НЕ спец-слово — считаем, что это обычное имя файла
            final_files.append(item)
    
    # Страховка: если после всех поисков список пустой
    if len(final_files) == 0:
        final_files = ["README.md"]
    
    files_to_check = final_files

# Вызываем функцию проверки с итоговым списком
report = process_files(files_to_check)

# Записываем отчёт в файл (имя пришло из терминала)
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")

print(f"💾 Готово! Отчёт сохранён в: {output_filename}")
print(f"📂 Проверено файлов: {len(files_to_check)}")

