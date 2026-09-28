import subprocess  # <-- Подключаем модуль для запуска команд терминала (как будто ты печатаешь в bash)
import sys         # <-- Подключаем модуль для управления выходом из программы (коды ошибок)

# Функция-помощник: запускает любую git-команду и возвращает её результат
def run_git_command(command):
    # subprocess.run(...) — запускает команду
    # command — сама команда (например, "git status --porcelain")
    # capture_output=True — ловит то, что команда выводит на экран (stdout и stderr)
    # text=True — превращает вывод из байтов в обычный текст (чтобы можно было читать)
    # shell=True — позволяет писать команду как в терминале (нужен для простых строк)
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )
    # Возвращаем три вещи: вывод команды, ошибки и код возврата (0 = успех, 1 = ошибка)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def main():
    # Запускаем git status --porcelain. 
    # Porcelain — это режим для машин: он выдает короткий, понятный код (MM, ??), а не красивый текст для человека.
    status_out, status_err, status_code = run_git_command("git status --porcelain")
    
    # Если status_out не пустой — значит, есть изменения (файлы изменены или новые)
    if status_out:
        print("❌ Error: There are uncommitted changes or untracked files:")
        print(status_out)          # <-- Покажем человеку, какие именно файлы мешают
        sys.exit(1)               # <-- Завершаем скрипт с кодом 1. Для Ansible это значит: "СТОП, дальше не иди!"
    else:
        # Если статус пустой — всё чисто
        print("✅ OK: Repository is clean.")
        sys.exit(0)               # <-- Завершаем с кодом 0. Для Ansible: "Всё хорошо, можно деплоить."

# Эта конструкция говорит Python: "Запускай функцию main только если ты запустил этот файл напрямую"
if __name__ == "__main__":
    main()

