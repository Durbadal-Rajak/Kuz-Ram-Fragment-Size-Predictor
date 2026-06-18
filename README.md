⛏️ Kuz-Ram Fragment Size Predictor

A Python + Streamlit web application for predicting blast fragmentation using the Kuz-Ram model and Rosin-Rammler distribution.

📌 Overview

This project estimates the mean fragment size generated after blasting and visualizes the fragment size distribution curve.
It also calculates key fragmentation parameters such as P20, P50, and P80 and classifies blast quality.

✨ Features

- Mean fragment size prediction using the Kuz-Ram equation
- Rosin-Rammler particle size distribution
- Interactive Streamlit web interface
- P20, P50, and P80 calculation
- Fragmentation curve visualization
- Blast quality classification
- Real-time parameter adjustment

🛠 Tech Stack

- Python
- Streamlit
- NumPy
- Matplotlib

📂 Project Structure

KuzRam_Fragment_Predictor
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/KuzRam_Fragment_Predictor.git

Navigate to the project folder

cd KuzRam_Fragment_Predictor

Create a virtual environment

python -m venv venv

Activate the virtual environment

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

---

📥 Inputs

- Rock Factor (A)
- Rock Volume per Hole (V)
- Explosive Charge per Hole (Q)

📤 Outputs

- Mean Fragment Size
- P20
- P50
- P80
- Rosin-Rammler Distribution Curve
- Fragmentation Quality Assessment

📈 Example Output

- Interactive fragmentation curve
- P20, P50, and P80 values
- Blast quality verdict:
  - Good Fragmentation ✅
  - Coarse Fragmentation ⚠️
  - Very Coarse Fragmentation ❌

🚀 Future Improvements

- Additional blast design parameters
- CSV data upload support
- Export results to Excel
- Multiple blast scenario comparison
- Machine learning-based fragmentation prediction
- Deployment on Streamlit Community Cloud

📚 Theory Used

Kuz-Ram Model

Predicts the mean fragment size generated after blasting.

Rosin-Rammler Distribution

Models the particle size distribution and allows estimation of P20, P50, and P80 values.

👨‍💻 Author
Durbadal Rajak 
Mining Engineering Student
IIEST, SHIBPUR
