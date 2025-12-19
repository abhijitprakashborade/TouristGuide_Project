from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from app.models import Place

class ContentBasedRecommender:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        
    def get_recommendations(self, place_id, limit=5):
        # 1. Fetch all places
        places = Place.query.all()
        if not places:
            return []
            
        # 2. Create DataFrame
        data = [{'id': p.id, 'description': p.description} for p in places]
        df = pd.DataFrame(data)
        
        # 3. Compute TF-IDF Matrix
        tfidf_matrix = self.tfidf.fit_transform(df['description'])
        
        # 4. Compute Similarity
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
        # 5. Get indices
        indices = pd.Series(df.index, index=df['id']).drop_duplicates()
        if place_id not in indices:
            return []
            
        idx = indices[place_id]
        
        # 6. Get pairwise similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:limit+1]
        
        # 7. Get place indices
        place_indices = [i[0] for i in sim_scores]
        
        # 8. Return recommended places
        return [places[i] for i in place_indices]
    
    def recommend_by_preferences(self, preferences):
        """
        Future implementation: Recommending based on user keywords/tags.
        """
        pass
