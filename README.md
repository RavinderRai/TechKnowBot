# Tech Know Bot

A chatbot to help in deciding what electronic device to purchase, using a dataset of youtube reviews and related videos.


Project Outline with Vector Database Integration

1. Project Overview
Develop an AI chatbot for an e-commerce platform that can recommend products, answer queries, provide personalized shopping assistance using multiple LLMs, and summarize product reviews. The chatbot will leverage YouTube closed captions (CC) for video reviews to enhance product recommendations and provide summaries. The project will include LLMOps tracking using Comet LLM and a small dashboard for monitoring model performance. It will be a B2C micro SaaS, incorporating affiliate links for monetization. A vector database will be used to store and manage the CC text data.

2. Architecture
Frontend: A web interface built using Streamlit.
Backend: AWS services for handling chatbot logic, data storage, processing, analytics, summarization, and LLMOps tracking.
Vector Database: Store and manage YouTube CC text data for efficient search and retrieval.

3. Tools and Services
Amazon SageMaker: Train and deploy LLMs for product recommendation, NER, sentiment analysis, and summarization.
Amazon Lex: Build the conversational interface for the chatbot.
Amazon Comprehend: Analyze customer sentiments and queries.
Amazon RDS/Aurora: Store product information and customer data.
Amazon Lambda: Integrate various services and handle backend logic.
Amazon API Gateway: Expose the chatbot API.
Amazon S3: Store product images, CC texts, and other static assets.
AWS Step Functions: Orchestrate workflows.
YouTube API: Collect closed captions (CC) from video reviews.
Comet LLM: Track LLM experiments, monitor performance, and manage LLMOps.
Vector Database: Use a vector database like Pinecone, Milvus, or Weaviate to store and manage CC text embeddings.

4. Implementation Steps
Step 1: Data Collection and Preparation
YouTube API Integration: Use the YouTube API to collect CC texts for videos.
Initial Search: Query for "top ten laptops" to collect batch data.
Common Laptops Identification: Analyze the CC texts to find the most common laptops mentioned.
Specific Reviews Search: Perform another search for detailed reviews on each identified laptop.
Data Storage: Store the collected CC texts and metadata in S3 or an RDS database.
Step 2: Vector Database Setup
Choose a Vector Database: Select a vector database like Pinecone, Milvus, or Weaviate.
Vectorization: Convert the CC texts into embeddings using a pre-trained model (e.g., BERT, Sentence-BERT).
Store Embeddings: Store the embeddings in the vector database along with metadata.
Step 3: Summarization and Additional Models
Prepare Summarization Dataset: Manually create summary pairs for a subset of the collected CC texts to fine-tune the model.
Train the Summarization Model: Fine-tune a summarization model on the CC text and summary pairs using Amazon SageMaker.
Additional Models: Train and deploy models for product recommendation, NER, and sentiment analysis.
Step 4: Build the Conversational Interface
Amazon Lex Setup: Create a Lex bot with intents for various user queries like product recommendations, general inquiries, customer support, product analytics, and review summaries.
Intent Training: Train the Lex bot with example phrases and responses.
Lambda Functions: Create Lambda functions to handle Lex intent fulfillment by querying the summarization model deployed on SageMaker.
Step 5: Integrate and Deploy the System
Backend Integration: Use Lambda functions to integrate Lex with SageMaker, RDS, the vector database, and other necessary services.
API Gateway Setup: Expose the chatbot functionalities through API Gateway.
Streamlit Development: Develop a web app interface using Streamlit for the chatbot, allowing users to interact, request product analytics, and view summaries.
Step 6: Add Summarization and Vector Search Functionality
Summarization Requests: Implement a feature in the Streamlit app for users to request summaries of product reviews.
Vector Search: Use the vector database to perform semantic search on CC texts to find relevant reviews and information.
Summary Presentation: Display the summaries in a user-friendly manner within the Streamlit app.
Step 7: Enhance Functionality with Sentiment Analysis and NER
Amazon Comprehend: Use Comprehend to analyze customer sentiments from chat interactions.
NER and Sentiment Analysis: Perform NER and sentiment analysis on the summarized reviews to highlight key features and sentiments.
Step 8: Test and Optimize
Testing: Conduct thorough testing of the chatbot’s functionalities and interactions.
Optimization: Optimize the system for performance, scalability, and accuracy.
Step 9: Monitor and Maintain
Monitoring: Set up monitoring for the chatbot using AWS CloudWatch.
Continuous Improvement: Regularly update the model and chatbot logic based on new data and user feedback.
Step 10: LLMOps Dashboard
Comet LLM Dashboard: Develop a dashboard to monitor LLM performance, track experiments, and visualize metrics using Comet LLM.
Dashboard Integration: Integrate the Comet LLM dashboard with the Streamlit app for easy access to model performance metrics.