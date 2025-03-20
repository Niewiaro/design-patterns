import sqlite3
import xml.etree.ElementTree as ET


class Config:
    def __init__(self, xml_path: str = 'person.xml', sq3_path: str = 'person.sq3') -> None:
        self.xml_path = xml_path
        self.sq3_path = sq3_path


def xml_parse(path: str):
    tree = ET.parse(path)
    root = tree.getroot()
    return root


def sq3_push_xml_data(path: str, root):
    # Połączenie z bazą SQLite
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Tworzenie tabel
    cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        age INTEGER,
        streetAddress TEXT,
        city TEXT,
        state TEXT,
        postalCode TEXT,
        gender TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS phoneNumbers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER,
        type TEXT,
        number TEXT,
        FOREIGN KEY (person_id) REFERENCES persons(id)
    )''')

    # Wstawianie danych
    for person in root.findall('person'):
        firstName = person.find('firstName').text
        lastName = person.find('lastName').text
        age = int(person.find('age').text)
        address = person.find('address')
        streetAddress = address.find('streetAddress').text
        city = address.find('city').text
        state = address.find('state').text
        postalCode = address.find('postalCode').text
        gender = person.find('gender/type').text

        cursor.execute(
            "INSERT INTO persons (firstName, lastName, age, streetAddress, city, state, postalCode, gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (firstName, lastName, age, streetAddress, city, state, postalCode, gender))

        person_id = cursor.lastrowid

        for phone in person.find('phoneNumbers').findall('phoneNumber'):
            phone_type = phone.get('type')
            phone_number = phone.text
            cursor.execute("INSERT INTO phoneNumbers (person_id, type, number) VALUES (?, ?, ?)",
                           (person_id, phone_type, phone_number))

    # Zapisanie zmian i zamknięcie bazy
    conn.commit()
    conn.close()


def main() -> None:
    config = Config()
    root = xml_parse(config.xml_path)
    sq3_push_xml_data(config.sq3_path, root)


if __name__ == "__main__":
    main()
