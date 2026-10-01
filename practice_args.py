import os
import argparse  # <-- Это главный модуль для аргументов. Он умеет разбирать команды вида --output, -f и т.д.

def process_files(files_list):
    """
    Та же логика проверки файлов, что и раньше.
    Ничего не печатает, просто собирает строки отчёта.
    """
    report_lines = []
    report_lines.append("📁 ОТЧЁТ ПО ФАЙЛАМ")
    report_lines.append("-" * 40)
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            status_icon = "✅"
            status_text = "найден"
        else:
            status_icon = "❌"
            status_text = "НЕ найден (но есть в плане)"
        
        line = f"{status_icon} {file_name} — {status_text}"
        report_lines.append(line)
        
        if exists:
            if file_name.endswith(".md"):
                report_lines.append(f"   📄 Это документ — можно собрать оглавление.")
            elif file_name == "requirements.txt":
                report_lines.append(f"   📦 Это список зависимостей — нужно установить пакеты.")
            else:
                report_lines.append(f"   ℹ️ Тип не определён — пропускаю автоматическую обработку.")
    
    return report_lines

def main():
    # --- НАСТРОЙКА АРГУМЕНТОВ (самое важное) ---
    parser = argparse.ArgumentParser(
        description="Скрипт проверки файлов с гибкими параметрами."
    )
    
    # --files: список файлов для проверки. nargs='+' означает «один или больше файлов»
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,          # Обязательно: без этого параметра скрипт не запустится
        help="Список файлов для проверки (например: --files README.md Dockerfile)"
    )
    
    # --output: имя файла, куда сохранить отчёт. По умолчанию — file_report.txt
    parser.add_argument(
        "--output",
        default="file_report.txt",
        help="Имя выходного файла для отчёта (по умолчанию: file_report.txt)"
    )
    
    # --verbose: флаг-переключатель. Если указан — выводим больше информации в терминал
    parser.add_argument(
        "--verbose",
        action="store_true",     # Если пользователь напишет --verbose, переменная станет True
        help="Включить подробный вывод в терминале"
    )

    # Парсим аргументы, которые пользователь передал при запуске
    args = parser.parse_args()

    # Теперь вместо жёстко прописанного списка используем то, что передал пользователь
    files = args.files
    output_filename = args.output
    verbose = args.verbose

    if verbose:
        print(f"🔍 Режим подробного вывода включён.")
        print(f"📂 Проверяем файлы: {', '.join(files)}")
        print(f"💾 Отчёт будет сохранён в: {output_filename}\n")

    # Получаем отчёт через нашу функцию
    report = process_files(files)

    # Записываем отчёт в файл (логика та же, что и раньше)
    with open(output_filename, "w", encoding="utf-8") as f:
        for line in report:
            f.write(line + "\n")
    
    print(f"💾 Отчёт сохранён: {output_filename}")

    # Если verbose включён — ещё и выводим в терминал
    if verbose:
        print("\n👁 Содержимое отчёта:")
        for line in report:
            print(line)

if __name__ == "__main__":
    main()

