# Recommendation System with Web Interface

A robust recommendation system with a modern web interface built using Python and Flask.

## Features

- Content-based recommendation system using TF-IDF and cosine similarity
- Modern and responsive web interface
- Easy-to-use API endpoints
- Support for custom datasets
- Real-time recommendations

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Recommendations_System
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Upgrade pip to the latest version:
```bash
python -m pip install --upgrade pip
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

If you encounter any installation issues, you can try installing packages one by one:
```bash
pip install numpy
pip install pandas
pip install scikit-learn
pip install flask
pip install flask-wtf
pip install python-dotenv
pip install gunicorn
pip install jupyter
pip install matplotlib
pip install seaborn
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Load your dataset:
   - Enter the path to your CSV dataset in the "Dataset Path" field
   - Click "Load Data" to process the dataset

4. Get recommendations:
   - Enter an item ID in the "Item ID" field
   - Click "Get Recommendations" to see similar items

## Dataset Format

Your dataset should be a CSV file with the following columns:
- `id`: Unique identifier for each item
- `title`: Title or name of the item
- Additional features that will be used for recommendations

## API Endpoints

- `POST /load_data`: Load and process a new dataset
- `POST /recommend`: Get recommendations for a specific item ID

## Troubleshooting

If you encounter any installation issues:

1. Make sure you have the latest version of pip:
```bash
python -m pip install --upgrade pip
```

2. Install setuptools first:
```bash
pip install --upgrade setuptools wheel
```

3. If you still have issues, try creating a new virtual environment with Python 3.11:
```bash
python3.11 -m venv venv
```

## Contributing

Feel free to submit issues and enhancement requests!