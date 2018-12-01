#FROM twalter/openshift-nginx
FROM nginx:stable

RUN rm -rf /etc/nginx/conf.d/
COPY nginx-config/app /etc/nginx/conf.d/app.conf

# support running as arbitrary user which belogs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

# users are not allowed to listen on priviliged ports
#RUN sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf
RUN sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/app.conf

# comment user directive as master process is run as user in OpenShift anyhow
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf

EXPOSE 8081

#RUN ls -l -R /usr/share/nginx/html/
#RUN ls /etc/nginx/conf.d/
#RUN nginx -T

#RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
#USER appuser