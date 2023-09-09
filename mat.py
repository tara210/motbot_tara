from flask import Flask, render_template, request, jsonify, send_file, url_for
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

app = Flask(__name__)

sp.init_printing()

# Define the chatbot responses
def chatbot_response(user_input):
    # Check for keywords in user input
    if "solve" in user_input:
        # Extract the equation from user input
        equation = user_input.replace("solve", "")
        try:
            x = sp.symbols('x')
            equation = sp.sympify(equation)
            solutions = sp.solve(equation, x)
            response = f"Solutions: {sp.pretty(solutions)}"
        except Exception as e:
            response = f"Error: {str(e)} enter valid expression in the format x**2 + 2x + 3"
    
    elif "differentiate" in user_input:
        # Extract the expression from user input
        expression = user_input.replace("differentiate", "")
        try:
            x = sp.symbols('x')
            expression = sp.sympify(expression)
            derivative = sp.diff(expression, x)
            response = f"Derivative: {sp.pretty(derivative)}"
        except Exception as e:
            response = f"Error: {str(e)}"
    
    elif "integrate" in user_input:
        # Extract the expression from user input
        expression = user_input.replace("integrate", "")
        try:
            x = sp.symbols('x')
            expression = sp.sympify(expression)
            integral = sp.integrate(expression, x)
            response = f"Integral: {sp.pretty(integral)}"
        except Exception as e:
            response = f"Error: {str(e)}"
    
    else:
        response = "I'm sorry, I can only solve, differentiate, or integrate. Please provide a valid prompt."

    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def process():
    user_message = request.args.get('msg')  # Get the user's input

    
    response = chatbot_response(user_message)
    return jsonify({"response": response})
    

if __name__ == "__main__":
    app.run(debug=True)

