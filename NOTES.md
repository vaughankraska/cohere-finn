## Output After running `make first-run`
```bash
✅ Your .env file has been set up.
🎉 You're all set up! You can now run 'make migrate' and 'make dev' to start the Cohere Toolkit. Make sure Docker is running.
📚 Here are some examples to get you started:
1. Navigate to the Cohere Toolkit frontend: 
	http://localhost:4000
2. Ask a question to the Cohere Platform model
	curl --location 'http://localhost:8000/v1/chat-stream' --header 'User-Id: test-user' --header 'Content-Type: application/json' --data '{"message": "hey"}'
3. Ask a question to the SageMaker model
	curl --location 'http://localhost:8000/v1/chat-stream' --header 'User-Id: test-user' --header 'Deployment-Name: SageMaker' --header 'Content-Type: application/json' --data '{"message": "hey"}'
4. List all available models deployments and their models
	curl http://localhost:8000/deployments
For more examples, please visit the Cohere Toolkit README.md
make migrate
docker compose run --build backend alembic -c src/backend/alembic.ini upgrade head
[+] Running 10/10
...
```

## Settings >> tools (ready to use)
Can be controlled/created and destroyed by using src/community/tools

# TODO: learning
- Add vector extension to pg 14 using the `DB_EXTENSION` env var
- Add own model to talk to + client provider for frontend
* install model(s)
* uncomment lines at community/config/deployments and set model path
* add model labels in class in local_model.py
* (from comments) To use local models install poetry with: poetry install --with setup,community,local-model --verbose
* LEFTOFF err:
Exception ignored in: <function Llama.__del__ at 0xffff77ead120>
AttributeError: 'Llama' object has no attribute '_stack'
- Figure out how to choose agents
- Figure out how to configure connectors (some already exist)
- Explore backend
- Figure out how the codegen happens from the api to frontend
