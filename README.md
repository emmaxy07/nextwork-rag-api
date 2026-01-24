<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-api)

**Author:** Emmanuel Iyare  
**Email:** emmanueliyare7@gmail.com

---

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_g3h4i5j6)

---

## Introducing Today's Project!

In this project, I will demonstrate how to build a RAG API with FastAPI. I'm doing this project to learn how to build an LLM-styled platform which I will eventually deploy to Kubernetes.

### Key services and concepts

Services I used were:
- RAG API
- Fast API
- Chroma DB
- Swagger UI
- Ollama

 Key concepts I learnt include how to setup and write the RAG API using Fast API, how to setup Ollama, how to setup Chroma DB to store my knowledge base, and how to test the api with Swagger UI.

### Challenges and wins

This project took me approximately one hour. It was most rewarding to my api respond with the correct answer to the question I asked it in an LLM-style.

### Why I did this project

I did this project because I want to learn how to build LLM-based APIs and deploy them to the internet.

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama. Python is the programming language I will use to write this API. Ollama is a tool that runs AI machines locally on my computer. I need these tools because RAG API needs them both to be able to run.

### Python and Ollama setup

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is an LLM tool that runs locally on my computer.  I downloaded the tinyllama model because it is is an AI model that contains everything the AI needs to understand and generate text. The model will help my RAG API such that when I run Ollama commands, it uses this model to answer my questions.

---

## Setting Up a Python Workspace

In this step, I'm setting up a Python workspace. I need it because I need to write the RAG API using Python's FastAPI framework.

### Python workspace setup

### Virtual environment

A virtual environment is an isolated Python environment that keeps your project's dependencies separate from other Python projects on your computer.
Without a virtual environment, installing packages for one project could break another project that needs a different version. A virtual environment makes sure each project has its own set of packages, preventing conflicts.
I created one for this project to handle the development of my FastAPI. 
To create a virtual environment, I ran the command: python -m venv venv

### Dependencies

The packages I installed are:
- chromadb
- fastapi
- ollama
- uvicorn
FastAPI web framework helps us build APIs quickly. Think of it as a toolkit that handles all the networking and routing logic (like complex HTTP request/response), so we can focus on writing the actual RAG func.
Chroma is used for storing document embeddings (numerical representations of text). When a user asks a question, ChromaDB searches through these embeddings to find the most relevant documents, which is the "Retrieval" part of RAG.. 
Uvicorn is used for running the FastAPI app and makes it accessible locally on your computer (or on the internet). When you start your API, uvicorn listens for incoming requests on your local machine and routes them to the right functions in your code. 
Ollama is a Python client library that lets your code talk to Ollama. While you can use Ollama from the command line, this package gives your Python API a way to send questions to tinyllama and get responses programmatically.

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base. A knowledge base is a what contains all the information that will be searched for using the RAG API. 

### Knowledge base setup

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are numerical representations of text that capture meaning. Words with similar meanings are placed close together, while unrelated words are far apart. For example, "container" and "Docker" would have embeddings that are mathematically similar. This allows the computer to understand relationships between words based on their meaning, not just spelling. 

I created them by running my embed.py script. The db/ folder contains my knowledge base's embeddings so Chroma can quickly search through them when my API is running.

This is important for RAG because it needs to be able to search the knowledge base in an efficient manner which in this case is the Embedding.

---

## Building the RAG API

In this step, I'm building a RAG API. An API is lets software retrieve and share data with other apps. For example, when you use a travel app to see flight prices, the app uses airline APIs to request up-to-date prices and display them for you. 

FastAPI is a Python client library that is used to write APIs based in python code. It's designed to be fast, easy to use, and automatically generates interactive documentation.

I'm creating this because I need it to write the RAG API. FastAPI takes care of a lot of this background work for you: it handles how requests come in and go out, checks if incoming information is correct, and returns answers in the right format. This means engineers can focus on describing what should happen rather than all the complicated communication and data handling rules that usually go into building an API.

### FastAPI setup

### How the RAG API works

My RAG API works by:
(i) Question arrives: Someone sends a question to my API at /query
(ii) Search my documents: Chroma searches through your knowledge base to find text that matches the question's meaning
(iii) Get matching text: Chroma returns the most relevant information from your documents (this is called "context")
(iv) Generate answer: The question and the matching text are sent together to tinyllama, which creates an answer
(v) Send back the answer: The answer is sent back to whoever asked the question

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using Swagger UI. 
Swagger UI is an automatically generated, interactive documentation page for your FastAPI server. 
It lets you visually explore your API's endpoints, see what parameters they accept, and even try them out right from your browser - no special tools or coding required. 

### Testing the API

### API query breakdown

I queried my API by running the command: Invoke-RestMethod -Uri "http://127.0.0.1:8000/query?q=What is Kubernetes?" -Method Post

The command uses the POST method, which means my question was sent as a post to the RAG API. The API responded with: "Kubernetes (pronounced "cuben-trays") is a container orchestration platform that uses Kubern..."

![Image](http://learn.nextwork.org/refreshed_maroon_agile_abiu/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI is an automatically generated, interactive documentation page for your FastAPI server. 
It lets you visually explore your API's endpoints, see what parameters they accept, and even try them out right from your browser - no special tools or coding required. 

I used it to test my RAG API implementation by putting the question: "What is Kubernetes?" inot the query input field. The best part about using Swagger UI was it was seamless to use to test the API.

---

## Adding Dynamic Content

### Adding the /add endpoint

### Dynamic content endpoint working

---

---
