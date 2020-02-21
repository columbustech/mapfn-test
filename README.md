## How to use this repo to create a map function container

1. Clone this repo.
2. Replace src/foo/process.py with your custon process.py file.
3. Add any additional libraries you use in process.py to requirements.txt.
4. Install docker.
5. Build the container from the root directory of the repo:
  `docker build -t IMAGE_NAME .`
6. Push the image to docker hub (or some other container registry).
7. Give the image url to the sm-mapper app on Columbus.
