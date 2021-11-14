from container import Container
from sys import argv


def main(args):
    try:
        fin = open(args[0], 'r')
    except:
        print(f'File {args[0]} is unavailable to read from!')
        return

    try:
        fout = open(args[1], 'w+')
    except:
        print(f'File {args[1]} is unavailable to write to!')
        return

    cont = Container.create(fin)
    if cont is None:
        print('Bad input file!')
        fout.write('Bad input file!')
        return

    fout.write('Container before changes:\n')
    cont.write_to_file(fout)
    fout.write('\n')

    cont.remove_lesser_than_average()

    fout.write('Container after changes:\n')
    cont.write_to_file(fout)
    fout.write('\n')

    try:
        fin.close()
        fout.close()
    except:
        pass


if __name__ == '__main__':
    if len(argv) != 3:
        print("Incorrect arguments format!\n", "Correct:\n", "main.py in_file out_file\n", sep='')
    else:
        main(argv[1:])
