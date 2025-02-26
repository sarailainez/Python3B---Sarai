from population import Population

# Object(Population)
pop = Population()

# Data loaded from CSV file
pop.import_csv("census_population.csv")

# Calculate population changes
biannual_count = pop.biannual_delta()
annual_count = pop.annual_delta()

# Print results
print(f"Increase count - Biannual population: {biannual_count}")
print(f"Increase count - Annual population: {annual_count}")

# City Search
city_name = "New York city, New York"
result = pop.search_by_city(city_name)
print(f"Changes in population for {city_name}: {result}")

# CSV export
pop.export_csv("output_population.csv")
