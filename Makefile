build:
	nikola build
run:
	nikola serve --browser firefox

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
