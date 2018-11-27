git add .
IF NOT [%1]==[] (git commit -m "%1") ELSE (git commit -m "%COMPUTERNAME% commit with OS %OS%")

git push

s2i build https://github.com/silvaBrian987/facebook_django_mock.git centos/python-36-centos7 facebook-django-mock

REM docker login registry.starter-ca-central-1.openshift.com -u $(oc whoami) -p $(oc whoami -t)

docker tag facebook-django-mock registry.starter-ca-central-1.openshift.com/sku/facebook-django-mock:latest

docker push registry.starter-ca-central-1.openshift.com/sku/facebook-django-mock:latest