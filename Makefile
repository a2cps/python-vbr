API ?= https://a2cps.tapis.io
USERNAME ?= $(A2CPS_USERNAME)
PASSWORD ?= $(A2CPS_PASSWORD)

deps:
	pip install pytest flake8 yapf

lint: deps
	# stop the build if there are Python syntax errors or undefined names
	flake8 src/vbr --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src/vbr --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

pytest: deps
	python -m pytest

tests: lint pytest

reformat:
	yapf -i --recursive src/vbr

classfiles-clean:
	cd src ; python -m scripts.redcap_classfiles clean

classfiles: classfiles-clean
	cd src ; python -m scripts.redcap_classfiles build

definitions:
	cd src ; python -m scripts.definitions; mv -f *.json  ../files/

definitions-clean:
	rm -f files/*.json

clean: definitions-clean

create_tables:
	cd src ; python -m scripts.create_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

drop_tables:
	cd src ; python -m scripts.drop_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

bootstrap_tables:
	cd src ; python -m scripts.bootstrap_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

export_tables: 
	cd src ; python -m scripts.export_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

import_tables: 
	cd src ; python -m scripts.import_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

export_tables-clean:
	cd exports; rm *.csv

clean_tables:
	cd src; echo "Cleaning: $(SCRIPT_ARGS)"

reset: drop_tables create_tables load_tables
