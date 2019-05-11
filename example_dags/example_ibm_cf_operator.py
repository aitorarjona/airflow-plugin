# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import airflow
from airflow.operators.ibm_cloud_functions_plugin import IbmCloudFunctionsOperator

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = airflow.models.DAG(
    dag_id='example_ibm_cf_operator',
    default_args=args,
    schedule_interval=None,
)

run_first = IbmCloudFunctionsOperator(
    task_id='my_function_1',
    function_name='my_function',
    function_path='/home/aitor/airflow/functions/my_file.py',
    dag=dag,
)

run_second = IbmCloudFunctionsOperator(
    task_id='my_function_2',
    function_name='my_function',
    function_path='/home/aitor/airflow/functions/my_file.py',
    dag=dag,
)
run_first >> run_second
