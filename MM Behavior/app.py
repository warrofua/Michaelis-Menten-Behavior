"""
In the context of ABA therapy, the adapted equation could be used to 
model the relationship between the rate of learning (R) and the amount 
of experience or exposure to stimuli (E):

R = (R_max * [E]) / (K_b + [E])

Here, R_max represents the maximum possible rate of learning or improvement 
for a specific behavior or skill, and K_b is a constant that indicates the 
amount of experience required for the learning rate to reach half of its 
maximum value.
"""
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r_max = float(request.form['r_max'])
        k_b = float(request.form['k_b'])
        e_min = float(request.form['e_min'])
        e_max = float(request.form['e_max'])

        e_values = np.linspace(e_min, e_max, 100)
        r_values = (r_max * e_values) / (k_b + e_values)

        plt.plot(e_values, r_values)
        plt.xlabel('Experience (E)')
        plt.ylabel('Rate of Learning (R)')
        plt.title('Learning Rate vs Experience')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()

        plt.clf()

        return render_template('index.html', graph_url=graph_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
