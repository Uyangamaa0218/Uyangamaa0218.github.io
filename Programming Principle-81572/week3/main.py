# from magic_eight_ball import get_eight_ball_response
# question = input("Ask the Magic Eight Ball a question: ")

# try:
#     if not question.strip():
#         raise ValueError("Question cannot be empty.")
#     answer = get_eight_ball_response()
#     print(f'Magic Eight Ball says: {answer}')
# except ValueError as error:
#     print(error)

# balance = 500.00
# print("welcome to the class Bank")

# while True:
#     print("\n1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     option = input("Choose an option: ")
#     match option:
#         case "1":
#             print(f"Your balance is: ${balance:.2f}")
#         case "2":
#             try:
#                 amount = float(input("Enter deposit amount: "))
#                 if amount <= 0:
#                     raise ValueError("Deposit amount must be positive.")
#                 balance += amount
#                 print(f"Deposit successful")
#                 print(f"New balance: {balance:.2f}")
#             except ValueError as error:
#                 print(f"Error:",error)
#         case "3":
#             try:
#                 amount = float(input("Enter withdrawal amount: "))
#                 if amount <= 0:
#                     raise ValueError("Withdrawal amount must be positive.")
#                 balance -= amount
#                 print(f"Withdrawal successful")
#                 print(f"New balance: {balance:.2f}")
#             except ValueError as error:
#                 print(f"Error:",error)

print("Temperature converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

option = input("Choose an option: ")

try:
    temperature = float(input("Enter the temperature: "))

    match option:
        case "1":
            result = (temperature * 9/5) + 32
            print(f"{temperature} C = {result:.2f}°F")
        case "2":
            result = (temperature - 32) * 5/9
            print(f"{temperature} F = {result:.2f}°C") 

except ValueError as error:
    print("Error",error)