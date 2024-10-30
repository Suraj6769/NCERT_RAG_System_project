import os
from dotenv import load_dotenv
import pinecone

# Load environment variables
load_dotenv()

# Pinecone API Setup
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

def query_vector_db(query):
    """
    Query Pinecone VectorDB with the given query.
    """
    # Assuming you have an index in Pinecone
    index = pinecone.Index("your-index-name")

    # Example of querying Pinecone
    result = index.query(queries=[query], top_k=10)

    return result
