from hw6 import Name, Phone, Birthday, Record, AddressBook

if __name__ == "__main__":
    ab = AddressBook()
    name = Name("Bill Gates")
    name.value = "Bill Gates"
    record = Record(name)
    phone1 = Phone("2617627334")
    print(name.value)
    print(phone1.value)
    ab.add_record(record)
    record.add_phone(phone1)
    birthday = Birthday("22/07/2023")
    record.birthday = birthday
    print(record.days_to_birthday())