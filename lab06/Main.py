import MyLinkedList
import Stos
import Student

my_list = MyLinkedList.MyLinkedList()

# Dodawanie elementów do listy
my_list.append(3)
my_list.append(1)
my_list.append(4)
my_list.append(1)

# Wyświetlanie listy
print("Lista po dodaniu elementów:")
print(my_list)

# Usuwanie elementów z listy
my_list.delete(1)
my_list.delete(5)

# Wyświetlanie listy po usunięciu elementów
print("Lista po usunięciu elementów:")
print(my_list)

# Pobieranie elementów z listy
print("Element o wartości 3:")
print(my_list.get(3))
print("Element o wartości 5:")
print(my_list.get(5))

# Dodawanie kolejnych elementów do listy w sposób posortowany
my_list.append(2)
my_list.append(5)
my_list.append(0, func=lambda x, y: x < y)

# Wyświetlanie listy po dodaniu kolejnych elementów
print("Lista po dodaniu kolejnych elementów:")
print(my_list)

stos = Stos.Stos(3)
stos.push("element1")
stos.push("element2")

print(stos)
print(stos.pop())
print(stos.pop())

print(stos)

student = Student.Student("adam@adamski.com", "adam", "zawadzki")
student2 = Student.Student("bob@bobowski", "bob", "abaccki")
print(student)



