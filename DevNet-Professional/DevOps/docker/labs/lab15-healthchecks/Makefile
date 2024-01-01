
DOCKER_IMG = net-inventory
DOCKER_TAG = 0.1
PORT_HOST = 5000
PORT_CONTAINER = 5000
CONTAINER_NAME = net-inventory

build:
	docker build -t $(DOCKER_IMG):$(DOCKER_TAG) .

exec:
	docker exec -w /net-inventory -it $(CONTAINER_NAME) bash -c 'flask run --host=0.0.0.0'

start:
	docker start $(CONTAINER_NAME)

run:
	docker run -itd \
	-p $(PORT_HOST):$(PORT_CONTAINER) \
	--name $(CONTAINER_NAME) \
	-v $(PWD):/net_inventory \
	$(DOCKER_IMG):$(DOCKER_TAG)

rebuild:
	docker stop $(CONTAINER_NAME); \
	docker rm $(CONTAINER_NAME); \
	docker rmi $(DOCKER_IMG):$(DOCKER_TAG); \
	make build; \
	make run
