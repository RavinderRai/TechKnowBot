# Tech Know Bot

A chatbot to help in deciding what electronic device to purchase, using a dataset of youtube reviews and related videos.


Project Outline with Vector Database Integration

## Project Overview
Develop an AI chatbot for an e-commerce platform that can recommend products, answer queries, provide personalized shopping assistance using multiple LLMs, and summarize product reviews. The chatbot will leverage YouTube closed captions (CC) for video reviews to enhance product recommendations and provide summaries. The project will include LLMOps tracking using Comet LLM and a small dashboard for monitoring model performance. It will be a B2C micro SaaS, incorporating affiliate links for monetization. A vector database will be used to store and manage the CC text data.


## Implementation Steps

### Step 1: Data Collection and Preparation
YouTube API Integration: Use the YouTube API to collect CC texts for videos.
Initial Search: Query for "top ten laptops" to collect batch data.
Common Laptops Identification: Analyze the CC texts to find the most common laptops mentioned.
Specific Reviews Search: Perform another search for detailed reviews on each identified laptop.
Data Storage: Store the collected CC texts and metadata in S3 or an RDS database.

### Step 2: ETL with AWS Glue:
Extraction: Use AWS Glue to extract raw data from S3.
Transformation: Clean and preprocess the data using AWS Glue jobs.
Loading: Load the transformed data into a data warehouse like Amazon Redshift or back into S3 for further analysis.

### Step 3: Vector Database Setup
Choose a Vector Database: Select a vector database like Pinecone.
Vectorization: Convert the CC texts into embeddings using a pre-trained model (e.g., BERT, Sentence-BERT).
Store Embeddings: Store the embeddings in the vector database along with metadata.

### Step 4: Summarization and Additional Models
Prepare Summarization Dataset: Manually create summary pairs for a subset of the collected CC texts to fine-tune the model.
Train the Summarization Model: Fine-tune a summarization model on the CC text and summary pairs using Amazon SageMaker.
Product Analysis Dashboard: Use other models for NER and sentiment analysis from Amazon Bedrock, to display aggregated reviews for relevant features.

### Step 5: Build the Chatbot
Amazon Lex Setup: Create a Lex bot with intents for various user queries like product recommendations, general inquiries, customer support, product analytics, and review summaries.
Intent Training: Train the Lex bot with example phrases and responses.
Lambda Functions: Create Lambda functions to handle Lex intent fulfillment by querying the summarization model deployed on SageMaker.

### Step 6: Integrate and Deploy the System
Backend: Integrate Lex, SageMaker, RDS, vector database, Kafka, and other tools using Lambda.
API Gateway: Expose chatbot functionalities.
Streamlit/Reflex: Develop the web app interface for user interactions.
Docker and Kubernetes: Containerize and orchestrate your application.
CI/CD Pipelines: Automate deployment with Jenkins or GitHub Actions.
IaC: Use IaC tools to provision and manage infrastructure.

### Step 7: Add Summarization and Vector Search Functionality
Summarization Requests: Implement a feature in the Streamlit app for users to request summaries of product reviews.
Vector Search: Use the vector database to perform semantic search on CC texts to find relevant reviews and information.
Summary Presentation: Display the summaries in a user-friendly manner within the Streamlit app.

### Step 8: Test and Optimize
Testing: Add unit tests.
Optimization: Optimize the system for performance, scalability, and accuracy.

### Step 9: Monitor and Maintain
Monitoring: Set up monitoring for the chatbot using AWS CloudWatch.
Continuous Improvement: Regularly update the model and chatbot logic based on new data and user feedback.

### Step 10: LLMOps Dashboard
Comet LLM Dashboard: Develop a dashboard to monitor LLM performance, track experiments, and visualize metrics using Comet LLM.
Dashboard Integration: Integrate the Comet LLM dashboard with the Streamlit/Reflex app for easy access to model performance metrics.