from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "data-eng",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="daily_elt",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2025,1,1),
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="meltano_extract",
        bash_command="cd ~/projects/training-kit/training-meltano && meltano elt tap-csv target-postgres"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /home/sathya/projects/training-kit && dbt run --profiles-dir /home/sathya/projects/training-kit"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /home/sathya/projects/training-kit && dbt test --profiles-dir /home/sathya/projects/training-kit"
    )

    extract >> dbt_run >> dbt_test
