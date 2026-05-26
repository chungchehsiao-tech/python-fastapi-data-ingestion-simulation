FROM python:3.9-slim

#non-root user
RUN groupadd -r localgroup && useradd -r -g localgroup localuser

WORKDIR /app

#install dependency as root user before change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code and change the ownership 
COPY --chown=localuser:localgroup . .

USER localuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]