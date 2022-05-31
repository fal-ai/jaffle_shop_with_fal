## How to use fal cli

This instance of the jaffle shop project, showcases a fal script that downloads selected dbt models as parquet files locally using the fal cli.

Inspired by the slack thread at the #duck-db channel.

### Instructions to run the project locally:

```
pip install fal
```

// seeds data into the database

```
dbt seed
```

// customers and orders dbt models are written as parquet files

```
fal flow run
```

output:

```
(fal-3vP5iebW-py3.8) ➜  jaffle_shop_with_fal git:(fal_parquet) fal flow run
15:04:55  Found 5 models, 20 tests, 0 snapshots, 0 analyses, 188 macros, 0 operations, 3 seed files, 0 sources, 0 exposures, 0 metrics
Executing command: dbt --log-format json run --project-dir /Users/gorkemyurtseven/dev/fal_ai_jaffle_shop_parquet/jaffle_shop_with_fal --select orders customers raw_customers stg_customers raw_orders raw_payments stg_payments stg_orders
Running with dbt=1.0.0
Found 5 models, 20 tests, 0 snapshots, 0 analyses, 188 macros, 0 operations, 3 seed files, 0 sources, 0 exposures, 0 metrics
Concurrency: 1 threads (target='dev')
1 of 5 START view model dbt_gorkem.stg_customers................................ [RUN]
1 of 5 OK created view model dbt_gorkem.stg_customers........................... [OK in 1.39s]
2 of 5 START view model dbt_gorkem.stg_orders................................... [RUN]
2 of 5 OK created view model dbt_gorkem.stg_orders.............................. [OK in 1.30s]
3 of 5 START view model dbt_gorkem.stg_payments................................. [RUN]
3 of 5 OK created view model dbt_gorkem.stg_payments............................ [OK in 1.34s]
4 of 5 START table model dbt_gorkem.customers................................... [RUN]
4 of 5 OK created table model dbt_gorkem.customers.............................. [CREATE TABLE (100.0 rows, 6.0 KB processed) in 10.39s]
5 of 5 START table model dbt_gorkem.orders...................................... [RUN]
5 of 5 OK created table model dbt_gorkem.orders................................. [CREATE TABLE (99.0 rows, 6.5 KB processed) in 7.24s]
Finished running 3 view models, 2 table models in 22.92s.
Completed successfully
Done. PASS=5 WARN=0 ERROR=0 SKIP=0 TOTAL=5
10:05:21 | Starting fal run for following models and scripts:
customers: /Users/gorkemyurtseven/dev/fal_ai_jaffle_shop_parquet/jaffle_shop_with_fal/model_to_parquet.py
orders: /Users/gorkemyurtseven/dev/fal_ai_jaffle_shop_parquet/jaffle_shop_with_fal/model_to_parquet.py

Concurrency: 1 threads
Wrote contents of customers dbt model to /Users/gorkemyurtseven/.fal/customers.parquet
Wrote contents of orders dbt model to /Users/gorkemyurtseven/.fal/orders.parquet
```

If you want to download more dbt models as parquet files you will have to add the following block of configuration under the model in the schema.yml file:

```
meta:
    fal:
    scripts:
        after:
            - model_to_parquet.py
```

## Testing dbt project: `jaffle_shop`

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.

### What is this repo?

What this repo _is_:

- A self-contained playground dbt project, useful for testing out scripts, and communicating some of the core dbt concepts.

What this repo _is not_:

- A tutorial — check out the [Getting Started Tutorial](https://docs.getdbt.com/tutorial/setting-up) for that. Notably, this repo contains some anti-patterns to make it self-contained, namely the use of seeds instead of sources.
- A demonstration of best practices — check out the [dbt Learn Demo](https://github.com/dbt-labs/dbt-learn-demo) repo instead. We want to keep this project as simple as possible. As such, we chose not to implement:
  - our standard file naming patterns (which make more sense on larger projects, rather than this five-model project)
  - a pull request flow
  - CI/CD integrations
- A demonstration of using dbt for a high-complex project, or a demo of advanced features (e.g. macros, packages, hooks, operations) — we're just trying to keep things simple here!

### What's in this repo?

This repo contains [seeds](https://docs.getdbt.com/docs/building-a-dbt-project/seeds) that includes some (fake) raw data from a fictional app.

The raw data consists of customers, orders, and payments, with the following entity-relationship diagram:

![Jaffle Shop ERD](/etc/jaffle_shop_erd.png)

### Running this project

To get up and running with this project:

1. Install dbt using [these instructions](https://docs.getdbt.com/docs/installation).

2. Clone this repository.

3. Change into the `jaffle_shop` directory from the command line:

```bash
$ cd jaffle_shop
```

4. Set up a profile called `jaffle_shop` to connect to a data warehouse by following [these instructions](https://docs.getdbt.com/docs/configure-your-profile). If you have access to a data warehouse, you can use those credentials – we recommend setting your [target schema](https://docs.getdbt.com/docs/configure-your-profile#section-populating-your-profile) to be a new schema (dbt will create the schema for you, as long as you have the right privileges). If you don't have access to an existing data warehouse, you can also setup a local postgres database and connect to it in your profile.

5. Ensure your profile is setup correctly from the command line:

```bash
$ dbt debug
```

6. Load the CSVs with the demo data set. This materializes the CSVs as tables in your target schema. Note that a typical dbt project **does not require this step** since dbt assumes your raw data is already in your warehouse.

```bash
$ dbt seed
```

7. Run the models:

```bash
$ dbt run
```

> **NOTE:** If this steps fails, it might mean that you need to make small changes to the SQL in the models folder to adjust for the flavor of SQL of your target database. Definitely consider this if you are using a community-contributed adapter.

8. Test the output of the models:

```bash
$ dbt test
```

9. Generate documentation for the project:

```bash
$ dbt docs generate
```

10. View the documentation for the project:

```bash
$ dbt docs serve
```

### What is a jaffle?

A jaffle is a toasted sandwich with crimped, sealed edges. Invented in Bondi in 1949, the humble jaffle is an Australian classic. The sealed edges allow jaffle-eaters to enjoy liquid fillings inside the sandwich, which reach temperatures close to the core of the earth during cooking. Often consumed at home after a night out, the most classic filling is tinned spaghetti, while my personal favourite is leftover beef stew with melted cheese.

---

For more information on dbt:

- Read the [introduction to dbt](https://docs.getdbt.com/docs/introduction).
- Read the [dbt viewpoint](https://docs.getdbt.com/docs/about/viewpoint).
- Join the [dbt community](http://community.getdbt.com/).

---
