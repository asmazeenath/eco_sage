🌱 Eco Sage — AI-Powered Environmental Intelligence System

Eco Sage is an AI-powered conversational environmental analysis system designed to understand environmental conditions and provide data-driven insights, risk analysis, and actionable recommendations.

The system combines Streamlit, Google Gemini AI, environmental datasets, a risk analysis engine, and a Retrieval-Augmented Generation (RAG) knowledge layer to generate meaningful environmental reports.

---

🎯 Project Objective

The main objective of Eco Sage is to analyze environmental information such as:

- 🌱 Soil health
- 💧 Water conditions
- 🌡️ Climate conditions
- 🌳 Land use and land cover
- 🦋 Biodiversity
- 🌍 Human environmental impact

Based on the available information, the system identifies environmental risks and generates recommendations for improving ecosystem health.

---

🏗️ System Architecture

                         ┌─────────────────────┐
                         │     Streamlit UI     │
                         │       app.py         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                     ┌──────────────────────────┐
                     │   Environmental Agent     │
                     │ environmental_agent.py    │
                     └────────────┬─────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
      │ Risk Engine  │    │ CSV Dataset  │    │ RAG Layer    │
      │              │    │              │    │              │
      │ Soil         │    │ Environmental│    │ ChromaDB     │
      │ Water        │    │ Soil         │    │ Scientific   │
      │ Climate      │    │ datasets     │    │ Knowledge    │
      │ Land         │    │              │    │              │
      └──────────────┘    └──────────────┘    └──────┬───────┘
                                                     │
                                                     ▼
                                           ┌─────────────────┐
                                           │ Scientific      │
                                           │ Evidence        │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │   Gemini AI     │
                                           │    Reasoning    │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ Environmental   │
                                           │ Report &        │
                                           │ Recommendations │
                                           └─────────────────┘

---

🔄 System Workflow

User Input
    │
    ▼
Streamlit Interface
    │
    ▼
Input Validation
    │
    ▼
Environmental Agent
    │
    ├──► Environmental Dataset
    │
    ├──► Soil Dataset
    │
    ├──► Risk Analysis
    │
    └──► RAG Knowledge Retrieval
              │
              ▼
       Scientific Evidence
              │
              ▼
          Gemini AI
              │
              ▼
    Environmental Analysis
              │
              ▼
     Recommendations
              │
              ▼
       User Report

---

✨ Key Features

1. Conversational Environmental Analysis

Users can provide environmental information using natural language.

Example:

The area has low soil organic carbon, decreasing rainfall,
high temperature and increasing agricultural activity.

Eco Sage analyzes the provided information and generates environmental insights.

---

2. Environmental Risk Analysis

The system evaluates environmental conditions related to:

- Soil
- Water
- Climate
- Land use
- Biodiversity
- Human impact

The risk engine helps identify potentially important environmental conditions before the information is passed to the AI reasoning layer.

---

3. Soil Analysis

Soil-related parameters can include:

- Soil pH
- Organic carbon
- Soil moisture

Example analysis:

Low organic carbon may indicate declining soil quality.
Recommended actions may include increasing organic matter
and reducing excessive soil disturbance.

---

4. Climate Analysis

The system can consider:

- Temperature
- Rainfall
- Humidity
- Seasonal patterns

These parameters can be used to understand environmental stress and ecosystem conditions.

---

5. Land Use Analysis

Eco Sage can analyze different land-use categories such as:

- Forest
- Cropland
- Built-up areas
- Water bodies
- Grassland

Changes in land use can be considered when generating biodiversity and environmental recommendations.

---

6. Biodiversity Analysis

The system considers biodiversity-related information such as:

- Species richness
- Habitat diversity
- Habitat degradation
- Land-use changes

The goal is to provide recommendations that support ecosystem and habitat health.

---

🧠 RAG Layer

Eco Sage uses a Retrieval-Augmented Generation architecture.

The RAG layer connects environmental questions with relevant information stored in the knowledge base.

User Query
     │
     ▼
Retriever
     │
     ▼
ChromaDB
     │
     ▼
Relevant Knowledge
     │
     ▼
Gemini AI
     │
     ▼
Evidence-Based Response

The knowledge base contains environmental information covering topics such as:

knowledge_base/
├── soil_health.txt
├── biodiversity.txt
├── climate.txt
├── agroforestry.txt
└── ecosystem_restoration.txt

This allows the AI system to use relevant environmental knowledge while generating its response.

---

🤖 Gemini AI Reasoning

Gemini AI acts as the reasoning layer of Eco Sage.

The model receives:

1. User environmental input
2. Dataset information
3. Risk analysis results
4. Retrieved environmental knowledge

It then generates:

- Environmental interpretation
- Risk explanation
- Possible causes
- Recommended actions
- Scientific reasoning

---

📊 Dataset

Eco Sage uses structured CSV datasets.

data/
├── environmental dataset.csv
└── soil.csv

Environmental Dataset

The environmental dataset can contain information related to:

- Climate
- Land use
- Biodiversity
- Environmental conditions
- Location
- Time

Soil Dataset

The soil dataset contains soil-related parameters such as:

- Soil pH
- Organic carbon
- Moisture
- Other soil measurements

---

📁 Project Structure

eco_sage/
│
├── app.py
│
├── agents/
│   ├── __init__.py
│   └── environmental_agent.py
│
├── rag/
│   ├── __init__.py
│   ├── ingest.py
│   └── retriever.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
├── data/
│   ├── environmental dataset.csv
│   └── soil.csv
│
├── knowledge_base/
│   ├── soil_health.txt
│   ├── biodiversity.txt
│   ├── climate.txt
│   ├── agroforestry.txt
│   └── ecosystem_restoration.txt
│
├── assets/
│   └── eco_background.jpg
│
├── chroma_db/
│
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md

---

📌 Component Description

Component| Purpose
"app.py"| Streamlit user interface
"environmental_agent.py"| Main AI environmental agent
"ingest.py"| Loads knowledge into the vector database
"retriever.py"| Retrieves relevant environmental knowledge
"validators.py"| Validates user inputs
"environmental dataset.csv"| Environmental structured data
"soil.csv"| Soil information
"knowledge_base/"| Environmental knowledge documents
"chroma_db/"| Vector database
"eco_background.jpg"| Application background
"requirements.txt"| Python dependencies
"runtime.txt"| Deployment Python version
".gitignore"| Files excluded from Git

---

🛠️ Technologies Used

Frontend

Streamlit

Used to build the interactive web interface.

AI Model

Google Gemini

Used for environmental reasoning and natural-language response generation.

RAG

Retrieval-Augmented Generation

Used to retrieve relevant environmental knowledge before generating responses.

Vector Database

ChromaDB

Used to store and retrieve embeddings from the environmental knowledge base.

Programming Language

Python

Data Processing

- Pandas
- NumPy

---

⚙️ Installation

1. Clone the Repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd eco_sage

---

2. Create a Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

---

3. Install Dependencies

pip install -r requirements.txt

---

🔑 API Key Configuration

Eco Sage requires a Google Gemini API key.

Create an environment file:

.env

Add:

GOOGLE_API_KEY=your_api_key_here

Do not upload your API key to GitHub.

Make sure ".env" is included in ".gitignore".

Example:

.env
chroma_db/
__pycache__/
*.pyc

---

🗃️ Build the RAG Knowledge Base

Before running the application, ingest the environmental knowledge documents.

python rag/ingest.py

This creates the local ChromaDB vector database.

The generated database is stored in:

chroma_db/

---

▶️ Run the Application

Start Streamlit using:

streamlit run app.py

The application will open in your browser.

Typical local address:

http://localhost:8501

---

💬 Example User Input

The region has a soil pH of 5.2, low organic carbon,
low moisture, increasing temperature and reduced rainfall.
The surrounding land is mainly agricultural with limited
forest cover.

---

📄 Example Output

Eco Sage can generate a report containing:

Environmental Assessment
Architecture

```text
                         ┌─────────────────────┐
                         │     Streamlit UI     │
                         │   app.py             │
                         └──────────┬──────────┘
                                    │
                                    ▼
                     ┌──────────────────────────┐
                     │ Environmental Agent       │
                     │ environmental_agent.py    │
                     └────────────┬─────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
      │ Risk Engine  │    │ CSV Dataset  │    │ RAG Layer    │
      │              │    │              │    │              │
      │ Soil         │    │ Environmental│    │ ChromaDB     │
      │ Water        │    │ Soil         │    │ Scientific   │
      │ Climate      │    │ datasets     │    │ Knowledge    │
      │ Land         │    │              │    │              │
      └──────────────┘    └──────────────┘    └──────┬───────┘
                                                     │
                                                     ▼
                                           ┌─────────────────┐
                                           │ Scientific      │
                                           │ Evidence       │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ Gemini AI       │
                                           │ Reasoning       │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ Environmental   │
                                           │ Report &        │
                                           │ Recommendations │
                                           └─────────────────

eco_sage/
│
├── app.py
│
├── agents/
│   ├── __init__.py
│   └── environmental_agent.py
│
├── rag/
│   ├── __init__.py
│   ├── ingest.py
│   └── retriever.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
├── data/
│   ├── environmental dataset.csv
│   └── soil.csv
│
├── knowledge_base/
│   ├── soil_health.txt
│   ├── biodiversity.txt
│   ├── climate.txt
│   ├── agroforestry.txt
│   └── ecosystem_restoration.txt
│
├── assets/
│   └── eco_background.jpg
│
├── chroma_db/
│
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md┘
