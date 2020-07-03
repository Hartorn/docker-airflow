"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG

# from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

from airflow.operators.docker_operator import DockerOperator
# from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=20),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    "docker_hello",
    catchup=False,
    default_args=default_args,
    schedule_interval=timedelta(1),
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = DockerOperator(
    task_id="hello",
    image="library/hello-world",
    dag=dag,
    cpus=1.0,
    docker_url="tcp://docker:2375",
    force_pull=True
)  # command=None,

#  https://github.com/puckel/docker-airflow/issues/535

# tcp://0.0.0.0:2375
#  https://stackoverflow.com/questions/50253082/broken-dag-no-module-named-docker
# https://airflow.apache.org/docs/stable/_api/airflow/operators/docker_operator/index.html#module-airflow.operators.docker_operator
# (image, api_version=None, command=None, container_name=None, cpus=1.0, docker_url='unix://var/run/docker.sock', environment=None, force_pull=False, mem_limit=None, host_tmp_dir=None, network_mode=None, tls_ca_cert=None, tls_client_cert=None, tls_client_key=None, tls_hostname=None, tls_ssl_version=None, tmp_dir='/tmp/airflow', user=None, volumes=None, working_dir=None, xcom_push=False, xcom_all=False, docker_conn_id=None, dns=None, dns_search=None, auto_remove=False, shm_size=None, tty=False, *args, **kwargs)

# t2 = DockerOperator(task_id="sleep", bash_command="sleep 5", retries=3, dag=dag)

# templated_command = """
#     {% for i in range(5) %}
#         echo "{{ ds }}"
#         echo "{{ macros.ds_add(ds, 7)}}"
#         echo "{{ params.my_param }}"
#     {% endfor %}
# """

# t3 = BashOperator(
#     task_id="templated",
#     bash_command=templated_command,
#     params={"my_param": "Parameter I passed in"},
#     dag=dag,
# )

# t1
# t2.set_upstream(t1)
# t3.set_upstream(t1)
