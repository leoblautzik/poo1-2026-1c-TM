def main():
    verduras = ["papa", "zapallo", "radicheta"]

    try:
        print(verduras[3])
    except IndexError:
        print("Fijate lo que estas escribiendo, papá!!")


if __name__ == "__main__":
    main()
