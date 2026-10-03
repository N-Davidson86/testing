import os

# --- НАСТРОЙКИ (меняй тут, не лазая глубоко в код) ---
output_filename = "my_simple_report.txt"  # <-- Вот тут меняешь имя файла, куда писать отчёт
files_to_check = ["README.md", "Dockerfile", "requirements.txt"]  # <-- А тут список файлов

def process_files(files_list):
    """Собирает строки отчёта, ничего не печатает."""
    report_lines = []
    report_lines.append("📁 ПРОСТОЙ ОТЧЁТ")
    report_lines.append("-" * 30)
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            line = f"✅ {file_name} — найден"
        else:
            line = f"❌ {file_name} — НЕ найден"
        
        report_lines.append(line)
    
    return report_lines

# --- ОСНОВНАЯ ЛОГИКА ---
report = process_files(files_to_check)

# Пишем в файл (имя берём из переменной output_filename)
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")

print(f"💾 Готово! Отчёт сохранён в: {output_filename}")

