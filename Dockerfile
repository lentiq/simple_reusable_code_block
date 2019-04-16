FROM bigstepinc/jupyter_bdl:2.4.1-1

RUN mkdir -p /myapp
ADD /myapp /myapp
RUN rm -f /opt/spark-2.4.1-bin-hadoop2.7/jars/guava-14*

ENTRYPOINT /opt/conda/bin/python /myapp/my_test_program.py
