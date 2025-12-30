import sys

def greet(name):
    return f"hello, {name}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        print("hello,stranger")
2222222222222222
