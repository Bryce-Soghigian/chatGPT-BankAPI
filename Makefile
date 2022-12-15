# specify the name of the Docker image to build
IMAGE_NAME = my-app

# specify the port to expose the app on
APP_PORT = 5000

# build the Docker image
build:
	@docker build -t $(IMAGE_NAME) .

# run the Docker container
run:
	@docker run -p $(APP_PORT):$(APP_PORT) $(IMAGE_NAME)

# stop the Docker container
stop:
	@docker container stop $(IMAGE_NAME)

