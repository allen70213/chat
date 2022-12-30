#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#轉格式
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

#寫入檔案
def write_file(filename, chat):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for lines in chat:
            f.write(lines + '\n')

def main():
    filename = 'input.txt'
    lines = read_file(filename)
    chat = convert(lines)
    write_file('output.txt', chat)

main()