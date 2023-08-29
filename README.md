# Learning Rate Web App

This web application is designed to help visualize the relationship between the rate of learning (R) and the amount of experience or exposure to stimuli (E) in the context of Applied Behavior Analysis (ABA) therapy.  This is a toy model approximating this relationship and should not be used clinically, as it has not been researched! It uses an adapted version of the Michaelis-Menten equation (a la enzyme kinetics from biochemistry) to model this relationship.

## Equation

The adapted equation used in this web app is:

R = (R_max * [E]) / (K_b + [E])

Where:
- R: Rate of learning
- R_max: Maximum possible rate of learning or improvement for a specific behavior or skill
- E: Amount of experience or exposure to stimuli
- K_b: Constant that indicates the amount of experience required for the learning rate to reach half of its maximum value

## How to Use

1. Install the required dependencies:

pip install -r requirements.txt

2. Run the Flask app:

python app.py

3. Open your web browser and go to `http://127.0.0.1:5000/` to access the web app.

4. Input the R_max, K_b, E_min, and E_max values, and click the "Calculate" button. The web app will generate a graph that displays the relationship between the rate of learning (R) and the amount of experience (E) based on the provided values.

## License

This project is open source and available under the MIT License. See the `LICENSE` file for more information.
