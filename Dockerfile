FROM usgsastro/miniflask
WORKDIR /app
VOLUME /app
EXPOSE 80

CMD ["python", "app.py"]
