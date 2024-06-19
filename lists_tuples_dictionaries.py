# Array types: lists, tuples, dictionaries

# lists
people_to_meet = [" hi", "Akxa", "Sean", "Baby Luv", "Jovi", "one"]
print(people_to_meet)
print(people_to_meet[0])
print(len(people_to_meet))
people_to_meet.remove("one")
print(people_to_meet)
people_to_meet.append("Alex")
people_to_meet.append("Hupe")
print(people_to_meet)
person = people_to_meet.pop()
person2 = people_to_meet.pop()
print(person)
print(person2)
print(people_to_meet[1:])
print(people_to_meet[:2])

num = [3, 6, 9, 16]
print(min(num))
print(max(num))
print(sum(num))

# tuples
driver = ("Akxa", "BMW", "2003")
print(driver)
print(driver.count("Akxa"))

point = (1.5, 2.0)
point2 = (-1.5, 2.0)
graph = [point, point2]
print(graph)
graph.append((3.0, 16.0))
print(graph)

# dictionaries
students = {110: "Akxa",
            111: "Sean",
            112: "Baby",
            113: "Jovi"}
print(students)
print(students[110])
