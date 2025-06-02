class ExcelSheetColumnNumber:
    number_map = {'A':1,'B':2,'C':3,'D':4}
    max_alphabets = 26

    def __init__(self, column_name):
        self.column_name = column_name
        
    def convert_to_number(self):
        column_number = 0
        for i in range(len(self.column_name)):
            column_number = column_number * self.max_alphabets + self.number_map[self.column_name[i]]
        return column_number

    

if __name__ == "__main__":
    column_name = 'BA'
    converter = ExcelSheetColumnNumber(column_name)
    print (converter.convert_to_number())

    

