
def main():
    mass = int(input("Enter mass in kilograms: "))
    energy = mass * (3.0 * 10 ** 8) ** 2
    print(
        f"The equivalent energy in Joules is: {int(energy / 10 ** 8)} * 10 ^ 8 ")


if __name__ == "__main__":
    main()
