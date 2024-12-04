class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person_inf in people:
        person = Person(person_inf["name"], person_inf["age"])
        persons.append(person)

    for person_inf in people:
        person = Person.people[person_inf["name"]]
        if person_inf.get("wife"):
            person.wife = Person.people[person_inf["wife"]]
        if person_inf.get("husband"):
            person.husband = Person.people[person_inf["husband"]]

    return persons
