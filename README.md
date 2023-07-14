# ChatGPT-with-documents

The **ChatGPT-with-documents** is a tool designed to simplify the process of accessing relevant information within an organization. This tool eliminates the need to manually sift through numerous documents, providing a fast, efficient, and conversational way to retrieve information. The project draws inspiration from the [`openai/chatgpt-retrieval-plugin`](https://github.com/openai/chatgpt-retrieval-plugin) and [`jerryjliu/llama_index`](https://github.com/jerryjliu/llama_index)
 repositories.

⚠️ Please note that this project is the result of dedicated work by budding developers and may contain some bugs. It is an experimental project primarily designed for learning and exploration purposes. Detailed instructions are provided, and you can always seek help if you have any questions or issues. 🐛

**Co-Authored By:**
- [SHINYOONCHAN](mailto:tlsdbscks123@gmail.com) ✨
- [vlqhel3440](mailto:vlqhel3440@naver.com) ✨
- [changchangwoo](mailto:changchangwoo@naver.com) ✨

## Key Features

- **Rapid Information Retrieval:** Quickly access the information you need by efficiently searching through the documents.
- **Convenient Interaction:** Interact with the system in a chatbot-like manner, asking questions in natural language and receiving prompt and accurate responses.
- **Enhanced Productivity:** Save time and effort, leading to a significant boost in work efficiency.
- **Consistent Information Provision:** Receive consistent and reliable information every time.

## Development Environment

The project is built using **Python version 3.11.4** and utilizes **Flask** for crafting the web application. It takes advantage of **Pinecone** and **MySQL8** for data management.

## Local Setup and Usage

Note: This setup guide is based on instructions from the [openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) with some modifications.


To run the program locally, follow the instructions below:

1. Make sure **Python version 3.10 or higher** is installed.
2. Clone the source files from [here](repository URL).
3. Navigate to the cloned directory and install **Poetry** using pip.
4. Create and activate a new **Python 3.10 virtual environment**.
5. Install all dependencies with **Poetry**.
6. Set the required environment variables for the datastore, Bearer Token, and OpenAI API Key.
7. Set the environment variables for the Pinecone Vector DB.
8. **Run the API** locally.
9. Navigate to the **Flask server directory**, install the necessary packages, and configure MySQL settings as per server.py.
10. **Run the Flask server**.

## Administrator Page Usage

Admins have access to the following features on the administrator page:

- **File Upload:** Upload and manage files.
- **Set Model:** Configure and manage models.
- **Search & Verify:** Perform searches and verify results.

## Client Page Usage

Clients can interact with the chatbot on the client page by following these steps:

1. **Select a category.** 📂
2. **Ask questions** in natural language. ❓
3. **Receive responses** based on the internal documents related to the chosen category. 📝

We welcome contributions! Feel free to submit a pull request. 👋

---
