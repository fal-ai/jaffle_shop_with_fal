# dbt iris ML example

<p align="center">
  <a href="https://getdbt.slack.com/archives/C02V8QW3Q4Q">
    <img src="https://badgen.net/badge/icon/%23tools-fal%20on%20dbt%20Slack/orange?icon=slack&label" alt="Slack channel" />
  </a>&nbsp;
</p>

In this tutorial, we will build a simple ML training and batch prediction pipeline using the dbt-fal adapter. We are going to be storing the model weights inside the datawarehouse (in this case duckdb, but could be snowflake etc) by pickling it. To run batch predictions, we will deserialize the model and run predictions against it, which we then store the results into another dbt Model.

### Installing Instructions:

1. Install `fal` and `dbt-fal`

```
$ pip install fal dbt-fal[duckdb] or "dbt-fal[duckdb]" for zsh
# Add your favorite adapter here
```

2. Specify the `fal` adapter in your `profiles.yml`:

```yaml
jaffle_shop:
  target: development
  outputs:
    development:
      type: fal
      db_profile: dev_duckdb

    dev_duckdb:
      type: duckdb
      path: "/Users/burkaygur/src/duck_db_dbt_dump.db"
      threads: 4
```

With this profiles configuration, fal will run all the Python models and will leave the SQL models to the `db_profile`.

3. Check out the `fal_project.yml` file to see the isolate Python environment that we create with our Python dependencies. In this case, sklearn.

4. Seed iris training and test datasets by running this:

```
$ dbt seed
```

### Running Instructions:

1. Train the model

```bash
$ dbt run --select classification_model
```

This trains a model and stores the artifacts in a model called `classification_model`

2. Run batch predictions against the model

```bash
$ dbt run --select model_predictions
```

This runs batch predictions against the `classification_model` and stores the results in `model_predictions`

3. Train and run batch predictions at the same time

```bash
$ dbt run --select classification_model+
```

### Curious to learn more?

If you would like to learn more about managing multiple environments for Python models and more, check out the [docs](https://docs.fal.ai)!

Or say hi 👋 in the [#tools-fal](https://getdbt.slack.com/archives/C02V8QW3Q4Q) Slack channel.
