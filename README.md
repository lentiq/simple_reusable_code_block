# simple_reusable_code_block
Really simple reusable code block example using python, based on Lentiq's data science image.

To build:
```bash
docker build -t simple_reusable_code_block .
```

To test:
```bash
docker run -it -e OUTPUT_DIR="/tmp/output.parquet" -v /tmp:/tmp simple_reusable_code_block:latest
```

To push:
```bash
docker login
docker tag simple_reusable_code_block <your_id>/reusable_code_block_test
docker push
```
