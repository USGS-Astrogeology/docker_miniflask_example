FROM usgsastro/miniflask
WORKDIR /app
VOLUME /app
EXPOSE 80

# Potentially install other dependencies
RUN conda install -c conda-forge pvl

CMD ["python", "app.py"]
