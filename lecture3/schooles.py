class Student:
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old, and my score is {self.score}"
        )

    @classmethod
    def make_premium_student(cls, name: str, age: int):
        return cls(name, age, 100)

    @classmethod
    def make_five_student(cls):
        return [
            cls("eko", 20, 90),
            cls("susi", 20, 60),
            cls("joko", 20, 70),
            cls("budi", 20, 80),
            cls("agus", 20, 75),
        ]

    @classmethod
    def make_random_student(cls, jumlah: int):
        import random
        students = []
        for _ in range(jumlah):
            students.append(
                cls(
                    f"student-id-{random.randint(1, 100)}",
                    random.randint(15, 20),
                    random.randint(50, 100),
                )
            )
        return students


class School:
    students: list[Student] = []

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def daftar_siswa(self, student: Student):
        self.students.append(student)
        print(
            f"jumlah siswa di {self.name} sekarang adalah {len(self.students)} baru masuk namanya {student.name}"
        )

    def display_students(self):
        for student in self.students:
            student.introduce()

    def average_score(self):
        total_score = 0
        for student in self.students:
            print(f"calculate score from {student.name} with score {student.score}")
            total_score += student.score
            print(f"total score now: -> {total_score}")
        # total dibagi jumlah
        jumlah_siswa = len(self.students)
        return total_score / jumlah_siswa


stephen = Student.make_premium_student("stephen", 20)


# eko = Student("eko", 20, 90)
# susi = Student("susi", 20, 60)
# joko = Student("joko", 20, 70)
# students: list[Student] = Student.make_random_student(200)
# print(len(students))
# smp_binaraga = School("SMP Binaraga", "Jl. Binaraga No. 1")
# for student in students:
#     smp_binaraga.daftar_siswa(student)
# smp_binaraga.display_students()
# print(f"total score for {smp_binaraga.name} is {smp_binaraga.average_score()}")
# smp_binaraga.daftar_siswa(eko)
# smp_binaraga.daftar_siswa(susi)
# smp_binaraga.display_students()
# print(f"total score for {smp_binaraga.name} is {smp_binaraga.average_score()}")
