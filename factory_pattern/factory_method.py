import json
import xml.etree.ElementTree as etree
import sqlite3


class Config:
    def __init__(self, json_path: str = 'data/movies.json', xml_path: str = 'data/person.xml',
                 sq3_path: str = 'data/person.sq3') -> None:
        self.json_path = json_path
        self.xml_path = xml_path
        self.sq3_path = sq3_path


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f: self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


class SQ3DataExtractor:
    def __init__(self, filepath) -> None:
        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()

    @property
    def parsed_data(self):
        return self.cursor

    def __del__(self) -> None:
        self.conn.close()


def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    elif filepath.endswith('sq3'):
        extractor = SQ3DataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main() -> None:
    config = Config()

    # json
    print("JSON")
    json_factory = extract_data_from(config.json_path)
    json_data = json_factory.parsed_data
    print(f"Received data type {type(json_data)}")
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()

    # xml
    print("XML")
    xml_factory = extract_data_from(config.xml_path)
    xml_data = xml_factory.parsed_data
    print(f"Received data type {type(xml_data)}")
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text)
         for p in liar.find('phoneNumbers')]
        print()

    # sq3
    print("SQ3")
    sqlite_factory = extract_data_from(config.sq3_path)
    sqlite_data = sqlite_factory.parsed_data
    print(f"Received data type {type(sqlite_data)}")
    sqlite_data.execute("SELECT id, firstName, lastName FROM persons WHERE lastName = 'Liar'")
    liars = sqlite_data.fetchall()
    print(f'found: {len(liars)} persons')
    for person in liars:
        person_id, firstname, lastname = person
        print(f'first name: {firstname}')
        print(f'last name: {lastname}')

        sqlite_data.execute("SELECT type, number FROM phoneNumbers WHERE person_id = ?", (person_id,))
        phone_numbers = sqlite_data.fetchall()

        for phone_type, phone_number in phone_numbers:
            print(f"phone number ({phone_type}): {phone_number}")
        print()


if __name__ == "__main__":
    main()
