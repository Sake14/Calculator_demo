from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML шаблон прямо в коде
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Простой калькулятор</title>
    <style>
        body { font-family: Arial; max-width: 400px; margin: 0 auto; padding: 20px; }
        input, button { padding: 8px; margin: 5px; font-size: 16px; }
        .result { font-size: 20px; color: green; }
    </style>
</head>
<body>
    <h2>Калькулятор</h2>
    <form method="POST">
        <input type="text" name="expression" placeholder="2+2" required>
        <button type="submit">=</button>
    </form>
    {% if result is not none %}
    <div class="result">Результат: {{ result }}</div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            # Безопасное вычисление выражения
            expression = request.form['expression']
            result = eval(expression, {'__builtins__': None}, {})
        except:
            result = "Ошибка в выражении"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
