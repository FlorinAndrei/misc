df = pd.read_csv(data_file_name, header=None)
df.columns = ["cost", "weight"]
bqm = knapsack_bqm(df["cost"], df["weight"], weight_capacity)
sampler = LeapHybridSampler()
response = sampler.sample(bqm)
process_results(response)
