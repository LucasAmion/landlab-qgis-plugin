default: all
all: clean resources zip
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	rm -f landlab_algorithm_provider/resources.py
	rm -f landlab_algorithm_provider.zip
resources:
	pyrcc5 -o landlab_algorithm_provider/resources.py  landlab_algorithm_provider/resources.qrc
zip:
	zip -r landlab_algorithm_provider.zip landlab_algorithm_provider
