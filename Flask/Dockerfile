FROM nikolaik/python-nodejs

WORKDIR /flask

ENV FLASK_APP=app.py

RUN npm install -g nodemon

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]