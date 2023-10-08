import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
nltk.download('stopwords')

english_stopwords = set(stopwords.words('english'))

def refined_sentence(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    filtered_words = [word for word in words if word.lower() not in english_stopwords]
    return ' '.join(filtered_words)

def query_similarity(text1, text2):
    text1 = refined_sentence(text1)
    text2 = refined_sentence(text2)
    tfidf_vectorizer = TfidfVectorizer()

    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return cosine_sim[0][0]

def jac_sim(sent1, sent2):
    stemmer = PorterStemmer()
    stemmed_tokens1 = [stemmer.stem(word) for word in refined_sentence(sent1)]
    stemmed_tokens2 = [stemmer.stem(word) for word in refined_sentence(sent2)]
    intersection = len(set(stemmed_tokens1).intersection(stemmed_tokens2))
    union = len(set(stemmed_tokens1).union(stemmed_tokens2))
    jaccard_similarity = intersection / union if union != 0 else 0

    return jaccard_similarity

def project_similarity_score(project, query):
    title_score = query_similarity(project['title'], query)
    desc_score = query_similarity(project['description'], query) * 0.5
    summary_score = query_similarity(project['summary'], query) * 0.5
    jac_similarity = jac_sim(project['title'], query)
    
    return title_score + desc_score + summary_score + jac_similarity * 0.25

def sort_and_return_projects(projects, query: str, k=3):
    project_scores = []
    for project in projects:
        score = project_similarity_score(project, query)
        project_dict = {
            'id': project['id'],
            'stacks': project['stacks'],
            'domains': project['domains'],
            'links': project['links'],
            'title': project['title'],
            'description': project['description'],
            'summary': project['summary'],
            'level': project['level'],
            'github_uri': project['github_uri'],
            'contributor_count': project['contributor_count'],
            'score': score
        }
        project_scores.append(project_dict)
    
    sorted_projects = sorted(project_scores, key=lambda x: x['score'], reverse=True)
    
    # We remove the 'score' key before returning the projects
    for project in sorted_projects:
        del project['score']
    
    return sorted_projects[:k]

projects = [
    {
        "id": 40,
        "stacks": [
            {
                "id": 1,
                "name": "HTML"
            }
        ],
        "domains": [
            {
                "id": 1,
                "name": "Physics"
            }
        ],
        "links": [
            {
                "id": 6,
                "title": "linkedin",
                "url": "https://linkedin.com/in/sampleuser"
            }
        ],
        "title": "Sample Project",
        "description": "This is a sample project description.",
        "summary": "This is a sample summary.",
        "level": "intermediate",
        "github_uri": "https://github.com/sampleuser/sampleproject",
        "contributor_count": 2
    },
    {
        "id": 41,
        "stacks": [
            {
                "id": 1,
                "name": "HTML"
            }
        ],
        "domains": [
            {
                "id": 1,
                "name": "Physics"
            }
        ],
        "links": [
            {
                "id": 7,
                "title": "linkedin",
                "url": "https://linkedin.com/in/sampleuser"
            }
        ],
        "title": "Hello World",
        "description": "This is a description.",
        "summary": "This is a summary.",
        "level": "intermediate",
        "github_uri": "https://github.com/sampleuser/sampleproject",
        "contributor_count": 0
    }
]

print(sort_and_return_projects(projects=projects, query="World"))
