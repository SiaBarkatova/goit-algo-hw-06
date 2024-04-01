from collections import UserDict
import re

class Field: # base class to store all values
    def __init__(self, value):
        self.value = value

    def __str__(self): 
        return str(self.value)

class Name(Field): 
    def __init__(self, name=None): # redifine field's init to make name required
        if not name: 
            raise ValueError
        super().__init__(name) 

class Phone(Field):
    def __init__(self, phone):
        pattern = '^\d{10}$' # the phone must be 10 digits
        is_phone = re.match(pattern, phone)
 
        if not is_phone:
            raise ValueError
        super().__init__(phone)	

class Record: 
    def __init__(self, name):
        self.name = Name(name) # create base fields
        self.phones = []

    def add_phone(self, phone):
        for ph in self.phones: 
            if ph.value == phone: # do not need to add if already exists
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones: 
            if ph.value == phone:
                self.phones.remove(ph)
                return
        raise ValueError # raise error if no such phone found
    
    def edit_phone(self, old_phone, new_phone):
        for ph in self.phones: 
            if ph.value == old_phone:
                ph.value = new_phone # update phone value 
                return
        raise ValueError # raise error if no such phone found
    
    def find_phone(self, phone):
        for ph in self.phones: 
            if ph.value == phone:
                return ph.value
        raise ValueError # raise error if no such phone found

    def __str__(self): # converting obj to a printable string
        return f"Contact name: {self.name}, phones: {'; '.join(ph.value for ph in self.phones)}"

class AddressBook(UserDict): # extending functionality of a standard dict
    def add_record(self, record: Record): # adding record. name as key, Record obj as value
        name = record.name.value
        self.data[name] = record # {'Ihor': Record('Ihor')}

    def find(self, name) -> Record: # find record by name
        return self.get(name) 
    
    def delete(self, name):
        del self[name]
    


# creating address book
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

janee_record = Record("Janee")
janee_record.add_phone("1234567890")
janee_record.add_phone("9872102345")
book.add_record(janee_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)