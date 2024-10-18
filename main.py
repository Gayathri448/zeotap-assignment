from rule_engine import create_rule, combine_rules, evaluate_rule
from weather_monitor import fetch_weather_data, process_weather_data, calculate_daily_aggregates, check_thresholds

def main():
    print("Select application to run: ")
    print("1. Rule Engine with AST")
    print("2. Weather Monitoring System")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        # Rule Engine with AST
        print("Running Rule Engine with AST...")
        rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        
        # Create ASTs from rules
        ast1 = create_rule(rule1)
        ast2 = create_rule(rule2)
        
        # Combine ASTs
        combined_ast = combine_rules([ast1, ast2])
        
        # Sample user data
        user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        
        # Evaluate rule
        result = evaluate_rule(combined_ast, user_data)
        print(f"User eligibility result: {result}")

    elif choice == '2':
        # Weather Monitoring System
        print("Running Weather Monitoring System...")
        cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
        api_key = "your_openweather_api_key"

        for city in cities:
            weather_data = fetch_weather_data(city, api_key)
            processed_data = process_weather_data(weather_data)
            print(f"Processed data for {city}: {processed_data}")
        
        # Simulate daily weather data for rollups
        daily_data = [
            {"temp": 35, "condition": "Clear"},
            {"temp": 34, "condition": "Rain"},
            {"temp": 36, "condition": "Clear"},
        ]
        
        daily_summary = calculate_daily_aggregates(daily_data)
        print(f"Daily Weather Summary: {daily_summary}")
        
        # Check thresholds
        check_thresholds(daily_summary['max_temp'], threshold=35)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
