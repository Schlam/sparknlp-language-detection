import os

# Install java
get_ipython().system(' apt-get update -qq')
get_ipython().system(' apt-get install -y openjdk-8-jdk-headless -qq > /dev/null')

# Setup environment
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
get_ipython().system(' java -version')

# Install pyspark
get_ipython().system(' pip install --ignore-installed pyspark==2.4.4')
# Install Spark NLP
get_ipython().system(' pip install --ignore-installed spark-nlp==2.6.2')
