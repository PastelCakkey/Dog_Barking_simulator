import random
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    # Create labels and text fields for the number of dogs and the probability of barking
    num_dogs_label = QLabel("Number of dogs:")
    self.num_dogs_field = QLineEdit()
    prob_label = QLabel("Probability of barking (0-1):")
    self.prob_field = QLineEdit()

    # Create a button to run the simulation
    self.simulate_button = QPushButton("Simulate")
    self.simulate_button.clicked.connect(self.run_simulation)

    # Create a vertical layout to hold the UI elements
    layout = QVBoxLayout()
    layout.addWidget(num_dogs_label)
    layout.addWidget(self.num_dogs_field)
    layout.addWidget(prob_label)
    layout.addWidget(self.prob_field)
    layout.addWidget(self.simulate_button)

    # Set the layout for the main window
    self.setLayout(layout)

  def run_simulation(self):
    # Get the number of dogs and probability of barking from the text fields
    num_dogs = int(self.num_dogs_field.text())
    prob = float(self.prob_field.text())

    # Initialize lists to store dog data
    dog_names = []
    barking_data = []

    # Loop through each dog
    for i in range(num_dogs):
      # Generate a random number between 0 and 1
      bark = random.random()

      # If the random number is less than the probability of barking, the dog will bark
      if bark < prob:
        barking_data.append(1)
      else:
        barking_data.append(0)

      # Store the dog's name and breed in the list of dog names
      dog_names.append("Dog {}".format(i+1))

    # Create a scatter plot showing which dogs barked
    plt.scatter(range(len(dog_names)), barking_data)

    # Add labels for the dog names and breeds
    plt.xticks(range(len(dog_names)), dog_names, rotation=90)

    # Add more space to the x-axis to avoid overlap
    plt.subplots_adjust(bottom=0.25)

    # Create a FigureCanvas object to display the chart in the GUI
    self.canvas = FigureCanvas(plt.gcf())

    # Add the FigureCanvas object to the layout
    self.layout().addWidget(self.canvas)

if __name__ == '__main__':
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec_()
