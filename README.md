To execute the code

> python3 -m venv airflow-venv
> pip3 install apache-airflow
> airflow db migrate
> airflow web server -p 8080 & airflow scheduler &

Additional Commands
> Airflow users list
> airflow users delete -u <user-name>

Kill servers running on port:
  sudo lsof -i : <port_num>
  kill -9 <pid>


Set it to False to not to load any example DAGs on airflow
  Airflow.cfg
  # Variable: AIRFLOW__CORE__LOAD_EXAMPLES
  #
  load_examples = False

Ideal way to shutdown AIRFLOW
  pkill -f "airflow scheduler"
  OR
  ps aux | grep "airflow scheduler"
  kill <PID>

  pkill -f "airflow webserver"
  OR
  ps aux | grep "airflow webserver"
  kill <PID>

  (Optional)
  pkill -f "airflow celery"

