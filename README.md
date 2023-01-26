# Testing dbt + fal: `jaffle_shop_with_fal`

<p align="center">
  <a href="https://getdbt.slack.com/archives/C02V8QW3Q4Q">
    <img src="https://badgen.net/badge/icon/%23tools-fal%20on%20dbt%20Slack/orange?icon=slack&label" alt="Slack channel" />
  </a>&nbsp;
</p>

It is year 2 for our [jaffle shop](https://github.com/dbt-labs/jaffle_shop) and the shop owner started collecting advanced attributes about the [orders](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/seeds/raw_order_attributes.csv).

We are tasked to understand what kind of jaffles we make the most money from.

So we decided to run a [clustering algorithm](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/clustering.py) to separate the orders into 3 different clusters and then to calculate all the [revenue for each cluster](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/models/cluster_stats.sql). Once our clustering algorithm is done, we want to send a notification to a Slack channel notifying our team that the results are ready for viewing.

The [fal](https://github.com/fal-ai/fal) + [dbt-fal](https://github.com/fal-ai/fal/tree/main/adapter) combination is the perfect tool for the task at hand:

- `dbt-fal` adapter lets us iterate on and ship our clustering algorithm **right within our dbt project**. This Python model works with any data warehouse, including ones without dbt Python support such as Postgres and Redshift. For Bigquery, it makes it easier to run Python models without having to stand up a Dataproc cluster.

- `fal flow` CLI command lets us send a Slack notification, via a Python post-hook. We could also execute any arbitrary Python here, for example to push data to external services.

With this combo, you won't have to leave your dbt project and still add more capabilities to your stack.

### Pre-requisites

- [Install Docker](https://docs.docker.com/get-docker/). Check if the installation is ok with `docker --version`.
  - **Note:** if you're on Linux, check the [post-install steps](https://docs.docker.com/engine/install/linux-postinstall/).
- Make sure `dbt-core` is installed. Verify with `dbt --version`. If not, see [DBT Installation](https://docs.getdbt.com/docs/get-started/installation) for instructions.
- **[Optional but recommended]** [Install `pyenv`](https://github.com/pyenv/pyenv) or an alternative to leverage isolated Python environments.

### Installing Instructions:

1. Install dependencies

    ```
    $ pip install -r requirements.txt
    ```

2. Create the database

    #### Option 1: Docker

    We provide a ready-to-use environment. To set up the environment using `docker-compose`, follow these steps:

    - Install [`docker`](https://docs.docker.com/get-docker) and [`docker-compose`](https://docs.docker.com/compose/install) on your machine.
    - Run `docker-compose up` to start the database.
      - Note: If you want to run the container in background use `docker-compose up -d`.

    ```
    $ docker-compose up
    ```

    **Note:** the stack includes adminer, an admin interface for easy database browsing. You can access it at `http://localhost:58080`.

    #### Option 2: Local database

    If you want to bring your own database, make sure to update the connection settings on `profiles.yml` to match your database.

3. Seed the test data

    ```
    $ dbt seed
    ```

**Note:** As aforementioned, fal works with any dbt adapter. Although this example is ready for Postgres, feel free to play around with it and switch to your favorite dbt-supported database.

### Running Instructions:

1. Run your dbt models

    ```bash
    $ dbt run
    ## Runs the SQL models on the datawarehouse and Python models locally with fal
    ```

2. Run `fal flow run` to execute the full graph including fal Python scripts, that is the `fal_scripts/notify.py` script.
You can use the dbt [graph selectors](https://docs.getdbt.com/reference/node-selection/graph-operators) and [much more](https://docs.fal.ai/).
With `fal flow run`, you will not have to run `dbt run` since fal handles the full execution.

    ```bash
    $ fal flow run
    ## Runs dbt run and the associated scripts, in this case a Slack notification is triggered
    ```

### Curious to learn more?

If you would like to learn more about managing multiple environments for Python models and more, check out the [docs](https://docs.fal.ai)!

Or say hi 👋 in the [#tools-fal](https://getdbt.slack.com/archives/C02V8QW3Q4Q) Slack channel.
