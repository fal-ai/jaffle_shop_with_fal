import os
from pathlib import Path

fal_dir = os.path.join(Path.home(), ".fal")
df = ref(context.current_model.name)
Path(fal_dir).mkdir(exist_ok=True)
target = os.path.join(fal_dir, f"{context.current_model.name}.parquet")
df.to_parquet(target)

print(f"Wrote contents of {context.current_model.name} dbt model to {target}")
