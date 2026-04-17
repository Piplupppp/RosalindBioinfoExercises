# Rosalind RNA: transcribe DNA into RNA


def transcribe(t):
    return t.replace("T","U")



def main():
    t = input("Insert a DNA sequence: ")
    print(transcribe(t))


if __name__ == "__main__":
    main()