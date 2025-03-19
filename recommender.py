import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import joblib
import os

class RecommendationSystem:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = StandardScaler()
        self.model = None
        self.data = None
        
    def load_data(self, file_path):
        """Load and preprocess the dataset"""
        try:
            self.data = pd.read_csv(file_path)
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def preprocess_data(self):
        """Preprocess the data for recommendation"""
        if self.data is None:
            return False
        
        # Combine relevant features into a single text column
        self.data['combined_features'] = self.data.apply(
            lambda x: ' '.join(x.astype(str)), axis=1
        )
        
        # Create TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(self.data['combined_features'])
        
        # Calculate cosine similarity
        self.model = cosine_similarity(tfidf_matrix)
        
        return True
    
    def get_recommendations(self, item_id, n_recommendations=5):
        """Get recommendations for a specific item"""
        if self.model is None:
            return []
        
        try:
            # Get the index of the item
            idx = self.data[self.data['id'] == item_id].index[0]
            
            # Get similarity scores
            similarity_scores = list(enumerate(self.model[idx]))
            
            # Sort items based on similarity scores
            similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
            
            # Get top N recommendations
            recommendations = []
            for i, score in similarity_scores[1:n_recommendations+1]:
                recommendations.append({
                    'id': self.data.iloc[i]['id'],
                    'title': self.data.iloc[i]['title'],
                    'similarity_score': float(score)
                })
            
            return recommendations
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            return []
    
    def save_model(self, model_path):
        """Save the trained model"""
        try:
            joblib.dump({
                'vectorizer': self.vectorizer,
                'model': self.model,
                'data': self.data
            }, model_path)
            return True
        except Exception as e:
            print(f"Error saving model: {e}")
            return False
    
    def load_model(self, model_path):
        """Load a trained model"""
        try:
            saved_model = joblib.load(model_path)
            self.vectorizer = saved_model['vectorizer']
            self.model = saved_model['model']
            self.data = saved_model['data']
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False 