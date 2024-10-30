def calculator(query):
    try:
        if "add" in query:
            numbers = [float(n) for n in query.split() if n.replace('.', '', 1).isdigit()]
            result = sum(numbers)
            return f"The result of adding {numbers} is {result}"
        
        elif "subtract" in query:
            numbers = [float(n) for n in query.split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] - numbers[1]
            return f"The result of subtracting {numbers[1]} from {numbers[0]} is {result}"
        
        elif "multiply" in query:
            numbers = [float(n) for n in query.split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] * numbers[1]
            return f"The result of multiplying {numbers[0]} and {numbers[1]} is {result}"
        
        elif "divide" in query:
            numbers = [float(n) for n in query.split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] / numbers[1] if numbers[1] != 0 else "undefined"
            return f"The result of dividing {numbers[0]} by {numbers[1]} is {result}"
        
        else:
            return "Sorry, I can only help with basic arithmetic: add, subtract, multiply, or divide."
    
    except Exception as e:
        return f"Error in calculation: {str(e)}"
