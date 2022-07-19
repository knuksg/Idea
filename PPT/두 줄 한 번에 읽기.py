def main():
    try:
        f = open('result.txt', 'r')  # 'r' is optional
        while True:
            line = f.readline()
            if not line: break    
            print(line.strip('\n'), end=' ')
            line = f.readline()
            print(line.strip('\n'))  # Read first line
    except IOError:
        print('There was an error opening the file!')
        return
 
 
if __name__ == '__main__':
    main()