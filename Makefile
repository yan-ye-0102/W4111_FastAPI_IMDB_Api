dev-shell:
	python3 -m venv venv;
	source venv/bin/activate && exec bash;
install-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt
