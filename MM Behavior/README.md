# ABA Therapy Learning Rate Web App

This web application is designed to help visualize the relationship between the rate of learning (R) and the amount of experience or exposure to stimuli (E) in the context of Applied Behavior Analysis (ABA) therapy. It uses an adapted version of the Michaelis-Menten equation to model this relationship.

## Equation

The adapted equation used in this web app is:

R = (R_max * [E]) / (K_b + [E])

Where:
- R: Rate of learning
- R_max: Maximum possible rate of learning or improvement for a specific behavior or skill
- E: Amount of experience or exposure to stimuli
- K_b: Constant that indicates the amount of experience required for the learning rate to reach half of its maximum value

How to Use:

Download all the necessary files from the repository.

Open the command line or terminal and navigate to the folder where you downloaded the files.

Install the required dependencies by running:

pip install -r requirements.txt

Start the Flask app by executing:

python app.py

Open your web browser and visit http://127.0.0.1:5000/ to access the web app.

Enter the R_max, K_b, E_min, and E_max values in the corresponding input fields, and click the "Calculate" button.

The web app will display a graph illustrating the relationship between the rate of learning (R) and the amount of experience (E) based on your input values.

## License

This project is open source and available under the MIT License. See the `LICENSE` file for more information.
