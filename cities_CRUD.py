import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    while True:
        # Display menu
        print("\nCities Database Operations")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population")
        print("5. Display average population")
        print("6. Display city with highest population")
        print("7. Display city with lowest population")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            display_cities_sorted(cur, ascending=True)
        elif choice == '2':
            display_cities_sorted(cur, ascending=False)
        elif choice == '3':
            display_cities_sorted_by_name(cur)
        elif choice == '4':
            display_total_population(cur)
        elif choice == '5':
            display_average_population(cur)
        elif choice == '6':
            display_city_with_extreme_population(cur, highest=True)
        elif choice == '7':
            display_city_with_extreme_population(cur, highest=False)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    # Close the connection
    conn.close()


def display_cities_sorted(cur, ascending=True):
    order = 'ASC' if ascending else 'DESC'
    cur.execute(f"SELECT CityName, Population FROM Cities ORDER BY Population {order}")
    results = cur.fetchall()
    print(f"\n{'City':20}Population")
    print("-" * 30)
    for city, pop in results:
        print(f"{city:20}{pop:,}")


def display_cities_sorted_by_name(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName ASC")
    results = cur.fetchall()
    print(f"\n{'City':20}Population")
    print("-" * 30)
    for city, pop in results:
        print(f"{city:20}{pop:,}")


def display_total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    total = cur.fetchone()[0]
    print(f"\nTotal population of all cities: {total:,}")


def display_average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    avg = cur.fetchone()[0]
    print(f"\nAverage population of all cities: {avg:,.0f}")


def display_city_with_extreme_population(cur, highest=True):
    if highest:
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
        desc = "highest"
    else:
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
        desc = "lowest"
    city, pop = cur.fetchone()
    print(f"\nCity with {desc} population: {city} ({pop:,})")


if __name__ == '__main__':
    main()
