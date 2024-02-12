# Import modul yang digunakan
import time
import random
import tkinter as tk
from tkinter import filedialog

# ASCII art
print(r" _____       _                                 _         _____  _____  ____________ ")
print(r"/  __ \     | |                               | |       / __  \|  _  ||___  /___  / ")
print(r"| /  \/_   _| |__   ___ _ __ _ __  _   _ _ __ | | __    `' / /'| |/' |   / /   / /  ")
print(r"| |   | | | | '_ \ / _ \ '__| '_ \| | | | '_ \| |/ /      / /  |  /| |  / /   / /   ")
print(r"| \__/\ |_| | |_) |  __/ |  | |_) | |_| | | | |   <     ./ /___\ |_/ /./ /  ./ /    ")
print(r" \____/\__, |_.__/ \___|_|  | .__/ \__,_|_| |_|_|\_\    \_____/ \___/ \_/   \_/     ")
print(r"        __/ |               | |                                                     ")
print(r"       |___/                |_|                                                     ")

print(r"  ____                      _       _____           _                  _ ")
print(r" |  _ \                    | |     |  __ \         | |                | |")
print(r" | |_) |_ __ ___  __ _  ___| |__   | |__) | __ ___ | |_ ___   ___ ___ | |")
print(r" |  _ <| '__/ _ \/ _` |/ __| '_ \  |  ___/ '__/ _ \| __/ _ \ / __/ _ \| |")
print(r" | |_) | | |  __/ (_| | (__| | | | | |   | | | (_) | || (_) | (_| (_) | |")
print(r" |____/|_|  \___|\__,_|\___|_| |_| |_|   |_|  \___/ \__\___/ \___\___/|_|")

# Fungsi untuk generasi sekuens random
def generate_random_sequence(tokens, max_tokens):
    sequence_length = random.randint(2, max_tokens)
    random_sequence = ' '.join(random.sample(tokens, sequence_length))
    random_score = random.randint(-100, 100)  # Adjust the score range as needed
    return random_sequence, random_score

# Fungsi untuk generasi matriks random berdasarkan token yang diinput
def generate_random_matrix(tokens, width, height):
    return [[random.choice(tokens) for _ in range(width)] for _ in range(height)]

# Fungsi untuk generasi semua series yang mungkin secara iteratif
def generate_series(matrix, buffer_size):
    rows, cols = len(matrix), len(matrix[0])
    series_list = []

    # Fungsi untuk iterasi semua kemungkinan series
    def iterate(temp_series, temp_coordinates, same_row):
        nonlocal series_list

        if len(temp_series) == buffer_size and unique_coordinates(temp_coordinates):
            series_list.append((temp_series.copy(), temp_coordinates.copy()))

        elif len(temp_series) == 0:
            for i in range(cols):
                iterate([matrix[0][i]], [(0, i)], True)

        elif len(temp_series) < buffer_size:
            last_coordinate = temp_coordinates[-1]
            if same_row:
                for i in range(rows):
                    if i != last_coordinate[0]:
                        iterate(
                            temp_series + [matrix[i][last_coordinate[1]]],
                            temp_coordinates + [(i, last_coordinate[1])],
                            False,
                        )
            else:
                for i in range(cols):
                    if i != last_coordinate[1]:
                        iterate(
                            temp_series + [matrix[last_coordinate[0]][i]],
                            temp_coordinates + [(last_coordinate[0], i)],
                            True,
                        )

    # Fungsi untuk memastikan semua elemen dalam series unik
    def unique_coordinates(temp_coordinates):
        return len(set(temp_coordinates)) == len(temp_coordinates)

    iterate([], [], True)
    return series_list

# Fungsi untuk mengecek sekuens apa saja yang terdapat dalam series
def check_sequence_in_series(series, sequence_and_reward):
    total_score = 0
    series_string = ''.join(map(str, series))

    for sequence_string, reward in sequence_and_reward.items():
        if sequence_string.replace(" ", "") in series_string.replace(" ", ""):
            total_score += reward
    
    return total_score

# Fungsi untuk mencari series dengan total skor terbanyak
def find_highest_score_series(matrix, buffer_size, sequence_and_reward):
    result = generate_series(matrix, buffer_size)

    highest_score = 0
    best_series = None
    best_coordinates = None

    for series, coordinates in result:
        total_score = check_sequence_in_series(series, sequence_and_reward)
        if total_score > highest_score:
            highest_score = total_score
            best_series = series.copy()
            best_coordinates = coordinates.copy()
    
    first_series = result[0][0]

    return best_series, highest_score, best_coordinates, first_series

# Pilihan metode input
print("1. Input dengan file .txt")
print("2. Input melalui CLI")
input_option = int(input("Pilih yang mana (1/2)? "))

while (input_option != 1) and (input_option != 2):
    input_option = int(input("Pilihan tidak tersedia.\nSilahkan pilih kembali (1/2) "))

# Input dengan file .txt
if input_option == 1:
    # Pilih file input
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Penghitungan waktu dimulai
    start_time = time.time()

    # File handling
    with open(file_path, 'r') as file:
        buffer_size = int(file.readline().strip())
        
        if (buffer_size) <= 0:
            print("Ukuran buffer harus lebih dari 0.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)
        
        second_line = list(map(int, file.readline().strip().split()))
        
        matrix_width = second_line[0]
        
        if (matrix_width) <= 0:
            print("Lebar matriks harus lebih dari 0.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)
        
        matrix_height = second_line[1]
        
        if (matrix_height) <= 0:
            print("Tinggi matriks harus lebih dari 0.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)
        
        matrix = [[] for _ in range(matrix_height)]

        for i in range(matrix_height):
            matrix_row = file.readline().strip().split()

            if len(matrix_row) != matrix_width:
                print(f"Jumlah elemen di baris {i+1} tidak sesuai dengan lebar matriks.\nPerbaiki file input lalu jalankan kembali program.")
                exit(1)
            
            for element in matrix_row:
                if not element.isalnum() or len(element) != 2:
                    print(f"Elemen '{element}' di baris {i+1} bukan merupakan token yang valid.\nPerbaiki file input lalu jalankan kembali program.")
                    exit(1)

            matrix[i].extend(matrix_row)
        
        if len(matrix) != matrix_height:
            print("Jumlah baris tidak sesuai dengan tinggi matriks.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)

        sequence_and_reward = {}
        number_of_sequences = int(file.readline().strip())
        
        if (number_of_sequences) <= 0:
            print("Jumlah sekuens harus lebih dari 0.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)
        
        loaded_sequences = 0

        for _ in range(number_of_sequences):
            sequence = file.readline().strip()
            reward = int(file.readline().strip())
            if len(sequence.split()) < 2:
                print("Sekuens harus terdiri dari minimal dua token.\nPerbaiki file input lalu jalankan kembali program.")
            sequence_and_reward[sequence] = reward
            loaded_sequences += 1
        
        if loaded_sequences != number_of_sequences:
            print("Jumlah sekuens tidak sesuai.\nPerbaiki file input lalu jalankan kembali program.")
            exit(1)

    file.close()

# Input melalui CLI
elif input_option == 2:
    token_number = int(input("Jumlah token: "))

    while (token_number) <= 0:
        print("Jumlah token harus lebih dari 0.\nMasukkan angka yang valid.")
        token_number = int(input("Jumlah token: "))
    
    while True:
        token_line = input("Token (dipisahkan oleh spasi): ").split()

        valid_tokens = all(token.isalnum() and len(token) == 2 for token in token_line)

        if valid_tokens:
            break
        else:
            print("Terdapat token yang tidak valid. Harap masukkan token lagi.")

    buffer_size = int(input("Ukuran buffer: "))

    while (buffer_size) <= 0:
        print("Ukuran buffer harus lebih dari 0.")
        buffer_size = int(input("Ukuran buffer: "))

    matrix_size = input("Ukuran matriks (lebar dan tinggi dipisahkan oleh spasi): ").split()

    matrix_width = int(matrix_size[0])

    matrix_height = int(matrix_size[1])

    while (matrix_width <= 0) or (matrix_height <= 0):
        print("Lebar dan tinggi matriks harus lebih dari 0.")
        matrix_size = input("Ukuran matriks (lebar dan tinggi dipisahkan oleh spasi): ").split()
        matrix_width = int(matrix_size[0])
        matrix_height = int(matrix_size[1])

    sequence_number = int(input("Jumlah sekuens: "))

    while (sequence_number) <= 0:
        print("Jumlah sekuens harus lebih dari 0.")
        sequence_number = int(input("Jumlah sekuens: "))

    maximum_sequence_size = int(input("Ukuran maksimum sekuens: "))

    while (maximum_sequence_size) <= 0:
        print("Ukuran maksimal sekuens harus lebih dari 0.")
        maximum_sequence_size = int(input("Ukuran maksimum sekuens: "))

    start_time = time.time()

    # Generasi matriks random
    matrix = generate_random_matrix(token_line, matrix_width, matrix_height)

    # Output matriks
    print("\nGenerated Matrix:")
    for row in matrix:
        print(' '.join(row))

    # Generasi sekuens dan reward random
    generated_sequences = []
    for _ in range(sequence_number):
        random_sequence, random_score = generate_random_sequence(token_line, maximum_sequence_size)
        generated_sequences.append((random_sequence, random_score))
        print(f"Sequence: {random_sequence}, Score: {random_score}")

    # Pencarian sekuens terbaik
    sequence_and_reward = {seq: score for seq, score in generated_sequences}

best_series, highest_score, best_coordinates, first_series = find_highest_score_series(matrix, buffer_size, sequence_and_reward)

# Penghitungan waktu selesai
end_time = time.time()

print(highest_score)
if best_series is not None:
    print(" ".join(best_series))
else:
    print("No series found.")
if best_coordinates is not None:
    for coordinates in best_coordinates:
        print(f"{coordinates[1] + 1}, {coordinates[0] + 1}")
else:
    print("No coordinates found.")
print(f"{int((end_time - start_time) * 1000)} ms")

# Opsi menyimpan output dalam file .txt
file_option = input("Apakah ingin menyimpan solusi? (y/n) ")

# File handling
if file_option == "y":
    output_file_path = filedialog.asksaveasfilename(
        title="Save Output As",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not output_file_path:
        print("Output save cancelled.")
        
    else:
        with open(output_file_path, "w") as output_file:
            if input_option == 2:
                output_file.write("\nGenerated Matrix:\n")
                for row in matrix:
                    output_file.write(' '.join(row) + "\n")
                output_file.write("\nGenerated sequences and rewards:\n")
                for sequence, reward in generated_sequences:
                    output_file.write(f"{sequence}\n{reward}\n")
                output_file.write("\n")
            output_file.write(str(highest_score) + "\n")
            if best_series is not None:
                output_file.write(" ".join(best_series) + "\n")
            else:
                output_file.write("No series found.\n")
            if best_coordinates is not None:
                for coordinates in best_coordinates:
                    output_file.write(f"{coordinates[1] + 1}, {coordinates[0] + 1}\n")
            else:
                output_file.write("No coordinates found.\n")
            output_file.write(f"{int((end_time - start_time) * 1000)} ms\n")

        print(f"Output saved to {output_file_path}")
