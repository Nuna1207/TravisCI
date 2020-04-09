import unittest
import re

def check_info(file):
    lines = file.readlines()
    print('Contain file: ')
    print('_________________________________________________________')
    for line in lines:
        print(line)
    print('__________________________________________________________')
    print("Check info: ")
    for line in lines:
        sub_lines = line.split(r"|")
        for sub_line in sub_lines:
            if re.match(r"[A-Z a-z]", sub_line):
                email = re.sub(r"@@", "@", sub_line).replace(' ', '')
                print(email)
            if sub_line.startswith("+"):
                number = re.sub(r" ", "", sub_line)
                digits = number.replace('+', '')
                if (len(digits) == 11):
                    code = '(' + digits[1:4] + ")" + '-' + digits[4:7] + '-' + digits[7:9] + '-' + digits[9:11]
                    new_num = '+' + digits[0:1] + code
                    print(sub_line + " change " + new_num)
            elif re.match(r"[А-Я][а-я]+[А-Я]", sub_line):
                fio = sub_line.replace("", " ")
                print(fio)

file = open('info.txt', "r", encoding='utf-8')
lines = check_info(file)
print(lines)
file.close()
class check_info(unittest.TestCase):

    def test_normal(self):
       print("test passed")
    def tearDown(self):
        print("some text")
if __name__=='__main__':
    unittest.main()