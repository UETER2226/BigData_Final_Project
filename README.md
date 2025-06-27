# BigData_Final_Project
![image](https://github.com/user-attachments/assets/1c5d9daf-3854-4572-8dbc-950aa7edcaf4)

Đây là một chatbot đơn giản được tạo bởi Elasticsearch, LangChain và một số LLM API cùng với data của riêng bạn
## Demo
https://github.com/user-attachments/assets/cb668f4f-87e1-4898-917c-410838a464db
## Download the Project
Tải project về từ github
```bash
git clone https://github.com/UETER2226/BigData_Final_Project.git
```

## Installing and connecting to Elasticsearch

### Install Elasticsearch
Cài đặt elastic cloud và lấy một key api để lưu trữ dữ liệu của bạn. Xem thêm [tại đây](https://www.elastic.co/cloud)

### Connect to Elasticsearch
Kết nối với Elasticsearch của bạn bằng cách cài đặt các biến môi trường sau:
```sh
ELASTIC_CLOUD_ID="your_elastic_cloud_id"
ELASTIC_API_KEY="your_elastic_api_key"
```
## Connecting to LLM
Để sử dụng các LLM api, bạn cũng cần phải cài đặt các biến môi trường

Các tiểu mục sau đây định nghĩa các yêu cầu cấu hình của từng LLM được hỗ trợ.

### OpenAI
Để sử dụng OpenAI LLM, bạn sẽ cần cung cấp khóa OpenAI thông qua biến môi trường `OPENAI_API_KEY`:

```sh
LLM_TYPE=openai
OPENAI_API_KEY=...
```

Bạn có thể lấy OpenAI API tại [OpenAI dashboard](https://platform.openai.com/account/api-keys).

### Azure OpenAI

Nếu bạn muốn sử dụng Azure LLM, bạn hãy cài đặt các biến môi trường sau

```sh
LLM_TYPE=azure
OPENAI_VERSION=... # e.g. 2023-05-15
OPENAI_BASE_URL=...
OPENAI_API_KEY=...
OPENAI_ENGINE=... # deployment name in Azure
```

### Bedrock LLM

Để sử dụng Bedrock LLM, bạn cần thiết lập các biến môi trường sau để xác thực với AWS.

```sh
LLM_TYPE=bedrock
AWS_ACCESS_KEY=...
AWS_SECRET_KEY=...
AWS_REGION=... # e.g. us-east-1
AWS_MODEL_ID=... # Default is anthropic.claude-v2
```


### Vertex AI

Để sử dụng Vertex AI, bạn cần thiết lập các biến môi trường sau. Thông tin thêm [tại đây](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm).

```sh
LLM_TYPE=vertex
VERTEX_PROJECT_ID=<gcp-project-id>
VERTEX_REGION=<gcp-region> # Default is us-central1
GOOGLE_APPLICATION_CREDENTIALS=<path-json-service-account>
```

### Mistral AI

Để sử dụng Mistral AI, bạn cần thiết lập các biến môi trường sau. Ứng dụng đã được thử nghiệm với Mistral Large Model được triển khai thông qua Microsoft Azure. Thông tin [thêm](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-mistral).

```
LLM_TYPE=mistral
MISTRAL_API_KEY=...
MISTRAL_API_ENDPOINT=...  # should be of the form https://<endpoint>.<region>.inference.ai.azure.com
MISTRAL_MODEL=...  # optional
```

### Cohere

Để sử dụng Cohere bạn cần thiết lập các biến môi trường sau:

```
LLM_TYPE=cohere
COHERE_API_KEY=...
COHERE_MODEL=...  # optional
```

 ## Running the App
Cài đặt các thư viện cần thiết

 ```sh
pip install -r requirements.txt

```
 Chạy lệnh sau để index data của bạn và đưa lên elasticsearch
 ```sh
flask create-index
```

chạy chương trình
 ```sh
flask run
```

