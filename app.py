from flask import Flask, request, render_template, redirect, url_for
from promethee import promethee_ranking

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['POST'])
def recommendation():
    alternatives = request.form.getlist('alternatives[]')
    if len(alternatives) < 2:
        return "Minimal 2 alternatif diperlukan.", 400
    return render_template('recommendation.html', alternatives=alternatives)

@app.route('/calculate_promethee', methods=['POST'])
def calculate_promethee():
    alternatives = request.form.getlist('alternatives[]')
    criteria = ['biaya', 'waktu', 'kebutuhan', 'dampak', 'frekuensi']
    
    criteria_data = []
    for alt in alternatives:
        alt_data = []
        for criterion in criteria:
            value = request.form.get(f"{alt}_{criterion}", "3")
            try:
                alt_data.append(int(value))
            except ValueError:
                alt_data.append(3)
        criteria_data.append(alt_data)

    results = promethee_ranking(alternatives, criteria_data)
    
    return render_template('promethee_result.html', results=results)
if __name__ == '__main__':
    app.run(debug=True)