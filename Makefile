build:
	docker-compose build ris-image
run:
	docker-compose up --scale ris-image=0
send:
	docker-compose run ris-image python -m ris_4.scripts.send_word $(word)
