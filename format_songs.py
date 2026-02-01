import os

# папка list, если ее нет
if not os.path.exists("list"):
    os.makedirs("list")

while True:
    # имя исходника
    input_name = input("введите имя файла (без .txt) или 'exit' для выхода: ")

    if input_name.lower() == "exit":
        print("выход из программы..")
        break

    input_file = f"{input_name}.txt" # исходник
    output_file = os.path.join("list", f"{input_name}_list.txt")  # файл в папке list с окончанием _list

    try:
        # читаем исходник
        with open(input_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        # объединяем "трек — артист"
        result = []
        for i in range(0, len(lines), 2):
            track = lines[i]
            artist = lines[i+1] if i+1 < len(lines) else ""
            result.append(f"{track} — {artist}")

        # сохраняем в новый файл
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(result))

        print(f"готово! файл {output_file} создан с форматированными песнями.\n")

    except FileNotFoundError:
        print(f"файл {input_file} не найден, попробуйте снова.\n")