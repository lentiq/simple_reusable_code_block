FROM bigstepinc/jupyter_bdl:2.4.1-1

RUN mkdir -p /myapp
ADD /myapp /myapp
ADD /codeblock-entrypoint.sh /codeblock-entrypoint.sh

ENTRYPOINT /codeblock-entrypoint.sh /myapp/my_test_program.py
