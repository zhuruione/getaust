def gethead(file):
    with open(file, 'r', encoding='utf-8') as head:
        lines = head.readlines()
        headers = {}
        for line in lines:
            if line.startswith(':'):
                line=line[1:]
            index = line.find(':', 1, len(line))
            headers[line[0:index]] = line[index + 1:len(line) - 1]
        return headers