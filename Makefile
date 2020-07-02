build:
	nikola build

run:
	nikola serve --browser chromium-browser 

deploy:
	nikola github_deploy
	
new:
	nikola new_post -2

clean:
	rm -vfr ./cache ./output
	#nikola check --clean-files

create:
	nikola init --demo lanyon-port

tmpl:
	nikola theme -c base_helper.tmpl
	nikola theme -c base.tmpl

theme:	
	nikola theme -n lanyon --parent base --engine mako
	nikola theme -n purecss --parent bootstrap4 --engine mako

install:
	pip install nikola
	pip install ghp-import2
	pip install typogrify
	pip install pygal
	pip install pyphen

virutalenv:
	pip install --user virtualenv
	virtualenv -p $$(which python3) ~/website


