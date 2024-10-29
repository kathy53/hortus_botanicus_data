build:
	docker build -t scraper_p_t .

bash:
# docker run --rm -it -v $(shell pwd):/usr/src/app scraper_p_t /bin/bash
	docker run -it --rm -v $(shell pwd):/usr/src/app --ipc=host --security-opt seccomp=seccomp_profile.json scraper_p_t /bin/bash