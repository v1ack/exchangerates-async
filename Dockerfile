# base image

# Сборочный контейнер для приложения
FROM snakepacker/python:all as builder_app
RUN python3.7 -m venv /usr/share/python3/app
ADD requirements.txt /tmp/
RUN /usr/share/python3/app/bin/pip install --no-cache-dir -Ur /tmp/requirements.txt
ENV PATH="/usr/share/python3/app/bin:${PATH}"

########################################################################
# Image with app installed
FROM snakepacker/python:3.7 as app
COPY --from=builder_app /usr/share/python3/app /usr/share/python3/app 
ADD exchanges_rates/ /mnt/exchanges_rates/
ADD app.py /mnt/

SHELL ["/bin/bash", "-c"]
WORKDIR /mnt

EXPOSE 8080

CMD ["/usr/share/python3/app/bin/python3", "/mnt/app.py"]