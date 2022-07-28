from CsvToSepaXml import CsvToSepaXML

def main():
    converter = CsvToSepaXML()
    xml = converter.generate_xml("test.csv")
    with open("test_chris.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    main()