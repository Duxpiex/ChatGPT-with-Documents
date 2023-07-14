# ChatGPT-with-documents

The **ChatGPT-with-documents** is a tool designed to simplify the process of accessing relevant information within an organization. This tool eliminates the need to manually sift through numerous documents, providing a fast, efficient, and conversational way to retrieve information. The project draws inspiration from the [`openai/chatgpt-retrieval-plugin`](https://github.com/openai/chatgpt-retrieval-plugin) and [`jerryjliu/llama_index`](https://github.com/jerryjliu/llama_index)
 repositories.

⚠️ Please note that this project is the result of dedicated work by budding developers and may contain some bugs. It is an experimental project primarily designed for learning and exploration purposes. Detailed instructions are provided, and you can always seek help if you have any questions or issues. 🐛

**Co-Authored By:**
- [SHINYOONCHAN](mailto:tlsdbscks123@gmail.com) ✨
- [vlqhel3440](mailto:vlqhel3440@naver.com) ✨
- [changchangwoo](mailto:changchangwoo@naver.com) ✨

**Time to Develop: 2023-06-27 to 2023-07-10**



## Key Features

- **Rapid Information Retrieval:** Quickly access the information you need by efficiently searching through the documents.
- **Convenient Interaction:** Interact with the system in a chatbot-like manner, asking questions in natural language and receiving prompt and accurate responses.
- **Enhanced Productivity:** Save time and effort, leading to a significant boost in work efficiency.
- **Consistent Information Provision:** Receive consistent and reliable information every time.

## Development Environment

The project is built using <code>**Python version 3.11.4**</code> and utilizes <code>**Flask**</code> for crafting the web application. It takes advantage of <code>**Pinecone**</code> and <code>**MySQL8**</code> for data management.

## Local Setup and Usage

Note: This setup guide is based on instructions from the [openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) with some modifications.


To run the program locally, follow the instructions below:

1. Install <code>**Python version 3.10 or higher**</code> if it is not already installed.

2. Clone the source files from <code>**https://github.com/Duxpiex/ChatGPT-with-documents.git**</code>

3. Navigate to the cloned directory and install poetry using pip - <code>**cd/path/to/openai-chatgpt-retrieval-plugin**</code> <code>**pip install poetry**</code>

4. Create and activate a new virtual environment - <code>**poetry env use Python3.10**</code>

5. Activate the virtual environment - <code>**poetry shell**</code>

6. Install all dependencies - <code>**poetry install**</code>

7. Set the required environment variables - <code>**DATASTORE**</code>, <code>**BEARER_TOKEN**</code>, and <code>**OPENAI_API_KEY**</code>

8. Set the environment variables for the Pinecone Vector DB - <code>**PINECONE_API_KEY**</code>, <code>**PINECONE_ENVIRONMENT**</code>, and <code>**PINECONE_INDEX**</code>

9. Run the API locally - <code>**poetry run start**</code>

10. Navigate to the Flask server directory, install the necessary packages - <code>**cd/path/to/flaskserver**</code> <code>**pip install 'required package'**</code>

11. Customize the <code>**set_db()**</code> function in server.py according to your MySQL configuration.

12. Apply the SQL queries.
<pre><code>CREATE TABLE `listdata` (
  `filename` varchar(200) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `updatetime` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `index` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `model` (
  `modelname` varchar(45) DEFAULT NULL,
  `category` varchar(45) NOT NULL,
  PRIMARY KEY (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
</code></pre>


13. Run the Flask server - <code>**flask run**</code>

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
