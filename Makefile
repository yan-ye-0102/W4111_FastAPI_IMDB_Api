dev-shell:
	python3 -m venv venv;
	source venv/bin/activate && exec bash;
format:
	isort resources
	black resources
	isort tts
	black tts
install-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt
