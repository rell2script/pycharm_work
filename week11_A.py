from pathlib import Path

file_path= Path("student_info.txt")
file_path.write_text("Name: Tom \nCourse: Introduction to computer science \nfavorite programming language: python \ncurrent semester: fall 2026 ")
read_file = file_path.read_text()
print(read_file)