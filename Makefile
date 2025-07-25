default: all
all: clean resources zip
clean:
	rm -f landlab_algorithm_provider/resources.py
	rm -f landlab_algorithm_provider.zip
resources:
	pyrcc5 -o landlab_algorithm_provider/resources.py  landlab_algorithm_provider/resources.qrc
zip:
	zip -r landlab_algorithm_provider.zip landlab_algorithm_provider
