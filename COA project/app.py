from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Conversion functions with validation
def binary_to_decimal(binary_str):
    if re.fullmatch(r"[01]+", binary_str):
        return str(int(binary_str, 2))
    return "Invalid binary input"

def binary_to_octal(binary_str):
    if re.fullmatch(r"[01]+", binary_str):
        return oct(int(binary_str, 2))[2:]
    return "Invalid binary input"

def binary_to_hexadecimal(binary_str):
    if re.fullmatch(r"[01]+", binary_str):
        return hex(int(binary_str, 2))[2:].upper()
    return "Invalid binary input"

def decimal_to_binary(decimal_num):
    if re.fullmatch(r"\d+", decimal_num):
        return bin(int(decimal_num))[2:]
    return "Invalid decimal input"

def decimal_to_octal(decimal_num):
    if re.fullmatch(r"\d+", decimal_num):
        return oct(int(decimal_num))[2:]
    return "Invalid decimal input"

def decimal_to_hexadecimal(decimal_num):
    if re.fullmatch(r"\d+", decimal_num):
        return hex(int(decimal_num))[2:].upper()
    return "Invalid decimal input"

def octal_to_binary(octal_str):
    if re.fullmatch(r"[0-7]+", octal_str):
        return bin(int(octal_str, 8))[2:]
    return "Invalid octal input"

def octal_to_decimal(octal_str):
    if re.fullmatch(r"[0-7]+", octal_str):
        return str(int(octal_str, 8))
    return "Invalid octal input"

def octal_to_hexadecimal(octal_str):
    if re.fullmatch(r"[0-7]+", octal_str):
        return hex(int(octal_str, 8))[2:].upper()
    return "Invalid octal input"

def hexadecimal_to_binary(hex_str):
    if re.fullmatch(r"[0-9A-Fa-f]+", hex_str):
        return bin(int(hex_str, 16))[2:]
    return "Invalid hexadecimal input"

def hexadecimal_to_decimal(hex_str):
    if re.fullmatch(r"[0-9A-Fa-f]+", hex_str):
        return str(int(hex_str, 16))
    return "Invalid hexadecimal input"

def hexadecimal_to_octal(hex_str):
    if re.fullmatch(r"[0-9A-Fa-f]+", hex_str):
        return oct(int(hex_str, 16))[2:]
    return "Invalid hexadecimal input"

# Route for main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle conversions
@app.route('/conversion', methods=['POST'])
def conversion():
    data = request.get_json()
    from_choice = data.get("fromChoice")
    to_choice = data.get("toChoice")
    input_number = data.get("inputNumber")

    try:
        # Conversion logic based on from_choice and to_choice
        if from_choice == '1':  # Binary
            if to_choice == '2':  # Binary to Decimal
                result = binary_to_decimal(input_number)
            elif to_choice == '3':  # Binary to Octal
                result = binary_to_octal(input_number)
            elif to_choice == '4':  # Binary to Hexadecimal
                result = binary_to_hexadecimal(input_number)
            else:
                result = "Conversion not supported"

        elif from_choice == '2':  # Decimal
            if to_choice == '1':  # Decimal to Binary
                result = decimal_to_binary(input_number)
            elif to_choice == '3':  # Decimal to Octal
                result = decimal_to_octal(input_number)
            elif to_choice == '4':  # Decimal to Hexadecimal
                result = decimal_to_hexadecimal(input_number)
            else:
                result = "Conversion not supported"

        elif from_choice == '3':  # Octal
            if to_choice == '1':  # Octal to Binary
                result = octal_to_binary(input_number)
            elif to_choice == '2':  # Octal to Decimal
                result = octal_to_decimal(input_number)
            elif to_choice == '4':  # Octal to Hexadecimal
                result = octal_to_hexadecimal(input_number)
            else:
                result = "Conversion not supported"

        elif from_choice == '4':  # Hexadecimal
            if to_choice == '1':  # Hexadecimal to Binary
                result = hexadecimal_to_binary(input_number)
            elif to_choice == '2':  # Hexadecimal to Decimal
                result = hexadecimal_to_decimal(input_number)
            elif to_choice == '3':  # Hexadecimal to Octal
                result = hexadecimal_to_octal(input_number)
            else:
                result = "Conversion not supported"

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": "Error: " + str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
