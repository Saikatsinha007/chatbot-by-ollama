# Medical Chatbot with AI and Semantic Search

This repository contains the code and resources for a **Medical Chatbot** built using **Hugging Face's T5 model** and **Ollama model** for natural language processing, **Pinecone** for semantic search, and **Streamlit** for web deployment. The chatbot provides contextually accurate and real-time responses for medical consultations.

---

## 🚀 Features

- **NLP Model**: Utilizes Hugging Face’s **T5 model**, fine-tuned on medical data for domain-specific queries and responses.
- **Query Handling**: Capable of processing up to **5 queries per minute** with the **Ollama model**.
- **Semantic Search**: Uses **Pinecone** to index **5,086 embeddings** for fast, contextually relevant search with retrieval times under **300 ms**.
- **Performance Metrics**: 
  - Accuracy: **0.85**
  - Precision: **0.87**
  - Recall: **0.83**
  - F1-score: **0.85**
  - BLEU score: **0.82** for quality assurance in response generation.
- **Deployment**: Deployed as a user-friendly web app using **Streamlit**.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   .\env\Scripts\activate   # For Windows
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏗️ Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open the app** in your browser at `http://localhost:8501`.

3. **Interact with the chatbot** by entering medical queries. The chatbot will return relevant responses based on the fine-tuned T5 model and semantic search.

---

## 📊 Model Architecture

- **Hugging Face T5 Model**: Fine-tuned for medical consultation data to provide domain-specific responses.
- **Ollama Model**: Integrated for query handling and improved response time.
- **Pinecone**: Used for embedding storage and semantic search for fast, relevant information retrieval.
  
The combined architecture ensures fast and contextually relevant medical responses.

---

## ⚡ Performance Evaluation

- **Accuracy**: 0.85  
- **Precision**: 0.87  
- **Recall**: 0.83  
- **F1-score**: 0.85  
- **BLEU score**: 0.82  

These metrics demonstrate the chatbot’s ability to provide accurate, relevant, and understandable responses.

---

## 🌐 Deployment

The chatbot is deployed using **Streamlit**, offering an intuitive web interface. Pinecone integration ensures quick retrieval of embeddings and responses.

---

## 🛡️ Limitations and Disclaimers

- **Medical Advice**: The chatbot is designed for informational purposes and should not be used as a substitute for professional medical advice.
- **Performance**: While the chatbot achieves high accuracy, it is not 100% error-proof.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For any questions or feedback, please reach out to Saikat Sinha at saikatsinha21@gmail.com.
