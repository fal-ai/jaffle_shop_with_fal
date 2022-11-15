# jaffle_shop_with_fal

It is year 2 for our [jaffle shop](https://github.com/dbt-labs/jaffle_shop) and the shop owner started collecting advanced attributes about the [orders](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/seeds/raw_order_attributes.csv).

We are tasked to understand what kind of jaffles we make the most money from.

So we decided to run a [clustering algorithm](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/clustering.py) to separate the orders into 3 different clusters and then to calculate all the [revenue for each cluster](https://github.com/fal-ai/jaffle_shop_with_fal/blob/main/models/cluster_stats.sql). Once our clustering algorithm is done, we want to send a notification to a Slack channel notifying our team that the results are ready for viewing.

The [fal](https://github.com/fal-ai/fal) + [dbt-fal](https://github.com/fal-ai/fal/tree/main/adapter) combination is the perfect tool for the task at hand:

- Using the `dbt-fal` adapter, we can iterate on and ship our clustering algorithm written in Python with any datawarehouse **right within our dbt project.**

- Using the `fal flow` CLI command, we can send a Slack notification to notify our team.

With this combo, you won't to leave your dbt project while still bringing more capabilities to your stack.

### Installing Instructions:

1. Install `fal` and `dbt-fal`

```
$ pip install fal dbt-fal[duckdb, postgres, redshift, bigquery]
# Add your favorite adapter here
```

2. Install the data science libraries to run the clustering script.

```
$ pip install kmodes convertdate pystan prophet plotly kaleido
```

3. Run dbt seed

```
$ dbt seed
```

### Running Instructions:

1. Run `dbt run`

```bash
$ dbt run
## Runs the whole graph including the Python models
```

2. Run `fal flow` to execute the full graph including Python scripts. You can use the dbt [graph selectors](https://docs.getdbt.com/reference/node-selection/graph-operators) and [much more](https://docs.fal.ai/).

```bash
$ fal flow run
## Runs dbt run and the associated scripts, in this case a Slack notification is triggered
```

### Curious to learn more?

If you would like to learn more about managing multiple environments for Python models and more, check out the [docs](https://docs.fal.ai)!

Or say hi 👋 in the [#tools-fal](https://getdbt.slack.com/archives/C02V8QW3Q4Q) Slack channel.
